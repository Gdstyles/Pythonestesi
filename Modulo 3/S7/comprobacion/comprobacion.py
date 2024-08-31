#Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for,
#e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.



elementos = [4,7,3,8,9,5,6,0,13,2]

for i in elementos:
    if i == 0:
        print(f"El número {i} es cero")
    elif i % 2 == 0:
        print(f"El número {i} es par")    
    else:
        print(f"El número {i} es impar") 
 