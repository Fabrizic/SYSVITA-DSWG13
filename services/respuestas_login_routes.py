from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.login import Login

respuestas_login_routes = Blueprint("respuestas_login_routes", __name__)

@respuestas_login_routes.route('/login', methods=['POST'])
def login():
    correo = request.json['correo']
    contrasena = request.json['contrasena']

    login = Login.query.filter_by(correo=correo).first()

    if login and login.check_password(contrasena):
        data = {
            'message': 'Login exitoso',
            'status': 200,
            'data': {
                'login_id': login.id,
                'correo': login.correo
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
    logins = Login.query.all()
    data = {
        'message': 'Todos los logins',
        'status': 200,
        'data': [
            {
                'login_id': login.id,
                'correo': login.correo,
                'contrasena': login.contrasena
            } for login in logins
        ]
    }

    return make_response(jsonify(data), 200)

@respuestas_login_routes.route('/login/<int:login_id>', methods=['GET'])
def get_login(login_id):
    login = Login.query.get(login_id)

    if not login:
        data = {
            'message': 'Login no encontrado',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'Login encontrado',
        'status': 200,
        'data': {
            'login_id': login.id,
            'correo': login.correo,
            'contrasena': login.contrasena
        }
    }

    return make_response(jsonify(data), 200)

@respuestas_login_routes.route('/login/<int:login_id>', methods=['PUT'])
def update_login(login_id):
    login = Login.query.get(login_id)

    if not login:
        data = {
            'message': 'Login no encontrado',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)

    login.correo = request.json['correo']
    login.contrasena = Login.generate_password_hash(request.json['contrasena'])
    db.session.commit()

    data = {
        'message': 'Login actualizado',
        'status': 200,
        'data': {
            'login_id': login.id,
            'correo': login.correo,
            'contrasena': login.contrasena
        }
    }

    return make_response(jsonify(data), 200)

@respuestas_login_routes.route('/login/<int:login_id>', methods=['DELETE'])
def delete_login(login_id):
    login = Login.query.get(login_id)

    if not login:
        data = {
            'message': 'Login no encontrado',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)

    db.session.delete(login)
    db.session.commit()

    data = {
        'message': 'Login eliminado',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)