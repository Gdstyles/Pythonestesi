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

postgres=# create database nuevo_curso;
CREATE DATABASE
postgres=# create user gonzalo with password '1234';
CREATE ROLE
postgres=# create user sofia with password '1234';
CREATE ROLE
postgres=# create user pedro with password '1234';
CREATE ROLE
postgres=# \l
                                                                     Listado de base de datos
    Nombre     |  Due±o   | Codificaci¾n | Proveedor de locale |      Collate       |       Ctype        | configuraci¾n ICU | Reglas ICU: |      Privilegios
---------------+----------+--------------+---------------------+--------------------+--------------------+-------------------+-------------+-----------------------
 database_test | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             |
 nuevo_curso   | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             |
 postgres      | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             |
 template0     | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             | =c/postgres          +
               |          |              |                     |                    |                    |
     |             | postgres=CTc/postgres
 template1     | postgres | UTF8         | libc                | Spanish_Spain.1252 | Spanish_Spain.1252 |
     |             | =c/postgres          +
               |          |              |                     |                    |                    |                   |             | postgres=CTc/postgres
(5 filas)


postgres=#
postgres=#
postgres=# \c nuevo_curso;
Ahora está conectado a la base de datos «nuevo_curso» con el usuario «postgres».
nuevo_curso=#