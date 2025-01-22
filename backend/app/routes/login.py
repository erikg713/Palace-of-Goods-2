from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
import datetime

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    # Example: Hardcoded user for demonstration purposes
    users = {
        "admin": {"username": "admin", "role": "admin"},
        "user": {"username": "user", "role": "user"}
    }

    username = data.get("username")
    password = data.get("password")  # Example: No real password validation here

    if username in users:
        user = users[username]
        # Generate token with claims (identity is the user payload)
        access_token = create_access_token(
            identity=user,
            expires_delta=datetime.timedelta(hours=1)
        )
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Invalid username or password"}), 401
