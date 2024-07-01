from utils.db import db
from dataclasses import dataclass

@dataclass
class Puntuacion(db.Model):
    __tablename__ = 'puntuacion'
    puntuacionid: int
    testid: int 
    rango_inferior: int
    rango_superior: int
    diagnostico: str
    colorid: int

    puntuacionid = db.Column(db.Integer, primary_key = True)
    testid = db.Column(db.Integer, db.ForeignKey('tests.testid'))
    rango_inferior = db.Column(db.Integer)
    rango_superior = db.Column(db.Integer)
    diagnostico = db.Column(db.String(255))
    colorid = db.Column(db.Integer, db.ForeignKey('color.colorid'))

    test = db.relationship('Tests', backref='puntuacion')
    color = db.relationship('Color', backref='puntuacion')

    def __init__(self, testid, rango_inferior,rango_superior,diagnostico,colorid):
        self.testid = testid
        self.rango_inferior = rango_inferior
        self.rango_superior = rango_superior
        self.diagnostico = diagnostico
        self.colorid = colorid

