from flask import Blueprint, jsonify
from app.schemas.user_schemas import UserSchema

user_bp = Blueprint("user", __name__)

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = {
        "id": user_id,
        "username": "johndoe",
        "email": "john@example.com",
        "role": "user",
        "created_at": "2023-01-01T12:00:00Z",
        "updated_at": "2023-01-15T12:00:00Z"
    }
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user))
