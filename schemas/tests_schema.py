from utils.ma import ma
from marshmallow import fields

class TestSchema(ma.Schema):
    testid = fields.Integer()
    nombre = fields.String()
    descripcion = fields.String()

test_schema = TestSchema()
tests_schema = TestSchema(many=True)