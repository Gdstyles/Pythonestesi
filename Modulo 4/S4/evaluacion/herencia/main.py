from model.persona import Persona
from model.maratonista import Maratonista
from model.ciclista import Cliclista


if __name__ == "__main__":
    
    persona = Persona("Arturo")
    maratonista = Maratonista("Alexis")
    ciclista = Cliclista("Charles")
    
    print(f"{persona.nombre} esta {persona.movimiento()}")
    print(f"{maratonista.nombre} esta {maratonista.movimiento()}")
    print(f"{ciclista.nombre} esta {ciclista.movimiento()}")