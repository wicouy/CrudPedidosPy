# src/models/cliente.py
from src.models import db

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    
    idCliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    apellido = db.Column(db.String(150), nullable=False)
    direccion = db.Column(db.String(250), nullable=False)
    telefono = db.Column(db.String(25), nullable=False)
    detalle = db.Column(db.String(150), nullable=False)
    otro = db.Column(db.String(250), nullable=True)

    # Relación con Pedido
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

    def to_dict(self):
        return {
            'idCliente': self.idCliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'detalle': self.detalle,
            'otro': self.otro
        }

    def __repr__(self):
        return f'<Cliente {self.nombre} {self.apellido}>'
