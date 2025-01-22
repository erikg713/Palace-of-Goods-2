from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()

        # Ensure the JWT identity is valid
        if not current_user or "role" not in current_user:
            return jsonify({"message": "Invalid user credentials"}), 401

        # Check for admin role
        if current_user["role"] != "admin":
            return jsonify({"message": "Admin access required"}), 403

        return func(*args, **kwargs)
    
    return wrapper
