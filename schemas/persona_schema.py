from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
    persona_id = fields.Integer()
    nombre = fields.String()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    fecha_nacimiento = fields.Date()

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)
    