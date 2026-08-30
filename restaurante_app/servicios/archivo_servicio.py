import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self, carpeta="datos"):
        self.carpeta = carpeta

        os.makedirs(self.carpeta, exist_ok=True)

        self.productos_archivo = os.path.join(
            self.carpeta,
            "productos.json"
        )

        self.usuarios_archivo = os.path.join(
            self.carpeta,
            "usuarios.json"
        )

        self.ventas_archivo = os.path.join(
            self.carpeta,
            "ventas.json"
        )

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def guardar_productos(self, productos):
        datos = [producto.to_dict() for producto in productos]

        try:
            with open(
                self.productos_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print("Error: no hay permisos para guardar productos.")

    def cargar_productos(self):
        try:
            with open(
                self.productos_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                productos = []

                for registro in datos:
                    try:
                        producto = Producto.from_dict(registro)
                        productos.append(producto)

                    except (KeyError, ValueError, TypeError) as error:
                        print(
                            f"Error en un producto: {error}"
                        )

                return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para leer productos."
            )
            return []

    # ==========================================
    # USUARIOS
    # ==========================================

    def guardar_usuarios(self, usuarios):
        datos = [usuario.to_dict() for usuario in usuarios]

        try:
            with open(
                self.usuarios_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print(
                "Error: no hay permisos para guardar usuarios."
            )

    def cargar_usuarios(self):
        try:
            with open(
                self.usuarios_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                usuarios = []

                for registro in datos:
                    try:
                        usuario = Usuario.from_dict(registro)
                        usuarios.append(usuario)

                    except (KeyError, ValueError, TypeError) as error:
                        print(
                            f"Error en un usuario: {error}"
                        )

                return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: usuarios.json contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para leer usuarios."
            )
            return []

    # ==========================================
    # VENTAS
    # ==========================================

    def guardar_ventas(self, ventas):
        datos = [venta.to_dict() for venta in ventas]

        try:
            with open(
                self.ventas_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print(
                "Error: no hay permisos para guardar ventas."
            )

    def cargar_ventas(self):
        try:
            with open(
                self.ventas_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                ventas = []

                for registro in datos:
                    try:
                        venta = Venta.from_dict(registro)
                        ventas.append(venta)

                    except (KeyError, ValueError, TypeError) as error:
                        print(
                            f"Error en una venta: {error}"
                        )

                return ventas

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: ventas.json contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para leer ventas."
            )
            return []