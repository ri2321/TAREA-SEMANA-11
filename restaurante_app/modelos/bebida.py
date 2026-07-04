from modelos.producto import Producto

class Bebida(Producto):

    def __init__(self, nombre, precio, disponible, volumen):
        super().__init__(nombre, precio, disponible)
        self.volumen = volumen

    def mostrar_informacion(self):
        print("=== BEBIDA ===")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Disponible: {self.disponible}")
        print(f"Volumen: {self.volumen} ml")