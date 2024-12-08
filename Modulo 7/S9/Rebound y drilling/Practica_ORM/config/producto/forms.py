from django import forms 
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'descripcion': 'Descripción del producto'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class' : 'form-control', 'required' : True}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'required' : True}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'required' : True})
        }
    
