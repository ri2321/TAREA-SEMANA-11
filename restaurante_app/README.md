# Sistema de Restaurante - Programación Orientada a Objetos

## Estudiante

**Nombre:** Ricardo Rubén Cando Arguello

**Asignatura:** Programación Orientada a Objetos

**Semana:** 8

---

# Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión para un restaurante utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite registrar y listar productos, bebidas y clientes mediante un menú interactivo ejecutado desde la consola.

El proyecto está organizado de forma modular para facilitar el mantenimiento del código y demostrar la aplicación de los principios SOLID.

---

# Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

---

# Responsabilidad de cada clase

### Producto

Representa un producto general del restaurante y almacena información como código, nombre, categoría y precio.

### Bebida

Hereda de la clase Producto y añade información específica, como el tamaño o el tipo de envase. Además, sobrescribe el método `mostrar_informacion()`.

### Cliente

Representa la información de un cliente registrado mediante su identificación, nombre y correo electrónico.

### Restaurante

Administra las colecciones de productos y clientes. También valida que no existan códigos de productos ni identificaciones de clientes repetidas.

### main.py

Es el punto de entrada del programa. Presenta el menú interactivo, solicita la información al usuario y utiliza los métodos de la clase Restaurante.

---

# Relación entre Producto y Bebida

La clase **Bebida** hereda de **Producto**, ya que una bebida es un tipo de producto. Gracias a esta relación, ambos objetos pueden almacenarse en una misma colección y utilizar el método `mostrar_informacion()` mediante polimorfismo.

---

# Principios SOLID aplicados

## SRP (Single Responsibility Principle)

Cada clase tiene una única responsabilidad:

* Producto representa productos.
* Bebida representa bebidas.
* Cliente representa clientes.
* Restaurante administra el sistema.
* main.py controla la interacción con el usuario.

## OCP (Open/Closed Principle)

La clase Bebida amplía el comportamiento de Producto mediante herencia sin modificar la lógica del sistema.

## LSP (Liskov Substitution Principle)

Los objetos de la clase Bebida pueden utilizarse como objetos de la clase Producto sin afectar el funcionamiento del programa.

---

# Funcionalidades

* Registrar productos.
* Registrar bebidas.
* Registrar clientes.
* Listar productos.
* Listar clientes.
* Validar códigos de productos duplicados.
* Validar identificaciones de clientes duplicadas.
* Aplicar herencia y polimorfismo.

---

# Ejecución

Desde la carpeta **restaurante_app** ejecutar:

```bash
python main.py
```

o

```bash
python3 main.py
```

---

# Reflexión

Este proyecto permitió comprender la importancia de organizar el código mediante clases con responsabilidades específicas. La aplicación de los principios SOLID mejora la estructura del programa, facilita su mantenimiento y permite ampliar sus funcionalidades sin modificar el código existente. Además, el uso de herencia y polimorfismo demuestra cómo reutilizar código de manera eficiente.

---

# Autor

**Ricardo Rubén Cando Arguello**
