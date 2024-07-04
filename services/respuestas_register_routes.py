from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.persona import Persona
from model.usuario import Usuario
from model.ubigeo import Ubigeo
from model.diagnosticos import Diagnosticos

respuestas_register_routes = Blueprint("respuestas_register_routes", __name__)

@respuestas_register_routes.route('/register', methods=['POST'])
def register():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    nombre = request.json['nombre']
    apellidopaterno = request.json['apellidopaterno']
    apellidomaterno = request.json['apellidomaterno']
    fechanacimiento = request.json['fechanacimiento']
    departamento = request.json['departamento']
    provincia = request.json['provincia']
    distrito = request.json['distrito']
    tipousuarioid = request.json['tipousuarioid']
    
    ubigeo = Ubigeo.query.filter_by(departamento=departamento, provincia=provincia, distrito=distrito).first()

    if ubigeo:
        ubigeoid = ubigeo.ubigeoid
    else:
        ubigeoid = None

    new_persona = Persona(nombre=nombre, apellidopaterno=apellidopaterno, apellidomaterno=apellidomaterno, fechanacimiento=fechanacimiento, ubigeoid=ubigeoid)
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
            'fechanacimiento': new_persona.fechanacimiento,
            'ubigeoid': new_persona.ubigeoid
        }
    }

    return make_response(jsonify(data), 201)


@respuestas_register_routes.route('/persona/<int:persona_id>', methods=['GET'])
def get_persona_by_id(persona_id):
    persona = Persona.query.filter_by(persona_id=persona_id).first()
    if persona:
        data = {
            'message': 'Persona encontrada',
            'status': 200,
            'data': {
                'persona_id': persona.persona_id,
                'nombre': persona.nombre,
                'apellidopaterno': persona.apellidopaterno,
                'apellidomaterno': persona.apellidomaterno,
                'fechanacimiento': persona.fechanacimiento,
                'ubigeoid': persona.ubigeoid
            }
        }
    else:
        data = {
            'message': 'Persona no encontrada',
            'status': 404,
            'data': None
        }
    return make_response(jsonify(data), data['status'])
