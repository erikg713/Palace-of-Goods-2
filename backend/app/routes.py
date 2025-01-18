from flask import Blueprint, jsonify, request
from app.models import db, Product, User, Order
from flask_jwt_extended import jwt_required, get_jwt_identity
from pi_network import PiNetwork

main = Blueprint('main', __name__)

# Initialize Pi Network
pi = PiNetwork(api_key='your_pi_api_key', sandbox=True)

# Products
@main.route('/products', methods=['GET'])
def get_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    products = Product.query.filter(Product.name.ilike(f"%{query}%")).paginate(page, per_page, False)
    return jsonify([product.to_dict() for product in products.items])

@main.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

# Orders
@main.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    user_id = get_jwt_identity()
    data = request.json
    products = data['products']

    total_price = sum(Product.query.get(p['id']).price * p['quantity'] for p in products)
    new_order = Order(user_id=user_id, total_price=total_price)
    db.session.add(new_order)

    for product in products:
        product_data = Product.query.get(product['id'])
        product_data.stock -= product['quantity']

    db.session.commit()
    return jsonify({'status': 'Order placed!', 'order': new_order.to_dict()}), 201

# Payments
@main.route('/payments', methods=['POST'])
@jwt_required()
def process_payment():
    data = request.json
    tx_id = data.get("tx_id")

    try:
        payment = pi.process_payment(tx_id)
        return jsonify({"status": "success", "payment": payment}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
