# File: backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from pi_network_sdk import PiNetwork

app = Flask(__name__)
CORS(app)

# MongoDB Configuration
client = MongoClient("mongodb+srv://username:password@cluster.mongodb.net/dbname")
db = client['web3_marketplace']

# Pi Network Configuration
pi = PiNetwork(app_id="YOUR_PI_APP_ID", secret_key="YOUR_PI_SECRET_KEY")

@app.route('/api/items', methods=['GET'])
def get_items():
    items = list(db.items.find({}, {'_id': 0}))  # Exclude MongoDB ID
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.json
    db.items.insert_one(data)
    return jsonify({"message": "Item added successfully"}), 201

@app.route('/api/transaction', methods=['POST'])
def process_transaction():
    payload = request.json
    pi_authorization = payload.get('pi_authorization')
    
    # Verify Pi authorization
    user = pi.verify_user(pi_authorization)
    if user:
        # Transaction Logic
        transaction_data = {
            "user_id": user['uid'],
            "amount": payload['amount'],
            "item_id": payload['item_id']
        }
        # Store transaction data in MongoDB
        db.transactions.insert_one(transaction_data)
        return jsonify({"message": "Transaction successful"}), 200
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True)
