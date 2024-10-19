1. Crear un nuevo entorno virtual llamado: django_development y django_development_1. 

PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling> mkdir practica


    Directorio: C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        16-10-2024     21:27                practica


PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling> cd practica
PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> python -m venv django_development
PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> python -m venv django_development_1 


2. Activar y desactivar los entornos virtuales. 

PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> .\django_development\Scripts\activate.ps1   
(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> deactivate

PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> .\django_development_1\Scripts\activate.ps1
(django_development_1) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> deactivate

3. Eliminar el entorno virtual django_development_1. 

PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> rm django_development_1                                           

Confirmar
El elemento situado en C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica\django_development_1 tiene elementos secundarios y no se especificó el parámetro Recurse. Si continúa, se quitarán todos los 
secundarios junto con el elemento. ¿Está seguro de que desea continuar?
[S] Sí  [O] Sí a todo  [N] No  [T] No a todo  [U] Suspender  [?] Ayuda (el valor predeterminado es "S"): s

4. En el entorno virtual django_development, instala las siguientes dependencias: Django versión 4.0.5. 

(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> pip install django==4.0.5
Collecting django==4.0.5
  Downloading Django-4.0.5-py3-none-any.whl.metadata (4.0 kB)
Collecting asgiref<4,>=3.4.1 (from django==4.0.5)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.2.2 (from django==4.0.5)
  Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from django==4.0.5)
  Using cached tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading Django-4.0.5-py3-none-any.whl (8.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 13.5 MB/s eta 0:00:00
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
Using cached tzdata-2024.2-py2.py3-none-any.whl (346 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.8.1 django-4.0.5 sqlparse-0.5.1 tzdata-2024.2


5. Ejecutar el proyecto creado en el CUE02 site_django en el servidor web de desarrollo de Django. 

(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> django-admin startproject project

(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> django-admin startproject project
(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica> cd project
(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica\project> django-admin startapp app

(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica\project> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

(django_development) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S3\drilling\practica\project> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 16, 2024 - 21:42:11
Django version 4.0.5, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


