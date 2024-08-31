
suma = 0

while True:
    numero = int(input("Ingrese un número positivo: "))
    if numero < 0:
        print("Número no válido, por favor ingrese un número mayor a cero")
    suma += numero
    print(f"La suma total es de {suma}")