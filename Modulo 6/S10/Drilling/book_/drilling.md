# Modificar el sitio administrativo

* crear clase custom para modificar BookAdmin(admin.ModelAdmin) para modificar como se desplieghan los valores de cada campo

app/admin.py



* Habilitar campos fecha_creacion y decha_modificacion y que sean de solo lectura al visualizar un determinado libro

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')


* Visualizar el titulo, autor y valoracion respectivamente


class BookAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'autor', 'valoracion')
  



* agregar un filtro segun la valoracion, y la fecha de modificacion

  list_filter = ('autor', 'valoracion', 'fecha_modificacion')


* Registrar


admin.site.register(Book, BookAdmin)