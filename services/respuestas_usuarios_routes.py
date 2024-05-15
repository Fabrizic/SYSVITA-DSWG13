from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.respuestas_usuarios import Respuestas_usuarios
from schemas.respuestas_usuarios_schema import respuestas_usuarios_schema, respuestass_usuarios_schema

#TODO: Implementar las rutas de respuestas_usuarios AGREGAR y UPDATE

respuestas_usuarios_routes = Blueprint("respuestas_usuarios_routes", __name__)

@respuestas_usuarios_routes.route('/respuestas_usuarios', methods=['POST'])
def create_respuesta_usuario():
    respuesta_usuario_id = request.json['respuesta_usuario_id']
    usuario_id = request.json['usuario_id']
    pregunta_id = request.json['pregunta_id']
    respuesta_id = request.json['respuesta_id']

    new_respuesta_usuario = Respuestas_usuarios(respuesta_usuario_id, usuario_id, pregunta_id, respuesta_id)

    db.session.add(new_respuesta_usuario)
    db.session.commit()

    result = respuestas_usuarios_schema.dump(new_respuesta_usuario)

    data = {
        'message': 'Respuesta de usuario creada',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@respuestas_usuarios_routes.route('/respuestas_usuarios', methods=['GET'])
def get_respuestas_usuarios():
    respuestas_usuarios = Respuestas_usuarios.query.order_by(Respuestas_usuarios.usuario_id).all()
    result = respuestass_usuarios_schema.dump(respuestas_usuarios)

    data = {
        'message': 'Todas las respuesas de usuarios',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@respuestas_usuarios_routes.route('/respuestas_usuarios/<int:usuario_id>', methods=['GET'])
def get_respuesta_usuario(usuario_id):
    respuesta_usuario = Respuestas_usuarios.query.filter_by(usuario_id=usuario_id).all()

    if not respuesta_usuario:
        data = {
            'message': 'Respuesta de usuario no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = respuestass_usuarios_schema.dump(respuesta_usuario)

    data = {
        'message': 'Respuesta de usuario encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)


@respuestas_usuarios_routes.route('/respuestas_usuarios/<int:usuario_id>', methods=['PUT'])
def update_respuesta_usuario(usuario_id):
    respuesta_usuario = Respuestas_usuarios.query.filter_by(usuario_id=usuario_id).first()

    if not respuesta_usuario:
        data = {
            'message': 'Respuesta de usuario no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    respuesta_usuario.usuario_id = request.json['usuario_id']
    respuesta_usuario.pregunta_id = request.json['pregunta_id']
    respuesta_usuario.respuesta_id = request.json['respuesta_id']

    db.session.commit()

    result = respuestas_usuarios_schema.dump(respuesta_usuario)

    data = {
        'message': 'Respuesta de usuario actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@respuestas_usuarios_routes.route('/respuestas_usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_respuesta_usuario(usuario_id):
    respuestas_usuario = Respuestas_usuarios.query.filter_by(usuario_id=usuario_id).all()

    if not respuestas_usuario:
        data = {
            'message': 'Respuesta de usuario no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    for respuesta_usuario in respuestas_usuario:
        db.session.delete(respuesta_usuario)

    db.session.commit()

    data = {
        'message': 'Respuestas de usuario eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)