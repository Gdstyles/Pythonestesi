from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Producto
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login
from .forms import ProductoForm
from django.urls import reverse

# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'index.html'
    
def listar(request):
    productos = Producto.objects.using('default').all().order_by('id')
    return render(request, 'listar_productos.html', {'productos': productos})

def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado')
            return redirect('listar')
        else:
            messages.error(request, 'Error en datos ingresados')
            return HttpResponseRedirect('crear')
    else:
        form = ProductoForm()
        return render(request, 'crear_producto.html', {'producto_form':form})
    
    
def editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado')
            return redirect('listar')
        else:
            messages.error(request, 'Datos inválidos para editar el producto')
            return HttpResponseRedirect(reverse('editar_producto', args=[producto.id]))
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'producto_form':form, 'producto_id': producto_id})
    
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('listar')

def index(request):
    return render(request, 'index.html')

def buscar(request):  
    if request.method == 'GET':
        query = request.GET.get('query')
        try:     
            query_id = int(query)
        except ValueError:
            query_id = None
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) 
            | Q(descripcion__icontains=query)
            | (Q(id=query_id) if query_id is not None else Q())
            | (Q(precio=query_id) if query_id is not None else Q())
            ).order_by('id')
        return render(request, 'listar_productos.html', {'productos':productos})
    
def palabra(request, user):
    return render(request, 'username.html', {'user':user})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro exitoso')
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Modifica los datos de ingreso')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, F'Bienvenido {user}')          
                return redirect('listar')
        else:
            messages.error(request, 'usuario o password incorrectos')
            form = AuthenticationForm()
            return render(request, 'login.html', {'form':form}) 
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})   
    
def desconectar(request):
    logout(request)
    messages.success(request, 'Adiós')
    return render(request, 'index.html')  
    
    