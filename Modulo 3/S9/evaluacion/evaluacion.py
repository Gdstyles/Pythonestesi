


# Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo. Validar que ambos sean números positivos. 

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

def calcular_area_rectangulo(base, altura):
    if base < 0 or altura < 0:
        return print("Ingrese números válidos")
    return base * altura



print("El área es ", calcular_area_rectangulo(base, altura))


