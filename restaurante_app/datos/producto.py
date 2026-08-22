class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str) -> None:
        if id_producto <= 0:
            raise ValueError("El ID debe ser mayor que cero.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def to_dict(self) -> dict:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        return cls(
            id_producto=int(datos["id_producto"]),
            nombre=str(datos["nombre"]),
            precio=float(datos["precio"]),
            categoria=str(datos["categoria"])
        )

    def __str__(self) -> str:
        return (
            f"ID: {self.id_producto} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Categoría: {self.categoria}"
        )