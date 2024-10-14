-- TABLA categorias                                          * PK = primary key     * FK = foreign key
-- PK categoria_id, nombre

-- Tabla productos
-- PK producto_id, nombre, precio, FK categoria_id

CREATE database S2;



CREATE table categorias(
    categoria_id SERIAL PRIMARY KEY, 
    nombre VARCHAR(50)
);

CREATE TABLE productos(
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    precio INT,
	categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id) -- FOREIGN KEY campo_tabla_actual REFERENCES tabla_referencia(campo_referencia)
);

INSERT INTO categorias(nombre) VALUES('ELECTRÓNICA')
INSERT INTO categorias(nombre) VALUES('ROPA')
INSERT INTO categorias(nombre) VALUES('HOGAR')

-- consultar todas las filas de la tabla
SELECT * FROM categorias;

-- consultar todas las filas de la tabla de productos

SELECT * FROM productos;

-- eliminar tabala a traves de comandos
-- debe ser de la tabla menos importante a la mas importante
DROP TABLE productos;
DROP TABLE categorias;


COMMIT; -- guardar los cambios o transacciones en la base de datos
