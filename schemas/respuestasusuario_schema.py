from utils.ma import ma
from marshmallow import fields
from model.respuestasusuario import Respuestasusuario
from schemas.persona_schema import PersonaSchema
from schemas.tests_schema import TestSchema
from schemas.preguntas_schema import PreguntasSchema
from schemas.respuestas_schema import RespuestasSchema

class RespuestasusuarioSchema(ma.Schema):
    class Meta:
        model = Respuestasusuario
        fields = ('respuestausuarioid',
                  'personaid',
                  'persona',
                  'testid',
                  'test',
                  'preguntaid',
                  'pregunta',
                  'respuestaid',
                  'respuestas')
        

    persona = ma.Nested(PersonaSchema)
    test = ma.Nested(TestSchema)
    pregunta = ma.Nested(PreguntasSchema)
    respuestas = ma.Nested(RespuestasSchema)


respuestasusuario_schema = RespuestasusuarioSchema()
respuestasusuarios_schema = RespuestasusuarioSchema(many=True)