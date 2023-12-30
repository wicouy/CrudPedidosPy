from src.models import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'Usuario'  # Reemplaza con el nombre real de tu tabla

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(512), nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('Roles.id'), nullable=True)  # Asume una tabla de roles

    # Relación con Roles (asegúrate de que el nombre de la clase sea 'Roles' y no 'roles')
    rol = db.relationship('Roles', backref='usuarios', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'is_active': self.is_active,
            'rol_id': self.rol_id 
        }
    