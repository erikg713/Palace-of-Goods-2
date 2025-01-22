from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.user_schemas import LoginSchema

auth_bp = Blueprint("auth", __name__)
login_schema = LoginSchema()

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = login_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    return jsonify({"message": "Login successful!"})
