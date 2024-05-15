from utils.ma import ma
from model.respuestas_usuarios import Respuestas_usuarios
from marshmallow import fields
from schemas.respuestas_schema import RespuestasSchema
from schemas.usuarios_schema import UsuariosSchema
from schemas.preguntas_schema import PreguntasSchema

class Respuestas_usuariosSchema(ma.Schema):
    class Meta:
        model = Respuestas_usuarios
        fields = ('respuesta_usuario_id', 'usuario_id',
        'usuario',          
        'pregunta_id',
        'pregunta',
        'respuesta_id',
        'respuesta')

    usuario = ma.Nested(UsuariosSchema)
    pregunta = ma.Nested(PreguntasSchema)
    respuesta = ma.Nested(RespuestasSchema)

respuestas_usuarios_schema = Respuestas_usuariosSchema()
respuestass_usuarios_schema = Respuestas_usuariosSchema(many=True)