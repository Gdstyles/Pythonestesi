mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15] 


lista_sin_duplicado = []
for item in mi_lista:
    if item not in lista_sin_duplicado:
        lista_sin_duplicado.append(item)
        
print(lista_sin_duplicado)


lista_ordenada = sorted(lista_sin_duplicado)


print(lista_ordenada)

