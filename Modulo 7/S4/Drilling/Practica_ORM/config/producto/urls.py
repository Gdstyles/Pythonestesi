from django.urls import path
from .views import IndexPageView, listar, crear

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'), 
    path('listar/', listar, name='listar'),
    path('crear/', crear, name='crear'),
]
