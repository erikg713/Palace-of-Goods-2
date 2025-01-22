from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
import jwt
import datetime
from sqlalchemy.sql import func


class Product(db.Model):
    """Product model representing an item in the inventory."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def to_dict(self):
        """Convert Product instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class User(db.Model):
    """User model representing application users."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        """Hash and set the user's password."""
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def generate_token(self, expires_in=24):
        """Generate a JWT token for user authentication."""
        payload = {
            'id': self.id,
            'username': self.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=expires_in)
        }
        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")

    @staticmethod
    def verify_token(token):
        """Verify the JWT token and return the user ID if valid."""
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            return payload['id']
        except jwt.ExpiredSignatureError:
            return None  # Token expired
        except jwt.InvalidTokenError:
            return None  # Invalid token

    def to_dict(self, include_email=False):
        """Convert User instance to a dictionary."""
        user_data = {
            "id": self.id,
            "username": self.username,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        if include_email:
            user_data["email"] = self.email
        return user_data
