from app.config.db import db
from app.models.producto import Producto

class Copa(Producto):
    __tablename__ = None  
    __mapper_args__ = {
        'polymorphic_identity': 'copa' 
    }

    tipo_vaso = db.Column(db.String(50))

    def __repr__(self):
        return f'<Copa {self.nombre}>'
