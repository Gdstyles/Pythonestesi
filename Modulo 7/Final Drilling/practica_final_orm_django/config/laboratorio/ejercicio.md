Por medio de la consola interpretador de python (shell), realice las siguientes consultas: 1.  Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos.

'python manage.py shell'

'from laboratorio.models import, Laboratorio, DirectorGeneral, Producto

- laboratorio = Laboratorio.objects.all()

print('\n'.join(str(i.nombre) for i in laboratorio))
Laboratorio1
Laboratorio2
Laboratorio3

- director_general = DirectorGeneral.objects.all()

print('\n'.join(str(i.nombre) for i in director_general))
Director General 1
Director General 2
Director General 3

- producto = Producto.objects.all()

print('\n'.join(str(i.nombre) for i in producto))
Producto 1
Producto 2
Producto 3

2. Obtenga el laboratorio del Producto cuyo nombre es ‘Producto 1’.

query =  '''

    SELECT p.id, p.nombre as nombre_producto, l.id, l.nombre AS nombre_laboratorio FROM laboratorio_producto p INNER JOIN laboratorio_laboratorio l ON p.laboratorio_id = l.id WHERE p.nombre = %s;

    '''

consulta1 = Producto.objects.raw(query, ['Producto 1'])

print('\n'.join(str(i.nombre_laboratorio) for i in consulta1))

Laboratorio1

consulta2 = Producto.objects.filter(nombre='Producto 1').select_related('laboratorio').values('nombre', 'laboratorio')

print('\n'.join(str(i['laboratorio']) for i in consulta2))

1

3. Ordene todos los productos por nombre, y que muestre los valores de nombre y laboratorio.

consulta4 = Producto.objects.order_by('nombre').values('nombre', 'laboratorio')

Producto.objects.all()order_by('nombre').values('nombre', 'laboratorio')

<QuerySet [{'nombre': 'Producto 1', 'laboratorio': 1}, {'nombre': 'Producto 2', 'laboratorio': 2}, {'nombre': 'Producto 3', 'laboratorio': 3}]>

4. Realice una consulta que imprima por pantalla los laboratorios de todos los productos.

consulta6 = Producto.objects.all().select_related('laboratorio').values('nombre', 'laboratorio')

<QuerySet [{'nombre': 'Producto 1', 'laboratorio': 1}, {'nombre': 'Producto 2', 'laboratorio': 2}, {'nombre': 'Producto 3', 'laboratorio': 3}]>

Realice pruebas unitarias al modelo Laboratorio, donde se verifique:

- Que los datos en nuestra base de datos simulada coincidan con los que se crearon inicialmente en setUpTestData para un laboratorio dado.
- La URL para confirmar que devuelve una respuesta HTTP 200 para laboratorio.-
- Y finalmente, que la página usando reverse para llamar al nombre de la URL, busca una respuesta HTTP 200, verifica que se use la plantilla correcta, y confirma que el contenido HTML coincide con lo esperado.



(.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 7\Final Drilling\practica_final_orm_django\config> python manage.py test
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
---

Ran 3 tests in 0.036s

OK
Destroying test database for alias 'default'...
