from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.persona import Persona
from model.usuario import Usuario

respuestas_register_routes = Blueprint("respuestas_register_routes", __name__)

@respuestas_register_routes.route('/register', methods=['POST'])
def register():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    nombre = request.json['nombre']
    apellidopaterno = request.json['apellidopaterno']
    apellidomaterno = request.json['apellidomaterno']
    fechanacimiento = request.json['fechanacimiento']
    tipousuarioid = request.json['tipousuarioid']

    new_persona = Persona(nombre=nombre, apellidopaterno=apellidopaterno, apellidomaterno=apellidomaterno, fechanacimiento=fechanacimiento)
    db.session.add(new_persona)
    db.session.flush()

    new_Usuario = Usuario(persona_id=new_persona.persona_id,correo=correo,contrasena= contrasena, tipousuarioid=tipousuarioid)
    db.session.add(new_Usuario)
    db.session.commit()

    data = {
        'message': 'Registro exitoso',
        'status': 201,
        'data': {
            'Usuario_id': new_persona.persona_id,
            'tipousuarioid': new_Usuario.tipousuarioid, # 'tipousuarioid': '1' # Especialistas no se pueden registrar
            'correo': new_Usuario.correo,
            'nombre': new_persona.nombre,
            'apellidopaterno': new_persona.apellidopaterno,
            'apellidomaterno': new_persona.apellidomaterno,
            'fechanacimiento': new_persona.fechanacimiento
        }
    }

    return make_response(jsonify(data), 201)