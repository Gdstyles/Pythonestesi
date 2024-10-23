* URL: crear path para la ruta crear_libro/
book/urls.py


* View: crear una vista llamada crear_libro, que recibe un request y retorna el template book/crear_libro.html
book/views.py


* formulario: crear un formulario para la creacion de libros
book/forms.py

* Template: crear una plantilla llamada crear_libro.html, que recibe el formulario del libro.
app/template/crear_libro.html

* activar entorno
.\.venv\Scripts\activate.ps1

* ejecutar servidor, ubicado en la carpeta del proyecto donde se encuentra el archivo manage.py

pyhton manage.py runserver

* crear template footer.html

app/templates/footer.html

* incluirlo en base.html