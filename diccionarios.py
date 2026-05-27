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

productos = []
while True:

    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Eliminar producto")
    print("4. Actualizar producto")
    print("5. Salir")
    op = int(input("Seleccione una opción: "))
    match op:
        case 1:
            nombre = input("Ingrese el nombre del producto: ")
            precio = int(input("Ingrese el precio del producto: "))
            nuevo_producto = {"nombre":nombre, "precio":precio}
            productos.append(nuevo_producto)
        case 2:
            print(productos)
        case 3:
            ("")
        case 4:
            ("")
        case 5:
            print("Gracias por su preferencia")
            break
        case _:
            print("Opción inválida")

