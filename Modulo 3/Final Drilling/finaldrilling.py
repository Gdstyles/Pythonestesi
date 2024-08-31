"""
Dada la siguiente lista de nombres:
• Harry Houdini 
• Newton 
• David Blaine 
• Hawking 
• Messi 
• Teller 
• Einstein  
• Pele  
• Juanes 

Y sabiendo que Harry Houdini, David Blaine y Teller son magos. 
Y también que Newton, Hawking y Einstein son científicos. 
Debemos separar los nombres en tres grupos: magos, científicos y otros;
y escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago. 
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista. 
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; 
luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes. 
    
"""
# Definición

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]
        
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)
    

def crear_listas(magos, cientificos, otros, nombres):
    for temp in nombres:
        if temp in ["Harry Houdini", "David Blaine", "Teller"]:
            magos.append(temp) # se agrega el nombre a la lista
        elif temp in ["Newton", "Hawking", "Einstein"]:
            cientificos.append(temp)
        else:
            otros.append(temp)
            
def imprimir_todo():
    print("------------------------------------------------------------------------------")
    print("Los magos son: ", magos)
    print("------------------------------------------------------------------------------")
    print("Los cientificos son: ", cientificos)
    print("------------------------------------------------------------------------------")
    print("El resto son: ", otros)
    print("------------------------------------------------------------------------------")

#Declaración de listas

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"] 

magos = []

cientificos = []

otros = []


# Ejecución

crear_listas(magos, cientificos, otros, nombres)
hacer_grandioso(magos)
imprimir_nombres(nombres)
imprimir_todo()


