print()
print("======================================")
print("          RESTAURANTE APP")
print("======================================")
print("1. Registrar producto")
print("2. Listar productos")
print("3. Buscar producto")
print("4. Actualizar producto")
print("5. Eliminar producto")
print("6. Registrar usuario")
print("7. Listar usuarios")
print("8. Buscar usuario")
print("9. Realizar venta")
print("10. Consultar ventas de un usuario")
print("11. Listar ventas")
print("12. Salir")
print("======================================")

while True:
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        print()
        print("--- REGISTRAR PRODUCTO ---")
        codigo = input("Código: ")
        nombre = input("Nombre: ")

        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))

            print()
            print("Producto registrado correctamente.")
            print("Código:", codigo)
            print("Nombre:", nombre)
            print("Precio:", precio)
            print("Stock:", stock)

        except ValueError:
            print("Error: ingrese números válidos.")

    elif opcion == "2":
        print()
        print("--- LISTAR PRODUCTOS ---")
        print("No hay productos para mostrar.")

    elif opcion == "3":
        print()
        print("--- BUSCAR PRODUCTO ---")
        codigo = input("Ingrese el código: ")
        print("Buscando producto:", codigo)

    elif opcion == "4":
        print()
        print("--- ACTUALIZAR PRODUCTO ---")
        codigo = input("Ingrese el código: ")
        print("Actualizando producto:", codigo)

    elif opcion == "5":
        print()
        print("--- ELIMINAR PRODUCTO ---")
        codigo = input("Ingrese el código: ")
        print("Producto seleccionado:", codigo)

    elif opcion == "6":
        print()
        print("--- REGISTRAR USUARIO ---")
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")

        print()
        print("Usuario registrado correctamente.")
        print("Identificación:", identificacion)
        print("Nombre:", nombre)

    elif opcion == "7":
        print()
        print("--- LISTAR USUARIOS ---")
        print("No hay usuarios para mostrar.")

    elif opcion == "8":
        print()
        print("--- BUSCAR USUARIO ---")
        identificacion = input("Identificación: ")
        print("Buscando usuario:", identificacion)

    elif opcion == "9":
        print()
        print("--- REALIZAR VENTA ---")
        usuario = input("Identificación del usuario: ")
        producto = input("Código del producto: ")

        try:
            cantidad = int(input("Cantidad: "))

            print()
            print("Venta registrada correctamente.")
            print("Usuario:", usuario)
            print("Producto:", producto)
            print("Cantidad:", cantidad)

        except ValueError:
            print("Error: la cantidad debe ser un número entero.")

    elif opcion == "10":
        print()
        print("--- CONSULTAR VENTAS DE UN USUARIO ---")
        identificacion = input("Identificación: ")
        print("Consultando ventas de:", identificacion)

    elif opcion == "11":
        print()
        print("--- LISTAR VENTAS ---")
        print("No hay ventas para mostrar.")

    elif opcion == "12":
        print()
        print("======================================")
        print("Gracias por utilizar RESTAURANTE APP.")
        print("Programa finalizado.")
        print("======================================")
        break

    else:
        print()
        print("Opción no válida.")
        print("Seleccione una opción del 1 al 12.")
