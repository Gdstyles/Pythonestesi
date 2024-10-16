###### creacion de un proyecto django

1.- crear carpeta



2.- crear entorno local en carpeta

    PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django> python -m venv .venv

3.- activar entorno

    PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django> .venv\Scripts\activate.ps1

4.- Instalar Django en el entorno.

    (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django> pip install django
    Collecting django
    Using cached Django-5.1.2-py3-none-any.whl.metadata (4.2 kB)
    Collecting asgiref<4,>=3.8.1 (from django)
    Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
    Collecting sqlparse>=0.3.1 (from django)
    Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
    Collecting tzdata (from django)
    Using cached tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)
    Using cached Django-5.1.2-py3-none-any.whl (8.3 MB)
    Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
    Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
    Using cached tzdata-2024.2-py2.py3-none-any.whl (346 kB)
    Installing collected packages: tzdata, sqlparse, asgiref, django
    Successfully installed asgiref-3.8.1 django-5.1.2 sqlparse-0.5.1 tzdata-2024.2

5.- Inicializar proyecto django dentro de la carpeta creada en el primer paso

    (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django> django-admin startproject site_django

6.- Ingresar a la carpeta del proyecto creado con django-admin startproject

    cd nombre_proyecto
    django-admin startapp book

    (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django> cd site_django
    (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django\site_django> django-admin startapp book

7.- Modificar el archivo settings.py para registrar el aplicativo o app creada en el punto 6, con django-admin startapp

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'book.apps.BookConfig',  # agregando la app book
    ]

8.- Ejecutar migraciones

    python manage.py migrate
    python .\manage.py migrate

    (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django\site_django> python manage.py migrate
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


9.- Ejecutar el servidor de desarrollo de Django. 
    dirigirnos a donde se encuentra el archivo manage.py dentro del proyecto

    python manage.py runserver
    python .\manage.py runserver

    (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\evaluacion\practica_django\site_django> python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.    
    Run 'python manage.py migrate' to apply them.
    October 15, 2024 - 21:02:17
    Django version 5.1.2, using settings 'site_django.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

### para cerrar ctrl+C

10.- Con la ayuda de la terminal, describa qué función realiza cada uno de los siguientes comandos: 
    
#    makemigrations:

    Este comando crea archivos de migración basados en los cambios realizados en los modelos del proyecto Django. Las migraciones son una forma de propagar los cambios en los modelos (como la creación de nuevos campos o la eliminación de tablas) a la base de datos.

    Función:

    Detecta los cambios en los modelos y los convierte en migraciones para ser aplicados posteriormente

        python manage.py makemigrations


    
#    migrate:

    Aplica las migraciones pendientes a la base de datos. Esto asegura que la estructura de la base de datos esté sincronizada con los modelos de tu proyecto.

    Función:

    Ejecuta las migraciones creadas por makemigrations, modificando la base de datos

        python manage.py migrate


#    shell:

    Abre una consola interactiva de Python preconfigurada con el entorno de Django cargado. Desde esta consola puedes interactuar directamente con los modelos y demás componentes de Django.

    Función:

    Permite ejecutar comandos Python interactivos en el contexto de tu proyecto Django.

        python manage.py shell



#    dbshell:

    Abre la consola del motor de base de datos que estés utilizando (MySQL, PostgreSQL, SQLite, etc.). Esto te permite interactuar directamente con la base de datos, hacer consultas SQL, y administrar la base de datos.

    Función:

    Proporciona acceso directo a la base de datos de tu proyecto mediante la línea de comandos.

        python manage.py dbshell


#     showmigrations:

    Muestra una lista de todas las migraciones en el proyecto, indicando cuáles han sido aplicadas y cuáles no. Es útil para tener una visión general del estado de las migraciones.

    Función:

    Lista todas las migraciones y su estado (aplicadas o no).

        python manage.py showmigrations

#     dumpdata:

    Exporta los datos de tu base de datos en formato JSON, XML o YAML. Es útil para hacer copias de seguridad o mover datos entre entornos.

    Función:

    Extrae los datos de la base de datos en un formato serializable (JSON por defecto).

        python manage.py dumpdata


#     test:

    Ejecuta las pruebas automáticas definidas en tu proyecto. Busca archivos que comiencen con test_ en el nombre y ejecuta las pruebas definidas en ellos, generalmente utilizando unittest o pytest.

    Función:

    Corre la suite de pruebas del proyecto para verificar que todo funcione correctamente.

        python manage.py test

#    testserver:

    Inicia un servidor de desarrollo con datos de prueba cargados desde un archivo de fixtures. Es útil cuando quieres probar tu aplicación localmente con datos específicos sin afectar la base de datos principal.

    Función:

    Inicia un servidor local para realizar pruebas con datos de ejemplo cargados.

        python manage.py testserver fixture1.json fixture2.json

 #   diffsetting:

    Muestra una lista de las configuraciones que has sobrescrito en tu proyecto Django en comparación con las configuraciones predeterminadas. Es útil para depurar configuraciones personalizadas.

    Función:

    Muestra la diferencia entre las configuraciones predeterminadas y las que has modificado en tu proyecto.

        python manage.py diffsettings