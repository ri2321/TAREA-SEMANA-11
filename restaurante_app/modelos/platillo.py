from modelos.producto import Producto

class Platillo(Producto):

    def __init__(self, nombre, precio, disponible, tipo):
        super().__init__(nombre, precio)
        self.disponible = disponible
        self.tipo = tipo

    def mostrar_informacion(self):
        print("=== PLATILLO ===")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Disponible: {self.disponible}")
        print(f"Tipo: {self.tipo}")