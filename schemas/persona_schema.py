from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
    persona_id = fields.Integer()
    nombre = fields.String()
    apellidopaterno = fields.String()
    apellidomaterno = fields.String()
    fechanacimiento = fields.Date()
    ubigeoid = fields.Integer()

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)
    