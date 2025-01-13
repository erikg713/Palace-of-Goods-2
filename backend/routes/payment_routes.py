from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.payment import Payment
from app import db
from pi_pysdk import Pi
import os

payment_bp = Blueprint('payments', __name__)

PI_API_KEY = os.getenv("PI_API_KEY")
pi = Pi(api_key=PI_API_KEY)

# Create Payment
@payment_bp.route('/create', methods=['POST'])
@jwt_required()
def create_payment():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    amount = data.get('amount')
    memo = data.get('memo', 'Payment for goods')

    if not amount or amount <= 0:
        return jsonify({"msg": "Invalid payment amount"}), 400

    try:
        # Create payment request
        payment = pi.create_payment(
            amount=amount,
            memo=memo,
            metadata={"user_id": current_user_id}
        )
        # Save payment to the database
        new_payment = Payment(
            identifier=payment['identifier'],
            user_id=current_user_id,
            amount=amount,
            status="pending"  # Initial status
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"payment_id": payment['identifier']}), 201
    except Exception as e:
        return jsonify({"msg": "Failed to create payment", "error": str(e)}), 500

# Complete Payment
@payment_bp.route('/complete', methods=['POST'])
def complete_payment():
    data = request.get_json()
    payment_id = data.get('payment_id')

    if not payment_id:
        return jsonify({"msg": "Payment ID is required"}), 400

    try:
        # Complete payment
        payment = pi.complete_payment(payment_id)
        # Update payment status in the database
        db_payment = Payment.query.filter_by(identifier=payment_id).first()
        if db_payment:
            db_payment.status = "completed"
            db.session.commit()
        return jsonify({"msg": "Payment completed successfully", "payment": payment}), 200
    except Exception as e:
        return jsonify({"msg": "Failed to complete payment", "error": str(e)}), 500

# Webhook Listener
@payment_bp.route('/webhook', methods=['POST'])
def payment_webhook():
    data = request.get_json()
    payment_id = data.get('identifier')
    status = data.get('status')

    if not payment_id or not status:
        return jsonify({"msg": "Invalid webhook payload"}), 400

    # Update payment status in the database
    payment = Payment.query.filter_by(identifier=payment_id).first()
    if payment:
        payment.status = status
        db.session.commit()
    return jsonify({"msg": "Webhook processed"}), 200

# Check Payment Status
@payment_bp.route('/status/<payment_id>', methods=['GET'])
@jwt_required()
def check_payment_status(payment_id):
    try:
        # Fetch payment details from Pi Network
        payment = pi.get_payment(payment_id)
        return jsonify({
            "payment_id": payment['identifier'],
            "status": payment['status'],
            "amount": payment['amount']
        }), 200
    except Exception as e:
        return jsonify({"msg": "Failed to retrieve payment status", "error": str(e)}), 500
def validate_payment_data(data):
    errors = {}
    if 'amount' not in data or data['amount'] <= 0:
        errors['amount'] = "Invalid or missing payment amount."
    if 'memo' not in data or not data['memo']:
        errors['memo'] = "Memo is required."
    return errors
errors = validate_payment_data(data)
if errors:
    return jsonify(errors), 400