from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.preguntas import Preguntas

preguntas_routes = Blueprint("preguntas_routes", __name__)

@preguntas_routes.route('/preguntas', methods=['POST'])
def create_pregunta():
    preguntas_data = request.json
    preguntas_creadas = []

    for pregunta_data in preguntas_data:
        testid = pregunta_data['testid']
        textopregunta = pregunta_data['textopregunta']
        numeropregunta = pregunta_data['numeropregunta']

        pregunta = Preguntas(testid, textopregunta, numeropregunta)
        db.session.add(pregunta)
        db.session.commit()

        if not pregunta:
            data = {
                'message': 'No se pudo crear la pregunta',
                'status': 400,
                'data': {}
            }

            return make_response(jsonify(data), 400)
        
        preguntas_creadas.append({
            'preguntaid': pregunta.preguntaid,
            'testid': pregunta.testid,
            'textopregunta': pregunta.textopregunta,
            'numeropregunta': pregunta.numeropregunta
        })

    data = {
        'message': 'Preguntas creadas',
        'status': 201,
        'data': preguntas_creadas
    }

    return make_response(jsonify(data), 201)

@preguntas_routes.route('/preguntas', methods=['GET'])
def get_preguntas():
    preguntas = Preguntas.query.all()
    data = {
        'message': 'Todas las preguntas',
        'status': 200,
        'data': [
            {
                'preguntaid': pregunta.preguntaid,
                'testid': pregunta.testid,
                'textopregunta': pregunta.textopregunta,
                'numeropregunta': pregunta.numeropregunta
            } for pregunta in preguntas
        ]
    }

    return make_response(jsonify(data), 200)

@preguntas_routes.route('/preguntas/<int:testid>', methods=['GET'])
def get_preguntas_test(testid):
    preguntas = Preguntas.query.filter_by(testid=testid).all()
    data = {
        'message': 'Preguntas del test',
        'status': 200,
        'data': [
            {
                'preguntaid': pregunta.preguntaid,
                'testid': pregunta.testid,
                'textopregunta': pregunta.textopregunta,
                'numeropregunta': pregunta.numeropregunta
            } for pregunta in preguntas
        ]
    }

    return make_response(jsonify(data), 200)

@preguntas_routes.route('/preguntasindividual', methods=['POST'])
def create_preguntaindividual():
    pregunta_data = request.json

    testid = pregunta_data['testid']
    textopregunta = pregunta_data['textopregunta']
    numeropregunta = pregunta_data['numeropregunta']

    pregunta = Preguntas(testid, textopregunta, numeropregunta)
    db.session.add(pregunta)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        data = {
            'message': 'No se pudo crear la pregunta. Error: ' + str(e),
            'status': 400,
            'data': {}
        }
        return make_response(jsonify(data), 400)

    data = {
        'message': 'Pregunta creada',
        'status': 201,
        'data': {
            'preguntaid': pregunta.preguntaid,
            'testid': pregunta.testid,
            'textopregunta': pregunta.textopregunta,
            'numeropregunta': pregunta.numeropregunta
        }
    }

    return make_response(jsonify(data), 201)