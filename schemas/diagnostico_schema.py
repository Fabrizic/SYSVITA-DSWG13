from utils.ma import ma
from marshmallow import fields
from model.diagnosticos import Diagnosticos
from schemas.persona_schema import PersonaSchema
from schemas.tests_schema import TestSchema
from schemas.preguntas_schema import PreguntasSchema
from schemas.respuestas_schema import RespuestasSchema

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnosticos
        fields = ('diagnosticoid',
                  'personaid',
                  'persona',
                  'testid',
                  'test',
                  'fecha',
                  'puntaje',
                  'diagnostico')
        

    persona = ma.Nested(PersonaSchema)
    test = ma.Nested(TestSchema)