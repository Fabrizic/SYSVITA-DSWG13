from utils.db import db
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class Login(db.Model):
    __tablename__ = 'login'
    login_id: int
    correo: str
    contrasena: str
    fecha_registro: datetime

    login_id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100))
    contrasena = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, login_id, correo, contrasena):
        self.login_id = login_id
        self.correo = correo
        self.contrasena = contrasena
        self.fecha_registro = datetime.now(timezone.utc)