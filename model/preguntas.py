from utils.db import db
from dataclasses import dataclass

@dataclass
class Preguntas(db.Model):
    __tablename__ = 'preguntas'
    preguntaid: int
    testid: int
    textopregunta: str
    numeropregunta: int

    preguntaid = db.Column(db.Integer, primary_key=True)
    testid = db.Column(db.Integer, db.ForeignKey('tests.testid'))
    textopregunta = db.Column(db.String(100))
    numeropregunta = db.Column(db.Integer)

    test = db.relationship('Tests', backref='preguntas')

    def __init__(self, testid, textopregunta, numeropregunta):
        self.testid = testid
        self.textopregunta = textopregunta
        self.numeropregunta = numeropregunta
