from django.db import models

# Create your models here.

class Book(models.Model):
    # atributos
    titulo = models.CharField(max_length = 100, null= False)
    autor = models.CharField(max_length = 50, null = False)
    valoración = models.IntegerField(help_text= 'Valoración entre 0 y 100')