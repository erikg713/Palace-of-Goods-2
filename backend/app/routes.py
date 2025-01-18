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
