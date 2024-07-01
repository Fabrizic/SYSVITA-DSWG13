from utils.ma import ma
from marshmallow import fields
from model.diagnosticos import Diagnosticos
from schemas.persona_schema import PersonaSchema
from schemas.tests_schema import TestSchema
from schemas.preguntas_schema import PreguntasSchema
from schemas.respuestas_schema import RespuestasSchema
from schemas.puntuacion_schema import PuntuacionSchema

class DiagnosticoSchema(ma.Schema):
    class Meta:
        model = Diagnosticos
        load_instance = True
        include_fk = True
        fields = ('diagnosticoid',
                  'personaid',
                  'persona',
                  'testid',
                  'test',
                  'fecha',
                  'puntaje',
                  'puntuacionid',
                  'puntuacion',)
        

    persona = ma.Nested(PersonaSchema)
    test = ma.Nested(TestSchema)
    puntuacion = ma.Nested(PuntuacionSchema)