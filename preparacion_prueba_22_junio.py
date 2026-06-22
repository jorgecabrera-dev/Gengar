# Ejercicio 1: Creación y Agregación (Listas de Diccionarios)
# Contexto: Basado en el sistema médico
# . Objetivo: Crear una función que reciba datos y los guarde en la lista global como un diccionario.
# Instrucciones: Completa la función agregar_mascota para que guarde un nombre y una especie en la lista veterinaria.

# veterinaria = []

# def agregar_mascota():
#     nombre = input("Nombre de la mascota: ")
#     especie = input("Especie: ")

#     nueva_mascota = {
#         "nombre": nombre,
#         "especie": especie
#     }
    
#     veterinaria.append(nueva_mascota)
#     print("¡Mascota agregada con éxito!")

# agregar_mascota()
# print(f"Lista actual: {veterinaria}")



# Ejercicio 2: Lógica de Validación (Funciones con Retorno)
# Contexto: Basado en la función validarEstado que evalúa la temperatura (>39 es grave)
# . Objetivo: Crear una función que valide si un vehículo es "Pesado" según su peso.
# Instrucciones: La función debe retornar True si el peso es mayor a 3500 kg y False si no

# def es_pesado(peso):
#     if peso > 3500:
#         return True
#     return False

# validacion_peso = int(input("Ingrese el peso a calcular: "))
# resultado = es_pesado(validacion_peso)
# print(resultado)

# Prueba:
# print(es_pesado(4000)) -> Debería mostrar True
# print(es_pesado(2000)) -> Debería mostrar False



# Ejercicio 3: Cálculos con Diccionarios (Matemática y Descuentos)
# Contexto: Basado en el sistema de cobros de salud
# . Objetivo: Calcular el precio final aplicando un descuento según el tipo de cliente.
# Instrucciones: Si el cliente es "VIP", tiene un 50% de descuento. Si es "REGULAR", un 10%. El precio base es 10.000.

# def calcular_pago(tipo_cliente):
#     precio_base = 10000
#     if tipo_cliente.lower() == "vip":
#         return precio_base * 0.5
#     elif tipo_cliente.lower() == "regular":
#         return precio_base * 0.9

# tipo_cliente = input("Ingrese su tipo de cliente: ")
# resultado = calcular_pago(tipo_cliente)
# print(f"Total: {resultado}")



# Ejercicio 4: Recorrer Diccionarios de Listas (Ciclos)
# Contexto: Basado en el sistema de parking donde cada piso es una lista
# . Objetivo: Contar cuántos elementos hay en total en toda la estructura.
# Instrucciones: Suma la cantidad de vehículos que hay en todos los pisos del diccionario parking.

# parking = { 
#     1: ["auto1", "auto2"], 
#     2: ["auto3"], 
#     3: [], 
#     4: ["auto4", "auto5", "auto6"] 
# }

# def contar_total_vehiculos():
#     total = 0
#     for lista_pisos in parking.values():
#         total += len(lista_pisos)
#     return total

# print(f"Hay {contar_total_vehiculos()} vehículos en total")



# El "Desafío Final": Integración Total
# Para llegar al nivel de exigencia de la prueba el lunes, el último paso es unir todo en un menú interactivo. 
# Según tus fuentes, ambos ejercicios (el médico y el parking) terminan con un ciclo while True y un bloque try-except para que el programa no se cierre si hay un error
# .
# Aquí tienes un ejercicio integrador para cerrar tu preparación:
# Instrucciones: Crea un mini sistema para una tienda usando una lista de diccionarios.
# Crea una lista vacía llamada inventario.
# Crea una función agregar_producto() que pida el nombre y el precio, y los guarde como un diccionario: {"nombre": n, "precio": p}
# .
# Crea una función ver_total() que recorra la lista y sume todos los precios.
# Crea un menú principal con un while True que permita elegir entre agregar, ver total o salir, usando match op o if/elif

# inventario = []

