# src/routes/roles.py
from flask import request, jsonify
from src.models import db
from src.models.roles import Roles

# Obtener todos los roles
def get_roles():
    roles = Roles.query.all()
    return jsonify([rol.to_dict() for rol in roles]), 200

# Obtener un rol específico por ID
def get_rol_id(id):
    rol = Roles.query.get(id)
    if rol:
        return jsonify(rol.to_dict()), 200
    return jsonify({'mensaje': 'Rol no encontrado'}), 404

# Agregar un nuevo rol
def add_rol():
    data = request.get_json()
    nuevo_rol = Roles(nombre=data['nombre'])

    db.session.add(nuevo_rol)
    db.session.commit()
    return jsonify(nuevo_rol.to_dict()), 201


# Actualizar un rol
def update_rol(id):
    rol = Roles.query.get(id)
    if not rol:
        return jsonify({'mensaje': 'Rol no encontrado'}), 404

    datos_actualizados = request.get_json()
    rol.nombre = datos_actualizados['nombre']  # Actualiza el nombre del rol con el nuevo valor

    db.session.commit()
    return jsonify({"message": "Rol actualizado exitosamente"}), 200

# Eliminar un rol
def delete_rol(id):
    rol = Roles.query.get(id)
    if not rol:
        return jsonify({'mensaje': 'Rol no encontrado'}), 404

    db.session.delete(rol)
    db.session.commit()
    return jsonify({'mensaje': 'Rol eliminado'}), 200
