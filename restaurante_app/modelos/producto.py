class Producto:

    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def vender(self, cantidad):
        cantidad = int(cantidad)

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")

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