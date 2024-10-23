from django.shortcuts import render, redirect
from django.http import HttpResponse # type: ignore
from django.views.generic import TemplateView
from .models import Book
from .forms import BookForm


# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'index.html'

def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST': # si el metodo es POST
        form = BookForm(request.POST)
        if form.is_valid(): # si el formulario de valido
            form.save() #guarda los datos en la base de datos
            return redirect('lista_libros')
    else: # si el metodo es GET
        form = BookForm()
        return render(request, 'crear_libro.html', {'form': form})