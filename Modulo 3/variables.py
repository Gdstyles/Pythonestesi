# las variables se declaran como un nombre, que es su identificador
# van escritas en snake_case
# identificador = valor
nombre_variable = "una variable"
nombre_variable = 2

print(nombre_variable) #2

#variables locales y variables globales
s = "una variable global"

#las variables locales existen dentro de los bloques de codigo
# funciones, condicionales (if, else if), bucles (ciclos)

def f(s):
    s = "una variable local"
    print(s)

f(s) #invocando funcion f
print(s) #variable locaL


