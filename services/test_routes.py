from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.tests import Tests

tests_routes = Blueprint("tests_routes", __name__)

@tests_routes.route('/tests', methods=['POST'])
def create_test():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']

    test = Tests(nombre, descripcion)
    db.session.add(test)
    db.session.commit()

    if not test:
        data = {
            'message': 'No se pudo crear el test',
            'status': 400,
            'data': {}
        }

        return make_response(jsonify(data), 400)
    
    data = {
        'message': 'Test creado',
        'status': 201,
        'data': {
            'testid': test.testid,
            'nombre': test.nombre,
            'descripcion': test.descripcion
        }
    }

    return make_response(jsonify(data), 201)

@tests_routes.route('/tests', methods=['GET'])
def get_tests():
    tests = Tests.query.all()
    data = {
        'message': 'Todos los tests',
        'status': 200,
        'data': [
            {
                'testid': test.testid,
                'nombre': test.nombre,
                'descripcion': test.descripcion
            } for test in tests
        ]
    }

    return make_response(jsonify(data), 200)

@tests_routes.route('/tests/<int:testid>', methods=['GET'])
def get_test(testid):
    test = Tests.query.get(testid)

    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)
    
    data = {
        'message': 'Test encontrado',
        'status': 200,
        'data': {
            'testid': test.testid,
            'nombre': test.nombre,
            'descripcion': test.descripcion
        }
    }

    return make_response(jsonify(data), 200)

