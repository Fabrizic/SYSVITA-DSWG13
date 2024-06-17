from utils.db import db
from dataclasses import dataclass

@dataclass
class Respuestas(db.Model):
    __tablename__ = 'respuestas'
    respuestaid: int
    testid: int
    textorespuesta: str
    numerorespuesta: int

    respuestaid = db.Column(db.Integer, primary_key=True)
    testid = db.Column(db.Integer, db.ForeignKey('tests.testid'))
    textorespuesta = db.Column(db.String(100))
    numerorespuesta = db.Column(db.Integer)

    test = db.relationship('Tests', backref='respuestas')

    def __init__(self, testid, textorespuesta, numerorespuesta):
        self.testid = testid
        self.textorespuesta = textorespuesta
        self.numerorespuesta = numerorespuesta
        