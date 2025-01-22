from flask import Blueprint, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from app.utils.decorators import admin_required

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin", methods=["GET"])
@admin_required
def admin_dashboard():
    return jsonify({"message": "Welcome to the admin dashboard!"})

@admin_bp.route("/login", methods=["POST"])
def login():
    # Example user payload
    user = {"username": "admin", "role": "admin"}
    access_token = create_access_token(identity=user)
    return jsonify({"access_token": access_token})
