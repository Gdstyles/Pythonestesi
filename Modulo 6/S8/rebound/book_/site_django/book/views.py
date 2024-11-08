from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect # type: ignore
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
            messages.success(request, 'Libro creado correctamente')
            return redirect('lista_libros')
        else: # si el formulario no es valido
            messages.error(request, 'Modifica los datos de ingresos')
            return HttpResponseRedirect(reverse('crear_libro')) # redirecciona a la pagina
    else: # si el metodo es GET
        form = BookForm()
        return render(request, 'crear_libro.html', {'form': form})
    
    
def editar_libro(request, libro_id):
    book = get_object_or_404(Book, pk = libro_id) # obteniendo el libro a editar en la database o status 404 not found
    if request.method == 'POST': # si el metodo es POST
        form = BookForm(request.POST, instance=book)
        if form.is_valid(): # si el formulario de valido
            form.save() #guarda los datos en la base de datos
            messages.success(request, 'Libro editado correctamente')
            return redirect('lista_libros')
        else:
            messages.error(request, 'Modifica tus datos de ingreso')
            return HttpResponseRedirect(reverse('editar_libro', args=[book.id])) #redirecciona  ala pagina
    else: # si el metodo es GET
        form = BookForm(instance=book)
        return render(request, 'editar_libro.html', {'form': form, 'libro_id': libro_id})
    
def eliminar_libro(request, libro_id):
    book = get_object_or_404(Book, pk = libro_id) # obteniendo el libro a editar en la database o status 404 not found
    book.delete() # eliminando el libro de la base de datos
    messages.info(request, 'Libro eliminado correctamente')
    return redirect('lista_libros') # redirecciona a la lista de libros


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso')
            return redirect('lista_libros') # cambiar a login
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form' : form})



