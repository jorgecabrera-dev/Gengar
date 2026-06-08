# Ejercicio 1: Validar edad

# def es_mayor_de_edad(edad):
#     if edad >= 18:
#         return True
#     return False


# edad = int(input("Ingrese su edad: "))
# if es_mayor_de_edad(edad):
#     print("Puede entrar")
# else:
#     print("No puede entrar")



# Ejercicio 2: Validar una lista de notas

def validar_notas(lista):
    for nota in lista:
        nota = int(nota)
        if nota < 1 or nota > 7:
            return False
    return True      

def validar_enteros(lista):
    for nota in (lista):
        try:
            int(nota)
        except:
            return False
    return True

lista = input("Ingrese notas separadas por espacios: ")
lista = lista.split()

if validar_enteros(lista):
    if validar_notas(lista):
        print("Notas validas")
    else:
        print("Hay notas fuera del rango 1-7")
else:
    print("Las notas solo pueden ser numeros enteros")



