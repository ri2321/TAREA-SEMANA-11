# Restaurante App - Semana 10

## Nombre del estudiante

Ricardo Rubén Cando Arguello

## Descripción del proyecto

El proyecto Restaurante App corresponde a una aplicación desarrollada en Python utilizando Programación Orientada a Objetos. El sistema permite administrar productos de un restaurante mediante un menú interactivo en consola.

En esta Semana 10 se realizó una mejora al proyecto desarrollado anteriormente mediante la incorporación de persistencia de datos utilizando archivos JSON. De esta manera, los productos registrados pueden conservarse aunque la aplicación sea cerrada y posteriormente ejecutada nuevamente.

## Objetivo

Implementar la persistencia de los productos mediante un archivo JSON, manteniendo la arquitectura modular del proyecto y aplicando manejo de excepciones para controlar posibles errores durante la lectura y escritura de los datos.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Componentes principales

### Producto

La clase `Producto` representa los productos registrados en el restaurante. Contiene atributos como identificador, nombre, precio y categoría.

También dispone de métodos para convertir un producto en un diccionario y para reconstruir un objeto `Producto` a partir de los datos recuperados desde JSON.

### Usuario

La clase `Usuario` representa la información básica de los usuarios del sistema. En esta semana sus datos permanecen únicamente en memoria y no forman parte de la persistencia solicitada.

### Restaurante

La clase `Restaurante` administra la colección de productos y contiene las operaciones para registrar, buscar, listar, actualizar y eliminar productos.

### ArchivoServicio

`ArchivoServicio` es responsable de la persistencia de los productos. Se encarga de leer y escribir el archivo `datos/productos.json` utilizando el módulo `json`.

Se utiliza `json.dump()` para guardar la información y `json.load()` para recuperarla.

### main.py

El archivo `main.py` es el punto de entrada de la aplicación. Coordina el menú, recibe los datos mediante `input()`, carga los productos al iniciar y solicita el guardado después de las operaciones que modifican la colección.

## Persistencia mediante JSON

La persistencia permite conservar los productos después de cerrar el programa.

Los objetos `Producto` se convierten en diccionarios antes de ser almacenados en `productos.json`. Cuando la aplicación vuelve a ejecutarse, los datos son recuperados y cada registro válido se convierte nuevamente en un objeto `Producto`.

El archivo utilizado es:

```text
datos/productos.json
```

## Flujo de carga

Al iniciar el programa se crea el servicio de archivos y se intenta leer `productos.json`.

El proceso es:

```text
Inicio
  ↓
main.py crea ArchivoServicio
  ↓
Se lee productos.json
  ↓
json.load()
  ↓
Se validan los registros
  ↓
Se crean objetos Producto
  ↓
Los productos se cargan en Restaurante
  ↓
El menú queda disponible
```

## Flujo de guardado

Cuando se registra, actualiza o elimina un producto, la colección administrada por `Restaurante` se convierte a una estructura compatible con JSON y se guarda nuevamente en el archivo.

```text
Operación sobre producto
  ↓
Restaurante modifica la colección
  ↓
Producto se convierte a diccionario
  ↓
ArchivoServicio utiliza json.dump()
  ↓
Se actualiza productos.json
```

## Manejo de excepciones

El sistema controla diferentes situaciones que pueden producirse durante el funcionamiento:

* `FileNotFoundError`: permite iniciar el programa aunque todavía no exista el archivo JSON.
* `json.JSONDecodeError`: controla archivos que contienen información que no tiene un formato JSON válido.
* `PermissionError`: controla problemas relacionados con permisos de lectura o escritura.
* `KeyError`: permite detectar registros almacenados que no contienen alguna clave necesaria.
* `ValueError`: controla datos inválidos introducidos por el usuario y validaciones de la clase `Producto`.

Las excepciones se manejan de forma específica para evitar que errores previsibles provoquen el cierre inesperado de la aplicación.

## Funcionalidades

El programa permite:

1. Registrar productos.
2. Listar productos.
3. Buscar productos mediante su ID.
4. Actualizar productos.
5. Eliminar productos.
6. Guardar los cambios en formato JSON.
7. Cargar automáticamente los productos almacenados al iniciar.

## Ejecución del programa

Para ejecutar el proyecto se debe abrir una terminal dentro de la carpeta `restaurante_app` y utilizar:

```bash
python main.py
```

También puede ejecutarse utilizando la versión de Python instalada en el equipo.

## Comprobación de persistencia

Para comprobar el funcionamiento de la persistencia se realizó el siguiente procedimiento:

1. Se ejecutó `main.py`.
2. Se registró uno o más productos utilizando el menú.
3. Se verificó que la información apareciera en `datos/productos.json`.
4. Se cerró completamente la aplicación.
5. Se ejecutó nuevamente `main.py`.
6. Se seleccionó la opción para listar los productos.
7. Se comprobó que los productos registrados anteriormente continuaran disponibles.
8. Se realizó una actualización o eliminación.
9. Se reinició nuevamente el programa para comprobar que el cambio permaneciera guardado.

## Conclusión

La mejora implementada en la Semana 10 permitió incorporar persistencia de datos al proyecto Restaurante App mediante archivos JSON. Los productos ya no dependen únicamente de la memoria temporal del programa, sino que pueden conservarse y recuperarse en nuevas ejecuciones.

Además, se mantuvo la separación de responsabilidades entre las clases y servicios. `Restaurante` administra los productos, `ArchivoServicio` se encarga de la lectura y escritura del archivo JSON y `main.py` coordina la interacción con el usuario.

El manejo de excepciones permite controlar situaciones como la ausencia del archivo, errores en el formato JSON, problemas de permisos y datos inválidos. De esta manera, el sistema mantiene un funcionamiento más seguro y organizado.
