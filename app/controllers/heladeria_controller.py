from app.models.base import Base
from app.models.complemento import Complemento
from app.models.copa import Copa
from app.models.malteada import Malteada
from app.models.heladeria import Heladeria
from app.models.producto import Producto

class HeladeriaController:
    def __init__(self, app, db):
        self.app = app
        self.db = db
        self.heladeria = Heladeria("DG Heladería")
        self._agregar_productos()

    def _agregar_productos(self):
        with self.app.app_context():
            # Verificar si ya existen productos en la base de datos
            if Producto.query.count() == 0:
                # Ingredientes
                helado_de_vainilla = Base(nombre="helado de Vainilla", precio=1200, calorias=100, inventario=2.0, es_vegetariano=False, sabor="vainilla")
                helado_de_chocolate = Base(nombre="helado de Chocolate", precio=1500, calorias=250, inventario=6.0, es_vegetariano=False, sabor="chocolate")
                frutas_mixtas = Base(nombre="Frutas mixtas", precio=2000, calorias=50, inventario=1.0, es_vegetariano=True, sabor="fruta")
                fresas = Base(nombre="Fresas", precio=1500, calorias=35, inventario=3.0, es_vegetariano=True, sabor="fresa")
                mani_japones = Complemento(nombre="Mani Japones", precio=700, calorias=35, inventario=6.0, es_vegetariano=True)
                sirope_de_caramelo = Complemento(nombre="Sirope de Caramelo", precio=1000, calorias=200, inventario=2.0, es_vegetariano=False)
                sirope_de_fresa = Complemento(nombre="Sirope de Fresa", precio=1000, calorias=200, inventario=8.0, es_vegetariano=False)
                crema_de_leche = Complemento(nombre="Crema de Leche", precio=700, calorias=150, inventario=7.0, es_vegetariano=False)
                nuez_moscada = Complemento(nombre="Nuez Moscada", precio=700, calorias=40, inventario=1.0, es_vegetariano=True)

                # Productos
                malteada_de_vainilla = Malteada(nombre="Malteada de Vainilla", precio_publico=7500, ingredientes=[helado_de_vainilla, sirope_de_fresa, mani_japones], volumen=7)
                malteada_choconuez = Malteada(nombre="Malteada Choconuez", precio_publico=10000, ingredientes=[helado_de_chocolate, nuez_moscada, sirope_de_caramelo], volumen=8)
                champions_de_frutas = Copa(nombre="Champions de Frutas", precio_publico=7000, ingredientes=[frutas_mixtas, crema_de_leche, sirope_de_caramelo], tipo_vaso="Vaso de Vidrio")
                explosion_de_fresa = Copa(nombre="Explosión de Fresa", precio_publico=5000, ingredientes=[fresas, crema_de_leche, sirope_de_fresa], tipo_vaso="Vaso de Plástico")

                # Guardar en la base de datos
                self.db.session.add_all([helado_de_vainilla, helado_de_chocolate, frutas_mixtas, fresas, mani_japones, sirope_de_caramelo, sirope_de_fresa, crema_de_leche, nuez_moscada])
                self.db.session.add_all([malteada_de_vainilla, malteada_choconuez, champions_de_frutas, explosion_de_fresa])
                self.db.session.commit()

    def listar_productos(self):
        with self.app.app_context():
            # Consultar los productos directamente desde la base de datos
            return Producto.query.all()