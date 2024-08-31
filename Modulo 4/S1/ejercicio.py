#class nombre_objeto:

class Vehiculo:
    # constructor con parámetros, se necesitan todos los atributos o parametros para instanciar al objeto
    def __init__(self, marca, tipo, modelo, año, transmisión, combustible):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.año = año
        self.transmisión = transmisión
        self.combustible = combustible
        
        
    def __init__(self, marca=None, tipo=None, modelo=None, año=None, transmisión=None, combustible=None):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.año = año
        self.transmisión = transmisión
        self.combustible = combustible
        
    def stock(self):
        print(f"El vehículo {self.marca} {self.modelo} se encuentra en stock")
    
    def estado(self):
        print(f"El vehículo {self.marca} {self.modelo} se encuentra en buen estado")
    
    def mantencion(self):
        print(f"El vehículo {self.marca} {self.modelo} necesita mantención")
        
    def venta(self):
        print(f"El vehículo {self.marca} {self.modelo} está en venta")
    
    def reserva(self):
        print(f"El vehículo {self.marca} {self.modelo} está reservado")
           
    def __str__(self) -> str:
        return f"Vehiculo: marca: {self.marca}, tipo: {self.tipo}, modelo:{self.modelo}, año: {self.año}, transmisión:{self.transmisión}, combustible:{self.combustible}"
    
#instancia de vehículo invocando al constructor con parámetros
vehiculo1 = Vehiculo("Toyota", "Hatchback", "A86 Trueno", "1988", "mecánica", "bencina")
vehiculo2 = Vehiculo("DMC", "Gran Turismo", "DMC-12", "1985", "mecánica", "bencina")
vehiculo3 = Vehiculo("Cadillac", "carrozado", "El Dorado", "1959", "automático", "bencina")
vehiculo4 = Vehiculo("Tesla", "sedan", "model 3", "2024", "automático", "eléctrico")
vehiculo5 = Vehiculo("Scania", "tracto camión", "113H", "1997", "automático", "petróleo")

# instancia de vehiculo sin parametros, se omiten los atributos

vehiculo_seis = Vehiculo()
vehiculo_seis.marca = "Hyundai" #asignando atributos del objeto
vehiculo_seis.tipo = "Hatchback"
vehiculo_seis.modelo = "Getz"
vehiculo_seis.año = "2010"
vehiculo_seis.transmisión = "mecánico"
vehiculo_seis.combustible = "bencina"

vehiculo_siete = Vehiculo()
vehiculo_siete.marca = "Fiat" #asignando atributos del objeto
vehiculo_siete.tipo = "Hatchback"
vehiculo_siete.modelo = "Grande Punto"
vehiculo_siete.año = "2012"
vehiculo_siete.transmisión = "mecánico"
vehiculo_siete.combustible = "bencina"


# invocacion 

vehiculo1.stock()
print("-------------------------------------------------------------")
vehiculo2.estado()
print("-------------------------------------------------------------")
vehiculo3.mantencion()
print("-------------------------------------------------------------")
vehiculo4.venta()
print("-------------------------------------------------------------")
vehiculo5.reserva()
print("-------------------------------------------------------------")
vehiculo_seis.stock()
print("-------------------------------------------------------------")
vehiculo_siete.estado()

