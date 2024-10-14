Ordenes
IdOrden, Fecha, IdCliente, Cliente, Ciudad, Código, Artículo, Cantidad, Precio

Primera Forma Normal (1FN) establece que cada columna de un atabla debe contener un solo valor y no debe haber duplicacion de datos

Tabla Ordenes
IdOrden 
Fecha

Tabla Clientes
IdCliente
nombre_cliente
Ciudad

Tabla Artículos
codigo
nombre_articulo
Cantidad
Precio


Segunda Forma Normal (2FN) establece que una tabla debe cumplir con la 1FN y que cada columna no clave (ni pk, ni fk) debe depender completamente de la clave

Tabla Ordenes
PK idOrden
fecha

Tabla Clientes 
PK idCliente 
nombre_cliente
ciuedad

Tabla Artículos
PK codigo
nombre_articulo
Cantidad
Precio


Tercera Forma Normal (3FN) establece que una tabla debe cumplir con la 2FN y que no debe haber dependencias transitivas

Tabla Ordenes
PK idOrden
fecha
FK idCliente


Tabla Clientes 
PK idCliente 
nombre_cliente
ciudad


Tabla Artículos
PK codigo
nombre_articulo
Precio


Tabla DetalleOrdenes
PK idDetalleOrden
cantidad
FK idOrden
FK codigoArticulo


-- Desnormalización, sobrecarga de atributos en una tabla

Tabla Ordenes
idOrden
fecha
cantidad
codigo
idCliente
FK idCliente
FK codigo

Tabla Clientes 
PK idCliente 
nombre_cliente
ciudad

Tabla Artículos
PK codigo
nombre_articulo
Precio



-- Creacion de tablas

CREATE TABLE  clientes(
    cliente_id SERIAL PRIMARY KEY,
    nombre_cliente VARCHAR (100) NOT NULL,
    ciudad VARCHAR(50) NOT NULL
);

CREATE TABLE articulos(
    codigo VARCHAR(10) PRIMARY KEY,
    nombre_articulo(50) NOT NULL,
    precio DECIMAL(10,2) NOT NULL    
);

CREATE TABLE ordenes(
    orden_id INT, 
    fecha DATE NOT NULL,
    cantidad INT NOT NULL,
    codigo VARCHAR(10),  -- FK DE articulos
    cliente_id INT,      -- FK de clientes
    FOREIGN KEY (codigo_articulo) REFERENCES articulos(codigo),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

INSERT INTO clientes(nombre_cliente, ciudad) VALUES
('Martin', 'Santiago'),
('Martin', 'Santiago'),
('Martin', 'Santiago'),
('Hernan', 'Valparaíso'),
('Pedro', 'Concepcion'),
('Pedro', 'Concepcion');

INSERT INTO articulos(codigo, nombre_articulo, precio) VALUES
('3786', 'Red', 35,00),
('4011'. 'Raqueta', 65,00),
('9132', 'Paq-3', 4,75),
('5794', 'Paq-6', 5,00),
('4011', 'Raqueta', 65,00),
('3142', 'Funda', 10,00);

INSERT INTO ordenes(orden_id, fecha, cantidad, codigo_articulo, cliente_id) VALUES
('2301', '2020-02-23', 3, '3786', 1),
('2301', '2020-02-23', 3, '4011', 1),
('2301', '2020-02-23', 3, '9132', 1),
('2302', '2020-02-25', 4, '5794', 2),
('2303', '2020-02-27', 2, '4011', 3),
('2303', '2020-02-27', 2, '3141', 3);



 ====> -- ASI QUEDO


 CREATE TABLE  clientes(
    cliente_id SERIAL PRIMARY KEY,
    nombre_cliente VARCHAR (100),
    ciudad VARCHAR(50)
);

CREATE TABLE articulos(
    codigo VARCHAR(10) PRIMARY KEY,
    nombre_articulo VARCHAR(100),
    precio DECIMAL(10,2)    
);

CREATE TABLE ordenes(
    orden_id INT, 
    fecha DATE,
    cantidad INT,
    codigo_articulo VARCHAR(10),  -- FK DE articulos
    cliente_id INT,      -- FK de clientes
    FOREIGN KEY (codigo_articulo) REFERENCES articulos(codigo),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

INSERT INTO clientes(nombre_cliente, ciudad) VALUES
('Martin', 'Santiago'),
('Martin', 'Santiago'),
('Martin', 'Santiago'),
('Hernan', 'Valparaíso'),
('Pedro', 'Concepcion'),
('Pedro', 'Concepcion');

INSERT INTO articulos(codigo, nombre_articulo, precio) VALUES
('3786', 'Red', 35.00),
('4011', 'Raqueta', 65.00),
('9132', 'Paq-3', 4.75),
('5794', 'Paq-6', 5.00),
('3141', 'Funda', 10.00);

INSERT INTO ordenes(orden_id, fecha, cantidad, codigo_articulo, cliente_id) VALUES
('2301', '2020-02-23', 3, '3786', 1),
('2301', '2020-02-23', 3, '4011', 1),
('2301', '2020-02-23', 3, '9132', 1),
('2302', '2020-02-25', 4, '5794', 2),
('2303', '2020-02-27', 2, '4011', 3),
('2303', '2020-02-27', 2, '3141', 3);

select * from clientes;
select * from articulos;
select * from ordenes;