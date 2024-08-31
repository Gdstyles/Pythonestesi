from modelo.persona import Persona

class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, id_federacion):
        super().__init__(id, nombre, apellidos, edad) #invocacion constructor
        self.id_federacon: id_federacion
    
    #metodos heredados    
    def concentrarse(self):
        return super().concentrarse()   
    def viajar(self):
        return super().viajar()
    #metodos propios
    def dirigir_partido():
        print("El entrenador dirige el partido")
    def dirigir_entrenamiento():
        print("El entrenador dirige el entrenamiento")