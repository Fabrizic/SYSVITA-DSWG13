from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.diagnosticos import Diagnosticos
from model.respuestasusuario import Respuestasusuario
from model.respuestas import Respuestas
from model.puntuacion import Puntuacion
from schemas.diagnostico_schema import DiagnosticoSchema
from model.persona import Persona
from model.ubigeo import Ubigeo

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

    # Consulta la tabla Puntuacion para obtener el diagnóstico
    puntuacion_obj = Puntuacion.query.filter_by(testid=testid).filter(Puntuacion.rango_inferior <= puntaje, Puntuacion.rango_superior >= puntaje).first()

    if puntuacion_obj:
        puntuacionid = puntuacion_obj.puntuacionid
        diagnostico = puntuacion_obj.diagnostico
    else:
        puntuacionid = None

    diagnostico_obj = Diagnosticos(personaid, testid, puntaje, puntuacionid)
    db.session.add(diagnostico_obj)
    db.session.commit()

    data = {
        'message': 'Respuestas de usuario y diagnóstico creados',
        'status': 201,
        'data': respuestas_creadas,
        'puntaje': puntaje,
        'puntuacionid': puntuacionid,
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
                'puntuacionid': diagnostico.puntuacionid
            } for diagnostico in diagnosticos
        ]
    }

    return make_response(jsonify(data), 200)
