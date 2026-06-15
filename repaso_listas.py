# Ejercicio 1 — Básico: agregar y recorrer listas

# Crea un programa que:

# Cree una lista vacía llamada nombres.
# Pida al usuario ingresar 5 nombres.
# Guarde cada nombre dentro de la lista.
# Recorra la lista e imprima:

# Ejemplo:

# Nombre registrado: Carlos
# Nombre registrado: Ana
# Nombre registrado: Pedro


# nombres = []

# for i in range(5):
#     nombre = input("Ingrese un nombre: ")
#     nombres.append(nombre)

# for nombre in nombres:
#     print(f"Nombre registrado: {nombre}")



# Ejercicio 2 — Buscar datos dentro de una lista

# Tenemos:

# frutas = ["manzana", "pera", "plátano", "naranja", "uva"]

# Haz un programa que:

# Pida al usuario una fruta.
# Revise si esa fruta existe en la lista.
# Si existe, mostrar:
# La fruta sí está disponible
# Si no existe:
# La fruta no está disponible

# frutas = ["manzana", "pera", "plátano", "naranja", "uva"]

# fruta = input("Ingrese una fruta: ")
# if fruta in frutas:
#     print("La fruta sí está disponible")
# else:
#     print("La fruta no está disponible")



# Ejercicio 3 — Contar elementos con una condición

# Tenemos:

# numeros = [5, 12, 8, 20, 3, 15, 7]

# Crea un programa que recorra la lista y cuente cuántos números son mayores que 10.

# El resultado debería ser:

# Hay 3 números mayores que 10

# numeros = [5, 12, 8, 20, 3, 15, 7]
# mayores = []
# cantidad = 0

# for numero in numeros:
#     if numero > 10:
#         cantidad += 1
#         mayores.append(numero)

# print(f"Hay {cantidad} números mayores que 10, los cuales son:")

# for numero in mayores:
#     print(numero)



# Ejercicio 4 — Lista de listas (nivel evaluación)

# Tenemos:

# productos = [
#     ["Pan", 1000],
#     ["Leche", 1500],
#     ["Huevos", 3000],
#     ["Arroz", 900]
# ]

# Haz un programa que muestre solamente los productos que cuestan más de 1200.

# Resultado esperado:

# Leche cuesta 1500
# Huevos cuesta 3000

# "Muestra todos los productos que cuestan más de 1200 y al final muestra cuántos productos fueron encontrados".

# Ejemplo:

# Leche cuesta 1500
# Huevos cuesta 3000

# Total productos encontrados: 2

# mayores = []
# total_mayores = 0

# productos = [
#     ["Pan", 1000],
#     ["Leche", 1500],
#     ["Huevos", 3000],
#     ["Arroz", 900]
# ]

# for producto in productos:
#     if producto[1] > 1200:
#         mayores.append(producto)
#         total_mayores += 1
#         print(f"{producto[0]} cuesta {producto[1]}")

# print(f"Total productos encontrados: {total_mayores}")



# Ejercicio 5 — Sistema de notas

# Crea un programa que:

# Cree una lista vacía llamada notas.
# Solicite al usuario ingresar 5 notas.
# Guarde las notas en la lista.
# Muestre:
# Todas las notas ingresadas.
# El promedio.
# Cuántas notas son mayores o iguales a 4.

# Ejemplo:

# Entrada:

# 5
# 3
# 6
# 2
# 4

# Salida:

# Notas: [5, 3, 6, 2, 4]
# Promedio: 4.0
# Notas aprobadas: 3

notas = []
total_notas = 0
total_notas_aprobadas = 0
suma = 0

for n in range(5):
    nota = float(input(f"Ingrese la nota {n + 1}: "))
    notas.append(nota)
    total_notas += 1
    suma += nota
    if nota >= 4:
        total_notas_aprobadas += 1

promedio = suma / total_notas

print(f"Notas: {notas}")
print(f"Promedio: {round(promedio, 1)}")
print(f"Notas aprobadas: {total_notas_aprobadas}")