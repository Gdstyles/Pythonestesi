#Match case

while True:
    opcion = input("Hola Bienvenido\n" 
                +"1.- Opcion 1\n"
                +"2.- Opcion 2\n"
                +"3.- Opcion 3\n"
                +"4.- Salir"
                )


    match opcion:
        case "1":
            print("Opcion 1")
        case "2": 
            print("Opcion 2")
        case "3":
            print("Opcion 3")
        case "4":
            print("Hasta luego....")
            break
        case _: #under score
            print("Opción no válida, ingrese otra opción")

