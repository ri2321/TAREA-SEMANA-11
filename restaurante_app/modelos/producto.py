class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_informacion(self) -> str:
        return f"[{self.codigo}] {self.nombre} - {self.categoria} - ${self.precio:.2f}"