# def agregar_producto():
#     nombre = input("Ingrese el nombre del producto: ")
#     while True:
#         try:
#             precio = int(input("Ingrese el precio del producto: "))
#             nuevo_producto = {"nombre":nombre, "precio":precio}
#             inventario.append(nuevo_producto)
#             print("Producto agregado correctamente")
#             break
#         except ValueError:
#             print("Solo puede escribir numeros enteros")    

# def ver_total_producto():
#     totalP = 0
#     for precio in inventario:
#         totalP += precio["precio"]
#     return print(f"El total es {totalP}")

# def menu():
#     print("1. Agregar producto")
#     print("2. Ver total")
#     print("3. Salir")

# while True:
#     try:
#         menu()
#         op = int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 agregar_producto()
#             case 2:
#                 ver_total_producto()
#             case 3:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except ValueError:
#         print("Solo puede escribir numeros enteros")



# Ejercicio 1: Modificación en Listas de Diccionarios
# Contexto: Basado en la función tomarTemp() del sistema médico, donde buscas un elemento y cambias uno de sus valores
# .
# Situación: Tienes una lista de libros. Debes crear una función que permita cambiar el estado de un libro de "Disponible" a "Prestado".
# Estructura inicial:
# Tarea: Crea la función prestar_libro(). Debe mostrar los libros, pedir el número del libro (índice + 1) y cambiar su "estado" a "Prestado".

# biblioteca = {
#     1: {"nombre": "Libro de prueba", "estado": "disponible"},
#     2: {"nombre": "Python Pro", "estado": "disponible"}
# }

# def mostrar_libros():
#     print("Libros disponibles:")
#     # 'k' es el número, 'v' es el diccionario del libro
#     for k, v in biblioteca.items(): 
#         print(f"{k}.- {v['nombre']} ({v['estado']})")

# def prestar_libro():
#     mostrar_libros()
#     try:
#         prestar = int(input("Seleccione el número del libro: "))
        
#         # Validamos si el número existe en el diccionario (como en la fuente [2])
#         if prestar in biblioteca:
#             # Accedemos al diccionario del libro seleccionado
#             if biblioteca[prestar]["estado"] == "disponible":
#                 # CAMBIAMOS EL VALOR (Igual que tomarTemp en la fuente [1])
#                 biblioteca[prestar]["estado"] = "prestado"
#                 print("¡Libro prestado con éxito!")
#             else:
#                 print("El libro ya está prestado.")
#         else:
#             print("Ese número de libro no existe.")
#     except ValueError:
#         print("Debe ingresar un número.")

# prestar_libro()



# Ejercicio A (Listas):
# TAREA: Escribe el código para imprimir "pera"

frutas = ["manzana", "pera", "plátano"]

print(frutas[1])

# Ejercicio B (Diccionarios):
# TAREA: Escribe el código para imprimir el precio del auto

auto = {"marca": "Toyota", "precio": 5000}

print(auto["precio"])


# Ejercicio C:
# Basado en la fuente: pacientes = [{"nombre": "Ana", "temp": 36}, {"nombre": "Luis", "temp": 38}]
# TAREA 1: ¿Cómo accedes al diccionario COMPLETO de Luis?
# TAREA 2: ¿Cómo accedes SOLO a la temperatura de Ana? (Pista: usa el índice 0 y la llave "temp")

pacientes = [

    {"nombre": "Ana", "temp": 36}, 
    {"nombre": "Luis", "temp": 38}
]

print(pacientes[1])
print(pacientes[0]["temp"])


# Ejercicio D:
# Basado en la fuente: parking = { 1: , 2: [] }
# TAREA 1: ¿Cómo accedes a la lista de precios del piso 1? (Pista: usa la llave 1)
# TAREA 2: ¿Cómo agregas el valor 3000 a la lista del piso 2 usando .append()?

parking = {
    1: , # Piso 1: Tiene una lista con dos montos
    2: []            # Piso 2: Tiene una lista vacía
}
    
parking[2].append(3000)