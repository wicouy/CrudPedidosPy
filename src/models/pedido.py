# src/models/pedido.py
from src.models import db
from src.models.cliente import Cliente
from sqlalchemy import Column, Integer, String, Date

class Pedido(db.Model):
    __tablename__ = 'Pedido'

    nroPedido = db.Column(db.Integer, primary_key=True)
    idCliente = db.Column(db.Integer, db.ForeignKey('Cliente.idCliente'), nullable=False)
    direccion = db.Column(db.String(250), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    pedido = db.Column(db.String(150), nullable=False)
    movil = db.Column(db.String(50), nullable=False)
    tipoPago = db.Column(db.String(25), nullable=False)
    estado = db.Column(db.String(15), nullable=False)
    local = db.Column(db.String(25), nullable=False)
    otro = db.Column(db.String(250), nullable=True)

 
    def to_dict(self):
        return {
            'idCliente': self.idCliente,
            'direccion': self.direccion,
            'fecha': self.fecha,
            'pedido': self.pedido,
            'movil': self.movil,
            'tipoPago': self.tipoPago,
            'estado': self.estado,
            'local': self.local,
            'otro': self.otro
        }

def __repr__(self):
 return f'<Pedido {self.nroPedido}>'
