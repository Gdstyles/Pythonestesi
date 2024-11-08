# sitio administrativo

*ubicarse en la terminal en la ubicación del archivo manage.py

* crear superusuario
'python manage.py createsuperuser'
Nombre de usuario (leave blank to use 'gonza'): admin
Dirección de correo electrónico: admin@book.com
Password: admin
Password (again): admin
La contraseña es demasiado similar a la de nombre de usuario.
Esta contraseña es demasiado corta. Debe contener al menos 8 caracteres.
Esta contraseña es demasiado común.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

* registrar el modelo internamente dentro del admin.py
app/admin.py

https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin

from django.contrib import admin
from .models import Book

- admin.site.register(Book)

* ingresar a la ruta del sitio administrativo 
python manage.py runserver

Starting development server at http://127.0.0.1:8000/admin

* Configurar con la finalidad de que el sitio administrativo aparezca como Libro y Libros, respectivamente

<app/admin.py>

 class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    
* aplicar migraciones ya que se modifico el modelo Book

* Agregar dos atributos especiales al modelo del tipo fecha:
uno que se refiere a la fecha de creacion (fecha_creacion), y el otro a la fecha de modificación (fecha_modificación)

app/models.py

class Book 

    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    fecha_modificacion = models.DateTimeField(default=datetime.datetime.now())


* aplicar migraciones ya que se modifico el modelo Book

* Modificar el views para la edicion de libros agregar la fecha de modificacion


- def editar_libro(request, libro_id):
    book = get_object_or_404(Book, pk = libro_id) # obteniendo el libro a editar en la database o status 404 not found
    if request.method == 'POST': # si el metodo es POST
        form = BookForm(request.POST, instance=book)
        if form.is_valid(): # si el formulario de valido
            book = form.save(commit=False) # pre guardado de los datos
            book.fecha_modificacion = datetime.datetime.now()