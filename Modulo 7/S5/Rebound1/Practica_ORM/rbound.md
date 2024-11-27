 > La La fábrica de productos puede producir uno o más productos. ● El producto solo puede pertenecer a un fabricante. 

 * MODELO de la fabrica:

  MODEL:
  ---

  class Fabrica():
    nombre = models.Charfield(max_length=100)

  class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)
    # fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)


* Realizar migraciones
´´´python manage.py makemigrations´´´
''' python manage.py migrate'''