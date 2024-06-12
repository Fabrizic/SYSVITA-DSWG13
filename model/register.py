from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class Persona(db.Model):
    __tablename__ = 'persona'
    id: int
    nombre: str
    apellidopaterno: str
    apellidomaterno: str
    fechanacimiento: str

    id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    apellidopaterno = db.Column(db.String(250), nullable=False)
    apellidomaterno = db.Column(db.String(250), nullable=False)
    fechanacimiento = db.Column(db.Date, nullable=False)