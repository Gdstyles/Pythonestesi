

numero = int(input("Introduce un número: "))

if numero == 0:
    print("el número es cero")
elif numero > 0:
    if numero % 2 == 0: 
        print("el número es par y positivo")
    else:
        print("el número es impar y positivo")
elif numero < 0:
    if numero % 2 == 0:
        print("el número es par negativo")
    else:
        print("el número es impar y negativo")
