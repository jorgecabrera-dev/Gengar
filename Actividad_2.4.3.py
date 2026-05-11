totalIngresos = 0
cantPas = int(input("Ingrese la cantidad de pasajes a vender: "))

for i in range (cantPas):
    try:
        precio = int(input(f"Ingrese monto a pagar por el pasaje {i + 1}: "))
        totalIngresos += precio
    except:
        print("El valor ingresado no es un número entero")   
        break

print(f"El total de ingresos por la venta es {totalIngresos}")


# si el usuario se equivoca y queremos seguir pidiendo los valores restantes:

# totalIngresos = 0
# cantPas = int(input("Ingrese la cantidad de pasajes a vender: "))

# for i in range (cantPas):
#     while True:
#         try:
#             precio = int(input(f"Ingrese monto a pagar por el pasaje {i + 1}: "))
#             break
#         except:
#             print("El valor ingresado no es un número entero")   
#     totalIngresos += precio

# print(f"El total de ingresos por la venta es {totalIngresos}")