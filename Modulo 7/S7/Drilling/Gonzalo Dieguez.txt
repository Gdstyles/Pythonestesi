
* Conectar a la shell de python a la altura de manage.py
- python manage.py shell

1. Obtenga todos los registros de fábricas y productos. 

- from producto.models import Producto, Fabrica

- producto = Producto.objects.all().values() # SELECT * FROM producto_producto;
- producto
<QuerySet [{'id': 12, 'nombre': 'Downy Aroma Floral', 'precio': 3500, 'descripcion': 'Ambientador de aroma floral', 'fecha_vencimiento': datetime.date(2025, 5, 22), 'fabrica_id': 1}, {'id': 13, 'nombre': 'Crest Premium', 'precio': 2500, 'descripcion': 'Crema dental', 'fecha_vencimiento': datetime.date(2024, 11, 1), 'fabrica_id': 1}, {'id': 14, 'nombre': 'Ariel Suavizante', 'precio': 1500, 'descripcion': 'Suavizante para la ropa', 'fecha_vencimiento': datetime.date(2027, 6, 11), 'fabrica_id': 1}, {'id': 15, 'nombre': 'Colgate 360', 'precio': 1850, 'descripcion': 'Crema Dental', 'fecha_vencimiento': datetime.date(2024, 2, 29), 'fabrica_id': 2}, {'id': 16, 'nombre': 'Speed Stick 27/7', 'precio': 4500, 'descripcion': 'Desodorante para caballeros', 'fecha_vencimiento': datetime.date(2023, 4, 14), 'fabrica_id': 2}, {'id': 17, 'nombre': 'Protex Aloe', 'precio': 1250, 'descripcion': 'Jabon de Baño', 'fecha_vencimiento': datetime.date(2023, 10, 27), 'fabrica_id': 2}]>

- fabrica = Fabrica.objects.all().values() # SELECT * FROM producto_fabrica;
- fabrica
<QuerySet [{'id': 2, 'nombre': 'COLGATE', 'pais': 'EEUU'}, {'id': 1, 'nombre': 'P&G', 'pais': 'EEUU'}]>

2. Obtenga los campos de nombre, precio, y fecha de vencimiento de los productos. Demuestre también cuál es la consulta SQL que se genera del ORM. 

- consulta1 = producto.values_list('nombre', 'precio', 'fecha_vencimiento')
- consulta1
<QuerySet [('Downy Aroma Floral', 3500, datetime.date(2025, 5, 22)), ('Crest Premium', 2500, datetime.date(2024, 11, 1)), ('Ariel Suavizante', 1500, datetime.date(2027, 6, 11)), ('Colgate 360', 1850, datetime.date(2024, 2, 29)), ('Speed Stick 27/7', 4500, datetime.date(2023, 4, 14)), ('Protex Aloe', 1250, datetime.date(2023, 10, 27))]>

- str(consulta1.query)
'SELECT "producto_producto"."nombre", "producto_producto"."precio", "producto_producto"."fecha_vencimiento" FROM "producto_producto"'


3. Obtenga los productos donde el precio sea menor o igual a 2500, mostrando solo los campos de nombre y precio, respectivamente. Demuestra también cuál es la consulta SQL que se genera del ORM. 

- consulta2 = producto.filter(precio__lte=2500).values('nombre', 'precio')

<QuerySet [{'nombre': 'Crest Premium', 'precio': 2500}, {'nombre': 'Ariel Suavizante', 'precio': 1500}, {'nombre': 'Colgate 360', 'precio': 1850}, {'nombre': 'Protex Aloe', 'precio': 1250}]>

- str(consulta2.query)

'SELECT "producto_producto"."nombre", "producto_producto"."precio" FROM "producto_producto" WHERE "producto_producto"."precio" <= 2500'

# consulta3 = producto.filter(precio__gte=2500).values('nombre', 'precio') ==> si fuera mayor o igual

4. Consulte los productos que se vencen antes del año 2024, e imprima el nombre, precio, f_vencimiento, y fabricante. Demuestre también cuál es la consulta SQL que se genera del ORM. 

- consulta4 = producto.filter(fecha_vencimiento__lte='2023-12-1').values('nombre', 'precio', 'fecha_vencimiento', 'fabrica')
consulta4

<QuerySet [{'nombre': 'Speed Stick 27/7', 'precio': 4500, 'fecha_vencimiento': datetime.date(2023, 4, 14), 'fabrica': 2}, {'nombre': 'Protex Aloe', 'precio': 1250, 'fecha_vencimiento': datetime.date(2023, 10, 27), 'fabrica': 2}]>

- str(consulta4.query)
'SELECT "producto_producto"."nombre", "producto_producto"."precio", "producto_producto"."fecha_vencimiento", "producto_producto"."fabrica_id" FROM "producto_producto" WHERE "producto_producto"."fecha_vencimiento" <= 2023-12-01'