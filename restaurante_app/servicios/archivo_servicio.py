import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json") -> None:
        self.ruta_archivo = Path(ruta_archivo)

    def guardar_productos(self, productos: list[Producto]) -> None:
        try:
            self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)

            datos = [producto.to_dict() for producto in productos]

            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

        except PermissionError:
            print("Error: no existen permisos para escribir el archivo.")

    def cargar_productos(self) -> list[Producto]:
        productos: list[Producto] = []

        try:
            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                print("Error: el archivo JSON debe contener una lista.")
                return productos

            for registro in datos:
                try:
                    producto = Producto.from_dict(registro)
                    productos.append(producto)

                except KeyError as error:
                    print(
                        f"Registro omitido: falta la clave {error}."
                    )

                except ValueError as error:
                    print(
                        f"Registro omitido por datos inválidos: {error}"
                    )

        except FileNotFoundError:
            print("No existe productos.json. Se iniciará con una lista vacía.")

        except json.JSONDecodeError:
            print("Error: productos.json contiene un formato JSON inválido.")

        except PermissionError:
            print("Error: no existen permisos para leer el archivo.")

        return productos