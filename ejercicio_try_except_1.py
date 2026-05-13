# Fabrica de enlatados
# Se necesita hacer el algoritomo de productos enlatados
# Se debe consultar el peso del producto( en gramos) ( solo valores positivos)
# El porcentaje de sodio en él ( solo valores entre 1 y 100)
# y si se va a vender nacional o internacionalmente
# Considerar los criterios en la siguiente tabla

# menos de 500 grs, lata normal
# 501 hassta 1500 bgr, lata mediana
# 1501 y mas , lata grande
# si el sodio es menos de 5%, lata queda igual
# si es entre 5% y 8% lata especial
# si tiene 9% o mas, lata acorazada
# a las latas internacionales, se le debbe pegar 
# in sticker de validacion sanitaria

# Ej:800, 7%, 2==> lata mediana espacial con sticker sanitario

venta = 0

while True:
        try:
            peso = int(input("Ingrese el peso del producto en gramos: "))
            break
        except ValueError as e:
            print(e)
            print("Solo debe ingresar números positivos")
    
while True:
    try:
        sodio = int(input("Ingrese el porcentaje de sodio con él: "))
        break
    except ValueError as e:
        print(e)
        print("Solo debe ingresar valores entre 1 y 100")

while venta != 1 or venta != 2:
    try:
        print("¿Se venderá nacional o internacionalmente?")
        print("1. Nacional")
        print("2. Internacional")
        venta = int(input("Seleccione una opción: "))
        break
    except ValueError as e:
        print(e)
        print("Seleccione una opción válida")

if peso < 500:
    tl1 = "normal"
elif peso < 1500:
    tl1 = "mediana"
if sodio < 5:
    print()
elif sodio <= 8:
    tl2 = "especial"
elif sodio > 8:
    tl2 = "acorazada"
if venta == "internacional":
    sticker = "con sticker sanitario"
elif venta == "nacional":
    sticker = "sin sticker"

print(f"{peso}gr, {sodio}%, lata {tl1} {tl2} {sticker}")
