# explicación y ejemplos de while

# tabla de multiplicar con while

cont = 1
num = 8

while cont <= 10:
    print(f"{num} x {cont} = {num * cont}")
    cont += 1

# código secreto

code = 3434
pwd = int(input("Ingrese el pin: "))

while code != pwd:
    print("Pin incorrecto, intente nuevamente")
print("Acceso exitoso")    