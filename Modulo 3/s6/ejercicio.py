# Escribe un programa que pida al usuario una cadena de texto y cuente cuantas vocales (a,e,i,o,u,) contiene. El programa debe ser insensible a mayusculas y minusculas


# solicitar al usuario que ingrese una cadena de texto 

texto = input("Escribe una cadena de texto: ")

# ignorar mayusculas

texto = texto.lower()

#definir vocales

vocales = "aeiou"

#contador de vocales

contador_vocales = 0

#contar los carácteres de la cadena

for i in texto:
    if i in vocales:
        contador_vocales += 1
        
print(f"la palabra {texto} contiene {contador_vocales} vocales")



