
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
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese otro número: "))
            print(f"El resultado de la suma es: {num1 + num2}")
        case 2:
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese otro número: "))
            print(f"El resultado de la resta es: {num1 - num2}")
        case 3:
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese otro número: "))
            print(f"El resultado de la multiplicación es: {num1 * num2}")
        case 4:
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese otro número: "))
            print(f"El resultado de la división es: {num1 / num2}")
        case 5:
            print("Hasta pronto")
        case _:
            print("Opción inválida")
