* copiar preyecto anterior o crear uno con todas las configuraciones necesarias

* eliminar archivos dentro de la carpeta templates


* eliminar los path creados en urls.py de la app book 



* estructura de templates a crear
base.html -> estructura base
    include: navbar.html -> barra de navegacion

layout.html -> template a reutilizar
    extends: base.html -> estructura base

index.html -> pagina principal
    extends: layout.html -> template a reutilizar

actores o archivos a crear:
navbar.html
base.html
layout.html
index.html

* instalar en el entorno boostrap 5
pip install django-bootstrap-v5

* registrar el uso de bootstrap 5 como app en settings.py


* crear archivo navbar.html dentro de la carpeta templates

templates/navbar.html

* crear archivo base.html dentro de la carpeta templates
templates/base.html

* crear archivo layout.html que extiende de base.html dentro de la carpeta templates

templates/layout.html

* crear archivo index.html que extiende layout.html dentro de la carpeta templates

templates/index.html