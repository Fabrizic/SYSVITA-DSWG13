from utils.db import db
from dataclasses import dataclass

@dataclass
class Respuestasusuario(db.Model):
    respuestausuarioid: int
    personaid: int
    testid: int
    preguntaid: int
    respuestaid: int
    diagnosticoid: int

    respuestausuarioid = db.Column(db.Integer, primary_key=True)
    personaid = db.Column(db.Integer, db.ForeignKey('persona.persona_id'))
    testid = db.Column(db.Integer, db.ForeignKey('tests.testid'))
    preguntaid = db.Column(db.Integer, db.ForeignKey('preguntas.preguntaid'))
    respuestaid = db.Column(db.Integer, db.ForeignKey('respuestas.respuestaid'))
    diagnosticoid = db.Column(db.Integer, db.ForeignKey('diagnosticos.diagnosticoid'))

    persona = db.relationship('Persona', backref='respuestasusuario')
    test = db.relationship('Tests', backref='respuestasusuario')
    pregunta = db.relationship('Preguntas', backref='respuestasusuario')
    respuestas = db.relationship('Respuestas', backref='respuestasusuario')
    diagnosticos = db.relationship('Diagnosticos', backref='respuestasusuario')

    def __init__(self, personaid, testid, preguntaid, respuestaid, diagnosticoid):
        self.personaid = personaid
        self.testid = testid
        self.preguntaid = preguntaid
        self.respuestaid = respuestaid
        self.diagnosticoid = diagnosticoid