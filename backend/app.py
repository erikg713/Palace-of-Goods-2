from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production
jwt = JWTManager(app)

# Mock user database
users = {"admin": "password123"}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
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