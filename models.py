from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contraseña_hash = db.Column(db.String(128), nullable=False)
    es_admin = db.Column(db.Boolean, default=False)
    reset_token = db.Column(db.String(128), nullable=True)
    reset_token_expiracion = db.Column(db.DateTime, nullable=True)
    
    # Campos adicionales para el perfil y certificados
    apellidos = db.Column(db.String(100), nullable=True)
    tipo_documento = db.Column(db.String(20), nullable=True)  # CC, TI, CE, Pasaporte
    numero_documento = db.Column(db.String(50), nullable=True)
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    ciudad = db.Column(db.String(100), nullable=True)
    pais = db.Column(db.String(100), nullable=True)
    foto_perfil = db.Column(db.String(200), nullable=True)  # URL o ruta de la foto

    def set_password(self, contraseña_plana):
        self.contraseña_hash = generate_password_hash(contraseña_plana)

    def check_password(self, contraseña_plana):
        return check_password_hash(self.contraseña_hash, contraseña_plana)


class ClaseCompletada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    curso_slug = db.Column(db.String(100), nullable=False)
    clase_slug = db.Column(db.String(100), nullable=False)
    fecha_completado = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con Usuario
    usuario = db.relationship('Usuario', backref='clases_completadas')
    
    # Índice único para evitar duplicados
    __table_args__ = (db.UniqueConstraint('usuario_id', 'curso_slug', 'clase_slug', name='_usuario_curso_clase_uc'),)

