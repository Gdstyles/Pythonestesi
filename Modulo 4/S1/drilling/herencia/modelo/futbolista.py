from modelo.persona import Persona

class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad) #constructor de la clase padre
        #atributos propios de la clase futbolista
        self.dorsal = dorsal
        self.demarcacion = demarcacion
    
    #metodos heredados
    
    def concentrarse(self):
        return super().concentrarse()
    
    def viajar(self):
        return super().viajar()
    
    #metodos propios de la clase futbolista
               
    def jugar_partido(self):
        print("El futbolista {} con dorsal {} está jugando un partido".format(self.nombre, self.dorsal))
        
    def entrenar(self):
        print("El futbolista {} está jugando entrenando".format(self.nombre))