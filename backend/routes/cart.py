from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.models import CartItem, Product
from app import db

cart_bp = Blueprint("cart", __name__)

@cart_bp.route('/', methods=['GET'])
@jwt_required()
def get_cart():
    current_user = get_jwt_identity()
    cart_items = CartItem.query.filter_by(user_id=current_user["id"]).all()
    return jsonify([
        {"product_id": item.product_id, "quantity": item.quantity}
        for item in cart_items
    ])

@cart_bp.route('/', methods=['POST'])
@jwt_required()
def add_to_cart():
    current_user = get_jwt_identity()
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    existing_item = CartItem.query.filter_by(user_id=current_user["id"], product_id=product_id).first()
    if existing_item:
        existing_item.quantity += quantity
    else:
        new_item = CartItem(user_id=current_user["id"], product_id=product_id, quantity=quantity)
        db.session.add(new_item)

    db.session.commit()
    return jsonify({"message": "Item added to cart"}), 201
