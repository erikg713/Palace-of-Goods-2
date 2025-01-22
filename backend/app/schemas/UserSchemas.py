from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # Read-only field
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    role = fields.Str(required=True, validate=validate.OneOf(["admin", "user"]))
    created_at = fields.DateTime(dump_only=True)  # Automatically serialized
    updated_at = fields.DateTime(dump_only=True)

# Example usage:
# from app.schemas.user_schemas import UserSchema
# user_schema = UserSchema()
# user = {"username": "johndoe", "email": "john@example.com", "role": "user"}
# result = user_schema.load(user)  # Validates and deserializes the input
