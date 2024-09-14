class Vehiculo:
    def __init__(self, marca :str, modelo :str, numero_ruedas :str) -> None:
        self._marca = marca
        self._modelo = modelo
        self._numero_ruedas = numero_ruedas
    
    @property
    def marca(self) -> str:
        return self._marca
    @marca.setter
    def marca(self, marca :str) -> None:
        self._marca = marca
        
    @property
    def modelo(self) -> str:
        return self._modelo
    @modelo.setter
    def modelo(self, modelo :str) -> None:
        self._modelo = modelo
    
    @property
    def numero_ruedas(self) -> int:
        return self._numero_ruedas
    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas :int) -> None:
        self._numero_ruedas = numero_ruedas