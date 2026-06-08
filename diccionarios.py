# uso y explicación de diccionarios

# alumno = {
#     "nombre":"Shinji Ikari",
#     "edad":14,
#     "carrera":"Piloto"
# }

# print(alumno)
# print(alumno["carrera"])

# for i, j in alumno.items():
#     print(i, j)

# alumno["email"] = "shinji@nerv.com"
# alumno["carrera"] = "escritor"
# del alumno["edad"]

# for i, j in alumno.items():
#     print(i, j)


# productos = {
#     1:{"nombre":"control inlámbrico",
#        "categoría":"Electrónica",
#        "precio":45000},
#     2:{"nombre":"pilas recargables",
#        "categoría":"insumos",
#        "precio":5008},
#     3:{"nombre":"pasta térmica",
#        "categoría":"computación",
#        "precio":7000}
# }

# print(productos[1]["nombre"])


# Modificar el programa del carrito de compras 
# para poder utilizarlo con listas

# productos = []
# while True:

#     print("1. Agregar producto")
#     print("2. Mostrar producto")
#     print("3. Eliminar producto")
#     print("4. Actualizar producto")
#     print("5. Salir")
#     op = int(input("Seleccione una opción: "))
#     match op:
#         case 1:
#             nombre = input("Ingrese el nombre del producto: ")
#             precio = int(input("Ingrese el precio del producto: "))
#             nuevo_producto = {"nombre":nombre, "precio":precio}
#             productos.append(nuevo_producto)
#         case 2:
#             print(productos)
#         case 3:
#             borrar = input("Ingrese el nombre del producto que desea eliminar: ")
#             productos.remove(borrar)
#         case 4:
#             ("")
#         case 5:
#             print("Gracias por su preferencia")
#             break
#         case _:
#             print("Opción inválida")


# CRUD DE VEGETALES

# vegetales = {
#     1: "Maracuya",
#     2: "Pera",
#     3: "Cebolla",
#     7: "Papa"
# }

# def espacios():
#     print("-" * 40)

# def error():
#     print("Error. Solo puede ingresar números enteros")

# def escribir():
#     ingreso = input("Ingrese el nombre del vegetal a agregar: ")
#     nuevoKey = list(vegetales.keys())[-1]
#     vegetales[nuevoKey + 1] = ingreso
#     print(f"{ingreso} añadido correctamente")

# def mostrar():
#     print("-" * 40)
#     for num, nombre in vegetales.items():  
#         print(f"{num}. {nombre}")

# def borrar():
#     while True:
#         try: 
#             eliminar = int(input("Seleccione el vegetal a eliminar: "))
#             if eliminar in vegetales.keys():
#                 eliminado = vegetales[eliminar]
#                 del vegetales[eliminar]
#                 print(f"{eliminado} eliminado correctamente")
#                 return
#             else:
#                 print("Número de vegetal inválido. Inténtelo nuevamente.")
#         except ValueError:
#             error()

# def actualizar():
#     while True:
#         try:
#             actualizado = int(input("Seleccione el vegetal a actualizar: "))
#             if actualizado in vegetales.keys():
#                 vegetales [actualizado] = input("Ingrese el nuevo vegetal: ")
#                 print("Actualización exitosa")
#                 return
#             else:
#                 print("Número de vegetal inválido. Inténtelo nuevamente.")
#         except ValueError:
#             error()

# def menu():
#     espacios()
#     print("1. Agregar un vegetal")
#     print("2. Eliminar un vegetal")
#     print("3. Actualizar un vegetal")
#     print("4. Mostrar vegetales")
#     print("5. Salir")
#     espacios()

# while True:
#     try:
#         menu()
#         op = int(input("Seleccione una opción: "))
#         match op:
#             case 1:
#                 escribir()
#             case 2:
#                 mostrar()
#                 espacios()
#                 borrar()
#             case 3:
#                 mostrar()
#                 espacios()
#                 actualizar()
#             case 4:
#                 mostrar()
#             case 5:
#                 print("Hasta pronto")
#                 break
#             case _:
#                 print("Opción inválida")       
#     except ValueError:
#         error()


# Lista con diccionarios

productosDicc = {
    1:{"nombre": "Maracuya", "precio": 3000},
    2:{"nombre": "Pera", "precio": 1500},
    3:{"nombre": "Cebolla", "precio": 1200},
    4:{"nombre": "Papa", "precio": 3500}
}

def espacios2():
    print("-" * 40)

def error2():
    print("Error. Solo puede ingresar números enteros")

def escribir2():
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio: "))
    nuevoKey = list(productosDicc.keys())[-1]
    productosDicc[nuevoKey + 1] = {"nombre": nombre, "precio": precio}

def mostrar2():
    print("-" * 40)
    for nom, prec in productosDicc.items():  
        print(f"{nom}. {prec}")

def borrar2():
    while True:
        try: 
            eliminar = int(input("Seleccione el vegetal a eliminar: "))
            if eliminar in productosDicc.keys():
                eliminado = productosDicc[eliminar]
                del productosDicc[eliminar]
                print(f"{eliminado} eliminado correctamente")
                return
            else:
                print("Número de vegetal inválido. Inténtelo nuevamente.")
        except ValueError:
            error2()

def actualizar2():
    while True:
        try:
            actualizado = int(input("Seleccione el vegetal a actualizar: "))
            if actualizado in productosDicc.keys():
                nombre = input("Ingrese el nuevo nombre: ")
                precio = input("Ingrese su precio: ")
                productosDicc [actualizado] = {"nombre": nombre, "precio": precio}
                print("Actualización exitosa")
                return
            else:
                print("Número de vegetal inválido. Inténtelo nuevamente.")
        except ValueError:
            error2()

def menu2():
    espacios2()
    print("1. Agregar un vegetal")
    print("2. Eliminar un vegetal")
    print("3. Actualizar un vegetal")
    print("4. Mostrar vegetales")
    print("5. Salir")
    espacios2()

while True:
    try:
        menu2()
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                escribir2()
            case 2:
                mostrar2()
                espacios2()
                borrar2()
            case 3:
                mostrar2()
                espacios2()
                actualizar2()
            case 4:
                mostrar2()
            case 5:
                print("Hasta pronto")
                break
            case _:
                print("Opción inválida")       
    except ValueError:
        error2()