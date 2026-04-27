# Genera un número aleatorio entre 1 y 50
# El usuario tiene 7 intentos
# En cada intento:
# Si adivina → "¡Ganaste!" y termina el juego
# Si el número está a menos de 5 unidades:
# Mostrar "¡Muy cerca!"
# Si no:
# "Muy alto" si se pasó
# "Muy bajo" si está por debajo
# Si pierde, mostrar el número correcto

import random

azar = random.randint(1, 50)
intentos = 0
num = 0

while num == azar and intentos < 7:
    if num == azar:
        print("¡Ganaste!")
