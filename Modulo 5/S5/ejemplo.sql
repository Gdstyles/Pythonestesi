

-- Tabla Empresa

CREATE TABLE empresa(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(120),
    direccion VARCHAR(120),
    telefono VARCHAR(15),
    correo VARCHAR(80),
    web VARCHAR(50)
);

-- Tabla Herramienta

CREATE TABLE herramienta(
    id_herramienta INT PRIMARY KEY,
    nombre VARCHAR(120),
    precio_dia INT
);

-- Tabla Cliente

CREATE TABLE cliente(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(120),
    correo VARCHAR(80),
    direccion VARCHAR(120),
    celular VARCHAR(15)
);

-- Tabla Arriendo

CREATE TABLE arriendo(
    folio INT PRIMARY KEY,
    fecha DATE,
    dias INT, 
    valor_dia INT,
    garantia VARCHAR(30),
    herramienta_id_herramienta INT,
    cliente_rut VARCHAR(10)
);

ALTER TABLE arriendo ADD CONSTRAINT fk_herramienta_id_herramienta FOREIGN KEY (herramienta_id_herramienta) REFERENCES herramienta(id_herramienta);
ALTER TABLE arriendo ADD CONSTRAINT fk_cliente_rut FOREIGN KEY (cliente_rut) REFERENCES cliente(rut);


COMMIT;

BEGIN -- inicio de transaccion 


SAVEPOINT primero; -- guarda el estado actual de la base de datos

-- 1.- Inserte los datos de una empresa
INSERT into empresa VALUES
('76000000-1','Arrienda Herramientas','Avenida Siempre Viva',22658974,'datosarriendo@herramientas.tk','herramien.tas');

SAVEPOINT segundo;

-- 2.- Inserte 5 herramientas
INSERT into herramienta VALUES
(1,'Taladro Electrico',10000),
(2,'Cierra Electrica',20000),
(3,'Pistola de Clavos',30000),
(4,'Lijadora',40000),
 (5,'Serrucho Electrico',50000);


ROLLBACK TO SAVEPOINT primero;
ROLLBACK TO SAVEPOINT segundo;



-- 3.- Inserte 3 clientes                             
INSERT into cliente VALUES
('22222222-2','Tulio Triviño','t.triviño@mail.com','Titirilquen 123',2222222222),
('33333333-3','Marcela Cubillos','m.cubillos@USS.com','Las Condes',3333333333),
('44444444-4','Humberto Suazo','chupete@mail.com','Planeta Gol',4444444444);

SAVEPOINT tercero;

-- 4. Elimina el ultimo cliente
-- DELETE FROM {tabla} WHERE {atributo_campo} = {valor};
DELETE FROM cliente WHERE rut = '44444444-4';

SAVEPOINT cuarto;


-- 5. Elimina la primera herramienta
DELETE FROM herramienta WHERE id_herramienta = 1;

SAVEPOINT quinto;

-- 6.- Inserte 2 arriendos para cada cliente
INSERT into arriendo (folio, fecha, dias, valor_dia, garantia, id_herramienta, rut_cliente) 
VALUES
(1,'12/11/22',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),
(2,'12/11/22',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),
(3,'12/11/22',1,40000,'Eficacia en 1 dia',4,'33333333-3'),
(4,'12/11/22',3,40000,'Eficacia en solo 3 dias',4,'33333333-3');

SAVEPOINT sexto;


-- 7. Modifique el correo del primer cliente
UPDATE cliente SET correo = 't.triviño@31minutos.com' WHERE rut = '22222222-2';

-- 8. Liste todas las herramientas
SELECT * FROM herramienta;

-- 9. Liste todos los arrientos del cliente '33333333-3'
SELECT * FROM arriento WHERE rut = '33333333-3';

-- 10. Liste los clientes cuyo nombre contenta la letra 'a'
SELECT * FROM clientes WHERE nombre LIKE '%a%';
SELECT * FROM clientes WHERE UPPER(nombre) LIKE '%A%';
SELECT * FROM clientes WHERE LOWER(nombre) LIKE '%a%';

-- 11 Obtenga el nombre de la segunda herramienta insertada

SELECT * FROM herramienta WHERE id_herramienta = 2;

-- 12.- Modificar los dos arriendo insertados con fecha 15/01/2020

SELECT * FROM arriendo;
UPDATE arriendo SET fecha = '15/01/2020' where folio = 1;
UPDATE arriendo SET fecha = '15/01/2020' where folio = 2;

SELECT * FROM arriendo ORDER BY folio ASC; ---- ordenar litas

-- 13.- Liste Folio, Fecha, ValorDia de los arriendos de enero del 2020

SELECT folio, fecha, valor_dia FROM arriendo WHERE EXTRACT(MONTH FROM fecha) = 01 AND EXTRACT(YEAR FROM fecha) = 2020;

-- 14.-  Recuperar clientes que empiecen con Ma

SELECT * FROM cliente;
SELECT * FROM cliente WHERE nombre LIKE '%Tu%';

-- 15 Recuperar herramientas que tienen un precio diario de 20000

SELECT * FROM herramienta;
SELECT * FROM herramienta WHERE precio_dia = 20000;

-- 16.- Contar el numero de arriendos que ha hecho cada cliente
SELECT * FROM arriendo;
SELECT rut_cliente, COUNT(*) FROM arriendo GROUP BY rut_cliente;

-- 17 Calcular valor total de ariendos para cada cliente

SELECT * FROM arriendo;
SELECT rut_cliente, SUM(dias * valor_dia) AS valor_total FROM arriendo GROUP BY rut_cliente;

