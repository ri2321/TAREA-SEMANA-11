# Restaurante App – Semana 12

## Descripción del proyecto

Este proyecto corresponde a la evolución de la aplicación `restaurante_app` desarrollada durante las semanas anteriores de la asignatura de Programación Orientada a Objetos.

La aplicación permite administrar productos, usuarios y ventas. Además, mantiene el control del stock de los productos y conserva la información mediante archivos JSON.

Para la Semana 12 se realizaron mejoras internas relacionadas con el uso de colecciones en Python, buscando optimizar las búsquedas y consultas frecuentes sin modificar las funcionalidades principales desarrolladas anteriormente.

---

## Funcionalidades principales

El sistema permite:

* Registrar productos.
* Listar productos.
* Buscar productos mediante su código.
* Actualizar productos.
* Eliminar productos.
* Registrar usuarios.
* Listar usuarios.
* Buscar usuarios mediante su identificación.
* Realizar ventas.
* Controlar automáticamente el stock disponible.
* Consultar las ventas realizadas por un usuario.
* Listar las ventas registradas.
* Guardar y recuperar la información mediante archivos JSON.

---

## Mejoras implementadas en la Semana 12

La aplicación conserva las listas principales de productos, usuarios y ventas, ya que estas estructuras son útiles para almacenar objetos, recorrer la información y guardar los datos en archivos JSON.

Sin embargo, se incorporaron estructuras auxiliares utilizando diccionarios (`dict`) para optimizar operaciones que anteriormente requerían recorrer listas completas.

### Índice de productos

Se implementó el diccionario:

```python
productos_por_codigo
```

Este índice permite relacionar directamente el código de cada producto con su respectivo objeto.

De esta manera, la búsqueda de un producto se realiza directamente mediante su código:

```python
producto = productos_por_codigo.get(codigo)
```

---

### Índice de usuarios

Se implementó el diccionario:

```python
usuarios_por_identificacion
```

Este índice permite localizar rápidamente un usuario utilizando su número de identificación.

La búsqueda se realiza de la siguiente manera:

```python
usuario = usuarios_por_identificacion.get(identificacion)
```

---

### Índice de ventas por usuario

Se implementó el diccionario:

```python
ventas_por_usuario
```

Este índice agrupa las ventas realizadas por cada usuario.

Por ejemplo:

```text
Identificación del usuario
        ↓
Lista de ventas realizadas
```

Gracias a esta estructura, el sistema puede consultar las ventas de un usuario sin recorrer toda la colección general de ventas en cada consulta.

---

## Colecciones utilizadas

| Colección | Uso                                            |
| --------- | ---------------------------------------------- |
| `list`    | Almacenar productos, usuarios y ventas.        |
| `dict`    | Crear índices para realizar búsquedas rápidas. |

Las listas principales se mantienen porque permiten recorrer y persistir los objetos.

Los diccionarios funcionan como índices auxiliares para mejorar las operaciones de búsqueda y consulta.

---

## Sincronización de las colecciones

Los índices auxiliares se mantienen sincronizados cuando se realizan operaciones dentro del sistema.

Por ejemplo:

* Al registrar un producto, también se agrega al índice de productos.
* Al eliminar un producto, se elimina de la lista y del índice.
* Al registrar un usuario, también se agrega al índice de usuarios.
* Al realizar una venta, se agrega a la lista principal de ventas y al índice correspondiente al usuario.
* Al iniciar nuevamente la aplicación, los datos son recuperados desde los archivos JSON y los índices se reconstruyen en memoria.

---

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

---

## Ejecución del programa

Para ejecutar la aplicación, abra una terminal dentro de la carpeta del proyecto y ejecute:

```bash
python main.py
```

También puede utilizar:

```bash
python3 main.py
```

dependiendo de la configuración de Python instalada en el equipo.

---

## Pruebas realizadas

Durante el desarrollo se deben comprobar las siguientes operaciones:

1. Cargar los productos, usuarios y ventas desde los archivos JSON.
2. Buscar un producto mediante su código.
3. Buscar un usuario mediante su identificación.
4. Consultar las ventas registradas por un usuario.
5. Realizar una nueva venta.
6. Verificar que el stock del producto disminuya correctamente.
7. Comprobar que los índices auxiliares se actualicen después de registrar o eliminar información.
8. Cerrar y volver a ejecutar el programa.
9. Confirmar que los datos almacenados en JSON se recuperen correctamente.
10. Confirmar que los índices en memoria se reconstruyan al iniciar la aplicación.

---

## Conclusión

Las mejoras implementadas permiten utilizar de manera más eficiente las colecciones de Python dentro de la aplicación. Las listas continúan siendo utilizadas como estructuras principales para almacenar y recorrer los objetos del sistema, mientras que los diccionarios permiten crear índices auxiliares para realizar búsquedas y consultas frecuentes de forma más directa.

De esta manera, la aplicación conserva la arquitectura y funcionalidades desarrolladas en la Semana 11, incorporando mejoras relacionadas con el rendimiento y la organización de la información mediante colecciones.
