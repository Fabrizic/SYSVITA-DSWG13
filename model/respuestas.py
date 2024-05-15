from utils.db import db
from dataclasses import dataclass

@dataclass
class Respuestas(db.Model):
    __tablename__ = 'respuestas'
    respuesta_id: int
    pregunta_id: int
    texto_respuesta: str

    respuesta_id = db.Column(db.Integer, primary_key=True)
    pregunta_id = db.Column(db.Integer)
    texto_respuesta = db.Column(db.String(100))

    def __init__(self, respuesta_id, pregunta_id, texto_respuesta, nivel_intensidad):
        self.respuesta_id = respuesta_id
        self.pregunta_id = pregunta_id
        self.texto_respuesta = texto_respuesta
        