from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.puntuacion import Puntuacion
from model.color import Color

puntuacion_routes = Blueprint("puntuacion_routes", __name__)

@puntuacion_routes.route('/puntuacion', methods=['POST'])
def create_puntuaciones():
    puntuaciones_data = request.json 
    puntuaciones_creadas = []

    puntuaciones_instancias = []

    for puntuacion_data in puntuaciones_data:
        testid = puntuacion_data['testid']
        rango_inferior = puntuacion_data['rango_inferior']
        rango_superior = puntuacion_data['rango_superior']
        diagnostico = puntuacion_data['diagnostico']
        colorid = puntuacion_data['colorid']

        puntuacion = Puntuacion(testid, rango_inferior, rango_superior, diagnostico,colorid)
        db.session.add(puntuacion)
        puntuaciones_instancias.append(puntuacion)

    db.session.commit() 

    for puntuacion in puntuaciones_instancias:
        puntuaciones_creadas.append({
            'puntuacionid': puntuacion.puntuacionid,  # Ahora esto debería funcionar correctamente
            'testid': puntuacion.testid,
            'rango_inferior': puntuacion.rango_inferior,
            'rango_superior': puntuacion.rango_superior,
            'diagnostico': puntuacion.diagnostico,
            'colorid': puntuacion.colorid
        })

    data = {
        'message': 'Puntuaciones creadas',
        'status': 201,
        'data': puntuaciones_creadas
    }

    return make_response(jsonify(data), 201)

@puntuacion_routes.route('/puntuacion', methods=['GET'])
def get_puntuaciones():
    puntuaciones = Puntuacion.query.all()
    data = {
        'message': 'Todas las puntuaciones',
        'status': 200,
        'data': [
            {
                'puntuacionid': puntuacion.puntuacionid,
                'testid': puntuacion.testid,
                'rango_inferior': puntuacion.rango_inferior,
                'rango_superior': puntuacion.rango_superior,
                'diagnostico': puntuacion.diagnostico,
                'colorid': puntuacion.colorid
            } for puntuacion in puntuaciones
        ]
    }

    return make_response(jsonify(data), 200)

@puntuacion_routes.route('/puntuacionindividual', methods=['POST'])
def create_puntuacionindividual():
    puntuacion_data = request.json

    testid = puntuacion_data['testid']
    rango_inferior = puntuacion_data['rango_inferior']
    rango_superior = puntuacion_data['rango_superior']
    diagnostico = puntuacion_data['diagnostico']
    css = puntuacion_data['css']

    # Crear un nuevo registro en la tabla Color
    nuevo_color = Color(css=css)  # Asumiendo que el modelo Color tiene un campo 'css'
    db.session.add(nuevo_color)
    try:
        db.session.commit()
        colorid = nuevo_color.colorid  # Obtener el id del nuevo color insertado

        # Crear la nueva puntuación con el colorid obtenido
        nueva_puntuacion = Puntuacion(testid=testid, rango_inferior=rango_inferior, rango_superior=rango_superior, diagnostico=diagnostico, colorid=colorid)
        db.session.add(nueva_puntuacion)
        db.session.commit()

        # Resto del código para manejar la respuesta exitosa
    except Exception as e:
        db.session.rollback()
        print(f"Error al insertar en la base de datos: {e}")
        return jsonify({"error": "No se pudo crear la puntuación individual"}), 500

    # Si todo fue exitoso, retornar la puntuación creada
    return jsonify({
        "mensaje": "Puntuación individual creada exitosamente",
        "puntuacion": {
            "testid": testid,
            "rango_inferior": rango_inferior,
            "rango_superior": rango_superior,
            "diagnostico": diagnostico,
            "colorid": colorid
        }
    }), 201