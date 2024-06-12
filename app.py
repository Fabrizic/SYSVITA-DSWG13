from flask import Flask
from utils.db import db
from services.respuestas_usuarios_routes import respuestas_usuarios_routes
from services.respuestas_login_routes import respuestas_login_routes
from config import DATABASE_CONNECTION

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(respuestas_usuarios_routes)
app.register_blueprint(respuestas_login_routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)