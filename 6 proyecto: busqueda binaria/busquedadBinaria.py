# Si puedes imaginarlo, puedes programarlo. 

import random
import time

def busquedadIngenua (lista, objetivo):

    for i in range(len(lista)):
        
        if lista[i] == objetivo:
            return i
    
    return -1

# la lista tiene que estar ordenada
def busquedadBinaria(lista, objetivo, limite_inferior = None, limite_superior = None): 
    
    if limite_inferior is None:
        limite_inferior = 0
    
    if limite_superior is None:
        limite_superior = len(lista) - 1

    if limite_superior < limite_inferior:
        return - 1
    
    punto_medio = ((limite_inferior + limite_superior) // 2)
    
    if lista[punto_medio] == objetivo:
        return punto_medio
    
    elif objetivo < lista[punto_medio]:
        
        return busquedadBinaria(lista, objetivo, limite_inferior, punto_medio-1)

    else:
        return busquedadBinaria(lista, objetivo, punto_medio + 1, limite_superior )

if __name__=='__main__':

    # creamos una lista ordenada con 10.000 numeros aleatorios
    tamaño = 100000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:

        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
    
    lista_ordenada = sorted(list(conjunto_inicial))

    # medir el tiempo con las dos funciones:

    # medir tiempo busquedad ingenua 
    # inicio_1 = time.time()

    # for objetivo in lista_ordenada:
        
    #     busquedadIngenua(lista_ordenada, objetivo)
    
    # fin_1 = time.time()
    
    # print(f"Tiempo de busquedad ingenua: {fin_1 - inicio_1} segundos")

    # Medir el tiempo de busquedad binaria
    inicio_2 = time.time()

    for objetivo in lista_ordenada:
        busquedadBinaria(lista_ordenada, objetivo)

    fin_2 = time.time()

    print(f"Tiempo de busquedad binaria: {fin_2 - inicio_2} segundos")

