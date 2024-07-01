from flask import Flask
from flask_cors import CORS
from utils.db import db
from services.respuestas_login_routes import respuestas_login_routes
from services.respuestas_register_routes import respuestas_register_routes
from services.preguntas_routes import preguntas_routes
from services.respuestas_routes import respuestas_routes
from services.test_routes import tests_routes
from services.respuestasusuario_routes import respuestasusuario_routes
from services.realizartest_routes import realizartest_routes
from services.tipousuario_routes import tipousuario_routes
from services.puntuacion_routes import puntuacion_routes
from services.ubigeo_routes import ubigeo_routes
from services.color_routes import color_routes
from services.diagnostico_routes import diagnostico_routes
from config import DATABASE_CONNECTION

app = Flask(__name__)
CORS(app)# o poner CORS(app, origins='*') para permitir todas las conexiones
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(respuestas_login_routes)
app.register_blueprint(respuestas_register_routes)
app.register_blueprint(preguntas_routes)
app.register_blueprint(respuestas_routes)
app.register_blueprint(tests_routes)
app.register_blueprint(respuestasusuario_routes)
app.register_blueprint(realizartest_routes)
app.register_blueprint(tipousuario_routes)
app.register_blueprint(puntuacion_routes)
app.register_blueprint(ubigeo_routes)
app.register_blueprint(color_routes)
app.register_blueprint(diagnostico_routes)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)