#Calculadora básica, operaciones sumar, restar, multiplicar y dividir | y también potencias
#Simple calculator, addition, substract, multiply and division operations | and also exponents

#definir los numeros que se van a introducir
#defying the numbers we are introducing
def insertNumbers ():
    global num1, num2
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))

#definir las operaciones
#defying the operations
def add (a, b):
    print("La suma de ", a," + " ,b, " = ", a+b)

def subs (a, b):
    print("La resta de ", a," - " ,b, " = ", a-b)

def mul (a, b):
    print("La multiplicación de ", a," * " ,b, " = ", a*b)

def div (a, b):
    if b == 0:
        print("No se puede dividir entre 0")
    else:
        print("La división de ", a," / " ,b, " = ", a/b)

def ex (a, b):
    print("El resultado de ", a," elevado a " ,b, " = ", a**b)

while True:
    print("""
    Indique la operación:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Potencias
    6. Salir

    """)

    choice = int(input())

    if choice == 1:
        insertNumbers()
        add(num1, num2)
    elif choice == 2:
        insertNumbers()
        subs(num1, num2)
    elif choice == 3:
        insertNumbers()
        mul(num1, num2)
    elif choice == 4:
        insertNumbers()
        div(num1, num2)
    elif choice == 5:
        insertNumbers()
        ex(num1, num2)
    elif choice == 6:
        print("Adiós")
        break
