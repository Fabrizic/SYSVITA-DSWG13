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
    puntaje = 0

    for respuesta in respuestas:
        preguntaid = respuesta['preguntaid']
        respuestaid = respuesta['respuestaid']

        # Obtén el valor de numerorespuesta para el respuestaid dado
        respuesta_obj = Respuestas.query.filter_by(respuestaid=respuestaid).first()
        numerorespuesta = respuesta_obj.numerorespuesta if respuesta_obj else 0

        puntaje += numerorespuesta

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

        testid = respuestausuario.testid
        
        if testid == 1:
            if puntaje < 45:
                diagnostico = 'Ansiedad normal'
            elif puntaje >= 45 and puntaje < 60:
                diagnostico = 'Ansiedad mínima moderada'
            elif puntaje >= 60 and puntaje < 75:
                diagnostico = 'Ansiedad moderada severa'
            else:
                diagnostico = 'Ansiedad en grado máximo'

        elif testid == 4:
            if puntaje <= 28:
                diagnostico = 'Ausencia de depresión'
            elif puntaje > 28 and puntaje <= 41:
                diagnostico = 'Depresión leve'
            elif puntaje > 41 and puntaje < 53:
                diagnostico = 'Depresión moderada'
            else:
                diagnostico = 'Depresión grave'

    diagnostico_obj = Diagnosticos(personaid, testid, puntaje, diagnostico)
    db.session.add(diagnostico_obj)
    db.session.commit()

    data = {
        'message': 'Respuestas de usuario y diagnóstico creados',
        'status': 201,
        'data': respuestas_creadas,
        'puntaje': puntaje,
        'diagnostico': diagnostico
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
                'diagnostico': diagnostico.diagnostico
            } for diagnostico in diagnosticos
        ]
    }

    return make_response(jsonify(data), 200)