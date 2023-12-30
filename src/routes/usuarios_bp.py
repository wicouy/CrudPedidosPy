# src/routes/usuarios_bp.py
from flask import Blueprint
from flask_jwt_extended import jwt_required
from .usuarios import (get_usuarios, get_usuario_id, add_usuario, update_usuario, delete_usuario)

usuarios_bp = Blueprint('usuarios', __name__)

# Agrega la protección JWT antes de ejecutar las rutas del Blueprint
@usuarios_bp.before_request
@jwt_required()
def check_jwt():
    pass

@usuarios_bp.route('/usuarios', methods=['GET'])
def route_get_usuarios():
    return get_usuarios()

@usuarios_bp.route('/usuario/<int:id>', methods=['GET'])
def route_get_usuario_id(id):
    return get_usuario_id(id)

@usuarios_bp.route('/usuarios', methods=['POST'])
def route_add_usuario():
    return add_usuario()

@usuarios_bp.route('/usuario/<int:id>', methods=['PUT'])
def route_update_usuario(id):
    return update_usuario(id)

@usuarios_bp.route('/usuario/<int:id>', methods=['DELETE'])
def route_delete_usuario(id):
    return delete_usuario(id)
