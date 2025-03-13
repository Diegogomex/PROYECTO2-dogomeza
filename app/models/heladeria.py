from app.models.producto import Producto
from app.models.ingrediente import Ingrediente
from app.models.base import Base 
from app.models.complemento import Complemento

class Heladeria:
    def __init__(self, nombre:str)->None:
        self.__nombre = nombre
        self.__productos = []
        self.__inventario= []
        self.__ventas_dia = 0

    def producto_mas_rentable(self)-> Producto:
        """
        Determina el producto más rentable de la heladería.
        Retorna:
        - IProducto: El producto más rentable.
        """
        if not self.__productos:
            return None
        return max(self.__productos, key=lambda p: p.calcular_rentabilidad())

    def agregar_producto (self, producto: Producto)->None:
        """
        Agrega un producto a la lista de productos.
        Parámetro:
        - producto (Producto): Producto a agregar.
        """
        if len(self.__productos)>=4:
            raise ValueError ('Ya hay 4 productos, no se pueden agregar más')
        self.__productos.append(producto)
    
    def eliminar_producto(self, producto:Producto)->None:
        """
        Elimina un producto de la lista de productos.
        
        Parámetros:
        - producto (Producto): Producto a eliminar.
        """
        self.__productos.remove(producto)

    def listar_productos(self)->list:
        """
        Lista todos los productos de la heladería.
        Retorna:
        - list: Lista de productos.
        """
        return self.__productos
    
    def vender(self, nombre_producto: str) -> list:
        """
        Vende un producto si hay existencias suficientes.
        Parámetro:
        - nombre_producto (str): Nombre del producto a vender.
        Retorna:
        - bool: True si fue posible venderlo, False de lo contrario.
        """
        # Buscar el producto por nombre
        producto = next((p for p in self.__productos if p.nombre == nombre_producto), None)
        if not producto:
            return ["el producto no existe."]
        
        # Verificar existencias de ingredientes
        necesario_complemento = 1
        necesario_base = 0.2
        ingredientes_faltantes=[]
        
        for ingrediente in producto.ingredientes:
            if isinstance (ingrediente, Complemento) and ingrediente.inventario < necesario_complemento:
                ingredientes_faltantes.append(f"{ingrediente.nombre} (Complemento)") # no hay complementos suficientes
            elif isinstance (ingrediente, Base) and ingrediente.inventario < necesario_base:
                ingredientes_faltantes.append(f"{ingrediente.nombre} (Base)") # no hay base suficiente
        if ingredientes_faltantes:
            return ingredientes_faltantes # lista de ingredientes faltantes
            
        # Resta de cada uno de los ingredientes lo necesario para armar el producto    
        for ingrediente in producto.ingredientes:
            if isinstance (ingrediente, Complemento):
                ingrediente.inventario -= necesario_complemento
            elif isinstance (ingrediente, Base):
                ingrediente.inventario -= necesario_base
        
        # Sumar a las ventas del día el precio del producto
        self.__ventas_dia += producto.precio_publico
        return []
    
    def agregar_ingrediente (self, ingrediente:Ingrediente)-> None:
        """
        Agrega un ingrediente a la lista de inventario.
        Parámetro:
        - ingrediente (Ingrediente): Ingrediente a agregar.
        """
        self.__inventario.append(Ingrediente)

    def listar_ingredientes(self) -> list:
        """
        Lista todos los ingredientes en el inventario.
        Retorna:
        - list: Lista de ingredientes.
        """
        return self.__inventario

    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')
    
    @property
    def productos(self) -> list:
        """ Devuelve el valor del atributo privado 'productos' """
        return self.__productos
    
    @productos.setter
    def productos(self, value:list) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'productos'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if len(value) > 4:
            raise ValueError('no se pueden tener mas de 4 productos')
        if all(isinstance(producto, Producto)for producto in value):
            self.__productos = value
        else:
            raise ValueError('Expected list of Producto')
        
    @property
    def inventario(self) -> list:
        """ Devuelve el valor del atributo privado 'inventario' """
        return self.__inventario
    
    @inventario.setter
    def inventario(self, value: list) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'inventario'
        Valida que el valor enviado corresponda al tipo de dato del atributo.
        """ 
        if all(isinstance(ingrediente, Ingrediente)for ingrediente in value):
            self.__inventario = value
        else:
            raise ValueError('Expected list of Ingrediente')
    
    @property
    def ventas_dia(self) -> int:
        """ Devuelve el valor del atributo privado 'ventas_dia' """
        return self.__ventas_dia
    
    @ventas_dia.setter
    def ventas_dia(self, value: int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ventas_dia'
        Valida que el valor enviado corresponda al tipo de dato del atributo.
        """ 
        if isinstance(value, int):
            self.__ventas_dia = value
        else:
            raise ValueError('Expected int')