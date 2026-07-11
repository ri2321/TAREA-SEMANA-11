class Restaurante:


    def __init__(self):

        self.productos = []
        self.clientes = []


    # PRODUCTOS

    def agregar_producto(self, producto):

        self.productos.append(producto)


    def listar_productos(self):

        return self.productos


    def buscar_producto(self, nombre):

        for producto in self.productos:

            if producto.nombre.lower() == nombre.lower():
                return producto

        return None



    # CLIENTES


    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)


    def listar_clientes(self):

        return self.clientes


    def buscar_cliente(self, nombre):

        for cliente in self.clientes:

            if cliente.nombre.lower() == nombre.lower():
                return cliente

        return None