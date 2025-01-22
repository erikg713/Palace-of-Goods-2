from flask import Blueprint, request, jsonify
import requests
import os
from app import db
from models.models import Payment

payments_bp = Blueprint("payments", __name__)

PI_API_KEY = os.getenv("PI_API_KEY")
PI_BASE_URL = "https://api.minepi.com/v2"

@payments_bp.route('/initiate', methods=['POST'])
def initiate_payment():
    data = request.get_json()
    amount = data.get('amount')
    memo = data.get('memo', "Payment for goods")

    headers = {"Authorization": f"Bearer {PI_API_KEY}"}
    payload = {"amount": amount, "memo": memo}

    response = requests.post(f"{PI_BASE_URL}/payments", json=payload, headers=headers)
    if response.status_code == 201:
        payment = Payment(user_id=data.get("user_id"), amount=amount, status="pending")
        db.session.add(payment)
        db.session.commit()
        return jsonify({"message": "Payment initiated", "payment_id": payment.id}), 201

    return jsonify({"message": "Payment initiation failed"}), 400
