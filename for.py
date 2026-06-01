# uso y repaso de for

# for indice in range(1, 11):
#     print(f"7 x {indice} = {7 * indice}")

total_notas = 0

c_notas = int(input("Ingrese la cantidad de notas que va a promediar: "))
for i in range(c_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    total_notas += nota
    promedio = total_notas / c_notas

print(f"El promedio de las notas es {promedio}")

