from app.models.ingrediente import Ingrediente

class Base (Ingrediente):
    def __init__(self, nombre:str, precio:int, calorias:int, inventario:float, es_vegetariano:bool, sabor:str)->None:
        super().__init__(nombre=nombre, precio=precio, calorias=calorias, inventario=inventario, es_vegetariano=es_vegetariano)
        self.__sabor= sabor

    def abastecer(self, cantidad:float)->None:
        """ Abastece el inventario de la base sumando 5. """
        if isinstance(cantidad,(int, float)):
            self.inventario += 5
        else:
            raise ValueError ("La cantidad debe ser un número .")
    
    @property
    def sabor(self) -> str:
        """ Devuelve el valor del atributo privado 'sabor' """
        return self.__sabor
    
    @sabor.setter
    def sabor(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'sabor'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__sabor = value
        else:
            raise ValueError('Expected str')