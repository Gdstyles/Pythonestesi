

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

-- 1. Listar los clientes sin arriendos por medio de una subconsulta. 

SELECT c.rut, c.nombre, c.correo, c.direccion, c.celular FROM cliente c WHERE c.rut NOT IN (SELECT a.cliente_rut FROM arriendo a);



-- 2 Listar todos los arriendos con las siguientes columnas: Folio, Fecha, Dias, ValorDia, NombreCliente, RutCliente.  

SELECT a.folio, a.fecha, a.dias, a.valor_dia, c.nombre, c.rut FROM arriendo a INNER JOIN cliente c ON a.cliente_rut = c.rut;


-- 3 

SELECT cliente_rut, dias
CASE 
    WHEN dias BETWEEN 0 AND 1 THEN 'Bajo'
    WHEN dias BETWEEN 1 AND 3 THEN 'Medio'
    WHEN dias > 3 THEN 'Alto'
    ELSE 'No califica'
END AS Clasificacion
FROM arriendo;



-- 4. Por medio de una subconsulta, listar los clientes con el nombre de la herramienta más arrendada. 




SELECT 
    c.rut, c.nombre, 
    (SELECT h.nombre 
     FROM herramienta h 
     WHERE h.id_herramienta = (
         SELECT a.herramienta_id_herramienta 
         FROM arriendo a 
         GROUP BY a.herramienta_id_herramienta 
         ORDER BY COUNT(*) DESC 
         LIMIT 1)
    ) AS herr_mas_arrendada
FROM 
    cliente c
WHERE 
    c.rut IN (SELECT a.cliente_rut 
              FROM arriendo a 
              WHERE a.herramienta_id_herramienta = (
                  SELECT a.herramienta_id_herramienta 
                  FROM arriendo a 
                  GROUP BY a.herramienta_id_herramienta 
                  ORDER BY COUNT(*) DESC 
                  LIMIT 1)
             );