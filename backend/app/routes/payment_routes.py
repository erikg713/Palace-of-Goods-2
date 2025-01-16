from flask import Blueprint
from app.controllers.payment_controller import initiate_payment, handle_payment_webhook

payment_bp = Blueprint('payment', __name__)

# Routes
payment_bp.route('/', methods=['POST'])(initiate_payment)  # Initiate payment
payment_bp.route('/webhook', methods=['POST'])(handle_payment_webhook)  # Payment webhook
