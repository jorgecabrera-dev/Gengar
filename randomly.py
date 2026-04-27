# uso y explicación de random

import random
import time

# num = random.randint(1, 10)
# print(num)

# num = random.randint(1, 10)

# for i in range(num):
#     print("Hola Checha")

# strike = random.randint(10, 70)    

# if strike > 50:
#     print(f"It's a critical hit. Damage {strike}")
# else:
#     print(f"It's not very effective. Damage {strike}")

# 3 personas juegan golf
# cada persona tiene la posibilidad de golpear
# y la instancia varía entre 60 y 190 metros
# mostrar al final el golpe más fuerte

# g1 = "Golfista 1"
# g2 = "Golfista 2"
# g3 = "Golfista 3"

# dist1 = random.randint(60, 190)
# dist2 = random.randint(60, 190)
# dist3 = random.randint(60, 190)

# print(f"{g1} golpea la bola. La distancia de lanzamiento es: {dist1}")
# print(f"{g2} golpea la bola. La distancia de lanzamiento es: {dist2}")
# print(f"{g3} golpea la bola. La distancia de lanzamiento es: {dist3}")

# time.sleep(5)

# if dist1 > dist2 and dist1 > dist3:
#     print(f"El golpe más fuerte es de: {g1}, con {dist1} metros")
# elif dist2 > dist3:
#     print(f"El golpe más fuerte es de: {g2}, con {dist2} metros")
# else:
#     print(f"El golpe más fuerte es de: {g3}, con {dist3} metros")

# KILLER INSTINC

# dos peleadores se piden al inicio de la pelea 
# cada peleador inicia con 100 de HP
# se debe hacer una pelea por turnos 
# y cada golpe varía entre 7 y 18 
# se termina el match cuando uno de los dos 
# tiene su HP menor o igual a 0
# se debe mostrar el ganador al final
# BONUS: mostrar las barras de energía de cada peleador


hp1 = 100
hp2 = 100
turno = random.randint(1, 2)

p1 = (input("Ingrese el nombre del peleador 1: "))
p2 = (input("Ingrese el nombre del peleador 2: "))

while hp1 > 0 and hp2 > 0:
    if turno %2 == 0:
        print(f"Golpe de: {p1}")
        d1 = random.randint(7, 18)
        hp2 -= d1
        print(f"El daño fue de: {d1}")
    else:
        print(f"Golpe de: {p2}")
        d2 = random.randint(7, 18)
        hp1 -= d2
        print(f"El daño fue de: {d2}")
    print(f"HP restante de {p1}: {hp1}")
    print("█" * hp1)
    print(f"HP restante de {p2}: {hp2}")
    print("█" * hp2)
    print("")
    turno += 1
    time.sleep(3)
if hp1 > hp2:
    print(f"Ganó {p1}")
else:
    print(f"Ganó {p2}")