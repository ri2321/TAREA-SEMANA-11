class Producto:

    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible


    @property
    def nombre(self):
        return self._nombre


    @nombre.setter
    def nombre(self, valor):
        if valor == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor


    @property
    def categoria(self):
        return self._categoria


    @categoria.setter
    def categoria(self, valor):
        if valor == "":
            raise ValueError("La categoría no puede estar vacía")
        self._categoria = valor


    @property
    def precio(self):
        return self._precio


    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio = valor


    def mostrar_informacion(self):

        estado = "Disponible" if self.disponible else "Agotado"

        return (
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio}\n"
            f"Estado: {estado}"
        )