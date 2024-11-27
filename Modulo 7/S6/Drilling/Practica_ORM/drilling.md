EJERCICIO: 


Partiendo del modelo creado en el Rebound Exercise: 

1. Agregue los siguientes campos a los modelos, y genere las migraciones correspondientes.  

Fábrica: pais = Tipo cadena de 100 caracteres. 

Producto: f_vencimiento = Tipo fecha, que puede ser nulo o vacío. 

from django.db import models
import datetime
# Create your models here.


class Fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True, null=True)

class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    fecha_vencimiento = models.DateField(default=datetime.datetime.now(), blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    #fabrica = models.OneToOneField(Fabrica, on_delete=models.CASCADE, blank=True, null=True) # uno a muchos
    # fabrica = models.ManyToManyField(Fabrica) # muchos a muchos  

* Realizar migraciones
python manage.py makemigrations producto 0003
python manage.py migrate producto 0003


2. Revierta la migración actual a la 0001_inicial.py, y genere una nueva migración llamada: agregacion_de_relacion_y_campos 

python manage.py migrate producto 0001
python manage.py showmigrations
python manage.py migrate producto 0001
python manage.py makremigrations producto --name acion_de_relacion_y_campos
python manage.py migrate