from utils.db import db
from dataclasses import dataclass

@dataclass
class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    ubigeoid: int
    distrito: str
    provincia: str
    departamento: str
    poblacion: int
    superficie: float
    y: float
    x: float

    ubigeoid = db.Column(db.Integer, primary_key=True)
    distrito = db.Column(db.String(250), nullable=False)
    provincia = db.Column(db.String(250), nullable=False)
    departamento = db.Column(db.String(250), nullable=False)
    poblacion = db.Column(db.Integer, nullable=False)
    superficie = db.Column(db.Numeric, nullable=False)
    y = db.Column(db.Numeric, nullable=False)
    x = db.Column(db.Numeric, nullable=False)

    def __init__(self, distrito, provincia, departamento, poblacion, superficie, y, x):
        self.distrito = distrito
        self.provincia = provincia
        self.departamento = departamento
        self.poblacion = poblacion
        self.superficie = superficie
        self.y = y
        self.x = x