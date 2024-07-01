from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.color import Color

color_routes = Blueprint("color_routes", __name__)

@color_routes.route('/color', methods=['POST'])
def create_color():
    color_data = request.json

    color = Color(color_data['nombre'], color_data['css'])
    db.session.add(color)
    db.session.commit()

    data = {
        'message': 'Color creado',
        'status': 201,
        'data': {
            'colorid': color.colorid,
            'nombre': color.nombre,
            'css': color.css
        }
    }

    return make_response(jsonify(data), 201)

@color_routes.route('/color', methods=['GET'])
def get_color():
    colores = Color.query.all()
    data = {
        'message': 'Todos los colores',
        'status': 200,
        'data': [
            {
                'colorid': color.colorid,
                'nombre': color.nombre,
                'css': color.css
            } for color in colores
        ]
    }

    return make_response(jsonify(data), 200)