from django.contrib import admin
from .models import Vehiculo


# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'rating')
    list_filter = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_modificacion')
    
    def rating(self, obj):
        if 0 <= obj.precio < 10000:
            return 'bajo'
        elif 10000 <= obj.precio <= 30000:
            return 'medio'
        else:
            return 'alto'
    
    
admin.site.register(Vehiculo, VehiculoAdmin) # registro de los model separados por coma