from app.db import db
from app.models import BaseModel

class Category(BaseModel):
    __tablename__ = 'category'
    name = db.Column(db.String(50), nullable=False)
    
    productos = db.relationship('Product', backref='category', lazy=True)
    
    def __init__(self, name):
        self.name = name
        
    
    
class Product(BaseModel):
    __tablename__ = 'product'
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    unit = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)


    detalles = db.relationship('FacturaProducto', backref='producto', lazy=True)
    def __init__(self, name, description, price, unit, category_id):
        self.name = name
        self.description = description
        self.price = price
        self.unit = unit        
        self.category_id = category_id