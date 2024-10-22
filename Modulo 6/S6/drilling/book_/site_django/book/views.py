from django.shortcuts import render
from django.http import HttpResponse # type: ignore
from django.views.generic import TemplateView
from .models import Book


# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'index.html'

def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})