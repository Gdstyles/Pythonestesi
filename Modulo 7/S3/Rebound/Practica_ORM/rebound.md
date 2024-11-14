# instalar postgres
# instalar pgadmin
* crear base de datos
'CREATE DATABASE DB_PRACTICA_ORM';
* crear usuario
'CREATE USER user_db WITH PASSWORD 'user_db';

* Dar permisos al usuario
'GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO user_db;'
'GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO postgres;'



* Crear entorno virtual o usar existente
'python -m venv .venv'

* Instalar paquetes dentro del entorno
'pip install -r requirements.txt'
> django, django-bootstrap-v5, crispy-forms, crispy bootstrap, psycog2

* Crear proyecto Django

PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 7\S3\Rebound\Practica_ORM>
* 'django-admin startproject config'
'cd config'

* crear aplicacion con Django
'django-admin startapp producto'


* Configurar settings.py para la conexion a base de datos

* registrar aplicacion en settings.py

* Realizar migraciones
'python manage.py migrate'