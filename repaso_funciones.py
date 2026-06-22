def sumar(num1, num2):
    return num1 + num2

# def restar():
# def multiplicar():
# def dividir():

def pedir_numeros():
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese un numero: "))




print("1.- Sumar")
print("2.- Restar")
print("3.- Multiplicar")
print("4.- Dividir")
print("5.- Salir")
op = int(input("Seleccione una opcion: "))
match op:
    case 1:
        pedir_numeros()
        sumar()
        resultado = sumar(numero1, numero2)
        print(resultado)
    # case 2:
    # case 3:
    # case 4:
    # case 5:
    # case _:


