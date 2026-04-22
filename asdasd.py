
op = 0

def pin():
    print("--- Creador de PIN 4 dígitos ---")
    pin = int(input("Ingrese un pin de 4 dígitos: "))
    if len(str(pin)) == 4:
        print("Pin creado exitosamente")
    else:
        print("Cantidad de dígitos incorrecta")


def notas():
    print("--- Calculadora de promedio y aprobación de asignatura ---")
    suma = 0
    cantidad = int(input('Ingrese la cantidad de notas a calcular: '))
    for i in range(cantidad):
        nota = float(input('Ingrese la nota: '))
        suma += nota
        promedio = suma / cantidad 
        print('El promedio de las notas es:', promedio)
    if promedio >= 4:
        print('El alumno aprobó')
    else:    
        print('El alumno reprobó')


def tablaMulti():
    print("--- Tabla de multiplicar ---")
    cont = 1
    num = int(input("Ingrese el número que desea multiplicar hasta 10: "))
    while cont <= 10:
        print(f"{num} x {cont} = {num * cont}")
        cont += 1


def bye():
    print("Hasta pronto")


def inv():
    print("Opción inválida")


while op != 4:
    print("")
    print("1. Creador de PIN 4 dígitos")
    print("2. Calcular promedio y aprobación de asignatura")
    print("3. Tabla de multiplicar")
    print("4. Salir")
    op = int(input("Ingrese una opción: "))

    match op:
        case 1:
            pin()
        case 2:
            notas()
        case 3:
            tablaMulti()
        case 4:
            bye()
        case _:
            inv()