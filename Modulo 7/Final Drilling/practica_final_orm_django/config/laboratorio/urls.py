from django.urls import path, include
from .views import IndexPageView, listar_laboratorios, crear_laboratorio, editar_laboratorio, eliminar_laboratorio 

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'), 
    path('listar_laboratorios/', listar_laboratorios, name='listar_laboratorios'),
    path('crear_laboratorio/', crear_laboratorio, name='crear_laboratorio'),
    path('editar_laboratorio/<int:laboratorio_id>', editar_laboratorio, name='editar_laboratorio'),
    path('eliminar_laboratorio/<int:laboratorio_id>', eliminar_laboratorio, name='eliminar_laboratorio'),
]
