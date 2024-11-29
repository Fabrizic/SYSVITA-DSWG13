from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.diagnosticos import Diagnosticos
from model.respuestasusuario import Respuestasusuario
from model.respuestas import Respuestas
from model.puntuacion import Puntuacion
from schemas.diagnostico_schema import DiagnosticoSchema
from model.persona import Persona
from model.ubigeo import Ubigeo
from model.tests import Tests
from model.preguntas import Preguntas
from model.respuestas import Respuestas
import json

realizartest_routes = Blueprint("realizartest_routes", __name__)

@realizartest_routes.route('/realizartest', methods=['POST'])
def create_respuestausuario_and_diagnostico():
    personaid = request.json['personaid']
    testid = request.json['testid']
    respuestas = request.json['respuestas']
    respuestas_creadas = []
    puntaje = 0

    if isinstance(respuestas, str):
        respuestas = json.loads(respuestas)

    # Calcular el puntaje total primero
    for respuesta in respuestas:
        preguntaid = respuesta['preguntaid']
        respuestaid = respuesta['respuestaid']

        respuesta_obj = Respuestas.query.filter_by(respuestaid=respuestaid).first()
        numerorespuesta = respuesta_obj.numerorespuesta if respuesta_obj else 0

        puntaje += numerorespuesta

    # Crear el objeto Diagnostico con el puntaje calculado
    diagnostico_obj = Diagnosticos(personaid, testid, puntaje, None)
    db.session.add(diagnostico_obj)
    db.session.commit()
    diagnosticoid = diagnostico_obj.diagnosticoid  # Asumiendo que este es el ID generado

    # Crear respuestas de usuario asociadas al diagnóstico
    for respuesta in respuestas:
        preguntaid = respuesta['preguntaid']
        respuestaid = respuesta['respuestaid']

        respuestausuario = Respuestasusuario(personaid, testid, preguntaid, respuestaid, diagnosticoid)
        db.session.add(respuestausuario)
        db.session.commit()

        if not respuestausuario:
            data = {
                'message': 'No se pudo crear la respuesta de usuario',
                'status': 400,
                'data': {}
            }
            return make_response(jsonify(data), 400)
        
        respuestas_creadas.append({
            'respuestausuarioid': respuestausuario.respuestausuarioid,
            'personaid': respuestausuario.personaid,
            'testid': respuestausuario.testid,
            'preguntaid': respuestausuario.preguntaid,
            'respuestaid': respuestausuario.respuestaid,
            'diagnosticoid': diagnosticoid
        })

    # Actualizar el diagnóstico basado en el puntaje total
    puntuacion_obj = Puntuacion.query.filter_by(testid=testid).filter(Puntuacion.rango_inferior <= puntaje, Puntuacion.rango_superior >= puntaje).first()
    if puntuacion_obj:
        puntuacionid = puntuacion_obj.puntuacionid
        diagnostico_obj.puntuacionid = puntuacionid
        db.session.commit()

    data = {
        'message': 'Respuestas de usuario y diagnóstico creados',
        'status': 201,
        'data': respuestas_creadas,
        'puntaje': puntaje,
        'puntuacionid': puntuacionid if puntuacion_obj else None,
        'diagnostico': puntuacion_obj.diagnostico if puntuacion_obj else None,
        'diagnosticoid': diagnosticoid
    }

    print(data)
    return make_response(jsonify(data), 201)

@realizartest_routes.route('/realizartest/<int:persona_id>', methods=['GET'])
def get_diagnosticos(persona_id):
    diagnosticos = Diagnosticos.query.filter_by(personaid=persona_id).all()
    data = {
        'message': 'Todos los diagnósticos',
        'status': 200,
        'data': [
            {
                'diagnosticoid': diagnostico.diagnosticoid,
                'personaid': diagnostico.personaid,
                'testid': diagnostico.testid,
                'puntaje': diagnostico.puntaje,
                'puntuacionid': diagnostico.puntuacionid
            } for diagnostico in diagnosticos
        ]
    }

    return make_response(jsonify(data), 200)


@realizartest_routes.route('/susrespuestas/<int:diagnosticoid>', methods=['GET'])
def get_respuestasusuario(diagnosticoid):
    respuestasusuario = db.session.query(
        Respuestasusuario.respuestausuarioid,
        Respuestasusuario.personaid,
        Respuestasusuario.testid,
        Respuestasusuario.preguntaid,
        Respuestasusuario.respuestaid,
        Respuestasusuario.diagnosticoid,
        Preguntas.textopregunta,
        Respuestas.textorespuesta
    ).join(
        Preguntas, Preguntas.preguntaid == Respuestasusuario.preguntaid
    ).join(
        Respuestas, Respuestas.respuestaid == Respuestasusuario.respuestaid
    ).filter(
        Respuestasusuario.diagnosticoid == diagnosticoid
    ).all()

    data = {
        'message': 'Todas las respuestas de usuario',
        'status': 200,
        'data': [
            {
                'respuestausuarioid': respuesta.respuestausuarioid,
                'personaid': respuesta.personaid,
                'testid': respuesta.testid,
                'preguntaid': respuesta.preguntaid,
                'respuestaid': respuesta.respuestaid,
                'diagnosticoid': respuesta.diagnosticoid,
                'textopregunta': respuesta.textopregunta,
                'textorespuesta': respuesta.textorespuesta
            } for respuesta in respuestasusuario
        ]
    }

    return make_response(jsonify(data), 200)