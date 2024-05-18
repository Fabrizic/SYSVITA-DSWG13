from utils.db import db
from dataclasses import dataclass
from model.usuarios import Usuarios
from model.preguntas import Preguntas
from model.respuestas import Respuestas
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

@dataclass
class Respuestas_usuarios(db.Model):
    __tablename__ = 'respuestas_usuarios'
    respuesta_usuario_id: int
    usuario_id: int
    pregunta_id: int
    respuesta_id: int
    fecha_respuesta: DateTime

    respuesta_usuario_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    pregunta_id = db.Column(db.Integer, db.ForeignKey('preguntas.pregunta_id'))
    respuesta_id = db.Column(db.Integer, db.ForeignKey('respuestas.respuesta_id'))
    fecha_respuesta = Column(DateTime(timezone=True), server_default=func.now())

    usuario = db.relationship('Usuarios', backref='respuestas_usuarios')
    pregunta = db.relationship('Preguntas', backref='respuestas_usuarios')
    respuesta = db.relationship('Respuestas', backref='respuestas_usuarios')

    def __init__(self, respuesta_usuario_id, usuario_id, pregunta_id, respuesta_id):
        self.respuesta_usuario_id = respuesta_usuario_id
        self.usuario_id = usuario_id
        self.pregunta_id = pregunta_id
        self.respuesta_id = respuesta_id
