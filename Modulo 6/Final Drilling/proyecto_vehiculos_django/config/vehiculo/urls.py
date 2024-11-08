from django.urls import path
from . import views
from .views import IndexPageView, lista_vehiculos, crear_vehiculo, editar_vehiculo, eliminar_vehiculo, registro, iniciar_sesion, home_page, logout_view



urlpatterns = [
    path('', IndexPageView.as_view(),name='index'),
    path('lista_vehiculos/', lista_vehiculos, name='lista_vehiculos'),
    path('crear_vehiculo/', crear_vehiculo, name='crear_vehiculo'),
    path('editar_vehiculo/<int:vehiculo_id>', editar_vehiculo, name="editar_vehiculo"),
    path('eliminar_vehiculo/<int:vehiculo_id>', eliminar_vehiculo, name='eliminar_vehiculo'), # registrando ruta para editar vehiculo
    path('registro/', registro, name='registro'), # registrando ruta para el formulario de registro
    path('login/', iniciar_sesion, name= 'login'), # registrando ruta para el login
    path('home/', home_page, name='home'),
    path('logout_view/', logout_view, name='logout_view')
    
    
]