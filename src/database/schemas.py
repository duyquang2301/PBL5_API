from marshmallow import Schema,fields

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    email = fields.Str(required=True)

class PlainVehicleSchema(Schema):
    id = fields.Int(dump_only=True)

class PlainErrorPageSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    error_description = fields.String(required=False)

class UserSchema(PlainUserSchema):
    vehicles = fields.Nested(PlainVehicleSchema(), dump_only=True)

class UserUpdateSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    email = fields.Str(required=True)

class VehicleSchema(PlainVehicleSchema):
    user_id = fields.Int(required = True, load_only = True)
    user = fields.Nested(PlainUserSchema(), dump_only = True)
    error_papers = fields.List(fields.Nested(PlainErrorPageSchema()), dump_only = True)

class ErrorPageSchema(PlainErrorPageSchema):
    vehicle_id = fields.Int(required = True, load_only = True)
    vehicle = fields.Nested(PlainVehicleSchema(), dump_only = True)
