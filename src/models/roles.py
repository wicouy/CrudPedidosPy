from src.models import db

class Roles(db.Model):
    __tablename__ = 'Roles'  # Reemplaza con el nombre real de tu tabla

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        # Define cómo quieres convertir una instancia de Roles en un diccionario.
        return {
            'id': self.id,
            'nombre': self.nombre,
            # Otros campos aquí si los tienes
        }
