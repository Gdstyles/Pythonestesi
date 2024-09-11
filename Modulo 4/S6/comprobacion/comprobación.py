

suma = 3000
contador = 0

def division():
    try:
        div = suma/contador
        print(div)
    except ZeroDivisionError as error:
        print("División por cero")
        
division()