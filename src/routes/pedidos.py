# src/routes/pedidos.py
from flask import request, jsonify
from sqlalchemy import or_
from ..models.cliente import Cliente
from src.models import db
from src.models.pedido import Pedido
from datetime import datetime


# Obtener todos los pedidos
def get_pedidos():
    pedidos = Pedido.query.all()
    pedidos_dict = []

    for pedido in pedidos:
        # Obtén la fecha en el formato "DD/MM/YYYY HH:MM"
        fecha_formateada = pedido.fecha.strftime("%d/%m/%Y %H:%M")

        # Crea el diccionario para este pedido con la fecha formateada
        pedido_dict = {
            "nroPedido": pedido.nroPedido,
            "idCliente": pedido.idCliente,
            "direccion": pedido.direccion,
            "fecha": fecha_formateada,  # Fecha formateada
            "pedido": pedido.pedido,
            "movil": pedido.movil,
            "tipoPago": pedido.tipoPago,
            "estado": pedido.estado,
            "local": pedido.local,
            "otro": pedido.otro
        }

        pedidos_dict.append(pedido_dict)

    return jsonify(pedidos_dict), 200


# Obtener un pedido específico por número de pedido
def get_pedido_nro(nroPedido):
    pedido = Pedido.query.get(nroPedido)
    if pedido:
        return jsonify(pedido.to_dict()), 200
    return jsonify({'mensaje': 'Pedido no encontrado'}), 404

def get_pedido_idCliente(idCliente, cantidad=10, pagina=1):
    pedidos = Pedido.query.filter_by(idCliente=idCliente).order_by(Pedido.fecha.desc()).paginate(page=pagina, per_page=cantidad)
    return jsonify([pedido.to_dict() for pedido in pedidos.items]), 200, {'X-Total-Count': pedidos.total}

# Obtener un pedido específico por número de teléfono del cliente    
def get_pedido_telefonoCliente(telefono):
    cantidad = request.args.get('cantidad', default=10, type=int)

    # Realiza una consulta para encontrar al cliente con el número de teléfono dado
    cliente = Cliente.query.filter_by(telefono=telefono).first()

    if cliente is not None:
        # Si se encuentra un cliente con ese número de teléfono, busca los pedidos relacionados
        pedidos = Pedido.query.filter_by(idCliente=cliente.idCliente).order_by(Pedido.fecha.desc()).limit(cantidad).all()
        
        # Convierte los resultados a un formato JSON
        pedidos_json = [pedido.to_dict() for pedido in pedidos]

        return jsonify(pedidos_json), 200
    else:
        # Si no se encuentra un cliente con ese número de teléfono, devuelve una respuesta adecuada
        return jsonify({"message": "Cliente no encontrado"}), 404



# Agregar un nuevo pedido
def add_pedido():
    data = request.get_json()
    
    # Verificar si el teléfono del cliente existe en la base de datos
    telefono_cliente = data.get('telefono')
    cliente = Cliente.query.filter_by(telefono=telefono_cliente).first()
    
    if not cliente:
        return jsonify({'mensaje': 'Cliente no encontrado'}), 404

    nuevo_pedido = Pedido(
        idCliente=cliente.idCliente,
        direccion=data['direccion'],
        fecha=data['fecha'],
        pedido=data['pedido'],
        movil=data['movil'],
        tipoPago=data['tipoPago'],
        estado=data['estado'],
        local=data['local'],
        otro=data['otro']
    )
    db.session.add(nuevo_pedido)
    db.session.commit()
    return jsonify(nuevo_pedido.to_dict()), 201


# Actualizar un pedido
def update_pedido(nroPedido):
    data = request.get_json()
    pedido = Pedido.query.get(nroPedido)
    if not pedido:
        return jsonify({'mensaje': 'Pedido no encontrado'}), 404

    # Actualiza los campos del pedido con los nuevos valores
    if 'idCliente' in data:
        pedido.idCliente = data['idCliente']

    if 'direccion' in data:
        pedido.direccion = data['direccion']

    if 'fecha' in data:
        pedido.fecha = data['fecha']

    if 'pedido' in data:
        pedido.pedido = data['pedido']

    if 'movil' in data:
        pedido.movil = data['movil']

    if 'tipoPago' in data:
        pedido.tipoPago = data['tipoPago']

    if 'estado' in data:
        pedido.estado = data['estado']

    if 'local' in data:
        pedido.local = data['local']

    if 'otro' in data:
        pedido.otro = data['otro']

    # Guarda los cambios en la base de datos
    db.session.commit()

    # Devuelve una respuesta exitosa con los datos actualizados
    return jsonify(pedido.to_dict()), 200



# Eliminar un pedido
def delete_pedido(nroPedido):
    pedido = Pedido.query.get(nroPedido)
    if not pedido:
        return jsonify({'mensaje': 'Pedido no encontrado'}), 404

    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'mensaje': 'Pedido eliminado'}), 200
