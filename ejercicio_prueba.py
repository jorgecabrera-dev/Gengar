# Registro de juegos

# Debe preguntar al usuario Nombre del juego;
# - Al menos 5 caracteres
# -No debe incluir espacios
# Preguntar precio
# -Solo números enteros positivos
# -Si vale mas de 20000 es Indie pero menos de 40000
# -Si vale 40000 o mas, es de Estudio
# -Mostar al final cuantos hay de cada categoría
# Clasificación
# -E para todos
# - +12 para adolescentes
# - M para personas de mas de 18
# -MOSTRAR RESUMEN
# EJ: Hay 4 indies, y 5 de estudio. Solo 3 son clasificación E

clas = 0
CanIndie = 0
canEstudio = 0
CanClasE = 0
CanClas12 = 0
CanClas18 = 0

cantidad = int(input("Ingrese la cantidad de juegos: "))
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del juego {i + 1}: ")
    while len(nombre) < 5:
        print("El nombre del juego debe tener 5 o más carácteres")
        nombre = input(f"Ingrese el nombre del juego {i + 1}: ")
        while " " in nombre:
            print("El nombre no debe incluir espacios")  
            nombre = input("Ingrese el nombre del juego: ")
    precio = int(input(f"Ingrese el valor del juego {i + 1}: "))
    while precio < 1:
        print("El precio solo debe contener númneros enteros positivos")
        precio = int(input(f"Ingrese el valor del juego {i + 1}: "))
        if precio > 20000 and precio < 40000:
            indie = "Indie"
            CanIndie +=1
        elif precio > 40000:
            estudio = "Estudio"
            canEstudio += 1
    while clas != 1 or clas != 2 or clas != 3:
        print("1. E Para todos")
        print("2. T Adolescentes")
        print("3. M Adultos")
        clas = int(input("Seleccione la clasificación: "))
        if clas == 1:
            CanClasE += 1
        elif clas == 2:
            CanClas12 += 1
        elif clas == 3:
            CanClas18 += 1

if CanIndie >= 1 and canEstudio >= 1:
    print(f"Hay {CanIndie} {indie}, y {canEstudio} {estudio}")
elif CanIndie >= 1 and canEstudio == 0:
    print(f"Hay {CanIndie} {indie}")
elif canEstudio >= 1 and CanIndie == 0:
    print(f"Hay {canEstudio} {estudio}")