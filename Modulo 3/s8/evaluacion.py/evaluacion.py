# Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:  


# [[1,2,3], [0,4,5], [4,0,1], [6,5,4]] 


# Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
# • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
# • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
# • Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.   
# • Finalmente, imprimiremos en pantalla el diccionario resultante. 

lista_de_listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

diccionario = dict()

otro_diccionario = dict()

clave = ["A", "B", "C", "D"]

for i in range(len(lista_de_listas)):
    diccionario[clave[i]] = lista_de_listas[i]
    if lista_de_listas[i][0] == 0: # Si el primer número de la sublista es cero, omitir la impresión de toda la sublista
        continue
    for elemento in lista_de_listas[i]:
        if elemento == 0:
            continue
        print("El valor es: ", elemento)

print(diccionario)