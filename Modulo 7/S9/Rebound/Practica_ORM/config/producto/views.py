from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Producto
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ProductoForm
from django.urls import reverse

# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'index.html'
    
def listar(request):
    productos = Producto.objects.all()
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

