from utils.ma import ma
from marshmallow import fields

class RespuestasSchema(ma.Schema):
    respuesta_id = fields.Integer()
    texto_respuesta = fields.String()

respuestas_schema = RespuestasSchema()
respuestass_schema = RespuestasSchema(many=True)