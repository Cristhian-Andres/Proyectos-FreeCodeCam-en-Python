# Si puedes imaginarlo, puedes programarlo

'''
    Proyecto adivina el número la computadora: el usuario va a generar un numero y la computadora lo va adivinar
'''

import random


def adivina_numero_pc(x):

    limite_inferior = 1
    limite_superior = x

    intentos = 1

    respuesta = ""

    while respuesta != "c":
        
        #generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        # obtener respuesta del usuario

        respuesta = input(f"Mi prediccion es: {prediccion}  #intentos: {intentos} | Si es alta, ingresa (a). si es pequeña, ingresa (b). si es correcta, ingresa (c)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        
        elif respuesta == "b":
            limite_inferior = prediccion + 1
        
        intentos = intentos + 1;
        
    
    print(f"Si, la computadora adivino el número correctamente: {prediccion} en  #intentos: {intentos}")

    return

print("======================")
print("¡Bienvenid@ al juego! ")
print("======================")

x = int(input("Selecciona un número entre 1 y n para que la computadora intente adivinarlo..."))


adivina_numero_pc(x)

