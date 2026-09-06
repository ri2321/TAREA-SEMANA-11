from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self):
        self.archivo_servicio = ArchivoServicio()

        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()
        self.ventas = self.archivo_servicio.cargar_ventas()

        # Índices de la Semana 12
        self.productos_por_codigo = {}
        self.usuarios_por_identificacion = {}
        self.ventas_por_usuario = {}

        self.reconstruir_indices()

    def reconstruir_indices(self):

        self.productos_por_codigo.clear()
        self.usuarios_por_identificacion.clear()
        self.ventas_por_usuario.clear()

        for producto in self.productos:
            self.productos_por_codigo[producto.codigo] = producto

        for usuario in self.usuarios:
            self.usuarios_por_identificacion[
                usuario.identificacion
            ] = usuario

        for venta in self.ventas:

            if venta.usuario_id not in self.ventas_por_usuario:
                self.ventas_por_usuario[venta.usuario_id] = []

            self.ventas_por_usuario[
                venta.usuario_id
            ].append(venta)

    def buscar_producto(self, codigo):
        return self.productos_por_codigo.get(codigo)

    def buscar_usuario(self, identificacion):
        return self.usuarios_por_identificacion.get(
            identificacion
        )

    def consultar_ventas_usuario(self, identificacion):
        return self.ventas_por_usuario.get(
            identificacion,
            []
        )