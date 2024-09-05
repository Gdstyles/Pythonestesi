from model.persona import Persona

class Supervisor(Persona):
    def __init__(self, nombre, apellido, rut, area):
        super().__init__(nombre, apellido, rut)
        self._area = area
    
    #accesadores y mutadores (getter y setter)
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, area):
        self._area = area