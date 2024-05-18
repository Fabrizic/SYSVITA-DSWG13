from utils.ma import ma
from marshmallow import fields

class UsuariosSchema(ma.Schema):
    usuario_id = fields.Integer()
    nombre = fields.String()
    email = fields.String()
    edad = fields.Integer()

usuarios_schema = UsuariosSchema()
usuarioss_schema = UsuariosSchema(many=True)