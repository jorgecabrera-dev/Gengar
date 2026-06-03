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

def validar_lista_numeros(lista):
    verificacion = True
    for i in lista:
        try:
            num = int(i)
        except:
            verificacion = False
    return verificacion

listaINT = []
listaPar = []
listaImpar = []

while True:
    numeros = input("Ingrese una lista de números separados por un espacio: ")
    listastr = numeros.split()

    validar_lista_numeros(listastr)

    if validar_lista_numeros(listastr) == True:
        for i in listastr:
            listaINT.append(int(i))

        for i in listaINT:
            if i%2 == 0:
                listaPar.append(i)
            else:
                listaImpar.append(i)
        print(listaImpar)    
        print(listaPar)
        break
    else:
        print("Debe ingresar solo numeros enteros y espacios, vuelva a ejecutar el programa.")
            
   


            


