#programa para lanzar una moneda cara o cruz 
#importa la libreria random
import random

#aqui escoge un num aleatorio del 1 al 10 
num = random.randint(0,10)
#si el num es 5 o menor imprime cara
if num  > 5:
    print("cara")
else: #sino imprime cruz
    print("cruz")
