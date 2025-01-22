from marshmallow import Schema, fields

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)  # Don't expose in output
