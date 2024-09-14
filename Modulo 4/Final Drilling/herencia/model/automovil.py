from model.vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_ruedas: str, velocidad :int, cilindrada :int) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada
    
    @property
    def velocidad(self) -> int:
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad :int) -> None:
        self._velocidad = velocidad
        
    @property
    def cilindrada(self) -> int:
        return self._cilindrada
    @cilindrada.setter
    def cilindrada(self, cilindrada :int) -> None:
        self._cilindrada = cilindrada
    
    def __str__(self) -> str:
        return f"Datos del automovil: Marca {self._marca}, Modelo:{self._modelo}, {self._numero_ruedas} ruedas, {self._velocidad} Km/h, {self._cilindrada} cc)"