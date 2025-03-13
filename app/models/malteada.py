from app.config.db import db
from app.models.producto import Producto

class Malteada(Producto):
    __tablename__ = None  
    __mapper_args__ = {
        'polymorphic_identity': 'malteada' 
    }

    volumen = db.Column(db.Integer)

    def __repr__(self):
        return f'<Malteada {self.nombre}>'
    
