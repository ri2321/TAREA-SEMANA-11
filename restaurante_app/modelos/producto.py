class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if not codigo:
            raise ValueError("El código es obligatorio.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")

        self.stock -= cantidad

    def mostrar_info(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["precio"],
            datos["stock"]
        )