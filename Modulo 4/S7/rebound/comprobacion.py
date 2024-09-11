class CustomException(Exception):
    # constructor
    def __init__(self, mensaje) -> None:
        super().__init__(mensaje)
        


def excepcion_propia():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            print("Es adulto")
        elif edad <= 0:
            print("Error, ingrese un numero mayor a cero") 
            excepcion_propia()
        
        else:
            print("No es adulto") 
    except ValueError as e:
        print("Error, ingrese un numero")
        excepcion_propia()
    
        
excepcion_propia()
    