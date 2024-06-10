from marshmallow import fields, Schema


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)  # we need this while returning the data back to client
    name = fields.Str(required=True)  # this is a required field from client
    price = fields.Float(required=True)  # this is a required field from client
    store_id = fields.Str(required=True)  # this is a required field from client


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


