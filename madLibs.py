# Si puedes imaginarlo, puedes programarlo
'''
    Supongamos que queremos crear una cadena que diga:
    Aprender a progrmar con ___________. 
'''

# organizacion = "FreeCodeCam"

# print("Aprender a progrmar con "+organizacion)
# print("Aprender a progrmar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}")

adj = input("Adjetivo: ")
verbo1 = input("Verbo 1: ")
verbo2 = input("Verbo 2: ")
sustantivo_plural = input("Sustantivo: ")

madlib = f"Progrmar es tan {adj} simpre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con FreeCodeCam y alacanza tus {sustantivo_plural}"

print(madlib)
