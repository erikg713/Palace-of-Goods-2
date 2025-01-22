from flask import Blueprint, jsonify, request
from app.models import Product
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db

@bp.route("/api/register", methods=["POST"])
def register_user():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@bp.route("/api/login", methods=["POST"])
def login_user():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        token = user.generate_token()
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
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

@bp.route("/api/products", methods=["GET"])
def get_products():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    products = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        "products": [product.to_dict() for product in products.items],
        "total": products.total,
        "pages": products.pages,
        "current_page": products.page,
    })
