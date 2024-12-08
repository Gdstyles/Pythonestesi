from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad', 'pais')
    list_display_links = ['nombre']
   # list_filter = ('nombre')
    
    
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especialidad', 'laboratorio')
    list_display_links = ['nombre']
   # list_filter = ('nombre', 'laboratorio')
    
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'fecha_fabricacion', 'precio_costo', 'precio_venta')
    list_display_links = ['nombre']
   # list_filter = ('nombre', 'laboratorio')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)

