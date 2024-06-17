#TODO: Agregar id_persona vinculado al id_persona de la tabla persona
from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'
    usuario_id: int
    persona_id: int
    correo: str
    contrasena: str

    usuario_id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id'))
    correo = db.Column(db.String(250), unique=True, nullable=False)
    contrasena = db.Column(db.String(250), nullable=False)

    persona = db.relationship('Persona', backref='usuario')

    def __init__(self, persona_id, correo, contrasena):
        self.persona_id = persona_id
        self.correo = correo
        self.contrasena = generate_password_hash(contrasena)

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)