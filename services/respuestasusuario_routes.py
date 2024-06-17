from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.respuestasusuario import Respuestasusuario

respuestasusuario_routes = Blueprint("respuestasusuario_routes", __name__)

@respuestasusuario_routes.route('/respuestasusuario', methods=['POST'])
def create_respuestausuario():
    personaid = request.json['personaid']
    testid = request.json['testid']
    respuestas = request.json['respuestas']
    respuestas_creadas = []

    for respuesta in respuestas:
        preguntaid = respuesta['preguntaid']
        respuestaid = respuesta['respuestaid']

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

    data = {
        'message': 'Respuestas de usuario creadas',
        'status': 201,
        'data': respuestas_creadas
    }

    return make_response(jsonify(data), 201)