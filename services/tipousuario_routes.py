from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.tipousuario import Tipousuario

tipousuario_routes = Blueprint("tipousuario_routes", __name__)

@tipousuario_routes.route('/tipousuario', methods=['POST'])
def create_tipousuario():
    descripcion = request.json['descripcion']
    tipousuario = Tipousuario(descripcion)
    db.session.add(tipousuario)
    db.session.commit()

    if not tipousuario:
        data = {
            'message': 'No se pudo crear el tipo de usuario',
            'status': 400,
            'data': {}
        }

        return make_response(jsonify(data), 400)
    
    data = {
        'message': 'Tipo de usuario creado',
        'status': 201,
        'data': {
            'tipousuarioid': tipousuario.tipousuarioid,
            'descripcion': tipousuario.descripcion
        }
    }

    return make_response(jsonify(data), 201)

@tipousuario_routes.route('/tipousuario', methods=['GET'])
def get_tipousuarios():
    tipousuarios = Tipousuario.query.all()
    data = {
        'message': 'Todos los tipos de usuario',
        'status': 200,
        'data': [
            {
                'tipousuarioid': tipousuario.tipousuarioid,
                'descripcion': tipousuario.descripcion
            } for tipousuario in tipousuarios
        ]
    }

    return make_response(jsonify(data), 200)