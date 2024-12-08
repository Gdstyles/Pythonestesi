from django.urls import path
from .views import IndexPageView, listar, crear, editar, eliminar_producto, buscar, palabra, login_user, desconectar, registro

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'), 
    path('listar/', listar, name='listar'),
    path('crear/', crear, name='crear'),
    path('editar_producto/<int:producto_id>', editar, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('buscar/', buscar, name='buscar'),
    path('username/<str:user>', palabra),
    path('login/', login_user, name='login'),
    path('logout/', desconectar, name='logout'),
    path('registro/', registro, name='registro')
]
