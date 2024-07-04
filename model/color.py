from utils.db import db
from dataclasses import dataclass

@dataclass
class Color(db.Model):
    __tablename__ = 'color'
    colorid: int
    nombre: str
    css: str

    colorid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=True)
    css = db.Column(db.String(250), nullable=False)

    def __init__(self, css, nombre=None):
        self.nombre = nombre
        self.css = css