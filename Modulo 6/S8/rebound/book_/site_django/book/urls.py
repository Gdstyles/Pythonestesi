
from django.urls import path
from . import views
from .views import IndexPageView, lista_libros, crear_libro, editar_libro, eliminar_libro, registro

urlpatterns = [
   path('', IndexPageView.as_view(),name='index'),
   path('lista_libros/', lista_libros, name='lista_libros'),
   path('crear_libro/', crear_libro, name='crear_libro'),
   path('editar_libro/<int:libro_id>', editar_libro, name="editar_libro"),
   path('eliminar_libro/<int:libro_id>', eliminar_libro, name='eliminar_libro'), # registrando ruta para editar libro
   path('registro/', registro, name='registro') # registrando ruta para el formulario de registro
]