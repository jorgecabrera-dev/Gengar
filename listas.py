# explicación y uso de listas

# lista = [8, 20, 12, 87, 1024]
#        0   1   2   3   4

# print(lista)
# print(lista[4])

# for elemento in lista:
#     print(elemento)


# crear una lista de 4 frutas
# mostrar cada elemento individualmente

# frutas = ["manzana", "pera", "frutilla", "uva"]
# frutas.append("higo")
# vocales = "aeiou"

# for i in frutas:
#     if i[0].lower() in vocales:
#         print(f"La fruta {i} comienza con vocal")
#     else:    
#         print(f"La fruta {i} NO comienza con vocal")


# hacer una lista de nombres y otra de apellidos
# mostrar las listas como si fueran nombres
# vale decir, Diego Robles, Adolfo Hinako, Luis Mussolini

# nombres = ["Diego", "Adolfo", "Luis"]
# apellidos = ["Robles", "Hinako", "Mussolini"]

# for i in range(len(nombres)):
#     print(nombres[i], apellidos[i])


# Las listas pueden tener tipos de datos dispares

# datos = [4, 6.9, "Alonsonic", False]

# for i in datos:
#     print(i)


# para mostrar un elemento dentro de una lista
# que a su vez está dentro de otra

# matrix = [
#     [5, 8, 3], [79, 34, 24]
# ]

# print(matrix)
# print(matrix[1][0])


# colores = ["blanco", "negro", "purpura", "naranja"]

# for i in colores:
#     print(i)

# agregar = input("Ingrese un color: ")
# colores.append(agregar)

# for i in colores:
#     print(i)


juguetes = ["yo-yo", "tetris"]

def menu():
    print("-" * 20)
    print("1. Agregar un juguete")
    print("2. Eliminar un juguete")
    print("3. Actualizar un juguete")
    print("4. Mostrar un juguete")
    print("5. Salir")
    print("-" * 20)
    
def escribir():
    ingreso = input("Ingrese el nombre del juguete a agregar: ")
    juguetes.append(ingreso)
    print(f"{ingreso} añadido correctamente")

def borrar():
    try:
        eliminar = int(input("¿Cuál juguete desea eliminar?: "))
        if eliminar >= 1 and eliminar <= len(juguetes):
            eliminado = juguetes.pop[eliminar - 1]
            print(f"{eliminado} eliminado correctamente")
        else:
            print("Número de juguete inválido")
    except ValueError:
        error()

def actualizar():
    try:
        actualizado = int(input("¿Cuál juguete desea actualizar?: "))
        if actualizado >= 1 and actualizado <= len(juguetes):
            juguetes[actualizado - 1] = input("Ingrese el nuevo nombre: ")
            print("Actualizado correctamente")
        else:
            print("Número de juguete inválido")
    except ValueError:
        error()

def mostrar():
    c = 1
    for i in juguetes:
        print(f"{c}. {i}")
        c += 1

def error():
    print("Error. Solo puede ingresar números enteros")

while True:
    try:
        menu()
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                escribir()
            case 2:
                mostrar()
                print("-" * 20)
                borrar()
            case 3:
                mostrar()
                print("-" * 20)
                actualizar()
            case 4:
                mostrar()
            case 5:
                print("Hasta pronto")
                break
            case _:
                print("Opción inválida")       
    except ValueError:
        error()
