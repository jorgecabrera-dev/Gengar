# crear un gestor de estacionamiento
# un estacionamiento tiene 4 pisos 
# cada piso tiene 10 espacios
# preguntar cuando entra un vehiculo, cual tipo de vehiculo es 
# vehiculo ligero 2000
# vehiculo mediano 3000
# vehiculo pesado 3500
# luego acomodarlo en algun lugar del piso disponible
# el menu debe tener las siguientes alternativas
# 1 ingresar vehiculo
# 2 contar ganancias
# 3 contar vehiculos
# 4 ganancia promedio


estacionamiento = {
    1:[],
    2:[],
    3:[],
    4:[]
}

def espacios():
    print("-" * 30)

def menu1():
    espacios()
    print("1. Ingresar vehiculo")
    print("2. Contar ganancias")
    print("3. Contar vehiculos")
    print("4. Ganancia promedio")
    print("5. Estado de pisos")
    print("6. Salir")
    espacios()

def menu2():
    espacios()
    print("1. Vehiculo ligero")
    print("2. Vehiculo mediano")
    print("3. Vehiculo pesado")
    print("4. Salir")
    espacios()

precio_ligeros = 2000
precio_medianos = 3000
precio_pesados = 3500


while True:
    try:
        menu1()
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                while True:
                    menu2()
                    op = int(input("Seleccione una opción: "))
                    match op:
                        case 1:
                            if len(estacionamiento[1]) < 10:
                                estacionamiento[1].append(2000)
                                print("Ingreso exitoso en el piso 1")
                            elif len(estacionamiento[2]) < 10:
                                estacionamiento[2].append(2000)
                                print("Ingreso exitoso en el piso 2")
                            elif len(estacionamiento[3]) < 10:
                                estacionamiento[3].append(2000)
                                print("Ingreso exitoso en el piso 3")
                            elif len(estacionamiento[4]) < 10:
                                estacionamiento[4].append(2000)
                                print("Ingreso exitoso en el piso 4")
                            else:
                                print("No hay espacio suficiente para ingresar más vehículos")
                        case 2:
                            if len(estacionamiento[1]) < 10:
                                estacionamiento[1].append(3000)
                                print("Ingreso exitoso en el piso 1")
                            elif len(estacionamiento[2]) < 10:
                                estacionamiento[2].append(3000)
                                print("Ingreso exitoso en el piso 2")
                            elif len(estacionamiento[3]) < 10:
                                estacionamiento[3].append(3000)
                                print("Ingreso exitoso en el piso 3")
                            elif len(estacionamiento[4]) < 10:
                                estacionamiento[4].append(3000)
                                print("Ingreso exitoso en el piso 4")
                            else:
                                print("No hay espacio suficiente para ingresar más vehículos")
                        case 3:
                            if len(estacionamiento[1]) < 10:
                                estacionamiento[1].append(3500)
                                print("Ingreso exitoso en el piso 1")
                            elif len(estacionamiento[2]) < 10:
                                estacionamiento[2].append(3500)
                                print("Ingreso exitoso en el piso 2")
                            elif len(estacionamiento[3]) < 10:
                                estacionamiento[3].append(3500)
                                print("Ingreso exitoso en el piso 3")
                            elif len(estacionamiento[4]) < 10:
                                estacionamiento[4].append(3500)
                                print("Ingreso exitoso en el piso 4")
                            else:
                                print("No hay espacio suficiente para ingresar más vehículos")                         
                        case 4:
                            print("Volviendo al menú principal")
                            break
                        case _:
                            print("Opción inválida")
            case 2:
                total_ganancias = 0
                for dinero in estacionamiento.values():
                    total_ganancias += sum(dinero)
                print(f"Ganancias actuales: {total_ganancias}")
            case 3:
                total_vehiculos= 0
                for auto in estacionamiento.values():
                    total_vehiculos += (len(auto))
                print(f"Total: {total_vehiculos}")
            case 4:
                total_ganancias = 0
                total_vehiculos= 0     
                for piso in estacionamiento.values():
                    total_ganancias += sum(piso)
                    total_vehiculos += len(piso)
                if total_vehiculos > 0:
                    promedio = total_ganancias / total_vehiculos
                    print(f"La ganancia promedio por vehículo es de: ${promedio}")
                else:
                    print("No hay vehículos registrados")
            case 5:
                for piso, espacio in estacionamiento.items():
                    print(f"Piso {piso}, espacios usados: {len(espacio)}")
            case 6:
                print("Gracias por usar nuestro software")
                break
            case _:
                print("Opción inválida")
    except ValueError:
        print("Error. Solo puede ingresar números enteros")