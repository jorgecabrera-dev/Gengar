# Almacenamiento de Biblioteca
# Los espacios son noventa
# Cada libro usa un espacio
# === MENÚ PRINCIPAL ===
# 1. Espacios disponibles 
# 2. Poner libros 
# 3. Sacar libros 
# 4. Historial de ocupaciones 
# 5. Salir 

# Historial de Ocupaciones
# • Mostrar la cantidad de libros registrados en la
# biblioteca durante la sesión.
# • Cada registro debe aumentar el historial.
# • Cada retiro debe disminuir el historial.

total = 90
totalIngresos = 0
totalRetiros = 0
opc = 0

while opc != 5:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Espacios disponibles ")
    print("2. Poner libros ")
    print("3. Sacar libros")
    print("4. Historial de ocupaciones")
    print("5. Salir")
    while True:
        try:
            opc = int(input("Seleccione una opción: "))
            break
        except:
            print("Solo debe ingresar números enteros")
    match opc:
        case 1:
            print(f"El espacio disponible es {total}")
        case 2:
            print("Ingresando libros")
            while True:
                try:
                    ingreso = int(input("¿Cuántos libros va a ingresar?: "))
                    totalIngresos += 1
                    total += ingreso * 90
                    break
                except:
                    print("Solo debe ingresar números enteros")
        case 3:
            print("Retirando libros")
            while True:
                try:
                    retiro = int(input("¿Cuántos libros va a retirar?: "))
                    totalRetiros += 1
                    total -= retiro * 90
                    break
                except:
                    print("Solo debe ingresar números enteros")  
        case 4:
            print("Mostrando el historial de ocupaciones:")
            if totalIngresos >= 1 and totalRetiros ==0:
                print(f"Se han registrado {totalIngresos} libros")
            elif totalIngresos >= 1 and totalRetiros >= 1:
                print(f"Han ingresado {totalIngresos} libros y se han retirado {totalRetiros}")
            elif totalRetiros >= 1 and totalIngresos == 0:
                print(f"Se han retirado {totalRetiros} libros")
        case 5:
            print("Hasta pronto")
        case _:
            print("Opción inválida")




