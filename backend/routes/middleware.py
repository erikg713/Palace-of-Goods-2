from flask import jsonify
from flask_jwt_extended import get_jwt_identity

def admin_required(func):
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        if current_user["role"] != "admin":
            return jsonify({"message": "Admin access required"}), 403
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__  # Required for Flask routing
    return wrapper
