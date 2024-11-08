* Crear un campo dinámico con la finalidad de mostrar los libros según su valoración, y obtener un rating. Para ello debe aplicar el siguiente criterio:

o Si la valoración es menor que 30, es baja. 
o Si está entre 30 y 60, es media. 
o Si es mayor de 60, es alta. 


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('titulo', 'autor', 'valoracion', 'rating')
    list_filter = ('autor', 'valoracion', 'fecha_modificacion')
    
    def rating(self, obj):
        if obj.valoracion < 30:
            return 'baja'
        elif 30 <= obj.valoracion <= 60:
            return 'media'
        else:
            return 'alta'

 - no se guarda en base de datos - solo se visualiza            




* Crear usuarios mediante el sitio administrativo de Django, y asignar manualmente los permisos de development, scrum_master a los usuarios creados. 



