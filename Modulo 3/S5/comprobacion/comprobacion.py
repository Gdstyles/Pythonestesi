import math 


while True:
    numero = int(input("Ingrese numero: "))
    if numero > 0:
        break

var_factorial = math.factorial(numero)


print(f"El factorial del número {numero} es {var_factorial}")
