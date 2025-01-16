from flask import request, jsonify
from app.models.order_model import Order
from app.models.product_model import Product
from app import db

# Place a new order
def place_order():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Validate product availability
    product = Product.query.get(product_id)
    if not product or product.stock < quantity:
        return jsonify({'message': 'Product not available in sufficient quantity'}), 400

    # Calculate total price
    total_price = product.price * quantity

    # Create and save the order
    order = Order(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price)
    db.session.add(order)

    # Update product stock
    product.stock -= quantity
    db.session.commit()

    return jsonify({'message': 'Order placed successfully', 'order_id': order.id}), 201

# Get all orders (admin only)
def get_all_orders():
    orders = Order.query.all()
    return jsonify([{
        'id': order.id,
        'user_id': order.user_id,
        'product_id': order.product_id,
        'quantity': order.quantity,
        'total_price': order.total_price,
        'status': order.status
    } for order in orders]), 200

# Get orders for a specific user
def get_user_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': order.id,
        'product_id': order.product_id,
        'quantity': order.quantity,
        'total_price': order.total_price,
        'status': order.status
    } for order in orders]), 200

# Update order status
def update_order_status(order_id):
    data = request.get_json()
    status = data.get('status')

    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    order.status = status
    db.session.commit()

    return jsonify({'message': 'Order status updated successfully'}), 200

# Cancel an order
def cancel_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    # Restore product stock
    product = Product.query.get(order.product_id)
    if product:
        product.stock += order.quantity

    db.session.delete(order)
    db.session.commit()

    return jsonify({'message': 'Order cancelled successfully'}), 200
