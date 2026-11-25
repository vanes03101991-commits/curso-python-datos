
# 1. Crear al menos dos diccionarios de productos
# Cada diccionario representa un producto con sus propiedades (claves y valores)
producto1 = {
    "nombre": "Camiseta Deportiva",
    "categoria": "Ropa",
    "precio": 25.99,
    "cantidad": 50,
}

producto2 = {
    "nombre": "Zapatos de Running",
    "categoria": "Calzado",
    "precio": 60.50,
    "cantidad": 20,
}

producto3 = {
    "nombre": "Gorra Casual",
    "categoria": "Ropa",
    "precio": 15.00,
    "cantidad": 35,
}

# 2. Guardar los productos en una lista
# Creamos una lista llamada 'inventario' que contiene nuestros diccionarios
inventario = [producto1, producto2, producto3]

print("--- INVENTARIO INICIAL ---")
print(inventario)

# 3. Consultar el nombre de un producto (y otros datos)
# Podemos acceder a los elementos de la lista por su índice y buscar la clave 'nombre'
print("\n--- CONSULTANDO PRODUCTOS ---")
print(f"El primer producto es: {inventario[0]['nombre']}")
print(f"Su categoría es: {inventario[0]['categoria']}")
print(f"Su precio es: ${inventario[0]['precio']}")

# 4. Modificar un precio o una cantidad
# Supongamos que queremos bajar el precio de los Zapatos de Running (producto en el índice 1)
print("\n--- MODIFICANDO DATOS ---")
print(
    f"Precio anterior de {inventario[1]['nombre']}: ${inventario[1]['precio']}"
)

# Modificamos el precio y la cantidad
inventario[1]["precio"] = 55.00
inventario[1]["cantidad"] = 18

print(
    f"Nuevo precio de {inventario[1]['nombre']}: ${inventario[1]['precio']}"
)
print(f"Nueva cantidad disponible: {inventario[1]['cantidad']}")

# 5. Crear un conjunto de categorías únicas
# Usamos una comprensión de conjuntos ({...}) para recorrer la lista y extraer la categoría de cada producto.
# Los conjuntos (sets) eliminan automáticamente los elementos duplicados (como el segundo "Ropa").
categorias_unicas = {producto["categoria"] for producto in inventario}

print("\n--- CATEGORÍAS ÚNICAS ---")
print(categorias_unicas)
