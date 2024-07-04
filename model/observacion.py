import datetime
from utils.db import db
from dataclasses import dataclass

@dataclass
class Observacion(db.Model):
    __tablename__ = 'observacion'
    observacionid: int
    diagnosticoid: int
    fecha_observacion: datetime
    observacion: str
    recomendacion: str

    observacionid = db.Column(db.Integer, primary_key=True)
    diagnosticoid = db.Column(db.Integer, db.ForeignKey('diagnosticos.diagnosticoid'), nullable=False)
    fecha_observacion = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    observacion = db.Column(db.String(255), nullable=False)
    recomendacion = db.Column(db.String(255), nullable=False)

    def __init__(self, diagnosticoid, observacion, recomendacion):
        self.diagnosticoid = diagnosticoid
        self.observacion = observacion
        self.recomendacion = recomendacion