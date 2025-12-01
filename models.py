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
    es_profesor = db.Column(db.Boolean, default=False)
    reset_token = db.Column(db.String(128), nullable=True)
    reset_token_expiracion = db.Column(db.DateTime, nullable=True)
    
    # Campos adicionales para el perfil y certificados
    apellidos = db.Column(db.String(100), nullable=True)
    genero = db.Column(db.String(10), nullable=True)  # hombre, mujer
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


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    profesor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    activo = db.Column(db.Boolean, default=True)
    
    # Relaciones
    profesor = db.relationship('Usuario', backref='cursos_dictados')
    notas = db.relationship('Nota', backref='curso', cascade='all, delete-orphan')


class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    profesor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    tipo_evaluacion = db.Column(db.String(50), nullable=False)  # parcial, final, tarea, etc.
    nota = db.Column(db.Float, nullable=False)  # 0-100
    observaciones = db.Column(db.Text, nullable=True)
    fecha_subida = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, onupdate=datetime.utcnow)
    estado = db.Column(db.String(20), default='publicada')  # publicada, borrador, revisión
    
    # Relaciones
    alumno = db.relationship('Usuario', foreign_keys=[alumno_id], backref='notas_recibidas')
    profesor = db.relationship('Usuario', foreign_keys=[profesor_id], backref='notas_asignadas')
    
    # Índice único para evitar duplicados de mismo tipo
    __table_args__ = (db.UniqueConstraint('alumno_id', 'curso_id', 'tipo_evaluacion', name='_alumno_curso_tipo_uc'),)


class CargaNota(db.Model):
    """Registro de cada carga de notas para auditoría"""
    id = db.Column(db.Integer, primary_key=True)
    profesor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    tipo_evaluacion = db.Column(db.String(50), nullable=False)
    metodo = db.Column(db.String(20), nullable=False)  # archivo, manual
    archivo_original = db.Column(db.String(300), nullable=True)  # nombre del archivo
    cantidad_notas = db.Column(db.Integer, default=0)
    fecha_carga = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    profesor = db.relationship('Usuario', backref='cargas_realizadas')
    curso_rel = db.relationship('Curso', backref='cargas')


class TablaNotasPublicada(db.Model):
    """Tabla de notas publicada en el tablero público"""
    id = db.Column(db.Integer, primary_key=True)
    profesor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    curso_nombre = db.Column(db.String(200), nullable=False)  # Guardamos el nombre para búsquedas rápidas
    imagen_base64 = db.Column(db.Text, nullable=False)  # Imagen de la tabla en base64
    fecha_publicacion = db.Column(db.DateTime, default=datetime.utcnow)
    activa = db.Column(db.Boolean, default=True)  # Para poder ocultar/eliminar sin borrar
    
    # Relaciones
    profesor = db.relationship('Usuario', backref='tablas_publicadas')
    curso = db.relationship('Curso', backref='tablas_publicadas')
