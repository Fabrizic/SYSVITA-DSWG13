from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from werkzeug.security import generate_password_hash
from model.login import Login

respuestas_login_routes = Blueprint("respuestas_login_routes", __name__)

@respuestas_login_routes.route('/login', methods=['POST'])
def create_login():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    contrasena_encriptada = generate_password_hash(contrasena)

    login = Login.query.filter_by(correo=correo, contrasena=contrasena_encriptada).first()

    if not login:
        new_login = Login(None, correo, contrasena_encriptada)
        db.session.add(new_login)
        db.session.commit()

        data = {
            'message': 'Login creado',
            'status': 201,
            'data': {
                'login_id': new_login.login_id,
                'correo': new_login.correo,
                'contrasena': new_login.contrasena
            }
        }

        return make_response(jsonify(data), 201)

    data = {
        'message': 'Login ya existe',
        'status': 400,
        'data': {
            'login_id': login.login_id,
            'correo': login.correo,
            'contrasena': login.contrasena
        }
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
                'login_id': login.login_id,
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
            'login_id': login.login_id,
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
    login.contrasena = generate_password_hash(request.json['contrasena'])
    db.session.commit()

    data = {
        'message': 'Login actualizado',
        'status': 200,
        'data': {
            'login_id': login.login_id,
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
