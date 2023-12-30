# src/routes/clientes_bp.py
from flask import Blueprint
from flask_jwt_extended import jwt_required
from .clientes import get_clientes, get_cliente_id, get_cliente_telefono, add_cliente, update_cliente, delete_cliente

clientes_bp = Blueprint('clientes', __name__)
# Agrega la protección JWT antes de ejecutar las rutas del Blueprint
@clientes_bp.before_request
@jwt_required()
def check_jwt():
    pass

@clientes_bp.route('/clientes', methods=['GET'])
def route_get_clientes():
    return get_clientes()

@clientes_bp.route('/cliente/id/<int:id>', methods=['GET'])
def route_get_cliente_id(id):
    return get_cliente_id(id)

@clientes_bp.route('/cliente/telefono/<string:telefono>', methods=['GET'])
def route_get_cliente_telefono(telefono):
    return get_cliente_telefono(telefono)

@clientes_bp.route('/clientes', methods=['POST'])
def route_add_cliente():
    return add_cliente()

@clientes_bp.route('/clientes/telefonoCliente/<string:telefono>', methods=['PUT'])
def route_update_cliente_telefonoCliente(telefono):
    return update_cliente(telefono)

@clientes_bp.route('/clientes/telefonoCliente/<string:telefono>', methods=['DELETE'])
def route_delete_cliente(telefono):
    return delete_cliente(telefono)
