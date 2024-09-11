from model.persona import Persona

class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def movimiento(self):
        return "trotando"
     
        