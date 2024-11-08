from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect # type: ignore
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout 
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, User
import datetime

# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'index.html'

@login_required
def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

@login_required
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
    
@login_required   
def editar_libro(request, libro_id):
    book = get_object_or_404(Book, pk = libro_id) # obteniendo el libro a editar en la database o status 404 not found
    if request.method == 'POST': # si el metodo es POST
        form = BookForm(request.POST, instance=book)
        if form.is_valid(): # si el formulario de valido
            book = form.save(commit=False) # pre guardado de los datos
            book.fecha_modificacion = datetime.datetime.now()
            book.save()
            messages.success(request, 'Libro editado correctamente')
            return redirect('lista_libros')
        else:
            messages.error(request, 'Modifica tus datos de ingreso')
            return HttpResponseRedirect(reverse('editar_libro', args=[book.id])) #redirecciona  ala pagina
    else: # si el metodo es GET
        form = BookForm(instance=book)
        return render(request, 'editar_libro.html', {'form': form, 'libro_id': libro_id})

@login_required    
def eliminar_libro(request, libro_id):
    book = get_object_or_404(Book, pk = libro_id) # obteniendo el libro a editar en la database o status 404 not found
    book.delete() # eliminando el libro de la base de datos
    messages.info(request, 'Libro eliminado correctamente')
    return redirect('lista_libros') # redirecciona a la lista de libros


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # guardamos los datos de usuario en una variable
            
            content_type = ContentType.objects.get_for_model(Book)
            permission = Permission.objects.get(
            codename= 'development',
            content_type=content_type,
            )
            
            user.user_permissions.add(permission)
            user.save() # guardamos los datos del usuario en la base de datos
            
            
            messages.success(request, 'Registro exitoso')
            return redirect('login') # cambiar a login
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form' : form})
    
    
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # autentica el usuario en la db
        if user is not None: # si existe
            login(request, user) # persistir la data del usuario
            messages.success(request, F'Bienvenido {user}')
            return redirect('lista_libros') # redireccionar a ruta seleccionada
        else:
            messages.error(request, 'Credenciales inválidas')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html')

def home_page(request):
    return render(request, 'index.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Adiós')
    return render(request, 'index.html')
    


