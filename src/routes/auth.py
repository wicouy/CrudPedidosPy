# src/routes/auth.py

from flask import app, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.models.usuario  import Usuario  # Asegúrate de importar tu modelo de Usuario

@jwt_required()  # Esto protegerá la ruta, requiriendo un token válido
@app.route('/usuarios/token', methods=['POST'])
def create_token():
    # Obtén la identidad del usuario desde el token JWT
    current_user_id = get_jwt_identity()

    # Busca al usuario en la base de datos (asumiendo que tienes un modelo Usuario)
    user = Usuario.query.get(current_user_id)

    # Verifica que el usuario esté activo (personaliza esto según tu modelo)
    if not user or not user.is_active:
        return jsonify({"message": "Usuario inactivo"}), 401

    # Genera un nuevo token JWT para el usuario autenticado
    access_token = create_access_token(identity=current_user_id)

    # Retorna el token JWT en la respuesta
    return jsonify(access_token=access_token), 200
