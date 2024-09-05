class Persona:
    def __init__(self, nombre, apellido, rut):
        self._nombre = nombre             # atributos privados _nombre_variable
        self._apellido = apellido
        self._rut = rut
    
    #accesadores y mutadores (getter y setter)
    @property            #get
    def nombre(self):
        return self._nombre
    @nombre.setter       #set
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self, rut):
        self._rut = rut
        
    
    def get_tipo(self):
        print(f"Soy del tipo {self}")
        print(type(self))
        
    def __str__(self) -> str:
        return f"Persona(nombre:{self._nombre}, apellido:{self._apellido}, rut: {self._rut})"
        