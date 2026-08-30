# Sistema de Gestión de Restaurante - Semana 11

## Datos del estudiante

**Nombre:** Ricardo Ruben Cando Arguello

**Asignatura:** Programación Orientada a Objetos

**Actividad:** Semana 11

## Descripción del proyecto

El presente proyecto corresponde a la evolución del sistema `restaurante_app`, desarrollado durante las semanas anteriores de la asignatura Programación Orientada a Objetos.

En esta Semana 11 se incorporan nuevas funcionalidades relacionadas con el uso de colecciones de objetos, relaciones entre entidades y persistencia de información mediante archivos JSON.

El sistema permite administrar productos y usuarios, registrar ventas y consultar las ventas realizadas por un usuario. Además, cada producto posee un stock disponible que se actualiza automáticamente después de realizar una venta válida.

## Objetivo

El objetivo principal es aplicar los fundamentos de Programación Orientada a Objetos y colecciones para representar operaciones reales de un restaurante.

El sistema permite relacionar un usuario con un producto mediante una entidad `Venta`, controlar el stock disponible y mantener la información almacenada mediante archivos JSON.

## Funcionalidades

El sistema cuenta con las siguientes opciones:

1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Buscar usuario
8. Actualizar usuario
9. Eliminar usuario
10. Listar usuarios
11. Vender producto
12. Consultar ventas de un usuario
13. Mostrar categorías
14. Salir

## Relación Usuario + Producto → Venta

La principal mejora de esta semana es la incorporación de la clase `Venta`.

Una venta relaciona:

* La identificación del usuario.
* El código del producto.
* La cantidad vendida.

El proceso de venta funciona de la siguiente manera:

```text
Usuario registrado
       ↓
Producto existente
       ↓
Validar cantidad
       ↓
Validar stock
       ↓
Crear Venta
       ↓
Agregar Venta a la colección
       ↓
Disminuir stock
       ↓
Guardar productos.json
       ↓
Guardar ventas.json
```

## Control de stock

Cada producto contiene un atributo `stock`, que representa la cantidad disponible.

Antes de realizar una venta, el sistema comprueba que:

* El usuario exista.
* El producto exista.
* La cantidad sea mayor que cero.
* Exista stock suficiente.

Por ejemplo:

```text
Stock inicial: 10
Cantidad vendida: 2
Stock final: 8
```

Si se intenta vender una cantidad superior al stock disponible, la operación es rechazada y el stock no se modifica.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

## Responsabilidad de los componentes

### Producto

La clase `Producto` representa los productos disponibles en el restaurante.

Contiene información como:

* Código.
* Nombre.
* Precio.
* Categoría.
* Stock.

También permite disminuir el stock cuando se realiza una venta válida.

### Usuario

La clase `Usuario` representa a las personas registradas en el sistema que pueden realizar compras.

Su información puede almacenarse y recuperarse desde un archivo JSON.

### Venta

La clase `Venta` representa la operación realizada entre un usuario y un producto.

Contiene:

* `usuario_id`
* `producto_codigo`
* `cantidad`

### Restaurante

La clase `Restaurante` administra las colecciones de productos, usuarios y ventas.

También contiene las reglas principales del sistema, como:

* Buscar productos.
* Buscar usuarios.
* Registrar ventas.
* Validar stock.
* Disminuir el stock.
* Consultar ventas de un usuario.

### ArchivoServicio

`ArchivoServicio` se encarga de la persistencia de información mediante archivos JSON.

Administra:

* `productos.json`
* `usuarios.json`
* `ventas.json`

Utiliza `json.dump()` para guardar información y `json.load()` para recuperarla.

### main.py

Es el punto de entrada de la aplicación.

Se encarga de mostrar el menú, solicitar información mediante `input()` y llamar a los métodos correspondientes del servicio `Restaurante`.

La lógica de negocio no se realiza directamente en `main.py`.

## Persistencia de información

El sistema utiliza archivos JSON para conservar la información.

### productos.json

Almacena los productos registrados y su stock actualizado.

### usuarios.json

Almacena los usuarios registrados en el sistema.

### ventas.json

