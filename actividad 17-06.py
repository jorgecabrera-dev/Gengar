## Crear un gestor de pacientes

# crear al gestor de pacientes en un centro medico
# Para poner el nombre se debe validar que no este vacio 
# y ademas tenga mas de 8 caracteres
# Para la prevision de salud solo exiten 3 posibles valores
# Fonasa, Isapre, o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si esta grave o no
# Para que este grave debe tener mas de 39°
# Cada atencion vale $25.000
# Los despcuentos corresponden a 
# FOnasa 54%
# Isapre 27%
# Fodesa 12,5%


pacientes = [

    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
      "temperatura":34.6, "grave": False},

]

valor_atencion = 25000

# while True:
#     try:
#         c_pacientes = int(input("¿Cuántos pacientes va a registrar?: "))
#         for n in range(c_pacientes):
#             n_paciente = "hola"
#             while len(n_paciente) < 8: 
#                 n_paciente = input(f"Ingrese el nombre del paciente {n + 1}: ")
#                 if len(n_paciente) < 8:
#                     print("Debe tener más de 8 carácteres")
#                 else:
#                     while True:
#                         try:
#                             print("1. Fonasa")
#                             print("2. Isapre")
#                             print("3. Fodesa")
#                             prevision = int(input("Seleccione su previsión (1/2/3): "))
#                             if prevision == 1:
#                                 tipo_prevision = "Fonasa"
#                                 descuento = 0.54
#                                 break
#                             elif prevision == 2:
#                                 tipo_prevision = "Isapre"
#                                 descuento = 0.27
#                                 break
#                             elif prevision == 3:
#                                 tipo_prevision = "Fodesa"
#                                 descuento = 0.125
#                                 break
#                             else:
#                                 print("Seleccione una opción válida")
#                         except ValueError:
#                             print("Solo puede ingresar números enteros")

#                     while True:
#                         try:
#                             temp = float(input("Ingrese la temperatura: "))  
#                             if temp > 39:
#                                 estado = True
#                                 break
#                             else:
#                                 estado = False  
#                                 break
#                         except ValueError:
#                                 print("Solo puede ingresar números enteros")
#                     nuevo_paciente = {"nombre": n_paciente, "prevision": tipo_prevision, "temperatura": temp, "grave": estado}
#                     pacientes.append(nuevo_paciente)
#                     print(f"La atención del paciente {n_paciente} es de: {valor_atencion - valor_atencion * descuento}")
#                     print(pacientes)
#     except ValueError:
#             print("Solo puede ingresar números enteros")
      
def mostrar_pacientes():
    for p in pacientes.items():
        print(f"{[pacientes]}")

def validacion_nombre():
    n_paciente = "hola"
    while len(n_paciente) < 8: 
        n_paciente = input(f"Ingrese el nombre del paciente: ")
        if len(n_paciente) < 8:
            print("Debe tener más de 8 carácteres")

def tipo_prevision():
    while True:
        try:
            print("1. Fonasa")
            print("2. Isapre")
            print("3. Fodesa")
            prevision = int(input("Seleccione su previsión (1/2/3): "))
            if prevision == 1:
                tipo_prevision = "Fonasa"
                descuento = 0.54
                break
            elif prevision == 2:
                tipo_prevision = "Isapre"
                descuento = 0.27
                break
            elif prevision == 3:
                tipo_prevision = "Fodesa"
                descuento = 0.125
                break
            else:
                print("Seleccione una opción válida")
        except ValueError:
            print("Solo puede ingresar números enteros")

def registro_temperatura():
    while True:
        try:
            temp = float(input("Ingrese la temperatura: "))  
            if temp > 39:
                estado = True
                break
            else:
                estado = False  
                break
        except ValueError:
                print("Solo puede ingresar números enteros")

def resumen_paciente():
    nuevo_paciente = {"nombre": n_paciente, "prevision": tipo_prevision, "temperatura": temp, "grave": estado}
    pacientes.append(nuevo_paciente)
    print(f"La atención del paciente {n_paciente} es de: {valor_atencion - valor_atencion * descuento}")
    print(pacientes)

def costo_atencion():
    

print("1. Ingreso paciente")           
print("2. Ingreso paciente")           
print("3. Ingreso paciente")           
print("4. Ingreso paciente")           
print("5. Ingreso paciente")           
print("6. Ingreso paciente")
sel = int(input("Seleccione una opción: "))   
match sel:
    case 1:
        validacion_nombre()
        tipo_prevision()
        registro_temperatura()
        resumen_paciente
    case 2:
        
    case 3:
    case 4:
    case 5:
