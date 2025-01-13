from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

def role_required(role):
    """
    Custom decorator to check for a specific user role.
    Extendable if roles like admin/moderator are added.
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            current_user_role = get_jwt_identity().get('role', 'user')  # Default to 'user'
            if current_user_role != role:
                return jsonify({"msg": "Access denied"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper