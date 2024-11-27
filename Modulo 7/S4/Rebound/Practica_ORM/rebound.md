* agregar campos desde la consola o shell de django al modelo Producto

'python manage.py shell'

  (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 7\S4\Rebound\Practica_ORM\config> python manage.py shell
  Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)


* Importar para acceder al producto

from producto.models import Producto

'Producto.objects.create(nombre='Crema', precio=5000, descripcion='Crema de manos')'

'Producto.objects.create(nombre='Talco', precio=3000, descripcion='talco para pies')'

'Producto.objects.create(nombre='Pomada', precio=2000, descripcion='pomada heridas')'

* Listar los productos desde la consola psql

'psql -U postgres -W -d db_practica_orm'

'SELECT * FROM producto_producto;'

* consultar los productos desde la consola de django
'python manage.py shell'

from producto.models import Producto
Producto.objects.all().values()