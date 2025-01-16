import requests
import os
from flask import request, jsonify
from app.models.payment_model import Payment
from app import db

PI_BASE_URL = os.getenv('PI_BASE_URL')
PI_API_KEY = os.getenv('PI_API_KEY')

def initiate_payment():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    memo = data.get('memo', 'Payment for goods')
    metadata = data.get('metadata', {})

    # Construct payment request
    headers = {'Authorization': f'Bearer {PI_API_KEY}'}
    payload = {
        'amount': amount,
        'memo': memo,
        'metadata': metadata
    }

    try:
        response = requests.post(f'{PI_BASE_URL}/payments', json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 201:
            # Save the payment details in the database
            payment = Payment(
                user_id=user_id,
                pi_payment_id=response_data['identifier'],
                amount=amount,
                memo=memo,
                metadata=metadata
            )
            db.session.add(payment)
            db.session.commit()

            return jsonify({'message': 'Payment initiated successfully', 'payment': response_data}), 201
        else:
            return jsonify({'message': 'Failed to initiate payment', 'error': response_data}), response.status_code
    except Exception as e:
        return jsonify({'message': 'An error occurred while initiating payment', 'error': str(e)}), 500
