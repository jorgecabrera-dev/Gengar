productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}
productosDicc[4]={"nombre": "Tomate", "precio": 1500} 


# print(productosDicc.keys())
# print(productosDicc.values())
# print(productosDicc.items())
# listadeKeys=list(productosDicc.keys())

# print(list(productosDicc.keys())[-1])
carrito=[]
def agregaProducto():
    nombreP=input("Ingrese el nombre del Producto: ")
    precioP=int(input("Ingrese el precio del Producto: "))
    productosDicc[list(productosDicc.keys())[-1]+1]={"nombre": nombreP, "precio": precioP} 
def muestraProducto():
    print("-"*30)
    for nombre, precio in productosDicc.items():
        print(f"{nombre} .-  {precio}")
    print("-"*30)
def eliminaProducto():
    muestraProducto()
    borra=int(input("Cual desea eliminar?: "))
    del productosDicc[borra]
def actualiazaProducto():
    muestraProducto()
    actualiza=int(input("Cual producto desea actualizar?: "))
    nuevonombre=input("ingrese el nuevo nombre") 
    nuevoPRECIO=input("ingrese el nuevo precio") 
    productosDicc[actualiza]={"nombre":nuevonombre , "precio": nuevoPRECIO}

def comprar():
    while True:
        muestraProducto()
        try:
            comprar=int(input("¿Cual producto desea comprar? Ingrese un 0 para salir. "))
            if comprar in productosDicc:
                print(f"Usted ha comprado {productosDicc[comprar]['nombre']} por un valor de {productosDicc[comprar]['precio']}")
                carrito.append(productosDicc[comprar])
            elif comprar == 0:
                print("Volviendo al menú principal")
                print("-"*30)
                break
            else:
                print("Producto no existe")
        except ValueError:
            print("Debe ingresar un número válido")
def boleta():
    total=0
    for p in carrito:
        total+=int(p["precio"])
    iva=total*0.19
    print(f"El total de su compra es {total} y el IVA es {iva}")
    print(f"El total a pagar es  {total+iva} ")
def productosMenu():
    while True:
        try:
            print("1.- Agregar Producto")
            print("2.- Eliminar Producto")
            print("3.- Actualizar Producto")
            print("4.- Mostrar Producto")
            print("5.- Comprar Productos")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregaProducto()
                case 2:
                    eliminaProducto()
                case 3:
                    actualiazaProducto()
                case 4:
                    muestraProducto()
                case 5:
                    comprar()
                case 6:
                    boleta()
                    print("Gracias por su preferencia")
                    break
                case _:
                    print("Opcion invalida")  
        except Exception as e:
            print("Error :", e)


productosMenu()