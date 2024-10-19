1. Crear la carpeta template.

book/template




2. Proceder a crear nuestro archivo index.html. 



book/template/index.html

'html:5'

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Bienvenido a mi sitio de libros</h1>
</body>
</html>


3. Adecuar la vista views.py. 



from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')

class IndexPageView(TemplateView):
    template_name = 'index.html'





4. Configuración del Path /URLs. 



from django.urls import path
from . import views
from .views import IndexPageView

urlpatterns = [
   # path('', views.index, name='index'),
   path('', IndexPageView.as_view(),name='index'),
]






5. Configurar con la finalidad de que la página de inicio del proyecto se redireccione a la página index, previamente creada. 