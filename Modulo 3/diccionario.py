# diccionarios en python
# estructura para almacenar datos en pares clave-valor
#no tienen un orden especifico
# coleccion de datos no ordenados
# se declara con {}

estudiantes = {
    #clave : valor
    "Fulanito": 20,
    "Maria": 22,
    "Jose": 40,
    "Marta": 50
}

#acceder a un valor de diccionario, es a traves de su clave o key

print(estudiantes["Fulanito"]) #20
print(estudiantes.get("Fulanito"))

estudiantes.pop("Fulanito") #elimina la clade "Fulanito" del diccionario
print(estudiantes)

claves = estudiantes.keys() #retorna las claves del diccionario
print(claves) # dict_keys(['Maria', 'Jose', 'Marta'])
valores = estudiantes.values() # retorna los valores del diccionario
print(valores) # dict_values([22, 40, 50])