# Ejercicio 1 — Modificar elementos por índice

# Tenemos:

# colores = ["rojo", "azul", "verde", "amarillo"]

# Haz un programa que:

# Cambie "verde" por "negro".
# Cambie "rojo" por "blanco".
# Muestre la lista final.

# Resultado esperado:

# ["blanco", "azul", "negro", "amarillo"]

# colores = ["rojo", "azul", "verde", "amarillo"]

# print(colores) # antes del cambio

# colores[2] = "negro"
# colores[0] = "blanco"

# print(colores) # despues del cambio



# Ejercicio 2 — Eliminar por valor

# Tenemos:

# animales = ["perro", "gato", "conejo", "pez", "gato"]

# Haz un programa que elimine "gato".

# Muestra la lista final.

# Ojo con algo importante:

# ¿Qué crees que pasa cuando hay dos elementos iguales?

# Resultado esperado si usas correctamente el método:

# ["perro", "conejo", "pez", "gato"]

# animales = ["perro", "gato", "conejo", "pez", "gato"]

# animales.remove("gato") # elimina el primer valor que coincida con el valor dentro del remove
# animales.pop(4) #elimina el valor que tenga como indice 4, y al mismo tiempo permite guardar esta accion. Ej: eliminado = animales.pop(4) guarda "gato" en la variable eliminado
# del animales[4] # lo mismo que el anterior, solo que en este caso solo elimina el valor, y no guarda la accion

# print(animales)



# Ejercicio 3 — Eliminar por índice

# Tenemos:

# numeros = [10, 20, 30, 40, 50]

# Elimina el número que está en el índice 2.

# Resultado esperado:

# [10, 20, 40, 50]

# numeros = [10, 20, 30, 40, 50]

# del numeros[2]

# print(numeros)



# Ejercicio 4 — Buscar posición de un elemento

# Tenemos:

# frutas = ["manzana", "pera", "uva", "naranja"]

# Haz un programa que:

# Pida una fruta al usuario.
# Si existe, muestre su posición.
# Si no existe, muestre un mensaje indicando que no está.

# Ejemplo:

# Entrada:

# uva

# Salida:

# La fruta está en la posición 2

# frutas = ["manzana", "pera", "uva", "naranja"]

# fruta = input("Ingrese una fruta: ")
# if fruta in frutas:
#     print(f"La fruta esta en la posicion {frutas.index(fruta)}")
# else:
#     print("La fruta no está disponible")



# Ejercicio 5 — Mini inventario (más parecido a evaluación)

# Tenemos:

# productos = [
#     ["Pan", 1000],
#     ["Leche", 1500],
#     ["Huevos", 3000]
# ]

# Haz un programa que:

# Muestre todos los productos.
# Cambie el precio de la leche a 2000.
# Elimine los huevos.
# Muestre la lista actualizada.

# Resultado esperado:

# [
#     ["Pan", 1000],
#     ["Leche", 2000]
# ]

productos = [
    ["Pan", 1000],
    ["Leche", 1500],
    ["Huevos", 3000]
]

for producto in productos:
    print(producto[0])

productos[1][1] = 2000
del productos[2]

print(productos)