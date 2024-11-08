from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect # type: ignore
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, User
import datetime
from django.contrib import messages

# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'index.html'
    
    
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})


@login_required
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})

@login_required
def crear_vehiculo(request):
    if request.method == 'POST': # si el metodo es POST
        form = VehiculoForm(request.POST)
        if form.is_valid(): # si el formulario de valido
            form.save() #guarda los datos en la base de datos
            messages.success(request, 'Vehículo creado correctamente')
            return redirect('lista_vehiculos')
        else: # si el formulario no es valido
            messages.error(request, 'Modifica los datos de ingresos')
            return HttpResponseRedirect(reverse('crear_vehiculo')) # redirecciona a la pagina
    else: # si el metodo es GET
        form = VehiculoForm()
        return render(request, 'crear_vehiculo.html', {'form': form})
    
    
@login_required   
def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk = vehiculo_id) # obteniendo el vehiculo a editar en la database o status 404 not found
    if request.method == 'POST': # si el metodo es POST
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid(): # si el formulario de valido
            vehiculo = form.save(commit=False) # pre guardado de los datos
            vehiculo.fecha_modificacion = datetime.datetime.now()
            vehiculo.save()
            messages.success(request, 'Vehículo editado correctamente')
            return redirect('lista_vehiculos')
        else:
            messages.error(request, 'Modifica tus datos de ingreso')
            return HttpResponseRedirect(reverse('editar_vehiculo', args=[vehiculo.id])) #redirecciona  ala pagina
    else: # si el metodo es GET
        form = VehiculoForm(instance=vehiculo)
        return render(request, 'editar_vehiculo.html', {'form': form, 'vehiculo_id': vehiculo_id})
    
    
@login_required    
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk = vehiculo_id) # obteniendo el vehiculo a editar en la database o status 404 not found
    vehiculo.delete() # eliminando el vehiculo de la base de datos
    messages.info(request, 'Vehículo eliminado correctamente')
    return redirect('lista_vehiculos') # redirecciona a la lista de libros


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # guardamos los datos de usuario en una variable
            
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permission = Permission.objects.get(
            codename= 'vehiculo.view',
            content_type=content_type,
            )
            
            user.user_permissions.add(permission)
            
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
            return redirect('lista_vehiculos') # redireccionar a ruta seleccionada
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
        
    