from utils.ma import ma
from marshmallow import fields

class PuntuacionSchema(ma.Schema):
    puntuacionid = fields.Integer()
    testid = fields.Integer()
    rango_inferior = fields.Integer()
    rango_superior = fields.Integer()
    diagnostico = fields.String()
    colorid = fields.Integer()

puntuacion_schema = PuntuacionSchema()
puntuacions_schema = PuntuacionSchema(many=True)
