import requests
import os
from flask import request, jsonify, current_app as app
from app.models.payment_model import Payment
from app import db

# Load environment variables
PI_BASE_URL = os.getenv('PI_BASE_URL')
PI_API_KEY = os.getenv('PI_API_KEY')

# Validate critical environment variables
if not PI_BASE_URL or not PI_API_KEY:
    raise ValueError("Environment variables PI_BASE_URL and PI_API_KEY must be set")


def initiate_payment():
    """
    Initiates a payment request to the Pi Network and records it in the database.
    """
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    memo = data.get('memo', 'Payment for goods')
    metadata = data.get('metadata', {})

    # Validate required input fields
    if not user_id or not amount:
        app.logger.error("Missing required fields: 'user_id' or 'amount'")
        return jsonify({'message': "Missing required fields: 'user_id' or 'amount'"}), 400

    # Construct the payment request
    headers = {'Authorization': f'Bearer {PI_API_KEY}'}
    payload = {
        'amount': amount,
        'memo': memo,
        'metadata': metadata
    }

    try:
        # Send request to Pi Network
        response = requests.post(f'{PI_BASE_URL}/payments', json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 201:
            # Save the payment in the database
            payment = Payment(
                user_id=user_id,
                pi_payment_id=response_data.get('identifier'),
                amount=amount,
                memo=memo,
                metadata=metadata
            )
            db.session.add(payment)
            db.session.commit()

            # Return response to the frontend
            return jsonify({'message': 'Payment initiated successfully', 'payment': response_data}), 201

        else:
            # Handle non-successful responses
            error_message = response_data.get('error', 'Unknown error occurred')
            app.logger.error(f"Failed to initiate payment: {error_message}")
            return jsonify({'message': 'Failed to initiate payment', 'error': response_data}), response.status_code

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        app.logger.error(f"Network error during payment initiation: {str(e)}")
        return jsonify({'message': 'Network error occurred during payment initiation'}), 503

    except Exception as e:
        # Handle unexpected errors
        app.logger.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({'message': 'An unexpected error occurred while initiating payment'}), 500
