Server [localhost]: localhost
Database [postgres]: postgres
Port [5432]: 5432
Username [postgres]: postgres
Contraseña para usuario postgres:

psql (16.4)
ADVERTENCIA: El código de página de la consola (850) difiere del código
            de página de Windows (1252).
            Los caracteres de 8 bits pueden funcionar incorrectamente.
            Vea la página de referencia de psql «Notes for Windows users»
            para obtener más detalles.
Digite «help» para obtener ayuda.

postgres=# \dt
No se encontró ninguna relación.
postgres=# \du
                               Lista de roles
 Nombre de rol |                         Atributos
---------------+------------------------------------------------------------
 postgres      | Superusuario, Crear rol, Crear BD, Replicaci¾n, Ignora RLS


postgres=# \c postgres
Ahora está conectado a la base de datos «postgres» con el usuario «postgres».
postgres=# \du
                               Lista de roles
 Nombre de rol |                         Atributos
---------------+------------------------------------------------------------
 postgres      | Superusuario, Crear rol, Crear BD, Replicaci¾n, Ignora RLS


postgres=# CREATE database
postgres-# CREATE database database_test
postgres-# CREATE database database_test;
ERROR:  error de sintaxis en o cerca de «CREATE»
LÍNEA 2: CREATE database database_test
         ^
postgres=# create database database_test;
CREATE DATABASE
postgres=# create user test with password '1234';
CREATE ROLE
postgres=# \l
                                                                     Listado de base de datos
    Nombre     |  Due±o   | Codificaci¾n | Proveedor de locale |      Collate       |       Ctype        | configuraci¾n ICU | Reglas ICU: |      Privilegios
---------------+----------+--------------+---------------------+--------------------+--------------------+-------------------+-------------+-----------------------
 database_test | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             |
 postgres      | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             |
 template0     | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             | =c/postgres          +
               |          |              |                     |                    |                    |
     |             | postgres=CTc/postgres
 template1     | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             | =c/postgres          +
               |          |              |                     |                    |                    |
     |             | postgres=CTc/postgres
(4 filas)


postgres=# \c database_test;
Ahora está conectado a la base de datos «database_test» con el usuario «postgres».
database_test=#