from model.automovil import Automovil

def crear_vehiculo() -> Automovil:
    marca = input("Inserte la marca: ")
    modelo = input("Inserte el modelo: ")
    numero_ruedas = input("Inserte el número de ruedas: ")
    velocidad = input("Inserte la velocidad en Km/h: ")
    cilindrada = input("Inserte la cilindrada en cc: ")
    return Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)

def imprimir_objetos(lista):
    for i in lista:
        print(i)

def ingreso_cantidad() -> int:
    return int(input("Cuanto vehículos desea ingresar: "))

def orquestacion_creacion() -> list[Automovil]:
    cantidad_ingresos = ingreso_cantidad()

    lista_vehiculos = []

    for i in range(0, cantidad_ingresos):
        print("datos del automovil", i+1)
        vehiculo = crear_vehiculo()
        lista_vehiculos.append(vehiculo)
        return lista_vehiculos

lista = orquestacion_creacion()

print("Lista de vehiculos: ")
imprimir_objetos(lista)