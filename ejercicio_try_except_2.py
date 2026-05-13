# Simula un cajero automático con un saldo inicial de $100.000.
# Solo se puede sacar/ingresar montos de multiplos de $5000

# El usuario puede:

# 1.- Consultar saldo
# 2.- Retirar dinero
# 3.- Depositar dinero
# 4.- Salir

# Debes usar try-except para manejar:
# montos inválidos
# retiro mayor al saldo disponible
# opciones incorrectas
# entradas no numéricas


saldo = 100000
retiro = 0
deposito = 0
opc = 0

while opc != 4:
    try: 
        print("1.- Consultar saldo")
        print("2.- Retirar dinero")
        print("3.- Depositar dinero")
        print("4.- Salir")
        opc = int(input("Seleccione una opción: "))
    except ValueError as e:
        print(e)
        print("La entrada no es númerica")
        continue
    match opc:
        case 1:
            print(f"El saldo es {saldo}")
        case 2:
            try:
                retiro = int(input("Ingrese un monto a retirar: "))
                if retiro > 0 and retiro <= saldo and retiro % 5000 == 0:
                    saldo -= retiro
                    print("Retiro realizado correctamente")
                else:
                    print("El monto a retirar no puede ser superior al saldo disponible, ni en otros múltiplos fuera de $5.000")
            except ValueError as e:
                print(e)
                print("La entrada no es númerica")           
        case 3:
            try:
                deposito = int(input("Ingrese un monto a depositar: "))
                if deposito > 0 and deposito %5000 == 0:
                    saldo += deposito
                    print("Depósito realizado correctamente")
                else:
                    print("El monto a depositar debe estar en múltiplos de $5.000")
            except ValueError as e:
                print(e)
                print("La entrada no es númerica")
        case 4: 
            print("Gracias por su preferencia")
        case _:
            print("Opción inválida")
