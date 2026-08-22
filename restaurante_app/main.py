from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========== RESTAURANTE APP ==========")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("======================================")


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    try:
        print("\n--- REGISTRAR PRODUCTO ---")

        id_producto = int(input("Ingrese el ID: "))
        nombre = input("Ingrese el nombre: ")
        precio = float(input("Ingrese el precio: "))
        categoria = input("Ingrese la categoría: ")

        producto = Producto(
            id_producto,
            nombre,
            precio,
            categoria
        )

        restaurante.registrar_producto(producto)

        archivo_servicio.guardar_productos(
            restaurante.listar_productos()
        )

        print("Producto registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def buscar_producto(restaurante: Restaurante) -> None:
    try:
        id_producto = int(input("Ingrese el ID del producto: "))

        producto = restaurante.buscar_producto(id_producto)

        if producto is None:
            print("Producto no encontrado.")
        else:
            print("\nProducto encontrado:")
            print(producto)

    except ValueError:
        print("Error: el ID debe ser un número entero.")


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    try:
        print("\n--- ACTUALIZAR PRODUCTO ---")

        id_producto = int(input("Ingrese el ID del producto: "))
        nombre = input("Nuevo nombre: ")
        precio = float(input("Nuevo precio: "))
        categoria = input("Nueva categoría: ")

        actualizado = restaurante.actualizar_producto(
            id_producto,
            nombre,
            precio,
            categoria
        )

        if actualizado:
            archivo_servicio.guardar_productos(
                restaurante.listar_productos()
            )

            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    try:
        print("\n--- ELIMINAR PRODUCTO ---")

        id_producto = int(input("Ingrese el ID del producto: "))

        eliminado = restaurante.eliminar_producto(id_producto)

        if eliminado:
            archivo_servicio.guardar_productos(
                restaurante.listar_productos()
            )

            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    except ValueError:
        print("Error: el ID debe ser un número entero.")


def main() -> None:
    restaurante = Restaurante()
    archivo_servicio = ArchivoServicio()

    print("Cargando productos almacenados...")
    productos = archivo_servicio.cargar_productos()
    restaurante.cargar_productos(productos)

    print(
        f"Se cargaron {len(productos)} producto(s)."
    )

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            actualizar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "5":
            eliminar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()