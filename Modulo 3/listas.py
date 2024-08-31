# listas en python
# estructura para almacenar datos ordenados por orden de ingreso



    #   [0,1,2,3,4] indices positivos
    #   [-5,-4,-3,-2,-1] indice negativo
lista = [1,2,3,4,5] #lista con 5 elementos
lista_diferentes_valores = [1, "hola", 3.14, True] #lista con diferentes tipos de datos

#para acceder a una lista se realiza a traves de los indices
# indices van desde 0 a n-1, siendo n la cantidad de elementos de la lista
# nombre_lista[indice]
print(lista[0]) #1
print(lista[-1]) #5
print(lista[1:3]) # [2,3] entrega los valores en una lista

# las listas tienen metodos que permiten modificarlas o realizar alguna accion
lista.append(6) # agrega un elemento al final de la lista
print(lista) # [1, 2, 3, 4, 5, 6]


lista.remove(6) #elimina el elemento 6 de la lista
print(lista) #[1, 2, 3, 4, 5]

a = lista.pop(1) #elimina el elemento de la posicion 1
print(a) #2
print(lista) # [1, 3, 4, 5]

# insert(posicion,valor)
lista.insert(1,2) # inserta el valor 2 en la posicion 1
print(lista) #[1, 2, 3, 4, 5]

#indice # index(elemento)
elemento_indice_tres = lista.index(3) # retorna la posicion del elemento 3 en la lista
print(elemento_indice_tres) #2

# sort() ordena la lista

lista_diferentes_valores.sort() # TypeError: '<' not supported between instances of 'str' and 'int'
print(lista_diferentes_valores)