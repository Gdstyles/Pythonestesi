from multipledispatch import dispatch


class Animal:
    
        #constructor con parametros
    @dispatch(str, str, int, float)    
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
        # constructor vacio
    def __init__(self, nombre=None, raza=None, edad=None, peso=None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
    #constructor sin parametros
 #   def __init__(self):
  #      self.nombre = None
 #       self.raza = None
 #       self.edad = None
 #       self.peso = None
        
    def comer(self):
        print("comiendo")
        
    def caminar(self):
        print("caminando")
        
    def dormir(self):
        print("durmiendo")
        
    def __str__(self) -> str:
        return f"Animal(Nombre: {self.nombre}, Raza: {self.raza}, Edad:{self.edad}, Peso: {self.peso})"
    
#instancia con constructor con parametros

perro = Animal("Brando", "San Bernardo", 3, 30)
gato = Animal("Roll", "Persa", 4, 3)