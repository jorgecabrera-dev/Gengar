import random

num = random.randint(1, 100)
pos = 1
guess = int(input("Adivina el número: "))
while pos < 5 and guess != num:
    print(num)
    print(f"Intento {pos}")
    if guess > num:
        print("Te pasaste")
    else:
        print("El número a adivinar es mayor")
        guess = int(input("Adivina el número: "))
    pos += 1
if guess == num:
    print("Has adivinado")
else:
    print("Se te acabaron los intentos")     