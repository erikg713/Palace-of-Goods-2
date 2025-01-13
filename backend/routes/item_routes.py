from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.item import Item
from app import db

item_bp = Blueprint('items', __name__)

@item_bp.route('/', methods=['GET'])
@jwt_required()
def get_items():
    current_user_id = get_jwt_identity()
    items = Item.query.filter_by(user_id=current_user_id).all()
    return jsonify([{"id": item.id, "name": item.name, "category": item.category, "price": item.price} for item in items])

@item_bp.route('/', methods=['POST'])
@jwt_required()
def add_item():
    current_user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('name') or not data.get('price') or not data.get('category'):
        return jsonify({"msg": "Name, category, and price are required."}), 400

    new_item = Item(
        name=data['name'],
        category=data['category'],
        price=data['price'],
        user_id=current_user_id
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"msg": "Item added successfully"}), 201

@item_bp.route('/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    current_user_id = get_jwt_identity()
    data = request.get_json()
    item = Item.query.filter_by(id=item_id, user_id=current_user_id).first()

    if not item:
        return jsonify({"msg": "Item not found"}), 404

    item.name = data.get('name', item.name)
    item.price = data.get('price', item.price)
    item.category = data.get('category', item.category)
    db.session.commit()
    return jsonify({"msg": "Item updated successfully"}), 200

@item_bp.route('/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    current_user_id = get_jwt_identity()
    item = Item.query.filter_by(id=item_id, user_id=current_user_id).first()

    if not item:
        return jsonify({"msg": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"msg": "Item deleted successfully"}), 200