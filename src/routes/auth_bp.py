# Importa los módulos necesarios
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from src.models.usuario import Usuario  # Asegúrate de importar tu modelo de Usuario

auth_bp = Blueprint('auth', __name__)  # Define el Blueprint de autenticación

@auth_bp.route('/usuarios/token', methods=['POST'])
def create_token():
    # Obtiene las credenciales del usuario desde la solicitud POST
    credentials = request.get_json()

    # Verifica que se proporcionaron las credenciales
    if not credentials or 'username' not in credentials or 'password' not in credentials:
        return jsonify({"message": "Credenciales inválidas"}), 400

    # Obtiene el usuario por nombre de usuario (personaliza esto según tu modelo)
    user = Usuario.query.filter_by(username=credentials['username']).first()

    # Verifica si el usuario existe y si la contraseña es correcta
    if user and user.check_password(credentials['password']) and user.is_active:
        # Genera un nuevo token JWT para el usuario autenticado
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Credenciales inválidas o usuario inactivo"}), 401
