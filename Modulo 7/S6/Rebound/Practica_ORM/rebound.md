EJERCICIO:
 1. Partiendo del modelo creado en el CUE anterior, relacionado al modelo de fábricas y productos, liste todas las migraciones realizadas e indique por qué se crea el archivo 0001_inicial.py. 
 

(.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 7\S6\Rebound\Practica_ORM\config> python manage.py showmigrations
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
producto
 [X] 0001_initial
 [X] 0002_fabrica_producto_fabrica
sessions
 [X] 0001_initial

> el archivo 0001_inicial.py registra el modelo que se utiliza inicialmente en la base de datos, generando un modelo que se creó en la base de datos.


 2. ¿Cuál es el comando que permite observar el SQL antes de aplicar una determinada migración, por ejemplo la 0001_inicial.py? 
 
 (.venv) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 7\S6\Rebound\Practica_ORM\config> python manage.py sqlmigrate producto 0001           
BEGIN;
--
-- Create model Producto
--
CREATE TABLE "producto_producto" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "nombre" text NOT NULL, "precio" integer NOT NULL, "descripcion" text NOT NULL);
COMMIT;


 3. ¿Cuáles son las claves primarias de los modelos? 


name='Producto',
('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

name='Fabrica',
('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),