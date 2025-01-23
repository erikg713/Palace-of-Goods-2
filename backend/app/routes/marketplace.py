from flask import Blueprint, jsonify, request

marketplace_bp = Blueprint('marketplace', __name__)

# Sample route to get marketplace items
@marketplace_bp.route('/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Digital watch", "price": 100, "currency": "PI"},
        {"id": 2, "name": "Samsung Tablet", "price": 200, "currency": "PI"}
    ]
    return jsonify(items)

# Handle purchase transactions
@marketplace_bp.route('/purchase', methods=['POST'])
def purchase_item():
    data = request.json2
    # Handle Pi transaction here
    return jsonify({"message": "Transaction Successful!"})
