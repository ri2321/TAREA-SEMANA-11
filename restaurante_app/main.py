from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante()

while True:
    print("\n===== SISTEMA DE RESTAURANTE =====")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        producto = Producto(codigo, nombre, precio, categoria)
        restaurante.registrar_producto(producto)

    elif opcion == "2":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        tamano = input("Tamaño: ")

        bebida = Bebida(codigo, nombre, precio, categoria, tamano)
        restaurante.registrar_producto(bebida)

    elif opcion == "3":
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        cliente = Cliente(identificacion, nombre, correo)
        restaurante.registrar_cliente(cliente)

    elif opcion == "4":
        restaurante.listar_productos()

    elif opcion == "5":
        restaurante.listar_clientes()

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta.")