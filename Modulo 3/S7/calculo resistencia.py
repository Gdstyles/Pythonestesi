# calcular la resistencia  total dado el ingreso de 3 resistencias por consola
# rt = 1/((1/r1) + (1/r2) + (1/r3))

def ingreso_variable():
    while True:
        try:
            r = float(input("ingrese el valor de la resistencia: "))
            if r > 0:
                return r
            else:
                print("la resistencia ingresada es negativa")
        except Exception as error:
            print("Ha sucedido un error:", error)

resistencias = int(input("ingrese el número de resistencias"))

i = 0
lista = []
while i < resistencias:
    r = ingreso_variable()
    lista.append(r)
    i +=1

resistencia_total = 1/sum(1/r for temp in lista)

print(resistencia_total)
    
    
    
r1 = ingreso_variable()
r2 = ingreso_variable()
r3 = ingreso_variable()

rt = 1/((1/r1) + (1/r2) + (1/r3))

print(f"{rt:.2f}")


