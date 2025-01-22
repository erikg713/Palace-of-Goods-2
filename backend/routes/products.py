from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from models.models import Product

product_bp = Blueprint("products", __name__)

@product_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully"}), 201


@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "description": p.description, "price": p.price}
        for p in products
    ])
