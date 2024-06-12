from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class Login(db.Model):
    __tablename__ = 'login'
    id: int
    correo: str
    contrasena: str

    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(250), unique=True, nullable=False)
    contrasena = db.Column(db.String(250), nullable=False)

    def __init__(self, correo, contrasena):
        self.correo = correo
        self.contrasena = generate_password_hash(contrasena)

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)