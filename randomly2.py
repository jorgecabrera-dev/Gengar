# adivina el número

# crea un número random entre 1 y 100
# pide al usuario que adivine el número
# si el usuario pone un número mayor al generado
# debe decir "te pasaste", en caso contrario "El número a adivinar es mayor"
# solo hay 5 intentos para adivinar

import random

azar = random.randint(1, 100)
intento = 0
num = 0

while intento <5 and num != azar:
    print("")
    num = int(input("Ingrese un número: "))
    if num > azar:
        print("Te pasaste")
    else:
        print("El número a adivinar es mayor")
    intento += 1
    print(f"Intento restantes: {5 - intento}")
if num == azar:
    print("¡Adivinaste el número!")    
else:
    print("Se te acabaron los intentos")