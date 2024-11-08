* verificar la instalacion de auth y session en settings.py que se encuentra dentro del proyecto

URL: crear url para captar petición o request para el registro de usuarios
- app/urls.py

* VIEWS: crear la vista para el registro de usuarios 
- app/views.py
    * importar UserCreationForm 
    * from django.contrib.auth.forms import UserCreationForm

* crear funcion de registro de usuario

def registro()


* TEMPLATES: crear los templates para el registro de usuarios
    Instalar paquete django-crispy-forms para renderizar los formularios

https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html

    - 'pip install django-crispy-forms'

    instalar paquete para que django-crispy-forms renderice los formularios usando bootstrap
    - 'pip install crispy-bootstrap5'

* crear el template para registro de usuarios 
  templates/registro.html

registrar las aplicaciones o paquetes instalados en settings.py
proyecto/settings.py
