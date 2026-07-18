from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str, tamano: str):
        super().__init__(codigo, nombre, precio, categoria)
        self.tamano = tamano

    def mostrar_informacion(self) -> str:
        return (
            f"[{self.codigo}] {self.nombre} - {self.categoria} - "
            f"${self.precio:.2f} - Tamaño: {self.tamano}"
        )