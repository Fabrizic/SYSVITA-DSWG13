from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.ubigeo import Ubigeo
from model.persona import Persona
from model.diagnosticos import Diagnosticos
from model.puntuacion import Puntuacion
from model.color import Color
from model.tests import Tests

ubigeo_routes = Blueprint("ubigeo_routes", __name__)

@ubigeo_routes.route('/ubigeo', methods=['GET'])
def get_ubigeo():
    ubigeos = Ubigeo.query.all()
    data = {
        'message': 'Todos los ubigeos',
        'status': 200,
        'data': [
            {
                'ubigeoid': ubigeo.ubigeoid,
                'distrito': ubigeo.distrito,
                'provincia': ubigeo.provincia,
                'departamento': ubigeo.departamento,
                'poblacion': ubigeo.poblacion,
                'superficie': ubigeo.superficie,
                'y': ubigeo.y,
                'x': ubigeo.x
            } for ubigeo in ubigeos
        ]
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/departamento', methods=['GET'])
def get_departamento():
    departamentos = Ubigeo.query.with_entities(Ubigeo.departamento).distinct()
    data = {
        'message': 'Todos los departamentos',
        'status': 200,
        'data': [
            {
                'departamento': departamento[0]
            } for departamento in departamentos
        ]
    }

    return make_response(jsonify(data), 200)


@ubigeo_routes.route('/provincia/<string:departamento>', methods=['GET'])
def get_provincia(departamento):
    provincias = Ubigeo.query.with_entities(Ubigeo.provincia).filter_by(departamento=departamento).distinct()
    data = {
        'message': 'Todas las provincias',
        'status': 200,
        'data': [
            {
                'provincia': provincia[0]
            } for provincia in provincias
        ]
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/distrito/<string:departamento>/<string:provincia>', methods=['GET'])
def get_distrito(departamento, provincia):
    distritos = Ubigeo.query.with_entities(Ubigeo.distrito).filter_by(departamento=departamento, provincia=provincia).distinct()
    data = {
        'message': 'Todos los distritos',
        'status': 200,
        'data': [
            {
                'distrito': distrito[0]
            } for distrito in distritos
        ]
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/ubigeo/<int:ubigeoid>', methods=['GET'])
def get_ubigeo_by_id(ubigeoid):
    ubigeo = Ubigeo.query.filter_by(ubigeoid=ubigeoid).first()
    if ubigeo:
        data = {
            'message': 'Ubigeo encontrado',
            'status': 200,
            'data': {
                'ubigeoid': ubigeo.ubigeoid,
                'distrito': ubigeo.distrito,
                'provincia': ubigeo.provincia,
                'departamento': ubigeo.departamento,
                'poblacion': ubigeo.poblacion,
                'superficie': ubigeo.superficie,
                'y': ubigeo.y,
                'x': ubigeo.x
            }
        }
    else:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404,
            'data': {}
        }

    return make_response(jsonify(data), data['status'])

@ubigeo_routes.route('/circulos', methods=['GET'])
def get_coordenadas():
    ubigeos = Ubigeo.query\
    .join(Persona, Ubigeo.ubigeoid == Persona.ubigeoid)\
    .join(Diagnosticos, Diagnosticos.personaid == Persona.persona_id)\
    .join(Puntuacion, Puntuacion.puntuacionid == Diagnosticos.puntuacionid)\
    .join(Color, Puntuacion.colorid == Color.colorid)\
    .join(Tests, Tests.testid == Diagnosticos.testid)\
    .add_columns(
        Ubigeo.ubigeoid,
        Persona.nombre,
        Persona.apellidopaterno,
        Persona.apellidomaterno,
        Puntuacion.diagnostico,
        Color.css,
        Ubigeo.y,
        Ubigeo.x,
        Tests.nombre.label('testnombre'),
        Tests.testid,
        Diagnosticos.fecha
    )\
    .all()
    
    if ubigeos:
        data_list = []
        for ubigeo in ubigeos:
            data = {
                'ubigeoid': ubigeo.ubigeoid,
                'nombre': ubigeo.nombre,
                'apellidopaterno': ubigeo.apellidopaterno,
                'apellidomaterno': ubigeo.apellidomaterno,
                'diagnostico': ubigeo.diagnostico,
                'color': ubigeo.css,
                'y': ubigeo.y,
                'x': ubigeo.x,
                'testnombre': ubigeo.testnombre,
                'testid': ubigeo.testid,
                'fecha': ubigeo.fecha.strftime('%Y-%m-%d')
            }
            data_list.append(data)

        response_data = {
            'message': 'Coordenas encontradas',
            'status': 200,
            'data': data_list
        }
    else:
        response_data = {
            'message': 'No se encontraron coordenadas',
            'status': 404,
            'data': None
        }

    return make_response(jsonify(response_data), response_data['status'])