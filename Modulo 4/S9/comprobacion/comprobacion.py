import os

"""
Diseñe un programa en Python que cree un archivo si no se encuentra;
en caso de existir el archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente creado.
El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente:
Datos de información en la línea 1 
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5 
"""

#definir ruta
"""
def get_path(directorio, nombre_archivo):
    root_dir = os.path.dirname(os.path.abspath(__file__))  # raiz directorio
    folder_path = os.path.join(root_dir, directorio)       # ruta directorio
    file_path = os.path.join(folder_path, nombre_archivo)  # ruta archivo
    return file_path
print(get_path("data", "informacion.dat"))
"""
def crear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'x') as file:
            file.write("")
    except FileExistsError:
        print("Ojito: Archivo ya existe")

def escribir_archivo(lista, nombre_archivo):
    try:
        with open(nombre_archivo, "w", encoding= "utf-8") as file:
            for i in lista:
                file.write(i + "\n")
    except FileNotFoundError:
        print("Errot: Archvio no existe")
        
lista = [
    "Datos de información en la línea 1", 
    "Datos de información en la línea 2",
    "Datos de información en la línea 3",
    "Datos de información en la línea 4",
    "Datos de información en la línea 5",     
]

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding= "utf-8") as file:
            datos = file.read()
            print(datos)
    except FileNotFoundError:
        print("Error: Archivo no existe")
        
        
def agregar_datos(nombre_archivo, lista):        
    try:
        with open(nombre_archivo, "a", encoding= "utf-8") as file:
            for i in lista:
                file.write(i + "\n")
    except FileNotFoundError:
        print("Errot: Archvio no existe")   


lista_dos = [
    "Hola Mundo",  "Este en una nueva línea en el archivo", "agregando la segunda línea del archivo", "finalizando la línea agregada" 
    
]

crear_archivo("informacion.dat")
escribir_archivo(lista, "informacion.dat")

agregar_datos("informacion.dat", lista_dos)
leer_archivo("informacion.dat")