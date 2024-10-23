from django import forms 
from .models import Book


class BookForm(forms.ModelForm):
    
    class Meta: # clase meta para definir características del objeto
        model = Book # modelo a utilizar
        fields = ['titulo', 'autor', 'valoracion']
        Widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese el titulo del libro', 'required' : True}),
            'autor' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese el autor del libro', 'required' : True}),
            'valoracion' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingrese la valoracion del libro', 'required' : True})
            }