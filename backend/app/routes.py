from flask import Blueprint, jsonify, request
from app.models import Product

bp = Blueprint("api", __name__)

@bp.route("/api/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@bp.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    product = Product(name=data["name"], description=data["description"], price=data["price"])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201
