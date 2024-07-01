from utils.db import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

@dataclass
class Diagnosticos(db.Model):
    __tablename__ = 'diagnosticos'
    diagnosticoid: int
    personaid: int
    testid: int
    fecha: DateTime
    puntaje: int
    puntuacionid: int

    diagnosticoid = db.Column(db.Integer, primary_key=True)
    personaid = db.Column(db.Integer, db.ForeignKey('persona.persona_id'))
    testid = db.Column(db.Integer, db.ForeignKey('tests.testid'))
    fecha = db.Column(db.Date(),server_default=func.now())
    puntaje = db.Column(db.Integer)
    puntuacionid = db.Column(db.Integer, db.ForeignKey('puntuacion.puntuacionid'))

    persona = db.relationship('Persona', backref='diagnosticos')
    test = db.relationship('Tests', backref='diagnosticos')
    puntuacion = db.relationship('Puntuacion', backref='diagnosticos')

    def __init__(self, personaid, testid, puntaje, puntuacionid):
        self.personaid = personaid
        self.testid = testid
        self.puntaje = puntaje
        self.puntuacionid = puntuacionid

    
