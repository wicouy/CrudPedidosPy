# src/routes/pedidos_bp.py
from flask import Blueprint
from flask_jwt_extended import jwt_required
from .pedidos import get_pedido_idCliente, get_pedido_telefonoCliente, get_pedidos, get_pedido_nro, add_pedido, update_pedido, delete_pedido

pedidos_bp = Blueprint('pedidos', __name__)

# Agrega la protección JWT antes de ejecutar las rutas del Blueprint
@pedidos_bp.before_request
@jwt_required()
def check_jwt():
    pass

@pedidos_bp.route('/pedidos', methods=['GET'])
def route_get_pedidos():
    return get_pedidos()

@pedidos_bp.route('/pedido/nroPedido/<int:nroPedido>', methods=['GET'])
def route_get_pedido_nro(nroPedido):
    return get_pedido_nro(nroPedido)

@pedidos_bp.route('/pedido/idCliente/<int:idCliente>', methods=['GET'])
def route_get_pedido_idCliente(idCliente):
    return get_pedido_idCliente(idCliente)

@pedidos_bp.route('/pedido/telefonoCliente/<string:telefono>', methods=['GET'])
def route_get_pedido_telefonoCliente(telefono):
    return get_pedido_telefonoCliente(telefono)

@pedidos_bp.route('/pedidos', methods=['POST'])
def route_add_pedido():
    return add_pedido()

@pedidos_bp.route('/pedido/<int:nroPedido>', methods=['PUT'])
def route_update_pedido(nroPedido):
    return update_pedido(nroPedido)

@pedidos_bp.route('/pedido/<int:nroPedido>', methods=['DELETE'])
def route_delete_pedido(nroPedido):
    return delete_pedido(nroPedido)
