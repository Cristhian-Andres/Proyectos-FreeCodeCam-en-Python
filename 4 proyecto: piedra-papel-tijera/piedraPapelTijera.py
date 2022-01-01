# Si puedes imaginarlo, puedes programarlo 

'''
    Proyecto piedra, papel o tijera: tendremos un uruario que va a jugar contra la computadora en este clasico juego.  
'''
import random


def jugar():

    print('===JUGAR===')
    print("a. Piedra")
    print("b. Papel")
    print("c. Tijera")
    
    lista = ['a','b','c']

    usuario = input("Escoge una opcion: ").lower()

    computadora = random.choice(lista)

    if usuario == computadora:
        
        exit_1 = print(f"usuarion: {usuario} || {computadora} :Computadora. ¡EMPATE!")
        
        return exit_1
    
    if ganoJugador(usuario,computadora):
        
        exit_2 = print(f"Usuario: {usuario} || {computadora} :Computadora. ¡GANASTE!")

        return exit_2

    exit_3 = print(f"Usuario: {usuario} || {computadora} :Computadora. ¡PERDISTE!")    

    return exit_3

def ganoJugador(jugador, oponente):
     
    # retormar True si gano el jugador
    # piedra (a) gana tijera (c)
    # tijera (c) gana papel (b)
    # papel (b ) gana piedra (a)

    if((jugador == 'a' and oponente == 'c') or (jugador == 'c' and oponente == 'b') or (jugador == 'b' and oponente == 'a')):
        return True
    else: 
        return False

print(jugar())