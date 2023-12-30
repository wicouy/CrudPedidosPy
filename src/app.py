# src/app.py
from flask import Flask
from flask_jwt_extended import JWTManager
from src.models import db
from src.config import Config
from src.routes.usuarios_bp import usuarios_bp
from src.routes.roles_bp import roles_bp
from src.routes.clientes_bp import clientes_bp
from src.routes.pedidos_bp import pedidos_bp
from src.routes.auth_bp import auth_bp

app = Flask(__name__)

# Configuración de la aplicación
app.config.from_object(Config)
db.init_app(app)

# Registrar los Blueprints
app.register_blueprint(clientes_bp, url_prefix='/clientes')
app.register_blueprint(pedidos_bp, url_prefix='/pedidos')
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(roles_bp, url_prefix='/roles')
app.register_blueprint(auth_bp, url_prefix='/auth')  # Registra el Blueprint de autenticación

jwt = JWTManager(app)

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
