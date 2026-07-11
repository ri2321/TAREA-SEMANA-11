from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante



restaurante = Restaurante()



def menu():

    while True:

        print("""
==================================
       SISTEMA RESTAURANTE
==================================
1. Registrar producto
2. Mostrar productos
3. Buscar producto

4. Registrar cliente
5. Mostrar clientes
6. Buscar cliente

7. Salir
==================================
""")


        opcion = input("Seleccione una opción: ")



        if opcion == "1":

            registrar_producto()


        elif opcion == "2":

            mostrar_productos()


        elif opcion == "3":

            buscar_producto()


        elif opcion == "4":

            registrar_cliente()


        elif opcion == "5":

            mostrar_clientes()


        elif opcion == "6":

            buscar_cliente()


        elif opcion == "7":

            print("Programa finalizado")
            break


        else:

            print("Opción incorrecta")




def registrar_producto():

    try:

        nombre = input("Nombre del producto: ")

        categoria = input("Categoría: ")

        precio = float(input("Precio: "))


        producto = Producto(
            nombre,
            categoria,
            precio
        )


        restaurante.agregar_producto(producto)

        print("Producto registrado")


    except ValueError as error:

        print(error)




def mostrar_productos():

    productos = restaurante.listar_productos()


    if not productos:

        print("No hay productos")


    else:

        for producto in productos:

            print("-------------------")
            print(producto.mostrar_informacion())





def buscar_producto():

    nombre = input("Producto a buscar: ")


    producto = restaurante.buscar_producto(nombre)


    if producto:

        print(producto.mostrar_informacion())


    else:

        print("Producto no encontrado")





def registrar_cliente():


    id_cliente = int(input("ID cliente: "))

    nombre = input("Nombre: ")

    correo = input("Correo: ")



    cliente = Cliente(
        id_cliente,
        nombre,
        correo
    )


    restaurante.agregar_cliente(cliente)


    print("Cliente registrado")





def mostrar_clientes():

    clientes = restaurante.listar_clientes()


    if not clientes:

        print("No existen clientes")


    else:

        for cliente in clientes:

            print("-------------------")

            print(
                f"ID: {cliente.id_cliente}\n"
                f"Nombre: {cliente.nombre}\n"
                f"Correo: {cliente.correo}"
            )





def buscar_cliente():

    nombre = input("Nombre del cliente: ")


    cliente = restaurante.buscar_cliente(nombre)


    if cliente:


        print(
            f"ID: {cliente.id_cliente}\n"
            f"Nombre: {cliente.nombre}\n"
            f"Correo: {cliente.correo}"
        )


    else:

        print("Cliente no encontrado")





if __name__ == "__main__":

    menu()