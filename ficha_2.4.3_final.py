pares = []
impares = []

def validar_lista_numeros(lista):
        for i in lista:
            try:
                int(i)
            except:
                return False
        return True        
        
while True:
        lista = input("Ingrese numeros separados por un espacio: ")
        lista = lista.split()
        if validar_lista_numeros(lista):
            for i in lista:
                i = int(i)
                if i % 2 == 0:
                    pares.append(i)
                else:
                    impares.append(i)
            print(f"Pares: {pares}")
            print(f"Impares: {impares}")
            break
        else:
            print("Error. Solo debe ingresar numeros enteros. Inténtelo nuevamente")
            