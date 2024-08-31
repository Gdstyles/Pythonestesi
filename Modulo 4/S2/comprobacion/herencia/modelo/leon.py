from modelo.animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, edad, raza, peso)