-- crear trabla editoriales

CREATE TABLE editoriales(
    codigo INT PRIMARY KEY,
    nombre VARCHAR(50)
);


-- 2 crear tabla libros

CREATE TABLE libros(
    codigo INT PRIMARY KEY,
    titulo VARCHAR(100),
    codigo_editorial INT,
    CONSTRAINT fk_libros_codigo_editorial FOREIGN KEY (codigo_editorial) REFERENCES editoriales(codigo)
);

-- 3.- insertar editoriales y libros en la base de datos

INSERT INTO editoriales VALUES 
(1, 'Anaya'),
(2, 'Andina'),
(3, 'S.M.');

INSERT INTO libros VALUES 
(1, 'Don Quijote de la Mancha I', 1),
(2, 'El Principito', 2),
(3, 'El Principe', 3),
(4, 'Diplomacia', 3),
(5, 'Don Quijote de la Mancha II', 1);

-- 4. Modificar la trabla libros agregando la columna autor y precio

ALTER TABLE libros ADD COLUMN autor VARCHAR(100);
ALTER TABLE libros ADD COLUMN precio INT;


-- 5. Agregar autor y precio a los libros ya ingresados

UPDATE libros SET autor = CASE 
    WHEN codigo = 1 THEN 'Miguel de Cervantes'
    WHEN codigo = 2 THEN 'Antoine SaintExupery'
    WHEN codigo = 3 THEN 'Maquiavelo'
    WHEN codigo = 4 THEN 'Henry Kissinger'
    WHEN codigo = 5 THEN 'Miguel de Cervantes'
    END
WHERE codigo IN (1, 2, 3, 4, 5);

UPDATE libros SET precio = CASE 
    WHEN codigo = 1 THEN 150
    WHEN codigo = 2 THEN 120
    WHEN codigo = 3 THEN 180
    WHEN codigo = 4 THEN 170
    WHEN codigo = 5 THEN 140
    END
WHERE codigo IN (1, 2, 3, 4, 5);

-- 6. Insertar 2 nuevos libros

INSERT INTO libros VALUES(6, 'El señor de los anillos', 3, 200);
INSERT INTO libros VALUES(7, 'Icarito', 2, 100);

-- 7 eliminar los libros de la editorial Anaya, solo en memoria (ROLLBACK)

BEGIN;
    DELETE FROM libros WHERE codigo = 1;
ROLLBACK;

-- 8  Actualizar el nombre de la editorial Andina a Iberlibro en memoria, y actualizar el nombre de la editorial S.M. a Mountain en disco duro (SAVEPOINT / ROLLBACK TO). 

BEGIN;
    SAVEPOINT primero;
    UPDATE editoriales SET nombre = 'iberlibro' WHERE codigo = 2;
    UPDATE editoriales SET nombre = 'Mountain' WHERE codigo = 3;
    ROLLBACK TO primero;
ROLLBACK;
