from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.usuario import Usuario
from model.persona import Persona

respuestas_login_routes = Blueprint("respuestas_login_routes", __name__)

@respuestas_login_routes.route('/login', methods=['POST'])
def login():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    tipousuarioid = request.json['tipousuarioid']

    login = Usuario.query.filter_by(correo=correo, tipousuarioid=tipousuarioid).first()
    persona = Persona.query.filter_by(persona_id=login.persona_id).first()

    if login and login.check_password(contrasena):
        data = {
            'message': 'Login exitoso',
            'status': 200,
            'data': {
                'usuario_id': login.usuario_id,
                'persona_id': login.persona_id,
                'correo': login.correo,
                'tipousuarioid': login.tipousuarioid,
                'username': persona.nombre + ' ' + persona.apellidopaterno,
            }
        }

        return make_response(jsonify(data), 200)

    data = {
        'message': 'Correo o contraseña incorrectos',
        'status': 400,
        'data': {}
    }

    return make_response(jsonify(data), 400)

@respuestas_login_routes.route('/login', methods=['GET'])
def get_logins():
    logins = Usuario.query.all()
    data = {
        'message': 'Todos los logins',
        'status': 200,
        'data': [
            {
                'usuario_id': login.usuario_id,
                'persona_id': login.persona_id,
                'correo': login.correo,
                'contrasena': login.contrasena
            } for login in logins
        ]
    }

    return make_response(jsonify(data), 200)

@respuestas_login_routes.route('/login/<int:usuario_id>', methods=['GET'])
def get_login(usuario_id):
    login = Usuario.query.get(usuario_id)

    if not login:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'Usuario encontrado',
        'status': 200,
        'data': {
            'usuario_id': login.usuario_id,
            'persona_id': login.persona_id,
            'correo': login.correo,
            'contrasena': login.contrasena
        }
    }

    return make_response(jsonify(data), 200)

@respuestas_login_routes.route('/login/<int:usuario_id>', methods=['PUT'])
def update_login(usuario_id):
    login = Usuario.query.get(usuario_id)

    if not login:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)

    login.correo = request.json['correo']
    login.contrasena = Usuario.generate_password_hash(request.json['contrasena'])
    db.session.commit()

    data = {
        'message': 'Usuario actualizado',
        'status': 200,
        'data': {
            'usuario_id': login.usuario_id,
            'correo': login.correo,
            'contrasena': login.contrasena
        }
    }

    return make_response(jsonify(data), 200)

@respuestas_login_routes.route('/login/<int:usuario_id>', methods=['DELETE'])
def delete_login(usuario_id):
    login = Usuario.query.get(usuario_id)

    if not login:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)

    db.session.delete(login)
    db.session.commit()

    data = {
        'message': 'Usuario eliminado',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)