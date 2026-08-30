class Venta:
    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ):
        if not usuario_id:
            raise ValueError("La identificación del usuario es obligatoria.")

        if not producto_codigo:
            raise ValueError("El código del producto es obligatorio.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

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