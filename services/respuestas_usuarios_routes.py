from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.respuestas_usuarios import Respuestas_usuarios
from model.usuarios import Usuarios
from schemas.respuestas_usuarios_schema import respuestas_usuarios_schema, respuestass_usuarios_schema
from schemas.usuarios_schema import usuarios_schema

respuestas_usuarios_routes = Blueprint("respuestas_usuarios_routes", __name__)

@respuestas_usuarios_routes.route('/respuestas_usuarios', methods=['POST'])
def create_respuesta_usuario():
    usuario_id = request.json['usuario_id']
    nombre = request.json.get('nombre', None)
    email = request.json.get('email', None)
    edad = request.json.get('edad', None)
    respuestas_data = request.json['respuestas']

    usuario = Usuarios.query.get(usuario_id)

    if not usuario and nombre and email and edad:
        usuario = Usuarios(usuario_id, nombre, email,edad)
        db.session.add(usuario)

    new_respuestas_usuario = []

    for respuesta_data in respuestas_data:
        pregunta_id = respuesta_data['pregunta_id']
        respuesta_id = respuesta_data['respuesta_id']

        new_respuesta_usuario = Respuestas_usuarios(None, usuario_id, pregunta_id, respuesta_id)
        new_respuestas_usuario.append(new_respuesta_usuario)

        db.session.add(new_respuesta_usuario)

    db.session.commit()

    result = respuestas_usuarios_schema.dump(new_respuestas_usuario, many=True)

    data = {
        'message': 'Respuestas de usuario creadas',
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


@respuestas_usuarios_routes.route('/respuestas_usuarios', methods=['PUT'])
def update_respuesta_usuario():
    usuario_id = request.json.get('usuario_id', None)
    if not usuario_id:
        return make_response(jsonify({'message': 'No se proporcionó usuario_id', 'status': 400}), 400)

    usuario = Usuarios.query.get(usuario_id)

    if not usuario:
        return make_response(jsonify({'message': 'Usuario no encontrado', 'status': 404}), 404)

    nombre = request.json.get('nombre', None)
    email = request.json.get('email', None)
    edad = request.json.get('edad', None)  
    respuestas_data = request.json['respuestas']

    if nombre:
        usuario.nombre = nombre
    if email:
        usuario.email = email
    if edad:  
        usuario.edad = edad

    Respuestas_usuarios.query.filter_by(usuario_id=usuario_id).delete()

    new_respuestas_usuario = []

    for respuesta_data in respuestas_data:
        pregunta_id = respuesta_data['pregunta_id']
        respuesta_id = respuesta_data['respuesta_id']

        new_respuesta_usuario = Respuestas_usuarios(None, usuario_id, pregunta_id, respuesta_id)
        new_respuestas_usuario.append(new_respuesta_usuario)

        db.session.add(new_respuesta_usuario)

    db.session.commit()

    result = respuestas_usuarios_schema.dump(new_respuestas_usuario, many=True)

    data = {
        'message': 'Respuestas de usuario actualizadas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@respuestas_usuarios_routes.route('/respuestas_usuarios', methods=['DELETE'])
@respuestas_usuarios_routes.route('/respuestas_usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_respuesta_usuario(usuario_id=None):
    if not usuario_id:
        usuario_id = request.json.get('usuario_id', None)
        if not usuario_id:
            return make_response(jsonify({'message': 'No se proporcionó usuario_id', 'status': 400}), 400)

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