from app.db import db
from app.models import BaseModel



class Cliente(BaseModel):
    __tablename__ = 'cliente'
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    
    facturas = db.Relationship('Factura', backref='cliente', lazy=True)
    
    def __init__(self, nombre, direccion, telefono, correo, fecha_nacimiento, tipo):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo = tipo