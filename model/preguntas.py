from utils.db import db
from dataclasses import dataclass

@dataclass
class Preguntas(db.Model):
    __tablename__ = 'preguntas'
    pregunta_id: int
    test_id: int
    texto_pregunta: str

    pregunta_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer)
    texto_pregunta = db.Column(db.String(100))

    def __init__(self, pregunta_id, test_id, texto_pregunta, numero_pregunta):
        self.pregunta_id = pregunta_id
        self.test_id = test_id
        self.texto_pregunta = texto_pregunta
