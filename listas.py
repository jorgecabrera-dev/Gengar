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