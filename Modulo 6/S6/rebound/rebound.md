* copiar preyecto anterior o crear uno con todas las configuraciones necesarias

* eliminar archivos dentro de la carpeta templates


* eliminar los path creados en urls.py de la app book 



* estructura de templates a crear
base.html -> estructura base
    include: navbar.html -> barra de navegacion

layout.html -> template a reutilizar
    extends: base.html -> estructura base

index.html -> pagina principal
    extends: layout.html -> template a reutilizar

actores o archivos a crear:
navbar.html
base.html
layout.html
index.html

* instalar en el entorno boostrap 5
pip install django-bootstrap-v5

* registrar el uso de bootstrap 5 como app en settings.py


* crear archivo navbar.html dentro de la carpeta templates

templates/navbar.html

* crear archivo base.html dentro de la carpeta templates
templates/base.html

* crear archivo layout.html que extiende de base.html dentro de la carpeta templates

templates/layout.html

* crear archivo index.html que extiende layout.html dentro de la carpeta templates

templates/index.html



* agregar al archivo urls.py dentro de la app la estructura necesaria para listar los libros


    path('lista_libros/', lista libros, name='lista_libros'),

* en el archivo views.py agregar una funcion que despliegue una lista de libros

    def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})


* controlador para deplegar informacion: en el archivo views.py agregar una funcion que despliegue una lista de libros

* Model: crear un modelo para los libros

https://docs.djangoproject.com/en/5.1/topics/db/models/
    class Book(models.Model):
    # atributos
    titulo = models.CharField(max_length = 100, null= False)
    autor = models.CharField(max_length = 50, null = False)
    valoración = models.IntegerField(help_text= 'Valoración entre 0 y 100')

* creal template, crear un archivo html para listar los libros

templates/lista_libros.html



* ejecutar

realizar migracion
 python manage.py makemigrations book
 python manage.py sqlmigrate book 0001  # si hay SQL
 
 python manage.py migrate

