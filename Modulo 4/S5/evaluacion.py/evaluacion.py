class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno
        
class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        super().__init__(nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario
 
        
        
trabajador = Trabajador("Juan", "Pérez", 2005, "Ingeniería de Software", "IS", 20000)

print(trabajador.__dict__)

print(f"El trabajador es instancia de Persona:", isinstance(trabajador,Persona))
print(f"El trabajador es instancia de Departamento:", isinstance(trabajador,Departamento))
print(f"El trabajador es instancia de Trabajador:", isinstance(trabajador,Trabajador))
        
        
        