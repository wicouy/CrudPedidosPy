# src/routes/usuarios.py
from flask import request, jsonify
from src.models import db
from src.models.roles import Roles
from src.models.usuario import Usuario  # Asegúrate de que este modelo esté correctamente definido
from flask import Blueprint

# Obtener todos los usuarios
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

# Obtener un usuario específico por ID
def get_usuario_id(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify(usuario.to_dict()), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

# Agregar un nuevo usuario
def add_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(username=data['username'])
    nuevo_usuario.set_password(data['password'])  # Asegúrate de tener un método para configurar la contraseña

    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201

# Actualizar un usuario
def update_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    datos_actualizados = request.get_json()
    if 'username' in datos_actualizados:
        usuario.username = datos_actualizados['username']
    if 'password' in datos_actualizados:
        usuario.set_password(datos_actualizados['password'])  # Asume que tienes un método set_password

    db.session.commit()
    return jsonify({"message": "Usuario actualizado exitosamente"}), 200

# Eliminar un usuario
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado'}), 200

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def route_get_usuarios():
    return get_usuarios()

@usuarios_bp.route('/usuario/<int:id>', methods=['GET'])
def route_get_usuario_id(id):
    return get_usuario_id(id)

def add_usuario():
    data = request.get_json()
    username = data['username']
    password = data['password']
    rol_id = data.get('rol_id')  # Puede ser None si no se proporciona

    # Verificar que la contraseña no esté vacía
    if not password:
        return jsonify({'mensaje': 'La contraseña no puede estar vacía'}), 400

    # Verificar si el rol existe
    rol = Roles.query.get(rol_id)
    if not rol:
        return jsonify({'mensaje': 'El rol especificado no existe'}), 404

    # Verificar si el usuario ya existe
    usuario_existente = Usuario.query.filter_by(username=username).first()
    if usuario_existente:
        return jsonify({'mensaje': 'El usuario ya existe'}), 400

    nuevo_usuario = Usuario(username=username, rol_id=rol_id)
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201


@usuarios_bp.route('/usuario/<int:id>', methods=['PUT'])
def route_update_usuario(id):
    return update_usuario(id)

@usuarios_bp.route('/usuario/<int:id>', methods=['DELETE'])
def route_delete_usuario(id):
    return delete_usuario(id)
