from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.respuestas import Respuestas

respuestas_routes = Blueprint("respuestas_routes", __name__)

@respuestas_routes.route('/respuestas', methods=['POST'])
def create_respuesta():
    respuestas_data = request.json
    respuestas_creadas = []

    for respuesta_data in respuestas_data:
        testid = respuesta_data['testid']
        textorespuesta = respuesta_data['textorespuesta']
        numerorespuesta = respuesta_data['numerorespuesta']

        respuesta = Respuestas(testid, textorespuesta, numerorespuesta)
        db.session.add(respuesta)
        db.session.commit()

        if not respuesta:
            data = {
                'message': 'No se pudo crear la respuesta',
                'status': 400,
                'data': {}
            }

            return make_response(jsonify(data), 400)
        
        respuestas_creadas.append({
            'respuestaid': respuesta.respuestaid,
            'testid': respuesta.testid,
            'textorespuesta': respuesta.textorespuesta,
            'numerorespuesta': respuesta.numerorespuesta
        })

    data = {
        'message': 'Respuestas creadas',
        'status': 201,
        'data': respuestas_creadas
    }

    return make_response(jsonify(data), 201)

@respuestas_routes.route('/respuestas', methods=['GET'])
def get_respuestas():
    respuestas = Respuestas.query.all()
    data = {
        'message': 'Todas las respuestas',
        'status': 200,
        'data': [
            {
                'respuestaid': respuesta.respuestaid,
                'testid': respuesta.testid,
                'textorespuesta': respuesta.textorespuesta,
                'numerorespuesta': respuesta.numerorespuesta
            } for respuesta in respuestas
        ]
    }

    return make_response(jsonify(data), 200)

@respuestas_routes.route('/respuestas/<int:testid>', methods=['GET'])
def get_respuestas_test(testid):
    respuestas = Respuestas.query.filter_by(testid=testid).all()
    data = {
        'message': 'Todas las respuestas del test',
        'status': 200,
        'data': [
            {
                'respuestaid': respuesta.respuestaid,
                'testid': respuesta.testid,
                'textorespuesta': respuesta.textorespuesta,
            } for respuesta in respuestas
        ]
    }

    return make_response(jsonify(data), 200)

@respuestas_routes.route('/respuestasindividual', methods=['POST'])
def create_respuestaindividual():
    respuesta_data = request.json

    testid = respuesta_data['testid']
    textorespuesta = respuesta_data['textorespuesta']
    numerorespuesta = respuesta_data['numerorespuesta']

    respuesta = Respuestas(testid, textorespuesta, numerorespuesta)
    db.session.add(respuesta)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        data = {
            'message': 'No se pudo crear la respuesta. Error: ' + str(e),
            'status': 400,
            'data': {}
        }
        return make_response(jsonify(data), 400)

    data = {
        'message': 'Respuesta creada',
        'status': 201,
        'data': {
            'respuestaid': respuesta.respuestaid,
            'testid': respuesta.testid,
            'textorespuesta': respuesta.textorespuesta,
            'numerorespuesta': respuesta.numerorespuesta
        }
    }

    return make_response(jsonify(data), 201)