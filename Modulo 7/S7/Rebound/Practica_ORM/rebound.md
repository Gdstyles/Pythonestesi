EJERCICIO: 

1. Partiendo del modelo creado anteriormente (Fabrica y Productos), procedemos a agregar el modelo al administrador de Django para incluir los registros, tanto para Fábricas como para Productos. 


* crear clase que representen a los modelos dentro del admin.py

from django.contrib import admin
from .models import Fabrica
from .models import Producto
# Register your models here.


class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombe', 'pais')
    list_display_links = ['nombre', 'pais']
    list_filter = ('nombre', 'pais')



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'fecha_vencimiento', 'precio', 'fabrica')
    list_display_links = ['id', 'nombre']
    list_filter = ('nombre', 'fabrica')
    
    
 
    
admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Producto, ProductoAdmin)

* crear super usuario

 - python manage.py createsuperuser

PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 7\S7\Rebound\Practica_ORM\config> python manage.py createsuperuser
Username (leave blank to use 'gonza'): admin
Email address: gonzalo@superuser.cl
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.


2. Inserte los siguientes productos, con sus respectivos fabricantes: 

ID
Nombre
Descripcion
Fecha vencimiento
Precio
Fabrica
	17	Protex Aloe	Jabon de Baño	Oct. 27, 2023	1250	Fabrica object (2)
	16	Speed Stick 27/7	Desodorante para caballeros	April 14, 2023	4500	Fabrica object (2)
	15	Colgate 360	Crema Dental	Feb. 29, 2024	1850	Fabrica object (2)
	14	Ariel Suavizante	Suavizante para la ropa	June 11, 2027	1500	Fabrica object (1)
	13	Crest Premium	Crema dental	Nov. 1, 2024	2500	Fabrica object (1)
	12	Downy Aroma Floral	Ambientador de aroma floral	May 22, 2025	3500	Fabrica object (1)