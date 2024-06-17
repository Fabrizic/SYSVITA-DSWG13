from utils.db import db
from dataclasses import dataclass

@dataclass
class Tests(db.Model):
    __tablename__ = 'tests'
    testid: int
    nombre: str
    descripcion: str

    testid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
