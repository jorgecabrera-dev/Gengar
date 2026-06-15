# Mini evaluación listas — Nivel 1

# Crear un programa para administrar una lista de compras.
# Debe tener un menú:

# 1. Agregar producto
# 2. Mostrar productos
# 3. Buscar producto
# 4. Eliminar producto
# 5. Salir

# La lista inicialmente:
# compras = []

# Opción 1:
# El usuario ingresa un producto y se agrega.
# Opción 2:
# Mostrar todos los productos.
# Opción 3:
# Buscar un producto. Debe mostrar si el producto se encontro o no.
# Opción 4:
# Eliminar un producto. Validar existencia antes de realizar la eliminacion
# Opción 5:
# Salir

compras = []

def espacios():
    print("-" * 20)

def error():
    print("Solo debe seleccionar numeros enteros")

def menu():
    espacios()
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Salir")
    espacios()

def agregar():
    while True:
        producto_entrante = input("Ingrese el nombre del producto (Ingrese un 0 para terminar): ")
        if producto_entrante == "0":
            print("Volviendo al menu principal")
            break
        else:
            compras.append(producto_entrante)

def mostrar():
    espacios()
    n = 1
    for producto in compras:
        print(f"{n}. {producto}")
        n += 1
    espacios()    

def buscar():
    espacios()
    producto_a_buscar = input("Ingrese el producto a buscar: ")
    if producto_a_buscar in compras:
        print("Producto encontrado")
    else:
        print("Producto no encontrado")

def borrar():
    mostrar()    
    while True:
        try:
            producto_a_eliminar = int(input("Ingrese el producto que desea eliminar: "))
            if producto_a_eliminar >= 1 and producto_a_eliminar <= len(compras):
                eliminado = compras.pop(producto_a_eliminar - 1)
                print(f"Producto {eliminado} eliminado")
                break
            else:
                print("Producto no encontrado")
        except ValueError:
            error()

def actualizar():
    mostrar()
    while True:
        try:
            producto_actualizable = int(input("Seleccione el producto a actualizar: "))
            if producto_actualizable >= 1 and producto_actualizable <= len(compras):
                compras[producto_actualizable - 1] = input("Ingrese el nuevo nombre del producto: ")
                print("Actualizado correctamente")
                break
            else:
                print("Producto no encontrado")
        except ValueError:
            print("Solo debe seleccionar numeros enteros")

while True:
    try:
        menu()
        op = int(input("Seleccione una opcion: "))
        match op:
            case 1:
                agregar()
            case 2:
                mostrar()
            case 3:
                buscar()
            case 4:
                borrar()
            case 5:
                actualizar()
            case 6:
                print("Hasta pronto")
                break
            case _:
                print("Opcion invalida")
    except ValueError:
        error()            


































































































































