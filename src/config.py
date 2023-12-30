# src/config.py
import os

class Config:
    # Configuración para la conexión a la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://USER:PASS@IP:PORT/dbName'
    
    # Si quieres rastrear modificaciones de objetos y emitir señales
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Configuración para JWT
    JWT_SECRET_KEY = 'soy_una_papa'  # Cambia esto por una clave secreta real
    
    # Duración de los tokens de acceso en segundos (30 minutos)
    JWT_ACCESS_TOKEN_EXPIRES = 1800
    
    # Opcional: Duración de los tokens de actualización en segundos (por ejemplo, 1 hora)
    JWT_REFRESH_TOKEN_EXPIRES = 3600
