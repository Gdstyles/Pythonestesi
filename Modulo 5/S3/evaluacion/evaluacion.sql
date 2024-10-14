

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