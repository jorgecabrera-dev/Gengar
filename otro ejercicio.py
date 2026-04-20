# Calcular el puntaje de credito

# Debe calcular que tanto credito tiene una persona
# en cierta entidad financiera, debera considerar

# cantidad de ingresos, nivel educacional y nacionalidad
# Cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.001 o mas: 1.000.000
# Nivel Educacional
# Basico : x1, medio: x1.3 , superior: x1.5
# Nacionalidad 
# Chilena: +300.000, Extranjero: +0

credito = 0
sueldo = int(input("Ingrese su sueldo: "))

if sueldo >= 500000 and sueldo <= 1000000:
    credito = 300000
elif sueldo >= 1000001 and sueldo <= 1500000:
    credito = 650000
elif sueldo >= 1500001:
    credito = 1000000
else:
    print("Sueldo insuficiente para crédito")

print("1. Basico")
print("2. Medio")
print("3. Superior")
educacion = int(input("Ingrese su nivel educacional: "))    

if educacion == 1:
    credito *= 1
elif educacion == 2:
    credito *= 1.3
elif educacion == 3:
    credito *= 1.5        

nacionalidad = input("Ingrese su nacionalidad (chileno/extranjero:)")

if nacionalidad.lower() in ["chileno", "chilena"]:
    credito += 300000

print(f"Su crédito es de: {credito}")