from flask import Blueprint, jsonify, request
from app.models import Product, User
from app import db

# Create a Blueprint for the API
bp = Blueprint("api", __name__)

# Product Routes
@bp.route("/api/products", methods=["GET"])
def get_products():
    """Fetch paginated list of products."""
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    products = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        "products": [product.to_dict() for product in products.items],
        "total": products.total,
        "pages": products.pages,
        "current_page": products.page,
    })

@bp.route("/api/products", methods=["POST"])
def add_product():
    """Add a new product."""
    data = request.json
    product = Product(name=data["name"], description=data["description"], price=data["price"])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

# User Routes
@bp.route("/api/register", methods=["POST"])
def register_user():
    """Register a new user."""
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400
    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])  # Assuming User model has a set_password method
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@bp.route("/api/login", methods=["POST"])
def login_user():
    """Log in a user and return a token."""
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):  # Assuming User model has a check_password method
        token = user.generate_token()  # Assuming User model has a generate_token method
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Payment Routes
@bp.route("/api/payments/approve", methods=["POST"])
def approve_payment():
    """Approve a payment."""
    data = request.json
    payment_id = data.get("paymentId")
    print(f"Payment approved: {payment_id}")
    return jsonify({"message": "Payment approved"}), 200

@bp.route("/api/payments/complete", methods=["POST"])
def complete_payment():
    """Complete a payment."""
    data = request.json
    payment_id = data.get("paymentId")
    print(f"Payment completed: {payment_id}")
    return jsonify({"message": "Payment completed"}), 200
