estudiantes = [{'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
               {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
               {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
               {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
               {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
               ] 

def promedio(lista):
    return sum(lista)/ len(lista)

#Filtar estudiantes
estudiantes_filtrados = []
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and promedio(estudiante['calificaciones']) > 85:
        estudiantes_filtrados.append(estudiante)
        print(estudiante)
        
# edad numero primo


def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


for estudiante in estudiantes:
    if primo(estudiante['edad']) and estudiante['edad'] > 18:
        print(f"{estudiante['nombre']}:")
        print(f"Promedio calificacion {sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])}")

