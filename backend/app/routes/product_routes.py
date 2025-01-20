# backend/app/routes/product_routes.py

from flask import Blueprint, jsonify, request
from app.models import db, Product
from flask_jwt_extended import jwt_required

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    products = Product.query.filter(Product.name.ilike(f"%{query}%")).paginate(page, per_page, False)
    return jsonify([product.to_dict() for product in products.items])

@product_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201
