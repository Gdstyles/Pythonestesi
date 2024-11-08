from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('titulo', 'autor', 'valoracion')
    list_filter = ('autor', 'valoracion', 'fecha_modificacion')
    
    
admin.site.register(Book, BookAdmin) # registro de los model separados por coma