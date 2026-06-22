# Contexto: Debes administrar el inventario de una biblioteca. 
# Los datos se guardan en una lista general, donde cada libro 
# es un diccionario independiente.

# 🎯 Instrucciones de Funcionamiento
# Diseña un menú interactivo que permita al usuario realizar 
# las siguientes acciones de forma continua hasta que decida salir:

# Crear (Agregar Libro): Solicita el ISBN, título y autor.

#     Condición: El ISBN debe ser estrictamente un número entero de 4 dígitos.

#     Control de errores: Si el usuario ingresa letras o un número de 
#     diferente longitud, debe mostrar un error y volver a pedir el ISBN.

#     Validación: Si el ISBN ya existe en la biblioteca, rechaza el 
#     registro. El estado prestado debe ser False por defecto.

# Leer (Mostrar Inventario): Imprime una lista visualmente atractiva 
# de todos los libros. Si el estado prestado es True, debe mostrar 
# "(No Disponible)"; si es False, "(Disponible en sala)".

# Actualizar (Prestar/Devolver): Pide el ISBN de un libro.

#     Control de errores: Maneja el caso en que el usuario ingrese 
#     texto en lugar de un número.

#     Condición: Si el libro existe, invierte su estado (si estaba 
#     prestado, ahora está devuelto, y viceversa). Si el ISBN no existe, 
#     notifica al usuario.

# Borrar (Dar de baja): Pide un ISBN para eliminar un libro del 
# sistema de forma permanente.

#     Condición Crítica: No puedes eliminar un libro que esté actualmente 
#     prestado. Si el usuario intenta borrarlo, el sistema debe bloquear 
#     la acción advirtiendo que el libro debe ser devuelto primero.


# biblioteca = [
#     {"isbn": 1001, "titulo": "1984", "autor": "George Orwell", "prestado": False},
#     {"isbn": 1002, "titulo": "Dune", "autor": "Frank Herbert", "prestado": True}
# ]

# def agregar():
#     while True:
#         try:
#             agregar_ISBN = int(input("Ingrese el ISBN del libro: "))
#             if len(agregar_ISBN) != 4:
#                 print("El ISBN solo puede contener 4 digitos")
#             else:    
#                 for isbn in biblioteca:
#                     if agregar_ISBN in isbn["isbn"]:
#                         print("El libro a registrar ya se encuentra en el inventario")
#                     else:
#                         agregar_titulo = input("Ingrese el titulo del libro: ")
#                         agregar_autor = input("Ingrese el autor del libro: ")
#                         biblioteca.append({"isbn": agregar_ISBN, "titulo": agregar_titulo, "autor": agregar_autor, "prestado": False})
#                         print("Libro agregado correctamente")
#         except Exception as e:
#             print(e)

# def mostrar():
#         for libro in biblioteca:
#             if libro["prestado"] == False:
#                 prestado = "Disponible en sala"
#             else:
#                 prestado = "No Disponible"
#             print(f"ISBN: {libro["isbn"]} - titulo: {libro["titulo"]} - autor: {libro["autor"]} - estado prestamo: {prestado}")

# def devolver():
#     mostrar()
#     actualizar = int(input("Ingrese el ISBN: "))
#     for isbn in biblioteca:
#         if actualizar in ["isbn"]:
#             isbn["prestado"] = False
#             print("Libro devuelto correctamente")
#         else:
#             print("El libro no existe")

# def borrar():
#     mostrar()
#     eliminar = int(input("Ingrese el ISBN del libro a eliminar: "))
#     for isbn in biblioteca:
#         if eliminar == isbn["isbn"]:
#             biblioteca.remove(isbn)
#             print("Libro eliminado exitosamente")
#         else:
#             print("El libro no se encuentra en el inventario")

# def menu():
#     print("1. Agregar libro")
#     print("2. Mostrar inventario")
#     print("3. Actualizar estado de libros")
#     print("4. Eliminar libro")
#     print("5. Salir")

# while True:
#     try:
#         menu()
#         op = int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 agregar()
#             case 2:
#                 mostrar()
#             case 3:
#                 devolver()
#             case 4:
#                 borrar()
#             case 5:
#                 print("Saliendo del programa")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception as e:
#         print(e)

biblioteca = [
    {"isbn": 1001, "titulo": "1984", "autor": "George Orwell", "prestado": False},
    {"isbn": 1002, "titulo": "Dune", "autor": "Frank Herbert", "prestado": True}
]


def agregar():
    while True:
        agregar_ISBN = input("Ingrese el ISBN del libro: ")

        # Validación del ISBN
        if not agregar_ISBN.isdigit() or len(agregar_ISBN) != 4:
            print("El ISBN debe ser un número entero de 4 dígitos")
            continue

        agregar_ISBN = int(agregar_ISBN)

        # Revisar si el ISBN ya existe
        existe = False

        for libro in biblioteca:
            if agregar_ISBN == libro["isbn"]:
                existe = True

        if existe:
            print("El libro ya se encuentra en el inventario")
            continue

        agregar_titulo = input("Ingrese el título del libro: ")
        agregar_autor = input("Ingrese el autor del libro: ")

        biblioteca.append({
            "isbn": agregar_ISBN,
            "titulo": agregar_titulo,
            "autor": agregar_autor,
            "prestado": False
        })

        print("Libro agregado correctamente")
        break


def mostrar():
    print("\n--- INVENTARIO DE BIBLIOTECA ---")

    for libro in biblioteca:

        if libro["prestado"]:
            estado = "No Disponible"
        else:
            estado = "Disponible en sala"

        print(f'''
ISBN: {libro["isbn"]}
Título: {libro["titulo"]}
Autor: {libro["autor"]}
Estado: {estado}
-----------------------------
''')


def actualizar():
    mostrar()

    try:
        actualizar_ISBN = int(input("Ingrese el ISBN del libro: "))

        encontrado = False

        for libro in biblioteca:

            if actualizar_ISBN == libro["isbn"]:

                # Cambia True a False o False a True
                libro["prestado"] = not libro["prestado"]

                encontrado = True

                if libro["prestado"]:
                    print("Libro prestado correctamente")
                else:
                    print("Libro devuelto correctamente")

                break

        if encontrado == False:
            print("El libro no existe")

    except:
        print("Debe ingresar un número válido")


def borrar():
    mostrar()

    try:
        eliminar = int(input("Ingrese el ISBN del libro a eliminar: "))

        encontrado = False

        for libro in biblioteca:

            if eliminar == libro["isbn"]:

                encontrado = True

                if libro["prestado"]:
                    print("No puedes eliminar un libro que está prestado")
                    break

                biblioteca.remove(libro)
                print("Libro eliminado exitosamente")
                break

        if encontrado == False:
            print("El libro no se encuentra en el inventario")

    except:
        print("Debe ingresar un número válido")


def menu():

    print("""
=========================
      BIBLIOTECA
=========================
1. Agregar libro
2. Mostrar inventario
3. Prestar / Devolver libro
4. Eliminar libro
5. Salir
""")


while True:

    try:

        menu()

        op = int(input("Seleccione una opción: "))

        match op:

            case 1:
                agregar()

            case 2:
                mostrar()

            case 3:
                actualizar()

            case 4:
                borrar()

            case 5:
                print("Saliendo del programa")
                break

            case _:
                print("Opción inválida")


    except:
        print("Debe ingresar una opción válida")