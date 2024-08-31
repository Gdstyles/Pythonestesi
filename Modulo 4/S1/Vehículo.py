"""
Los objetos comienzan con la plabra class, inician con el nombre del objeto en mayuscula
los objetos tienen constructor(crear la instancia) y accesadores
"""


#class nombre_objeto:

class Vehiculo:
    # constructor con parámetros, se necesitan todos los atributos o parametros para instanciar al objeto
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        
        
    # constructor vacio o constructor sin parámetros    
    def __init__(self, marca=None, color=None, modelo=None, peso=None, ancho=None, alto=None):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    
    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} arrancó")
        
    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} frenó")
        
    def girar_izquierda(self):
        print(f"El vehículo {self.marca} {self.modelo} giró a la izquierda")
        
    def girar_derecha(self):
        print(f"El vehículo {self.marca} {self.modelo} giró a la derecha")
        
    def apagar(self):
        print(f"El vehículo {self.marca} {self.modelo} se apagó")
        
    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} se encendió")
        
    def retroceder(self):
        print(f"El vehículo {self.marca} {self.modelo} retrocedió")
    
    
    
    #funcion para imprimir los objetos en String y no la referencia en memoria del objeto    
    def __str__(self) -> str:
        return f"Vehiculo: marca: {self.marca}, color: {self.color}, modelo:{self.modelo}, peso: {self.peso}, ancho:{self.ancho}, alto:{self.alto}"
        
#instancia de vehículo invocando al constructor con parámetros
vehiculo = Vehiculo("BMW", "Blanco", "M3", "1500", "2", "1.5")
vehiculo.color = "Rojo" # set asignando valor a un atributo
print(vehiculo.color) # get accediendo imprimiento el valor del atributo
        
# instancia de vehiculo sin parametros, se omiten los atributos

vehiculo_uno = Vehiculo()
vehiculo_uno.marca = "Chevrolet" #asignando atributos del objeto
vehiculo_uno.color = "Negro"
vehiculo_uno.modelo = "Aveo"
vehiculo_uno.peso = "1500"
vehiculo_uno.ancho = "2"
vehiculo_uno.alto = "1.5"

#invocar metodos del objeto, accediendo a los metodos del objeto
vehiculo.arrancar()
vehiculo.frenar()
vehiculo.girar_izquierda()
vehiculo.girar_derecha()
vehiculo.apagar()
vehiculo.encender()
vehiculo.retroceder()
print("---------------------------------------------------------")

vehiculo_uno.arrancar()

print(vehiculo)
print(vehiculo_uno)
