# tuplas

#estructura de datos inmutable
# se declaran con ()

tupla_datos = () # tupla vacia
print(type(tupla_datos)) # <class 'tuple'>

tupla_datos = (1,2,3,4,5) # reasignacion de valores
print(tupla_datos) #(1, 2, 3, 4, 5)


cuenta = tupla_datos.count(1) #cuantas veces existe ese valor
print(cuenta) #1

indice_del_valor = tupla_datos.index(5)
print(indice_del_valor) #4

contenido_indice_cero = tupla_datos[0] # acceder a un elemento mediante su indice
print(contenido_indice_cero) # 1
