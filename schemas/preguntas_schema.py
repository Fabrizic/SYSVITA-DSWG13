from utils.ma import ma
from marshmallow import fields

class PreguntasSchema(ma.Schema):
    pregunta_id = fields.Integer()
    test_id = fields.Integer()
    texto_pregunta = fields.String()

preguntas_schema = PreguntasSchema()
preguntass_schema = PreguntasSchema(many=True)