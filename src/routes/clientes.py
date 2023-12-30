# src/routes/clientes.py
from flask import request, jsonify
from src.models.pedido import DuendePedido
from src.models import db
from src.models.cliente import DuendeCliente

# Obtener todos los clientes
def get_clientes():
    clientes = DuendeCliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes]), 200

# Obtener un cliente específico por id
def get_cliente_id(id):
    cliente = DuendeCliente.query.get(id)
    if cliente:
        return jsonify(cliente.to_dict()), 200
    return jsonify({'mensaje': 'Cliente no encontrado'}), 404

# Obtener un cliente específico por telefono
def get_cliente_telefono(telefono):
    cliente = DuendeCliente.query.filter_by(telefono=telefono.strip()).first()
    print (telefono)

    if cliente:
        return jsonify(cliente.to_dict()), 200
    return jsonify({'mensaje': 'Cliente no encontrado'}), 404

# Agregar un nuevo cliente
def add_cliente():
    data = request.get_json()

    # Eliminar espacios en blanco al principio y al final del número de teléfono
    telefono = data['telefono'].strip()

    # Verificar si el teléfono ya existe en la base de datos
    existing_cliente = DuendeCliente.query.filter_by(telefono=telefono).first()

    if existing_cliente:
        return jsonify({'mensaje': 'El teléfono ya está registrado'}), 400

    nuevo_cliente = DuendeCliente(nombre=data['nombre'], apellido=data['apellido'], direccion=data['direccion'], telefono=telefono, detalle=data['detalle'], otro=data['otro'])
    db.session.add(nuevo_cliente)
    db.session.commit()
    return jsonify(nuevo_cliente.to_dict()), 201

# Actualizar un cliente por teléfono
# Actualizar un cliente por teléfono
def update_cliente(telefono):
    # Obtiene los datos del cliente existente desde la base de datos
    cliente_existente = DuendeCliente.query.filter_by(telefono=telefono).first()

    if cliente_existente is None:
        # Si el cliente no existe, devuelve un mensaje de error
        return jsonify({"message": "Cliente no encontrado"}), 404

    # Obtén los datos que deseas actualizar desde la solicitud JSON
    datos_actualizados = request.get_json()

    # Verifica si el nuevo número de teléfono ya existe en la base de datos
    nuevo_telefono = datos_actualizados.get('telefono')
    if nuevo_telefono and nuevo_telefono != cliente_existente.telefono:
        cliente_existente = DuendeCliente.query.filter_by(telefono=nuevo_telefono).first()
        if cliente_existente:
            return jsonify({"message": "Ya existe un cliente con ese número de teléfono"}), 400

    # Actualiza los campos del cliente con los nuevos valores
    if 'nombre' in datos_actualizados:
        cliente_existente.nombre = datos_actualizados['nombre']

    if 'apellido' in datos_actualizados:
        cliente_existente.apellido = datos_actualizados['apellido']

    if 'direccion' in datos_actualizados:
        cliente_existente.direccion = datos_actualizados['direccion']

    if 'telefono' in datos_actualizados:
        cliente_existente.telefono = datos_actualizados['telefono']

    if 'detalle' in datos_actualizados:
        cliente_existente.detalle = datos_actualizados['detalle']

    if 'otro' in datos_actualizados:
        cliente_existente.otro = datos_actualizados['otro']

    # Guarda los cambios en la base de datos
    db.session.commit()

    # Devuelve una respuesta exitosa
    return jsonify({"message": "Cliente actualizado exitosamente"}), 200


# Eliminar un cliente por teléfono
def delete_cliente(telefono):
    cliente = DuendeCliente.query.filter_by(telefono=telefono).first()
    if not cliente:
        return jsonify({'mensaje': 'Cliente no encontrado'}), 404

    # Verificar si existen pedidos pendientes asociados a este cliente
    pedidos_pendientes = DuendePedido.query.filter_by(idCliente=cliente.idCliente, estado='pendiente').first()
    if pedidos_pendientes:
        return jsonify({'mensaje': 'No se puede eliminar el cliente debido a que tiene pedidos pendientes'}), 400

    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente eliminado'}), 200
