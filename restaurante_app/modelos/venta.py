class Venta:

    def __init__(self, usuario_id, producto_codigo, cantidad):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = int(cantidad)

    def mostrar_info(self):
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["usuario_id"],
            datos["producto_codigo"],
            datos["cantidad"]
        )