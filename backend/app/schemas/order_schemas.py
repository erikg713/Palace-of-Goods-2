from marshmallow import Schema, fields

class OrderSchema(Schema):
    id = fields.Int()
    product_name = fields.Str()

class UserWithOrdersSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    orders = fields.List(fields.Nested(OrderSchema))
