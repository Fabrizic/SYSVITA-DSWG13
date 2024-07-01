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
    tipousuarioid: int

    usuario_id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id'))
    correo = db.Column(db.String(250), unique=True, nullable=False)
    contrasena = db.Column(db.String(250), nullable=False)
    tipousuarioid = db.Column(db.Integer, db.ForeignKey('tipo_usuario.tipousuarioid'))

    persona = db.relationship('Persona', backref='usuario')
    tipo_usuario = db.relationship('Tipousuario', backref='usuario')

    def __init__(self, persona_id, correo, contrasena, tipousuarioid):
        self.persona_id = persona_id
        self.correo = correo
        self.contrasena = generate_password_hash(contrasena)
        self.tipousuarioid = tipousuarioid

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)