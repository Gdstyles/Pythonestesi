* Crea modelo producto

* Registrar las url dentro de urls.py del proyecto
> config/urls.py

  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('producto.urls')),
      path('producto/', include('producto.urls'))
  ]


* Registrar paquetes dentro de settings.py

  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'producto.apps.ProductoConfig',
    'bootstrap5',
    'crispy-forms',
    'crispy-bootstrap5',
    
]

* URL: crear archivo urls.py dentro del aplicativo 
>producto/urls.py

  from django.urls import path
  from .views import listar, crear

  urlpatterns = [
    path('listar/', listar, name='listar'),
    path('crear/', crear, name='crear'),
  ]



* VIEWS: crear views dentro de views.py

class IndexPageView(TemplateView):
  template_name = 'index.html'
    
def lista_vehiculos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

* FORMS: crear ProductoForm dentro de forms.py
>producto/forms.py



* TEMPLATES: crear templates html dentro de la carpeta templates
>producto/templates


base.html
navbar.html
layout.html
index.html