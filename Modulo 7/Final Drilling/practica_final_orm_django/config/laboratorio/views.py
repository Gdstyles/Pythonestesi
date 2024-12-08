from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Laboratorio 
from .forms import LaboratorioForm

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'


# views o controller para listar laboratorios
def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar_laboratorios.html', {'laboratorios': laboratorios})

# views o controller para crear laboratorios
def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio creado')
            return redirect('listar_laboratorios')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('crear_laboratorio'))
    else:
        form = LaboratorioForm()
        return render(request, 'crear_laboratorio.html', {'form':form}) 

# views o controller para editar laboratorios

def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio editado')
            return redirect('listar_laboratorios')
        else:
            messages.error(request, 'Datos inválidos para editar el laboratorio')
            return HttpResponseRedirect(reverse('editar_laboratorio', args=[laboratorio.id]))
    else:
        form = LaboratorioForm(instance=laboratorio)
        return render(request, 'editar_laboratorio.html', {'laboratorio_form':form, 'laboratorio_id': laboratorio_id})



# views o controller para eliminar laboratorios


def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    laboratorio.delete()
    messages.success(request, 'Laboratorio eliminado correctamente')
    return redirect('listar_laboratorios')

