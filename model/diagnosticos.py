from utils.db import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

@dataclass
class Diagnosticos(db.Model):
    diagnosticoid: int
    personaid: int
    testid: int
    fecha: DateTime
    puntaje: int
    diagnostico: str

    diagnosticoid = db.Column(db.Integer, primary_key=True)
    personaid = db.Column(db.Integer, db.ForeignKey('persona.persona_id'))
    testid = db.Column(db.Integer, db.ForeignKey('tests.testid'))
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    puntaje = db.Column(db.Integer)
    diagnostico = db.Column(db.String(255))

    persona = db.relationship('Persona', backref='diagnosticos')
    test = db.relationship('Tests', backref='diagnosticos')

    def __init__(self, personaid, testid, puntaje, diagnostico):
        self.personaid = personaid
        self.testid = testid
        self.puntaje = puntaje
        self.diagnostico = diagnostico

    
