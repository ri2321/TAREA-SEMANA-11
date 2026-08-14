from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


restaurante = Restaurante()


# TUPLA
OPCIONES_MENU = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
)


def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    categoria = input("Categoria: ")

    try:
        precio = float(input("Precio: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        resultado = restaurante.registrar_producto(producto)

        if resultado:
            print("Producto registrado correctamente.")
        else:
            print("ERROR: El codigo ya existe.")

    except ValueError:
        print("ERROR: El precio debe ser numerico.")


def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el codigo: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is not None:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("Producto no encontrado.")


def actualizar_producto():
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el codigo: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    nombre = input("Nuevo nombre: ")
    categoria = input("Nueva categoria: ")

    try:
        precio = float(input("Nuevo precio: "))

        resultado = restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        if resultado:
            print("Producto actualizado correctamente.")

    except ValueError:
        print("ERROR: El precio debe ser numerico.")


def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el codigo: ")

    resultado = restaurante.eliminar_producto(codigo)

    if resultado:
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario():
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Identificacion: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    resultado = restaurante.registrar_usuario(usuario)

    if resultado:
        print("Usuario registrado correctamente.")
    else:
        print("ERROR: La identificacion ya existe.")


def listar_usuarios():
    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias():
    print("\n--- CATEGORIAS ---")

    categorias = restaurante.obtener_categorias()

    if len(categorias) == 0:
        print("No hay categorias registradas.")
        return

    for categoria in categorias:
        print("-", categoria)


# DICCIONARIO
ACCIONES = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias
}


def mostrar_menu():
    print()
    print("========================================")
    print("       SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorias")
    print("9. Salir")
    print("========================================")


def main():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion not in OPCIONES_MENU:
            print("ERROR: Opcion no valida.")
            continue

        if opcion == "9":
            print("\nPrograma finalizado.")
            break

        accion = ACCIONES.get(opcion)

        if accion is not None:
            accion()


if __name__ == "__main__":
    main()