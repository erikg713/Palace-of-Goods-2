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

from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.extensions import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.filter_by(is_active=True).all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products]), 200

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        seller_id=data['seller_id'],
        category=data['category']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully!"}), 201