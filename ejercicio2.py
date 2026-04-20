# # Texto inicial
# texto = " Hola, Mundo! Bienvenido a Python. Python es increíble. "
# # Aplicando métodos
# texto_procesado = texto.strip() # Elimina espacios iniciales y finales
# texto_min = texto_procesado.lower() # Convierte todo el texto a minúsculas
# texto_may = texto_procesado.upper() # Convierte todo el texto a mayúsculas
# texto_reemplazado = texto_min.replace("python", "programación") # Reemplaza "python" por "programación"
# posicion_mundo = texto_reemplazado.find("mundo") # Encuentra la posición de la palabra "mundo"
# palabras_lista = texto_reemplazado.split() # Divide el texto en una lista de palabras
# # Resultados
# print("Texto original:")
# print(texto)

# print("\nTexto sin espacios iniciales y finales:")
# print(texto_procesado)
# print("\nTexto en minúsculas:")
# print(texto_min)
# print("\nTexto en mayúsculas:")
# print(texto_may)
# print("\nTexto con 'Python' reemplazado por 'programación':")
# print(texto_reemplazado)
# print("\nPosición de la palabra 'mundo':")
# print(posicion_mundo)
# print("\nLista de palabras:")
# print(palabras_lista)

# Pedir la clave al usuario y verificar
# que sea SHAZAM independiente de su case
# (indiferente de mayúsculas o minúsculas)

# passw = "SHAZAM"
# code = input("Ingrese la contraseña: ")

# if passw == code.upper():
#     print("Bienvenido al sistema")
# else:
#     print("Error, clave")

# crear un nombre de usuario y verificar que 
# su largo esté entre 4 y 10 carácteres

# user = input("Ingrese su nombre de usuario: ")

# if len(user) < 4:
#     print("Tiene muy pocos carácteres. Use al menos 4") 
# elif len(user) > 10:
#     print("Tiene muchos carácteres. Use 10 o menos")
# else:
#     print("Usuario creado correctamente")

# crear un pin y que éste tenga exactamente
# 4 dígitos

pin = int(input("Ingrese un pin de 4 dígitos: "))

if len(str(pin)) == 4:
    print("Pin creado exitosamente")
else:
    print("Cantidad de dígitos incorrecta")