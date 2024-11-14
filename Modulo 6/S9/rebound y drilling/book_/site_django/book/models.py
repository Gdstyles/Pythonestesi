from django.db import models

# Create your models here.

class Book(models.Model):
    # atributos
    titulo = models.CharField(max_length = 100, null= False)
    autor = models.CharField(max_length = 50, null = False)
    valoracion = models.IntegerField(help_text= 'Valoración entre 0 y 100')

    class Meta:
        permissions = [
            # ('permiso', 'descripción)
            # https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#custom-permissions
            ('book.view', 'Puede ver los libros'),
            ('development', 'Permiso como Desarrollador'),
            ('scrum_master', 'Permiso como Scrum Master'),
            ('product_owner', 'Permiso como Product Owner')            
        ]