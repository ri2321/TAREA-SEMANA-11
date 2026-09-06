class Usuario:

    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre

    def mostrar_info(self):
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre}"
        )

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["identificacion"],
            datos["nombre"]
        )