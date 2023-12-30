# src/routes/roles_bp.py
from flask import Blueprint
from flask_jwt_extended import jwt_required
from .roles import get_roles, get_rol_id, add_rol, update_rol, delete_rol
from src.models.roles import Roles  # Importa la clase Roles desde el módulo correcto

roles_bp = Blueprint('roles', __name__)

# Agrega la protección JWT antes de ejecutar las rutas del Blueprint
@roles_bp.before_request
@jwt_required()
def check_jwt():
    pass

@roles_bp.route('/roles', methods=['GET'])
def route_get_roles():
    return get_roles()

@roles_bp.route('/rol/<int:id>', methods=['GET'])
def route_get_rol_id(id):
    return get_rol_id(id)

@roles_bp.route('/roles', methods=['POST'])
def route_add_rol():
    return add_rol()

@roles_bp.route('/rol/<int:id>', methods=['PUT'])
def route_update_rol(id):
    return update_rol(id)

@roles_bp.route('/rol/<int:id>', methods=['DELETE'])
def route_delete_rol(id):
    return delete_rol(id)
