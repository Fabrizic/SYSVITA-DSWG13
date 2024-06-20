from utils.db import db
from dataclasses import dataclass

@dataclass
class Tipousuario(db.Model):
    __tablename__ = 'tipo_usuario'
    tipousuarioid: int
    descripcion: str

    tipousuarioid = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, descripcion):
        self.descripcion = descripcion