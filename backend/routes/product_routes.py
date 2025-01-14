from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.extensions import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(
        name=data['name'], description=data['description'],
        price=data['price'], seller_id=data['seller_id']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201