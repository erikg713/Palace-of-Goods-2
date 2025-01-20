from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Mock Database for Products and Orders
products = [
    {"id": 1, "name": "Product 1", "price": 10.0, "description": "Description for Product 1"},
    {"id": 2, "name": "Product 2", "price": 20.0, "description": "Description for Product 2"},
    {"id": 3, "name": "Product 3", "price": 30.0, "description": "Description for Product 3"}
]

orders = []

# Pi Network API Key
PI_API_KEY = "your_pi_network_api_key"

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/complete-payment/<payment_id>', methods=['POST'])
def complete_payment(payment_id):
    data = request.json
    total_amount = data.get('total_amount')
    txid = data.get('txid')

    profit = total_amount * 0.10  # Calculate 10% profit
    orders.append({"txid": txid, "total_amount": total_amount, "profit": profit})

    # Send to Pi Network API
    headers = {'Authorization': f'Bearer {PI_API_KEY}'}
    response = requests.post(f"https://api.minepi.com/v2/payments/{payment_id}/complete", headers=headers, json={"txid": txid})

    if response.status_code == 200:
        return jsonify({"message": "Payment completed", "profit": profit}), 200
    return jsonify({"error": "Payment failed"}), 500

@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)
