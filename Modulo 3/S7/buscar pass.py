# solicita al usuario ingresar una contraseña hasta que la contraseña ingresada coincida con una contraseña indefinida

pass_guardada = "1234perro"

while True:
    ingreso = input("Ingrese la contraseña: ")
    if pass_guardada == ingreso:
        print("pass encontrada")
        break
    else:
        print("volver a ingresar")

