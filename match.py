# ejemplo y explicación de match

op = 0
total = 0

while op != 4:
    print("")
    print("1. Radio stereo Sony $70.000")
    print('2. LG TV 55" Super Gamer $500.000')
    print("3. PS5 $580.000")
    print("4. Salir")
    print("")
    op = int(input("Seleccione una opción: "))

    match op:
        case 1:
                print(f"El precio a pagar es: {700000 * 1.19}")
                total += 700000 * 1.19
        case 2:
                print(f"El precio a pagar es: {500000 * 1.19}")
                total += 500000 * 1.19
        case 3:
                print(f"El precio a pagar es: {580000 * 1.19}")
                total += 580000 * 1.19
        case 4:
                print("Gracias por su compra")
        case _:
                print("Opción inválida") # Opción por defecto

print(f"Total a pagar: {total}")
