from datetime import datetime
from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.observacion import Observacion

observacion_routes = Blueprint("observacion_routes", __name__)

@observacion_routes.route('/observacion', methods=['POST'])
def create_observacion():
    observacion_data = request.json

    observacion = Observacion(observacion_data['diagnosticoid'], observacion_data['observacion'], observacion_data['recomendacion'])
    db.session.add(observacion)
    db.session.commit()

    data = {
        'message': 'Observación creada',
        'status': 201,
        'data': {
            'observacionid': observacion.observacionid,
            'diagnosticoid': observacion.diagnosticoid,
            'fecha_observacion': observacion.fecha_observacion.strftime('%Y-%m-%d %H:%M:%S'),
            'observacion': observacion.observacion,
            'recomendacion': observacion.recomendacion
        }
    }

    return make_response(jsonify(data), 201)