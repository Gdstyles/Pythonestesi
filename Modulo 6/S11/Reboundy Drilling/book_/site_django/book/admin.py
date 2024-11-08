from django.contrib import admin
from .models import Book


# Register your models here.
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
    
    
admin.site.register(Book, BookAdmin) # registro de los model separados por coma