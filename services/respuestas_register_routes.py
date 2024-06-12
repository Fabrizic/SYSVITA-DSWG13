from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.register import Persona
from model.login import Login

respuestas_register_routes = Blueprint("respuestas_register_routes", __name__)

@respuestas_register_routes.route('/register', methods=['POST'])
def register():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    nombre = request.json['nombre']
    apellidopaterno = request.json['apellidopaterno']
    apellidomaterno = request.json['apellidomaterno']
    fechanacimiento = request.json['fechanacimiento']

    new_login = Login(correo, contrasena)
    db.session.add(new_login)
    db.session.commit()

    new_persona = Persona(id=new_login.id, nombre=nombre, apellidopaterno=apellidopaterno, apellidomaterno=apellidomaterno, fechanacimiento=fechanacimiento)
    db.session.add(new_persona)
    db.session.commit()

    data = {
        'message': 'Registro exitoso',
        'status': 201,
        'data': {
            'login_id': new_login.id,
            'correo': new_login.correo,
            'nombre': new_persona.nombre,
            'apellidopaterno': new_persona.apellidopaterno,
            'apellidomaterno': new_persona.apellidomaterno,
            'fechanacimiento': new_persona.fechanacimiento
        }
    }

    return make_response(jsonify(data), 201)