from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

restaurante = Restaurante()
# Crear restaurante
restaurante = Restaurante()

# Crear platillos
platillo1 = Platillo(
    "Pizza",
    8.50,
    True,
    "Comida rápida"
)

platillo2 = Platillo(
    "Encebollado",
    5.00,
    True,
    "Tradicional"
)

# Crear bebidas
bebida1 = Bebida(
    "Coca-Cola",
    1.50,
    True,
    500
)

bebida2 = Bebida(
    "Jugo de Naranja",
    2.00,
    False,
    350
)

# Agregar productos
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)

# Mostrar productos
restaurante.mostrar_productos()

# Probar encapsulación
print("Precio actual:", platillo1.obtener_precio())

platillo1.cambiar_precio(9.00)

print("Nuevo precio:", platillo1.obtener_precio())

platillo1.cambiar_precio(-5)