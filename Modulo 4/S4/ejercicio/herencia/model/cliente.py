from model.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        super().__init__(nombre, apellido, rut)
        self._descuento = descuento
        
    #accesador de descuento
    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento

