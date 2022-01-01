#Si pudes imaginarlo, puedes programarlo. 

'''
    Proyecto adivina el número: EL usuario va adivinar un número generado por el código.
'''

import random 

def adivina_numero(x):

    # número aleatorio entre 1 y x
    numero_aleatorio = random.randint(1,x)

    prediccion = 0
    intentos = 0

    while prediccion != numero_aleatorio:
        
        # El usuario ingresa un número
        prediccion = int(input(f" Adivina un numero entre 1 y {x}: ")) # f- Stirng

        intentos = intentos + 1;

        if prediccion < numero_aleatorio:
            print(f"¡Intenta otra vez! {prediccion} es pequeño, #intentos: {intentos}")
            
        
        elif prediccion > numero_aleatorio:
            print(f"¡Intenta otra vez! {prediccion} es grande, #intentos: {intentos}")
    
    print(f"¡Felicitaciones! adivinaste el numero {numero_aleatorio} correctamente en {intentos} intentos (^.^) ")

    return

print("======================")
print("¡Bienvenid@ al juego! ")
print("======================")
print("Tú meta es adivinar el número generado en el intervao 1 y x")

x = int(input("Ingresa un numero x: "))

adivina_numero(x)

