--------------------------------
-- conectar a la base de datos desde psql shell
-------------------------------
Server [localhost]: localhost(127.0.0.1)
Database [postgres]: postgres
Port [5432]: 5432
Username [postgres]: postgres
Contraseña para usuario postgres: <PASSWORD> al instalar la base de datos

-------------------------
-- Conectarse a la base de datos desde cualquier terminal
-------------------------

psql -U {username} -W -d {database_name}
psql -U postgres -W -d postgres

---------------------------
-- Comandos Basicos de psql
---------------------------

\l                   | listar base de datos
\q                   | salir del shell
q                    | salir
\dt                  | listar las tablas de una base de datos
\du                  | listar los usuarios de una base de datos
\c {database_name}   | conectar a una base de datos 


-- crear base de dato
CREATE DATABASE {database_name};
CREATE database {database_test};

-- borrar una base de datos desde el Shell de postgreSQL
drop database {database_name};
drop database database_test;

-- crear usuario
create user {username} with PASSWORD '{<PASSWORD>}';

-- borrar usuario
drop user {username};

-- listar la nueva base de datos creada desde el Shell

\l 

- ingresar a la base de datos desde el Shell 

\c {database_name}
