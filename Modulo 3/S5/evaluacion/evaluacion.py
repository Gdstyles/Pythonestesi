
# [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
# [p,a,r,a,l,a,l,e,p,i,p,e,d,o]

palabra = "paralelepípedo"

patron = "aeiouAEIOUáéíóúÁÉÍÓÚ"

acumulador_consonantes = ""


for i in range(len(palabra)): #i es el indice de cada caracter
    if palabra[i] not in patron: # si el caracter no esta en el patron
        acumulador_consonantes += palabra[i] # se acumula cada caracter consonante dentro de una variable
        print(f"La letra {palabra [i]} se encuentra en la posicion {i}")

print("Las letras consonantes son {acumulador_consonantes}")


    

    



