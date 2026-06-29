from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model): # <--- 'Model' con M mayúscula
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    rol = db.Column(db.Enum('cliente', 'admin', name='roles_enum'), default='cliente') # <--- Nombre al Enum
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.now) # <--- Sin paréntesis '()'

    # -- Métodos de contraseña
    def set_password(self, password_plano):
        """ Hash a la contraseña en texto plano """
        self.password = generate_password_hash(password_plano)
    
    def check_password(self, passwd):
        """ Compara el texto plano con la contraseña hash """
        return check_password_hash(self.password, passwd) # <--- Corregido el parámetro y la variable
    
    def es_admin(self):
        return self.rol == "admin"
    
    def __repr__(self):
        return f'<Usuario {self.email} | {self.rol}>'