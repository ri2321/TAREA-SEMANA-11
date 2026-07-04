class Producto:

    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.__precio = precio   # Encapsulación
        self.disponible = disponible

    def obtener_precio(self):
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Disponible: {self.disponible}")