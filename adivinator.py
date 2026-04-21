#El objetivo es que la máquina piense un número y el usuario tenga que acertarlo

import random

#Variables
#el numero será uno entre el 1 y el 10
global mNum, uNum
mNum = random.randint(0,10)
win = False

uNum = int(input("Introduzca el número: "))

#el usuario tendrá que insertar un número hasta que esté sea correcto
while win == False:
    if mNum == uNum:
        print("Correcto!  Felicidades")
        win = True

    else: 
        print("Ese no es el número correcto, vuelve a intentarlo")
        uNum = int(input("Introduzca el número: "))



