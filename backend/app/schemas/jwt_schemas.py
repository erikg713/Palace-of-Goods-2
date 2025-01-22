from marshmallow import Schema, fields

class JWTSchema(Schema):
    access_token = fields.Str(required=True)
    expires_in = fields.Int(required=True)
