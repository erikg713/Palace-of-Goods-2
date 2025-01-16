from flask import Blueprint
from app.controllers.order_controller import (
    place_order,
    get_all_orders,
    get_user_orders,
    update_order_status,
    cancel_order
)

order_bp = Blueprint('order', __name__)

order_bp.route('/', methods=['POST'])(place_order)  # Place an order
order_bp.route('/', methods=['GET'])(get_all_orders)  # Admin: Get all orders
order_bp.route('/user/<int:user_id>', methods=['GET'])(get_user_orders)  # Get user's orders
order_bp.route('/<int:order_id>', methods=['PUT'])(update_order_status)  # Update order status
order_bp.route('/<int:order_id>', methods=['DELETE'])(cancel_order)  # Cancel an order
