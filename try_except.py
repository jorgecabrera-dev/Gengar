# while True:
#     try:
#         edad = int(input("Ingrese su edad: "))
#         print(f"Su edad es {edad}")
#         break
#     except ValueError as e:
#         print("Solo se aceptan números enteros")
#         print(e)


# for i in range(10):
#     n1 = int(input("Ingrese un número: "))
#     if n1 %2 != 0:
#         break


# ingrese números indefinidadmente
# y súmelos hasta que ponga el número 0
# muestre el total

# total = 0
# num = int(input("Ingrese un número: "))

# while num != 0:
#     num = int(input("Ingrese un número: "))
#     total += num
# print(f"La suma de todos los números es {total}")


# num = 0
# while True:
#     try:
#         n1 = int(input("Ingrese un número: "))
#         num += n1
#         if n1 == 0:
#             break
#     except:
#         print("Solo números enteros")

# print(f"El total es {num}")


# op = 0
# total = 0

# while op != 4:
#     try:
#         print("")
#         print("1. Radio stereo Sony $70.000")
#         print('2. LG TV 55" Super Gamer $500.000')
#         print("3. PS5 $580.000")
#         print("4. Salir")
#         print("")
#         op = int(input("Seleccione una opción: "))
#         match op:
#             case 1:
#                 print(f"El precio a pagar es: {700000 * 1.19}")
#                 total += 700000 * 1.19
#             case 2:
#                 print(f"El precio a pagar es: {500000 * 1.19}")
#                 total += 500000 * 1.19
#             case 3:
#                 print(f"El precio a pagar es: {580000 * 1.19}")
#                 total += 580000 * 1.19
#             case 4:
#                 print("Gracias por su compra")
#             case _:
#                 print("Opción inválida") # Opción por defecto
#     except ValueError as e:
#         print("Ingrese un número dentro del rango")
#         print(e)

# print(f"Total a pagar: {total}")


porc = int(input("Ingrese el porcentaje de rucos en su comuna: "))
