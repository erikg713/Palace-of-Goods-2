from flask import Blueprint, request, jsonify
from app.controllers.payment_controller import initiate_payment, handle_payment_webhook
import logging

payment_bp = Blueprint('payment', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Routes
@payment_bp.route('/', methods=['POST'])
def initiate_payment_route():
    """
    Initiate a payment.

    Request Body:
        Required fields: amount, currency, recipient_id

    Returns:
        Response: A JSON response with the payment initiation status.
    """
    try:
        data = request.json
        if not data or 'amount' not in data or 'currency' not in data or 'recipient_id' not in data:
            return jsonify({"error": "Invalid input data"}), 400
        
        result = initiate_payment(data)
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Error initiating payment: {str(e)}")
        return jsonify({"error": "An internal error has occurred."}), 500

@payment_bp.route('/webhook', methods=['POST'])
def handle_payment_webhook_route():
    """
    Handle payment webhook.

    Request Body:
        Webhook data from the payment gateway.

    Returns:
        Response: A JSON response with the webhook handling status.
    """
    try:
        data = request.json
        result = handle_payment_webhook(data)
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Error handling payment webhook: {str(e)}")
        return jsonify({"error": "An internal error has occurred."}), 500
