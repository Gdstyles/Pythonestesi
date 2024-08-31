from modelo.persona import Persona

class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, años_experiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.años_experiencia = años_experiencia
        
    def concentrarse(self):
        return super().concentrarse()
    def viajar(self):
        return super().viajar()
    def dar_masajes(self):
        print("masajeando")