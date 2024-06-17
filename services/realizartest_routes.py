from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.diagnosticos import Diagnosticos
from model.respuestasusuario import Respuestasusuario
from model.respuestas import Respuestas
from model.tests import Tests
from model.persona import Persona

realizartest_routes = Blueprint("realizartest_routes", __name__)

@realizartest_routes.route('/realizartest', methods=['POST'])
def create_respuestausuario_and_diagnostico():
    personaid = request.json['personaid']
    testid = request.json['testid']
    respuestas = request.json['respuestas']
    respuestas_creadas = []
    suma = 0

    for respuesta in respuestas:
        preguntaid = respuesta['preguntaid']
        respuestaid = respuesta['respuestaid']

        # Obtén el valor de numerorespuesta para el respuestaid dado
        respuesta_obj = Respuestas.query.filter_by(respuestaid=respuestaid).first()
        numerorespuesta = respuesta_obj.numerorespuesta if respuesta_obj else 0

        suma += numerorespuesta

        respuestausuario = Respuestasusuario(personaid, testid, preguntaid, respuestaid)
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
            'respuestaid': respuestausuario.respuestaid
        })

    if suma < 45:
        diagnostico = 'Ansiedad normal'
    elif suma >= 45 and suma < 60:
        diagnostico = 'Ansiedad mínima moderada'
    elif suma >= 60 and suma < 75:
        diagnostico = 'Ansiedad moderada severa'
    else:
        diagnostico = 'Ansiedad en grado máximo'

    diagnostico_obj = Diagnosticos(personaid, testid, suma, diagnostico)
    db.session.add(diagnostico_obj)
    db.session.commit()

    data = {
        'message': 'Respuestas de usuario y diagnóstico creados',
        'status': 201,
        'data': respuestas_creadas,
        'diagnostico': diagnostico
    }

    return make_response(jsonify(data), 201)