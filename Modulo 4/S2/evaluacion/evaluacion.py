class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
        
        # accesadores y mutadores 
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_apellidos(self):
        return self.apellidos
    
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
        
    def get_sexo(self):
        return self.sexo
    
    def set_sexo(self, sexo):
        self.sexo = sexo
        
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad
        
    def get_estatura(self):
        return self.estatura
    
    def set_estatura(self, estatura):
        self.estatura = estatura
        
    def get_peso(self):
        return self.peso
    
    def set_peso(self, peso):
        self.peso = peso
        
    def __str__(self) -> str:
        return f"Persona: nombre: {self.nombre}, apellidos: {self.apellidos}, sexo: {self.sexo}, edad: {self.edad}, estatura: {self.estatura}, peso: {self.peso}"
        
        
persona_uno = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg")
persona_dos = Persona("Juan", "Camargo", "Masculino", "18 años", "1.80 mts", "75 Kg")

print(persona_uno)
print(persona_dos)

persona_uno.set_edad("21 años")
persona_dos.set_apellidos("Santiago")


print(persona_uno)
print(persona_dos)