Almacena las ventas realizadas, relacionando al usuario con el producto vendido.

El flujo de persistencia es:

```text
Objeto
   ↓
Diccionario
   ↓
json.dump()
   ↓
Archivo JSON
```

Para recuperar la información:

```text
Archivo JSON
   ↓
json.load()
   ↓
Diccionario
   ↓
Objeto
```

## Persistencia después de una venta

Cuando se realiza una venta correctamente, se modifican dos elementos:

1. Se agrega una nueva `Venta` a la colección.
2. Se disminuye el stock del `Producto`.

Por esta razón se actualizan:

```text
ventas.json
productos.json
```

## Consulta de ventas por usuario

El sistema permite consultar únicamente las ventas relacionadas con un usuario determinado.

Para realizar esta operación se recorre la colección de ventas y se comparan las identificaciones:

```text
for venta in ventas:
    if venta.usuario_id == identificacion_usuario:
        agregar venta
```

De esta manera se demuestra el uso de colecciones para recorrer, comparar y filtrar objetos.

## Manejo de excepciones

El sistema contempla diferentes situaciones que pueden ocurrir durante la ejecución.

Se controlan excepciones como:

* `FileNotFoundError`: permite iniciar el programa con una colección vacía cuando todavía no existe un archivo JSON.
* `json.JSONDecodeError`: permite controlar archivos JSON que contienen información inválida.
* `PermissionError`: controla problemas relacionados con permisos de lectura o escritura.
* `KeyError`: controla registros JSON que no contienen las claves esperadas.
* `ValueError`: permite controlar datos inválidos durante las validaciones.

No se utiliza `except: pass` para ocultar errores.

## Pruebas realizadas

Para comprobar el funcionamiento del sistema se realizaron las siguientes pruebas:

### Prueba 1: Registrar producto

Se registró un producto con información de código, nombre, precio, categoría y stock.

### Prueba 2: Registrar usuario

Se registró un usuario en el sistema y se verificó que quedara almacenado.

### Prueba 3: Venta válida

Se seleccionó un usuario existente y un producto con stock disponible.

La venta fue registrada correctamente y el stock disminuyó.

### Prueba 4: Stock insuficiente

Se intentó vender una cantidad superior al stock disponible.

El sistema rechazó la operación y no permitió que el stock quedara negativo.

### Prueba 5: Consulta de ventas

Se consultaron las ventas asociadas a un usuario y se verificó que solamente aparecieran las operaciones relacionadas con dicho usuario.

### Prueba 6: Persistencia

Se cerró el programa y se volvió a ejecutar.

Los productos, usuarios y ventas almacenados en los archivos JSON fueron recuperados correctamente.

## Ejemplo de funcionamiento

Producto registrado:

```text
Código: P001
Nombre: Hamburguesa
Precio: $5.50
Categoría: Comida
Stock: 10
```

Venta realizada:

```text
Usuario: U001
Producto: P001
Cantidad: 2
```

Resultado:

```text
Venta registrada correctamente.
Stock restante: 8
```

## Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos
* Colecciones de objetos
* Archivos JSON
* `json.dump()`
* `json.load()`
* Git
* GitHub

## Forma de ejecución

Para ejecutar el proyecto se debe abrir una terminal dentro de la carpeta `restaurante_app` y utilizar:

```text
python main.py
```

También puede ejecutarse utilizando Python 3.13.

## Conclusión

El desarrollo de la Semana 11 permitió ampliar el sistema de restaurante construido durante las semanas anteriores, incorporando relaciones entre objetos mediante la entidad `Venta`.

La aplicación ahora permite relacionar usuarios con productos, controlar el stock disponible, registrar ventas y consultar las operaciones realizadas por cada usuario.

Además, se implementó la persistencia de productos, usuarios y ventas mediante archivos JSON, permitiendo recuperar la información después de cerrar y volver a ejecutar el programa.

Con esta implementación se fortaleció el uso de clases, objetos, colecciones, encapsulamiento, validaciones, manejo de excepciones y separación de responsabilidades dentro de una aplicación desarrollada con Programación Orientada a Objetos.
