"""
Bomba de tiempo
Enunciado: Escribe un programa que permita la simulacion de una bomba de tiempo, Al ejecutar el programa, se imprimirá el mensaje "Bomba de tiempo a explorta

"""
import time

i = 5

while i >= 0:
    print(i)
    i -= 1
    time.sleep(1)
print("Boom")
