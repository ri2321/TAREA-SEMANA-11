from collections.abc import Callable

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


archivo_servicio = ArchivoServicio()
restaurante = Restaurante(archivo_servicio)


# ---------------- GUARDADO ----------------

def guardar_productos() -> bool:
    productos = restaurante.listar_productos()
    return archivo_servicio.guardar_productos(productos)


def guardar_usuarios() -> bool:
    usuarios = restaurante.listar_usuarios()
    return archivo_servicio.guardar_usuarios(usuarios)


def guardar_ventas() -> bool:
    ventas = restaurante.listar_ventas()
    return archivo_servicio.guardar_ventas(ventas)


# ---------------- PRODUCTOS ----------------

def registrar_producto() -> None:
    codigo = input("Código del producto: ").strip()
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría del producto: ").strip()

    try:
        precio = float(input("Precio del producto: "))
        stock = int(input("Stock disponible: "))

        producto = Producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock
        )

        if restaurante.registrar_producto(producto):
            guardar_productos()
            print("Producto registrado correctamente.")
        else:
            print("No fue posible registrar el producto.")

    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto() -> None:
    codigo = input("Código del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print("\nProducto encontrado:")
    print(producto)


def actualizar_producto() -> None:
    codigo = input("Código del producto a actualizar: ").strip()
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    try:
        precio = float(input("Nuevo precio: "))
        stock = int(input("Nuevo stock: "))

        actualizado = restaurante.actualizar_producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock
        )

        if actualizado:
            guardar_productos()
            print("Producto actualizado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto() -> None:
    codigo = input("Código del producto a eliminar: ").strip()

    if restaurante.eliminar_producto(codigo):
        guardar_productos()
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos() -> None:
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- PRODUCTOS REGISTRADOS ---")

    for producto in productos:
        print(producto)


def mostrar_categorias() -> None:
    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    print("\n--- CATEGORÍAS ---")

    for categoria in sorted(categorias):
        print(f"- {categoria}")


# ---------------- USUARIOS ----------------

def registrar_usuario() -> None:
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    try:
        usuario = Usuario(
            identificacion=identificacion,
            nombre=nombre,
            correo=correo
        )

        if restaurante.registrar_usuario(usuario):
            guardar_usuarios()
            print("Usuario registrado correctamente.")
        else:
            print("No fue posible registrar el usuario.")

    except ValueError as error:
        print(f"Error: {error}")


def buscar_usuario() -> None:
    identificacion = input("Identificación del usuario: ").strip()
    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("Usuario no encontrado.")
        return

    print("\nUsuario encontrado:")
    print(usuario)


def actualizar_usuario() -> None:
    identificacion = input(
        "Identificación del usuario a actualizar: "
    ).strip()

    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("Usuario no encontrado.")
        return

    nombre = input("Nuevo nombre: ").strip()
    correo = input("Nuevo correo: ").strip()

    try:
        actualizado = restaurante.actualizar_usuario(
            identificacion=identificacion,
            nombre=nombre,
            correo=correo
        )

        if actualizado:
            guardar_usuarios()
            print("Usuario actualizado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_usuario() -> None:
    identificacion = input(
        "Identificación del usuario a eliminar: "
    ).strip()

    if restaurante.eliminar_usuario(identificacion):
        guardar_usuarios()
        print("Usuario eliminado correctamente.")
    else:
        print("Usuario no encontrado.")


def listar_usuarios() -> None:
    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\n--- USUARIOS REGISTRADOS ---")

    for usuario in usuarios:
        print(usuario)


# ---------------- VENTAS ----------------

def vender_producto() -> None:
    identificacion = input(
        "Identificación del usuario: "
    ).strip()

    codigo = input("Código del producto: ").strip()

    try:
        cantidad = int(input("Cantidad solicitada: "))
    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    venta_realizada = restaurante.vender_producto(
        codigo_producto=codigo,
        identificacion_usuario=identificacion,
        cantidad=cantidad
    )

    if venta_realizada:
        productos_guardados = guardar_productos()
        ventas_guardadas = guardar_ventas()

        if productos_guardados and ventas_guardadas:
            print("Venta registrada correctamente.")
        else:
            print(
                "La venta se realizó, pero ocurrió un problema "
                "al guardar los archivos."
            )
    else:
        print("La venta no pudo realizarse.")


def consultar_ventas_usuario() -> None:
    identificacion = input(
        "Identificación del usuario: "
    ).strip()

    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("Usuario no encontrado.")
        return

    ventas = restaurante.consultar_ventas_usuario(
        identificacion
    )

    if not ventas:
        print("El usuario no tiene ventas registradas.")
        return

    print(f"\n--- COMPRAS DE {usuario.nombre.upper()} ---")

    for venta in ventas:
        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        if producto is not None:
            nombre_producto = producto.nombre
        else:
            nombre_producto = "Producto no disponible"

        print(
            f"Código: {venta.producto_codigo} | "
            f"Producto: {nombre_producto} | "
            f"Cantidad: {venta.cantidad}"
        )


# ---------------- MENÚ ----------------

def salir() -> None:
    print("Gracias por utilizar el sistema.")


OPCIONES_MENU: tuple[str, ...] = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Buscar usuario",
    "Actualizar usuario",
    "Eliminar usuario",
    "Listar usuarios",
    "Vender producto",
    "Consultar ventas de un usuario",
    "Mostrar categorías",
    "Salir"
)


ACCIONES_MENU: dict[str, Callable[[], None]] = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": buscar_usuario,
    "8": actualizar_usuario,
    "9": eliminar_usuario,
    "10": listar_usuarios,
    "11": vender_producto,
    "12": consultar_ventas_usuario,
    "13": mostrar_categorias,
    "14": salir
}


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")

    for numero, opcion in enumerate(
        OPCIONES_MENU,
        start=1
    ):
        print(f"{numero}. {opcion}")

    print("========================================")


def cargar_informacion() -> None:
    productos = archivo_servicio.cargar_productos()
    usuarios = archivo_servicio.cargar_usuarios()
    ventas = archivo_servicio.cargar_ventas()

    restaurante.cargar_productos(productos)
    restaurante.cargar_usuarios(usuarios)
    restaurante.cargar_ventas(ventas)

    print(
        "\nInformación recuperada: "
        f"{len(productos)} producto(s), "
        f"{len(usuarios)} usuario(s) y "
        f"{len(ventas)} venta(s)."
    )


def main() -> None:
    cargar_informacion()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()
        accion = ACCIONES_MENU.get(opcion)

        if accion is None:
            print("Opción no válida.")
            continue

        accion()

        if opcion == "14":
            break


if __name__ == "__main__":
    main()