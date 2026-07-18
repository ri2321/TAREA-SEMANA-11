from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto: Producto):
        for p in self.productos:
            if p.codigo == producto.codigo:
                print("Ese código ya existe.")
                return
        self.productos.append(producto)
        print("Producto registrado correctamente.")

    def registrar_cliente(self, cliente: Cliente):
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                print("Ese cliente ya existe.")
                return
        self.clientes.append(cliente)
        print("Cliente registrado correctamente.")

    def listar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            print(producto.mostrar_informacion())

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("No hay clientes registrados.")
            return

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())