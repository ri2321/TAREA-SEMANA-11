class Usuario:

    def __init__(self, identificacion: str, nombre: str):

        if not identificacion:
            raise ValueError("La identificación es obligatoria.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        self.identificacion = identificacion
        self.nombre = nombre

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

    def mostrar_info(self):
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.nombre}"
        )