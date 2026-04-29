# op = 0
# cantPersonas = 0
# total = 0
# niños = 0
# adultos = 0
# adultosM = 0

# while op != 4:
#     print("1. Niño (1-17) $1.000")
#     print("2. Adulto (18-59) $3.000")
#     print("3. Adulto mayor (60 o más) $1.500")
#     print("4. Salir")
#     op = int(input("Seleccione una opción: "))
#     match op:
#         case 1:
#             print("Pagando el precio de niño")
#             niños = int(input("¿Cuántos niños son?: "))
#             while niños < 1 or niños > 10:
#                 print("El número está fuera de rango (1-10)")
#                 niños = int(input("¿Cuántos niños son?: "))
#             cantPersonas += niños
#             total += 1000 * niños
#         case 2:
#             print("Pagando el precio de adulto")
#             adultos = int(input("¿Cuántos adultos son?: "))
#             while adultos < 1 or adultos > 10:
#                 print("El número está fuera de rango (1-10)")
#                 adultos = int(input("¿Cuántos adultos son?: "))
#             cantPersonas += adultos
#             total += 3000 * adultos
#         case 3:
#             print("Pagando el precio de adulto mayor")
#             adultosM = int(input("¿Cuántos adultos mayores son?: "))
#             while adultosM < 1 or adultosM > 10:
#                  print("El número está fuera de rango (1-10)")
#                  adultosM = int(input("¿Cuántos adultos mayores son?: "))
#             cantPersonas += adultosM
#             total += 1500 * adultosM
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es: {total}")
#             print(f"La cantidad de personas son: {cantPersonas} ({niños} niños, {adultos} adultos y {adultosM} adultos mayores)")
#         case _:
#             print("Opción inválida")


# preguntar el folio de una entrada a un concierto
# validar que los folios estén entre 7.000 y 21.000
# preguntar si es en cancha vip, cancha general o tribuna
# cada entrada vale 40.000, pero los impuestos son 
# vip 1.8, general 1.4 y tribuna 1.2
# mostrar el valor a pagar al final

total = 0
ValorE = 40000
ValorEV = ValorE * 1.8
ValorEG = ValorE * 1.4
ValorET = ValorE * 1.2
cantECV = 0
cantECG = 0
cantET = 0
Tcancha = 0

Nfolio = int(input("Ingrese el número de folio: "))
while Nfolio < 7000 or Nfolio > 21000:
    print("Número de folio incorrecto")
    Nfolio = int(input("Ingrese el número de folio: "))
   
while Tcancha != 4:
    print("1. Cancha VIP")
    print("2. Cancha general")
    print("3. Tribuna")
    print("4. Salir")
    Tcancha = int(input("Seleccione una opción: "))

    match Tcancha:
        case 1: 
            print("Pagando cancha VIP")
            cantECV = int(input("Ingrese la cantidad de entradas a comprar: "))
            total += ValorEV * cantECV
        case 2: 
            print("Pagando cancha general")
            cantECG = int(input("Ingrese la cantidad de entradas a comprar: "))
            total += ValorEG * cantECG
        case 3: 
            print("Pagando cancha tribuna")
            cantET = int(input("Ingrese la cantidad de entradas a comprar: "))
            total += ValorET * cantET  
        case 4: 
            print("Saliendo")
            print(f"Total a pagar: {total}, por {cantECV} entradas VIP, {cantECG} entradas general y {cantET} entradas tribuna")     
        case _: 
            print("Opción inválida")



