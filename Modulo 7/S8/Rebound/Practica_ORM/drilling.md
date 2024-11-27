from producto.models import Producto, Fabrica


1. Obtenga los campos de nombre, precio, y fecha de vencimiento de los productos. 

consulta1 = Producto.objects.raw('SELECT id, nombre, precio, fecha_vencimiento FROM producto_producto')

print('\n'.join(str(i)) for i in consulta1)

for p in consulta1:
    print(f'El producto: {p.nombre} se vence en {p.fecha_vencimiento}, con un precio de: {p.precio}')


>>> consulta1 = Producto.objects.raw('SELECT id, nombre, precio, fecha_vencimiento FROM producto_producto')
>>> for p in consulta1:
...     print(f'El producto: {p.nombre} se vence en {p.fecha_vencimiento}, con un precio de: {p.precio}')
...
El producto: Downy Aroma Floral se vence en 2025-05-22, con un precio de: 3500
El producto: Crest Premium se vence en 2024-11-01, con un precio de: 2500
El producto: Ariel Suavizante se vence en 2027-06-11, con un precio de: 1500
El producto: Colgate 360 se vence en 2024-02-29, con un precio de: 1850
El producto: Speed Stick 27/7 se vence en 2023-04-14, con un precio de: 4500
El producto: Protex Aloe se vence en 2023-10-27, con un precio de: 1250


2. Obtenga los productos donde el precio sea menor o igual a 2500, y muestre solo los campos de nombre y precio, respectivamente.  

consulta2 = Producto.objects.raw('SELECT id, nombre, precio FROM producto_producto WHERE precio <= %s', [2500])

for p in consulta2:
    print(f'El producto: {p.nombre} tiene un precio de: {p.precio}')


>>> consulta2 = Producto.objects.raw('SELECT id, nombre, precio FROM producto_producto WHERE precio <= %s', [2500])
>>> for p in consulta2:
...     print(f'El producto: {p.nombre} tiene un precio de: {p.precio}')
...
El producto: Crest Premium tiene un precio de: 2500
El producto: Ariel Suavizante tiene un precio de: 1500
El producto: Colgate 360 tiene un precio de: 1850
El producto: Protex Aloe tiene un precio de: 1250


3. Modifique haciendo uso de SQL personalizado y cursores, la fábrica con nombre P&G en el país que se encuentra asignada a EEUU, o a Canadá. 
 - https://docs.djangoproject.com/en/5.1/topics/db/sql/#:~:text=The%20object%20django.db.connection%20represents%20the%20default%20database%20connection.,cursor.fetchone%28%29%20or%20cursor.fetchall%28%29%20to%20return%20the%20resulting%20rows.

from django.db import connection


    with connection.cursor() as cursor:
        cursor.execute("UPDATE producto_fabrica SET pais = %s WHERE nombre = %s", ['EEUU', 'P&G'])
        cursor.execute("UPDATE producto_fabrica SET pais = %s WHERE nombre = %s", ['Canada', 'Colgate'])
        cursor.execute('SELECT * FROM producto_fabrica')
        row = cursor.fetchone()



>>> with connection.cursor() as cursor:
...         cursor.execute("UPDATE producto_fabrica SET pais = %s WHERE nombre = %s", ['EEUU', 'P&G'])
...         cursor.execute("UPDATE producto_fabrica SET pais = %s WHERE nombre = %s", ['Canada', 'Colgate'])
...         cursor.execute('SELECT * FROM producto_fabrica')
...         row = cursor.fetchone()
...
>>> print(row)
(2, 'COLGATE', 'EEUU')