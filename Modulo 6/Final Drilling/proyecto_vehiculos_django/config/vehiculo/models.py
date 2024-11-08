from django.db import models
import datetime

# Create your models here.



class Vehiculo(models.Model):
    MARCA = {('FIAT', 'FIAT'), ('CHEVROLET', 'CHEVROLET'), ('FORD', 'FORD'), ('TOYOTA', 'TOYOTA')}
    CATEGORIA = {('PARTICULAR', 'PARTICULAR'), ('TRANSPORTE', 'TRANSPORTE'), ('CARGA', 'CARGA')}
    marca = models.CharField(max_length=20, default='Ford', choices=MARCA)
    modelo = models.TextField(max_length=100)
    serial_carroceria = models.TextField(max_length=50)
    serial_motor = models.TextField(max_length=50)
    categoria = models.CharField(max_length=20, default='Particular', choices=CATEGORIA)
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    fecha_modificacion = models.DateTimeField(default=datetime.datetime.now())
    
    class Meta:
        permissions = [
            # ('permiso', 'descripción)
            # https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#custom-permissions
            ('vehiculo.view', 'Puede ver los vehiculos'),
            ('development', 'Permiso como Desarrollador'),
            ('scrum_master', 'Permiso como Scrum Master'),
            ('product_owner', 'Permiso como Product Owner')            
        ]