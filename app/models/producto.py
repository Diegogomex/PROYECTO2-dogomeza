from app.config.db import db
from app.models.producto_ingrediente import producto_ingrediente

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio_publico = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50))  # Columna para manejar la herencia

    # Relación con la tabla de ingredientes
    ingredientes = db.relationship('Ingrediente', secondary=producto_ingrediente, back_populates='productos')

    __mapper_args__ = {
        'polymorphic_on': type  
    }

    def __repr__(self):
        return f'<Producto {self.nombre}>'
