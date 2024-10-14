

-- Tabla Empresa

CREATE TABLE empresa(
    rut VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(50),
    dirección VARCHAR(255),
    telefono VARCHAR(15),
    correo VARCHAR(255),
    web VARCHAR(255)
);


-- Tabla Cliente


CREATE TABLE cliente(
    rut VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(50),
    correo VARCHAR(255),
    dirección VARCHAR(255),
    telefono VARCHAR(14),
    alta BOOLEAN
);


-- Tabla TipoVehiculo


CREATE TABLE tipo_vehiculo(
    id_tipo_vehiculo SERIAL PRIMARY KEY,
    nombre VARCHAR(255)
);


-- Tabla mantencion


CREATE TABLE mantencion(
    id_mantencion SERIAL PRIMARY KEY,
    decha DATE,
    trabajos_realizados VARCHAR(255),
    folio INT    -- ALTER TABLE mantencion ADD CONSTRAINT fk_mantencion_folio FOREIGN KEY(folio) REFERENCES venta(folio);
);


-- Tabla ventas


CREATE TABLE venta(
    folio SERIAL PRIMARY KEY,
    fecha DATE,
    monto INT,
    rut_cliente VARCHAR(15), -- ALTER TABLE venta ADD CONSTRAINT fk_venta_rut_cliente FOREIGN KEY(rut_cliente) REFERENCES cliente(rut_cliente);
    id_vehiculo INT          -- ALTER TABLE venta ADD CONSTRAINT fk_venta_id_vehiculo FOREIGN KEY(id_vehiculo) REFERENCES vehiculo(id_marca);
);


-- Tabla vehiculo


CREATE TABLE vehiculo(
    id_vehiculo SERIAL PRIMARY KEY,
    patente VARCHAR(10),
    marca VARCHAR(50),
    modelo VARCHAR(50),
    color VARCHAR(50),
    precio INT,
    frecuencia_mantencion INT,
    id_marca INT,                     -- ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_marca FOREIGN KEY(id_marca) REFERENCES marca(id_marca);
    id_tipo_vehiculo INT              -- ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_tipo_vehiculo FOREIGN KEY(id_tipo_vehiculo) REFERENCES tipo_vehiculo(id_tipo_vehiculo);
);


-- Tabla marca

CREATE TABLE marca(
    id_marca SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Alterar las tablas luego de la creacion para agregar las claves foraneas

ALTER TABLE mantencion ADD CONSTRAINT fk_mantencion_folio FOREIGN KEY (folio) REFERENCES venta(folio);

ALTER TABLE venta ADD CONSTRAINT fk_venta_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES cliente(rut);
ALTER TABLE venta ADD CONSTRAINT fk_venta_id_vehiculo FOREIGN KEY (id_vehiculo) REFERENCES vehiculo(id_vehiculo);

ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_marca FOREIGN KEY (id_marca) REFERENCES marca(id_marca);
ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_tipo_vehiculo FOREIGN KEY (id_tipo_vehiculo) REFERENCES tipo_vehiculo(id_tipo_vehiculo);


