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

def ingresar():
    ingreso = input("Ingrese el nombre del juguete a agregar: ")
    juguetes.append(ingreso)
    print(f"{ingreso} añadido correctamente")

def borrar():
    eliminar = input("Ingrese el nombre del juguete que desea eliminar: ")
    juguetes.remove(eliminar)
    print(f"{eliminar} eliminado correctamente")

def mostrar():
    c = 1
    for i in juguetes:
        print(f"{c}. {i}")
        c += 1

while True:
    try:
        print("1. Agregar un juguete")
        print("2. Eliminar un juguete")
        print("3. Actualizar un juguete")
        print("4. Mostrar un juguete")
        print("5. Salir")
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                ingresar()
            case 2:
                borrar()
            case 3:
                reemplazo = input("Ingrese el nombre del juguete que desea actualizar: ")
                modificado = input("Ingrese el nombre del juguete nuevo: ")
                juguetes[reemplazo] = modificado
                print("Se ha actualizado correctamente")
            case 4:
                mostrar()
            case 5:
                print("Hasta pronto")
                break
            case _:
                print("Opción inválida")       
    except:
        print("Solo números enteros")
