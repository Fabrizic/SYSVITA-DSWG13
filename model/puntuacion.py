from utils.db import db
from dataclasses import dataclass

@dataclass
class Puntuacion(db.Model):
    __tablename__: 'puntuacion'
    puntuacionid: int
    testid: int 
    rango_inferior: int
    rango_superior: int
    diagnostico: str

    puntuacionid = db.Column(db.Integer, primary_key = True)
    testid = db.Column(db.Integer, db.ForeignKey('test.testid'))
    rango_inferior = db.Column(db.Integer)
    rango_superior = db.Column(db.Integer)
    diagnostico = db.Column(db.String(255))

    test = db.relationship('Tests', backref='puntuacion')

    def __init__(self, testid, rango_inferior,rango_superior,diagnostico):
        this.testid = testid
        this.rango_inferior = rango_inferior
        this.rango_superior = rango_superior
        this.diagnostico = diagnostico

