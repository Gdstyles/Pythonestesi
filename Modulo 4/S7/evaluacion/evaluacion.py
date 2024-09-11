

class RangoSalarioError(Exception):
    def __init__(self, mensaje, salario) -> None:
        super().__init__(mensaje)
        self.salario = salario
        self.mensaje = mensaje
    
    def __str__(self) -> str:
        return f"{self.salario} -> {self.mensaje}"

def validar_salario():
    try:
        salario = int(input("Ingrese el salario: "))
        if not (1000 <= salario <= 2000):
            raise RangoSalarioError("Salario no está definido en el rango (1000 a 2000)", 5000)
        print(f"El salario {salario} se encuentra dentro del rango")
    except Exception as e:
        print("Error" ":", str(e))
        
validar_salario()

