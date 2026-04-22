# ejemplo y explicación de definir

# name = "Carlos"

# def saludo():
#     print(f"¡Hola, {name}!")

# saludo()

# def chao():
#     print(f"¿Ya nos vamos, {name}?")

# chao()

def suma():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print(f"El resultado de la suma es: {num1 + num2}")
suma()

def resta():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print(f"El resultado de la resta es: {num1 - num2}")
resta()

def multi():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print(f"El resultado de la multiplicación es: {num1 * num2}")
multi()

def div():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print(f"El resultado de la división es: {num1 / num2}")
div()

def bye():
    print("Hasta pronto")
bye()

def inv():
    print("Opción inválida")
inv()

op = 0

while op != 5:
    
    print("")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("")

    op = int(input("Ingrese una operación: "))

    match op:
        case 1:
            suma
        case 2:
            resta
        case 3:
            multi
        case 4:
            div
        case 5:
            bye
        case _:
            inv