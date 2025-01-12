from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests for React development

@app.route('/api/items', methods=['GET'])
def get_items():
    # Mock data for your Palace of Goods
    items = [
        {"id": 1, "name": "Golden Cup", "price": 19.99},
        {"id": 2, "name": "Silver Sword", "price": 34.99},
        {"id": 3, "name": "Emerald Shield", "price": 49.99},
    ]
    return jsonify(items)

@app.route('/api/add-item', methods=['POST'])
def add_item():
    data = request.get_json()
    # Save the item to a database in the real implementation
    return jsonify({"message": "Item added successfully!", "data": data}), 201

if __name__ == "__main__":
    app.run(debug=True)