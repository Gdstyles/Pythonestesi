from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Producto
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ProductoForm

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

