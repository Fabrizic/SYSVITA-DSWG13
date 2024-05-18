from utils.db import db
from dataclasses import dataclass

@dataclass
class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    usuario_id: int
    nombre: str
    email: str
    edad: int

    usuario_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    edad = db.Column(db.Integer)

    def __init__(self, usuario_id, nombre, email,edad):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.email = email
        self.edad = edad
