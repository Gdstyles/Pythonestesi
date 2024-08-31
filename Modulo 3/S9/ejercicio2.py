""" Sistema de Gestión de Inventario
Enunciado: Crea un programa que gestione el inventario de una tienda.
El programa debe permitir al usuario agregar, eliminar y actualizar productos en el inventario.
Cada producto debe tener un nombre, una cantidad y un precio. Además, el programa debe permitir
al usuario ver el inventario completo y calcular el valor total del inventario.
Utilizar un diccionario para representar el inventario
 
{   “nombre”: {“cantidad”: “5”, “precio”:”5000”} }"""
 
 
# Base de datos // diccionario vacio
inventario = {}
 
#Funcion de agregar producto al inventario
def agregar_producto (nombre, cantidad, precio):
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
 
#Funcion de eliminar producto del inventario
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
    else :
        print("El producto no existe en el inventario ")
 
#Funcion de actualizar producto del inventario
def actualizar_producto(nombre, cantidad, precio):
    if nombre in inventario:
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    else:
        ("El producto no existe en el inventario")
 
def ver_inventario():
 
    total = 0
    for clave, valor in inventario.items():
        print(f"Producto :{clave}, Cantidad: {valor['cantidad']}, Precio: {valor['precio']}" )
 
        total += (valor["cantidad"] * valor ["precio"])
 
       # print ("total de inventario es", total)
 
#agregar_producto("manzana", 10, 300)
#agregar_producto("platanos", 10, 900)
 
#ver_inventario()
 
def ingreso_opcion():
    return input('Ingrese una Opcion: \n'
                 + '1.- agregar\n'
                 + '2.- eliminar\n'
                 + '3.- actualizar\n'
                 + '4.- ver inventario\n'
                 + '5.- salir\n')
   
def ingreso_valores_productos():    
    nombre = input('ingrese el nombre: ')
    cantidad = ingreso_numero('ingrese el cantidad: ')  
    precio = ingreso_numero('ingrese el precio: ')    
    return (nombre, cantidad, precio)
 
def ingreso_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Opción invalida, ingrese un número')
 
   
def verificar_opcion():
     while True:
        opcion_ingresada = ingreso_opcion()
        #match opcion_ingresada:
        if opcion_ingresada == '1':
            nombre,cantidad,precio = ingreso_valores_productos()
            agregar_producto(nombre,cantidad,precio)
        elif opcion_ingresada== '2':
            nombre_producto =  input("Ingrese el nombre del producto")
            eliminar_producto(nombre_producto)
        elif opcion_ingresada== '3':
            nombre,cantidad,precio = ingreso_valores_productos()
            actualizar_producto(nombre,cantidad,precio)
        elif opcion_ingresada == '4':
            ver_inventario()
        elif opcion_ingresada == '5':
            break
        else:
            print("Opcion invalida")
 
 
 
 
 
verificar_opcion()

