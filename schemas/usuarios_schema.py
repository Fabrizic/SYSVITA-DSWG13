from utils.ma import ma
from marshmallow import fields

class UsuariosSchema(ma.Schema):
    usuario_id = fields.Integer()
    nombre = fields.String()
    email = fields.String()

usuarios_schema = UsuariosSchema()
usuarioss_schema = UsuariosSchema(many=True)