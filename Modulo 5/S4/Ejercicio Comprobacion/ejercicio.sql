-- 1.- Crear una base de datos llamada empresa
CREATE DATABASE empresa;

-- Usar la base de datoa creada

USE empresa;
USE DATABASE empresa;

-- 2.- Crear una tabla llamada departamentos cons las siguientes columnas:

CREATE TABLE departamentos(
    id_departamento SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ubicación VARCHAR(100)
);


-- 3.- Crear tabla empleados

CREATE TABLE empleados(
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(100),
    salario DECIMAL(10,2),
    fecha_contratacion DATE,
    id_departamento INT
);

ALTER TABLE empleados ADD CONSTRAINT fk_empleados_id_departamento FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento);

-- 4.-  Modifica la tabla empleados para agregar una nueva columna llamada email

ALTER TABLE empleados ADD COLUMN email VARCHAR(100);
-- ALTER TABLE empleados DROP CLUMN email;   --- borrar

-- 5.- Cambiar nombre de empleados a trabajadores

-- modificar columna existente para armar su tipo de dato
-- ALTER TABLE empleados ALTER COLUMN email TYPE VARCHAR(200);

ALTER TABLE empleados RENAME TO trabajadores;

-- 6.- elimina la tabla departamentos
DROP TABLE trabajadores;
DROP TABLE departamentos;

