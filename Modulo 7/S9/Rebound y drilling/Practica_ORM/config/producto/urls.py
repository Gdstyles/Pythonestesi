from django.urls import path
from .views import IndexPageView, listar, crear, editar, eliminar_producto

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'), 
    path('listar/', listar, name='listar'),
    path('crear/', crear, name='crear'),
    path('editar_producto/<int:producto_id>', editar, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
]
