''' EJERCICIO: 
Partiendo del modelo creado en ejercicios anteriores (Fabrica y Producto), realizar las siguientes consultas: 

1. Obtener todas las fábricas y productos por medio de una consulta SQL, haciendo uso del método raw(). 
Para los productos imprima la fábrica correspondiente.  ''' 

from producto.models import Producto, Fabrica

fabrica = Fabrica.objects.raw('SELECT * FROM producto_fabrica')

producto = Producto.objects.raw('SELECT * FROM producto_producto')


for f in fabrica:
    print(f.nombre)

for p in producto:
    print(f'{p.nombre} es fabricado por {p.fabrica}')



(InteractiveConsole)
>>> from producto.models import Producto, Fabrica
>>> fabrica = Fabrica.objects.raw('SELECT * FROM producto_fabrica')
>>> producto = Producto.objects.raw('SELECT * FROM producto_producto')
>>> for f in fabrica:
...     print(f.nombre)
... 
COLGATE
P&G
>>> for p in producto:
...     print(f'{p.nombre} es fabricado por {p.fabrica}')
...
Downy Aroma Floral es fabricado por Fabrica object (1)
Crest Premium es fabricado por Fabrica object (1)
Ariel Suavizante es fabricado por Fabrica object (1)
Colgate 360 es fabricado por Fabrica object (2)
Speed Stick 27/7 es fabricado por Fabrica object (2)
Protex Aloe es fabricado por Fabrica object (2)



2. Realizar una consulta pasando los parámetros por raw que busque el producto “Protex Aloe”, y devuelva quien lo fabrica. 

producto = 'Protex Aloe'

producto = Producto.objects.raw('SELECT * FROM producto_producto WHERE nombre = %s', [producto])

>>> producto = 'Protex Aloe'
>>> producto = Producto.objects.raw('SELECT * FROM producto_fabrica WHERE nombre = %s', [producto])
>>> producto
<RawQuerySet: SELECT * FROM producto_fabrica WHERE nombre = Protex Aloe>
>>> producto = 'Protex Aloe'
>>> producto = Producto.objects.raw('SELECT * FROM producto_producto WHERE nombre = %s', [producto])
>>> for p in producto:
...     print(f'{p.nombre} es fabricado por {p.fabrica}')


Protex Aloe es fabricado por Fabrica object (2)