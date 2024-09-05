from model.cliente import Cliente
from model.supervisor import Supervisor
from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService

#instancias globales

# menu_service = MenuService()
# cliente_service = ClienteService()
# supervisor_service = SupervisorService()

def main():
    #creacion de instancias para acceso a los servicios
    menu_service = MenuService()
    cliente_service = ClienteService()
    supervisor_service = SupervisorService()
    
    while True:
        menu_service.imprimir_menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            cliente_service.crear_cliente()
        
        elif opcion == "2":
            supervisor_service.crear_supervisor()
        
        elif opcion == "3":
            print("Adios")
            break
            
        else:
            print("Opción inválida")
    
    pass 


#punto de entrada o ejecucion del programa
if __name__ == "__main__":
    main()
    