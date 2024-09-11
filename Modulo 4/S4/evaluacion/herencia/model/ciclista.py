from model.persona import Persona

class Cliclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        return "rodando"