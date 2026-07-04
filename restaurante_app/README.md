# Sistema de Restaurante - Programación Orientada a Objetos

## Estudiante

**Nombre:** Ricardo Cando

**Asignatura:** Programación Orientada a Objetos

**Semana:** 6

---

# Descripción

Este proyecto consiste en un sistema básico para administrar los productos de un restaurante utilizando Programación Orientada a Objetos (POO) en Python.

El sistema permite registrar platillos y bebidas, almacenarlos en una lista y mostrar su información en la consola. Durante el desarrollo se aplican los principios fundamentales de la POO como herencia, encapsulación y polimorfismo.

---

# Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py
```

---

# Herencia

La clase **Producto** es la clase padre del sistema.

De ella heredan las clases:

- Platillo
- Bebida

Esto permite reutilizar atributos y métodos comunes.

```
Producto
│
├── Platillo
└── Bebida
```

---

# Encapsulación

El atributo **__precio** fue declarado como privado dentro de la clase Producto para proteger la información.

Su acceso se realiza mediante los métodos:

- obtener_precio()
- cambiar_precio()

El método **cambiar_precio()** valida que el nuevo precio sea mayor que cero.

---

# Polimorfismo

Las clases **Platillo** y **Bebida** sobrescriben el método:

```
mostrar_informacion()
```

Cuando el programa recorre la lista de productos, cada objeto muestra información diferente según su tipo.

---

# Funcionalidades

- Registrar platillos.
- Registrar bebidas.
- Mostrar todos los productos.
- Modificar el precio de un producto.
- Validar que el precio sea mayor que cero.
- Aplicar herencia.
- Aplicar encapsulación.
- Aplicar polimorfismo.

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

La Programación Orientada a Objetos facilita la organización del código, permite reutilizar clases mediante la herencia, protege la información con encapsulación y hace posible que diferentes objetos respondan de manera distinta utilizando el mismo método gracias al polimorfismo. Estos principios contribuyen al desarrollo de aplicaciones más ordenadas, reutilizables y fáciles de mantener.

---

# Autor

**Ricardo Cando**