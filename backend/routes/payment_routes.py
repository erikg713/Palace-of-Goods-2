from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.payment import Payment
from app import db
from pi_pysdk import Pi
import os

payment_bp = Blueprint('payments', __name__)

PI_API_KEY = os.getenv("PI_API_KEY")
pi = Pi(api_key=PI_API_KEY)

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
        payment = pi.create_payment(
            amount=amount,
            memo=memo,
            metadata={"user_id": current_user_id}
        )
        new_payment = Payment(
            identifier=payment['identifier'],
            user_id=current_user_id,
            amount=amount
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"payment_id": payment['identifier']}), 201
    except Exception as e:
        return jsonify({"msg": "Failed to create payment", "error": str(e)}), 500

@payment_bp.route('/complete', methods=['POST'])
def complete_payment():
    data = request.get_json()
    payment_id = data.get('payment_id')

    if not payment_id:
        return jsonify({"msg": "Payment ID is required"}), 400

    try:
        payment = pi.complete_payment(payment_id)
        db_payment = Payment.query.filter_by(identifier=payment_id).first()

        if not db_payment:
            return jsonify({"msg": "Payment not found"}), 404

        db_payment.status = "completed"
        db.session.commit()
        return jsonify({"msg": "Payment completed successfully", "payment": payment}), 200
    except Exception as e:
        return jsonify({"msg": "Failed to complete payment", "error": str(e)}), 500

@payment_bp.route('/status/<payment_id>', methods=['GET'])
@jwt_required()
def check_payment_status(payment_id):
    db_payment = Payment.query.filter_by(identifier=payment_id).first()

    if not db_payment:
        return jsonify({"msg": "Payment not found"}), 404

    return jsonify({
        "payment_id": db_payment.identifier,
        "status": db_payment.status,
        "amount": db_payment.amount,
        "created_at": db_payment.created_at
    })