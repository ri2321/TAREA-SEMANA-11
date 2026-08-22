from modelos.producto import Producto


class Restaurante:
    def __init__(self) -> None:
        self.productos: list[Producto] = []

    def cargar_productos(self, productos: list[Producto]) -> None:
        self.productos = productos

    def registrar_producto(self, producto: Producto) -> None:
        if self.buscar_producto(producto.id_producto) is not None:
            raise ValueError("Ya existe un producto con ese ID.")

        self.productos.append(producto)

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_producto(self, id_producto: int) -> Producto | None:
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto

        return None

    def actualizar_producto(
        self,
        id_producto: int,
        nombre: str,
        precio: float,
        categoria: str
    ) -> bool:

        producto = self.buscar_producto(id_producto)

        if producto is None:
            return False

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        producto.nombre = nombre
        producto.precio = precio
        producto.categoria = categoria

        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        producto = self.buscar_producto(id_producto)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True