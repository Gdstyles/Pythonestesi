# escribe un programa que genere un numero aleatorio entre 1 y 100, y pida al usuario que lo adivine. 
# El programa debe dar pistas al usuario indicando si el número ingresado es demasiado alto demasiado bajo. 
# El juego termina cuando el usuario adivina el numero correctamente.
# Utilizar libreria random


import random

numero_aleatorio = random.randint(1, 100)


while True:
    ingresar_numero = int(input("Por favor ingrese un número del 1 al 100: "))
    if ingresar_numero > numero_aleatorio:
        print("El número que ingresaste es mayor")
    elif ingresar_numero < numero_aleatorio:
        print("El numero que ingresaste es menor")
    elif ingresar_numero == numero_aleatorio: 
        print("Enhorabuena chaval, has acertado")
        break
    
