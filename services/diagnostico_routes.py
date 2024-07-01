from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.diagnosticos import Diagnosticos
from model.persona import Persona
from model.ubigeo import Ubigeo
from model.puntuacion import Puntuacion
from model.tests import Tests
from model.color import Color
from schemas.diagnostico_schema import DiagnosticoSchema

diagnostico_routes = Blueprint("diagnostico_routes", __name__)

@diagnostico_routes.route('/resultados', methods=['GET'])
def get_all_diagnosticos():
    diagnosticos = Diagnosticos.query.join(Persona, Diagnosticos.personaid == Persona.persona_id)\
                                 .join(Tests, Diagnosticos.testid == Tests.testid)\
                                 .join(Puntuacion, Diagnosticos.puntuacionid == Puntuacion.puntuacionid)\
                                 .join(Color, Puntuacion.colorid == Color.colorid)\
                                 .join(Ubigeo, Persona.ubigeoid == Ubigeo.ubigeoid)\
                                 .add_columns(Diagnosticos.diagnosticoid, Diagnosticos.fecha, Persona.nombre, Persona.apellidopaterno, Persona.apellidomaterno, Tests.nombre.label('test_nombre'), Ubigeo.departamento, Ubigeo.provincia, Ubigeo.distrito, Puntuacion.diagnostico, Color.css)\
                                 .all()

    if diagnosticos:
        data_list = []
        for diagnostico in diagnosticos:
            data = {
                'diagnosticoid': diagnostico.diagnosticoid,
                'fecha': diagnostico.fecha.strftime('%Y-%m-%d'),
                'nombre': diagnostico.nombre,
                'apellidopaterno': diagnostico.apellidopaterno,
                'apellidomaterno': diagnostico.apellidomaterno,
                'test': diagnostico.test_nombre,
                'diagnostico': diagnostico.diagnostico,
                'color': diagnostico.css,
            }
            data_list.append(data)

        response_data = {
            'message': 'Diagnósticos encontrados',
            'status': 200,
            'data': data_list
        }
    else:
        response_data = {
            'message': 'No se encontraron diagnósticos',
            'status': 404,
            'data': None
        }

    return make_response(jsonify(response_data), response_data['status'])

@diagnostico_routes.route('/diagnostico', methods=['GET'])
def get_diagnosticos_all():
    diagnosticos = Diagnosticos.query.all()
    diagnostico_schema = DiagnosticoSchema(many=True)
    result = diagnostico_schema.dump(diagnosticos)
    data = {
        'message': 'Todos los diagnósticos',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
