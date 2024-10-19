# Crear carpeta

    Book

# crear entorno

    python -m venv .venv

# activar entornos

    .\.venv\Scripts\activate.ps1

# instalar django

    pip install django

# crear proyecto

    django-admin startproject site_django

# crear aplicativo

     (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S4\Rebound\book> cd site_django
    django-admin startapp book

# registrar aplicativo

    'book.app.BookConfig',

# migrar base de datos

    
    (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S4\Rebound\book\site_django> python manage.py migrate


1. Agregar al proyecto site_django una URL que incluya las URLs de la aplicación book, creada en la práctica anterior con el siguiente path: http://localhost:8000/book/. 


    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('book/', include('book.urls')),
        path('', include('book.urls'))
    ]

# crear urls del aplicativo

book/urls

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]

2. Crear una vista que retorne, por medio del método HttpResponse, el mensaje “Bienvenidos a mi sitio de libros”. 

    views.py
        from django.shortcuts import render
        from django.http import HttpResponse
        # Create your views here.

        def index(request):
        return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')


3.

(.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S4\Rebound\book\site_django> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 17, 2024 - 21:49:04
Django version 5.1.2, using settings 'site_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[17/Oct/2024 21:49:13] "GET / HTTP/1.1" 200 245
[17/Oct/2024 21:49:24] "GET / HTTP/1.1" 200 245
[17/Oct/2024 21:52:31] "GET /book HTTP/1.1" 301 0
[17/Oct/2024 21:52:31] "GET /book/ HTTP/1.1" 200 245