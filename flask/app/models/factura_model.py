from app.db import db
from app.models import BaseModel


class Factura(BaseModel):
    __tablename__ = 'factura'
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    igv = db.Column(db.Float, nullable=False, default=0)
    total = db.Column(db.Float, nullable=False)
    
    detalles = db.relationship('FacturaProducto', backref='factura', lazy=True)
    
    
    def __init__(self, cliente_id, fecha, subtotal, total):
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.total = total
        self.subtotal = subtotal
        self.igv = 0
        
        
class FacturaProducto(BaseModel):
    __tablename__ = 'factura_producto'
    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    
    def __init__(self, producto_id, precio_unitario, cantidad):
        self.precio_unitario = precio_unitario
        self.producto_id = producto_id
        self.cantidad = cantidad
        