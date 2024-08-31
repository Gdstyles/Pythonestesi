# Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos números, y otra que divida dos números.
# Adicionalmente, crear una función que acepte dos números como parámetros y regrese el resultado en forma de tupla de su suma, resta, multiplicación y división. 
# Los resultados se deben almacenar en un diccionario, cuyas claves serán: 
# Suma, Resta, Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función creada anteriormente. 



def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicación(a, b):
    return a * b

def división(a, b):
    return a / b

def resultado(a, b):
        #        ( 0        ,      1     ,      2              ,     3)
    return tuple((suma(a, b), resta(a, b), multiplicación(a, b), división(a, b)))


def resultado_como_diccionario(a, b):
    return { "suma": suma(a, b), "resta": resta(a, b), "multiplicación": multiplicación(a, b), "división": división(a , b)
        
    }

def construir_diccionario(resultado):
    diccionario_resultados = {
        "suma": resultado[0], "resta": resultado[1], "multiplicación": resultado[2], "división": resultado[3]
        }
    return diccionario_resultados




print(construir_diccionario(resultado(3,4)))






