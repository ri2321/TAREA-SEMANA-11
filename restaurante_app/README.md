restaurante_app – Semana 9
Datos del estudiante

Nombre: Ricardo Rubén Cando Argüello
Asignatura: Programación Orientada a Objetos
Semana: 9

Descripción

El proyecto restaurante_app corresponde a la continuación del sistema desarrollado durante las semanas anteriores. En esta Semana 9 se mejora el sistema mediante la administración de productos y usuarios utilizando estructuras de datos de Python.

El sistema funciona mediante un menú interactivo en consola y permite registrar, buscar, actualizar, eliminar y listar productos. También permite registrar y listar usuarios.

El objetivo principal es utilizar de manera funcional las estructuras de datos list, tuple, dict y set, manteniendo una correcta separación entre modelos, servicios y main.py. La actividad establece que cada estructura debe tener una función concreta dentro del sistema.

Estructura del proyecto
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
Componentes del sistema
Producto

La clase Producto representa los productos del restaurante y contiene:

Código
Nombre
Categoría
Precio
Usuario

La clase Usuario representa a las personas registradas en el sistema y contiene:

Identificación
Nombre
Correo
Restaurante

La clase Restaurante es el servicio encargado de administrar las colecciones de productos y usuarios. También realiza las operaciones de registro, búsqueda, actualización, eliminación y listado.

main.py

El archivo main.py es el punto de inicio del programa. Se encarga de mostrar el menú, solicitar información mediante input() y utilizar los métodos de la clase Restaurante.

Esta organización permite mantener separadas las responsabilidades de cada componente.

Estructuras de datos utilizadas
Lista — list

Las listas se utilizan para almacenar los productos y usuarios registrados.

self.productos = []
self.usuarios = []

Estas listas permiten administrar colecciones dinámicas de objetos.

Tupla — tuple

La tupla se utiliza para almacenar las opciones disponibles del menú.

OPCIONES_MENU = (
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9"
)

Se utiliza una tupla porque las opciones del menú permanecen estables durante la ejecución del programa.

Diccionario — dict

El diccionario relaciona cada opción del menú con la función que debe ejecutarse.

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

De esta manera se establece una relación clara de clave → valor.

Conjunto — set

El conjunto se utiliza para obtener las categorías de los productos sin repetir valores.

def obtener_categorias(self):
    return {producto.categoria for producto in self.productos}

Por ejemplo, si existen varios productos de la categoría Bebidas, esta categoría solamente se mostrará una vez.

Funcionalidades

El sistema cuenta con las siguientes opciones:

Registrar producto.
Buscar producto.
Actualizar producto.
Eliminar producto.
Listar productos.
Registrar usuario.
Listar usuarios.
Mostrar categorías.
Salir.

Estas funcionalidades corresponden al menú interactivo establecido como referencia en la actividad.

Validaciones

El sistema incorpora validaciones para evitar:

Códigos de productos duplicados.
Identificaciones de usuarios duplicadas.
Ingreso de precios que no sean valores numéricos.

También se utiliza manejo de excepciones para evitar que una entrada incorrecta detenga inesperadamente el programa.

Ejecución

Para ejecutar el programa, se debe abrir una terminal dentro de la carpeta restaurante_app y ejecutar:

python main.py

También se puede utilizar:

python3 main.py

Al iniciar el programa aparecerá el menú principal del sistema de restaurante.

Ejemplo del menú
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
----------------------------------------
6. Registrar usuario
7. Listar usuarios
----------------------------------------
8. Mostrar categorías
9. Salir
Reflexión

Durante la Semana 9 se aplicaron diferentes estructuras de datos de Python para mejorar la administración de la información del sistema. Las listas permiten almacenar colecciones dinámicas de productos y usuarios, mientras que las tuplas permiten mantener información estable como las opciones del menú.

Los diccionarios permiten relacionar cada opción con la función correspondiente y los conjuntos permiten obtener información única, como las categorías de los productos, evitando valores repetidos.

La utilización de cada estructura según la necesidad del problema permite desarrollar un programa más organizado, comprensible y fácil de mantener.

Conclusión

La implementación de la Semana 9 permitió continuar mejorando el proyecto restaurante_app mediante la administración organizada de productos y usuarios. Se incorporaron las estructuras list, tuple, dict y set de manera funcional dentro del sistema.

Además, se mantuvo la separación de responsabilidades entre los modelos, el servicio Restaurante y el archivo main.py. Con esto se obtiene un sistema modular que permite realizar las operaciones principales mediante un menú interactivo y que puede continuar evolucionando en las siguientes semanas.
