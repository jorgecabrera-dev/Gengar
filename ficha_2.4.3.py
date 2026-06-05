# Objetivo del programa: Un programa funcional que, dada una lista de números
# ingresada por el usuario, identifica y muestra los números pares e impares de
# manera clara y organizada.
# Reglas de negocio:
# 1. Solicitar al usuario que ingrese una lista de números enteros
# separados por espacios.
# 2. Implementar una función llamada validar_lista_numeros que verifique
# que todos los elementos ingresados sean números enteros. Si se
# ingresa algún valor no válido, solicitar nuevamente la lista.
# 3. la función validar_lista_numeros debe utilizar un bucle y maneja
# excepciones para asegurar que todos los elementos ingresados sean
# números enteros.
# 2
# 4. Utilizar el operador de módulo % (MOD) para determinar si un
# número es par o impar en la lista de números a ingresar. Considerar
# que un número es par cuando el mod es igual a 0, en caso contrario,
# es impar
# 5. Crear dos listas separadas: una para los números pares y otra para
# los impares.
# 6. Mostrar al usuario las listas resultantes, indicando los números
# pares, e indicando los números impares


lista1 = []
lista2 = []
pares = []
impares = []


def validar_lista_numeros():
    verificacion = True
    for i in lista1:
        try:
            if i == int(i):
                lista2.append(i)
        except:    
            verificacion = False
            print("Error. Intente ingresando solo números enteros")        

numeros = input("Ingrese números separados por un espacio: ")
separacion = numeros.split()
lista1.append(separacion)
validar_lista_numeros()
for i in lista2:
    if i %2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Pares {pares}")
print(f"Impares {impares}")
