from django import forms 
from .models import Vehiculo



class VehiculoForm(forms.ModelForm):
    
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'marca' : forms.Select(attrs={'class' : 'form-control', 'required' : True}),
            'modelo' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingrese el modelo del vehiculo', 'required' : True}),
            'serial_carroceria' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingrese el número de serie del vehículo', 'required' : True}),
            'serial_motor' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingrese el número de motor del vehículo', 'required' : True}),
            'categoria' : forms.Select(attrs={'class' : 'form-control', 'required' : True}),
            'precio' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'ingrese el precio del vehiculo', 'required' : True}),           
        }