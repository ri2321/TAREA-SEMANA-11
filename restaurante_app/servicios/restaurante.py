from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:

    def __init__(self, archivo_servicio):
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

        self.archivo_servicio = archivo_servicio

    # ==========================
    # CARGA DE INFORMACIÓN
    # ==========================

    def cargar_productos(self, productos: list[Producto]) -> None:
        self._productos = productos

    def cargar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._usuarios = usuarios

    def cargar_ventas(self, ventas: list[Venta]) -> None:
        self._ventas = ventas

    # ==========================
    # PRODUCTOS
    # ==========================

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        self.guardar_productos()
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self._productos:
            if producto.codigo.lower() == codigo.lower():
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int
    ) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        if not nombre.strip():
            return False

        if precio < 0 or stock < 0:
            return False

        producto.nombre = nombre.strip()
        producto.precio = precio
        producto.stock = stock

        self.guardar_productos()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        self.guardar_productos()
        return True

    # ==========================
    # USUARIOS
    # ==========================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self._usuarios.append(usuario)
        self.guardar_usuarios()
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    # ==========================
    # VENTAS
    # ==========================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:
        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None:
            return False

        if producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)
        producto.vender(cantidad)

        self.guardar_ventas()
        self.guardar_productos()

        return True

    def listar_ventas(self) -> list[Venta]:
        return self._ventas

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:
        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    # ==========================
    # PERSISTENCIA
    # ==========================

    def guardar_productos(self) -> bool:
        return self.archivo_servicio.guardar_productos(
            self._productos
        )

    def guardar_usuarios(self) -> bool:
        return self.archivo_servicio.guardar_usuarios(
            self._usuarios
        )

    def guardar_ventas(self) -> bool:
        return self.archivo_servicio.guardar_ventas(
            self._ventas
        )

    def cargar_datos(self) -> None:
        productos = self.archivo_servicio.cargar_productos()
        usuarios = self.archivo_servicio.cargar_usuarios()
        ventas = self.archivo_servicio.cargar_ventas()

        self.cargar_productos(productos)
        self.cargar_usuarios(usuarios)
        self.cargar_ventas(ventas)