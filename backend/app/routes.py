from flask import Blueprint, jsonify, request
from app.models import Product, db

main = Blueprint('main', __name__)

@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@main.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201


# backend/app/routes.py
from flask import Flask, jsonify, request
from pi_network import PiNetwork

app = Flask(__name__)

# Load environment variables
app.config.from_pyfile("config.py")

# Initialize Pi Network
pi = PiNetwork(api_key=app.config["PI_API_KEY"], sandbox=app.config["PI_SANDBOX"])

@app.route("/payment", methods=["POST"])
def process_payment():
    data = request.json
    tx_id = data.get("tx_id")
    try:
        payment = pi.process_payment(tx_id)
        return jsonify({"status": "success", "payment": payment}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
