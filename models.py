from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contraseña_hash = db.Column(db.String(128), nullable=False)
    es_admin = db.Column(db.Boolean, default=False)
    reset_token = db.Column(db.String(128), nullable=True)
    reset_token_expiracion = db.Column(db.DateTime, nullable=True)

    def set_password(self, contraseña_plana):
        self.contraseña_hash = generate_password_hash(contraseña_plana)

    def check_password(self, contraseña_plana):
        return check_password_hash(self.contraseña_hash, contraseña_plana)
