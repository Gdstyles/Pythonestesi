while True:
    n = int(input("Ingrese el número del que desea saber el factorial"))
    if n > 0:
        break
    
# n puede tener cualquier valor positivo y mayor de 0
i = 1 #iterador
acumulador = 1 # acumula el valor del factorial, la multiplicacion del acumulador *i
while True:
    acumulador *= i # acumulador = acumulador * i, 1 = 1 * 1, 1 = 1 * 2
    i += 1 # iterador cambia valor
    if i > n:
        break

print(f"El factorial de {n} es {acumulador}")



#convertir estructura a civlo for
