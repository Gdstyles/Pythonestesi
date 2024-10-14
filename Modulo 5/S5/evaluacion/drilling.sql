-- 1 crear base de datos peliculas

CREATE DATABASE peliculas;

-- 2 crear tablas basadas en archivos.csv

CREATE TABLE peliculas(
    id INT PRIMARY KEY,
    pelicula VARCHAR(255),
    estreno INT,
    director VARCHAR(255)
);

CREATE TABLE reparto(
    id_pelicula INT,
    actor VARCHAR(255),
    CONSTRAINT fk_reparto_peliculas FOREIGN KEY (id_pelicula) REFERENCES peliculas(id)
);

COMMIT


-- 3 cargar datos a las tablas, poblar tabla pelicuas y reparto

COPY peliculas FROM 'C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 5\S5\evaluacion\peliculas.csv' WITH CSV;
COPY reparto FROM 'C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 5\S5\evaluacion\reparto.csv' WITH CSV;

SELECT * FROM reparto;


-- 7 Listar todos los actores que aparecen en la película "Titanic", indicando el título de la película, año de estreno, director y todo el reparto. 

SELECT pelicula, estreno, director, actor FROM peliculas JOIN reparto ON peliculas.id = reparto.id_pelicula WHERE pelicula = 'Titanic';


-- con alias

SELECT p.pelicula, p.estreno, p.director, r.actor FROM peliculas AS p JOIN reparto as r ON p.id = r.id_pelicula WHERE plicula = 'Titanic';

-- 8 Listar los 10 directores más populares, indicando su nombre y cuántas películas aparecen en el top 100.

SELECT director, COUNT(*) AS cantidad_peliculas FROM peliculas GROUP BY director ORDER BY cantidad_peliculas DESC LIMIT 10;


-- 9 Indicar cuántos actores distintos hay. 

SELECT COUNT(DISTINCT actor) AS total_distintos FROM reparto;

-- 10  Indicar las películas estrenadas entre los años 1990 y 1999 (ambos incluidos), ordenadas por título de manera ascendente. 

SELECT pelicula, estreno FROM peliculas WHERE estreno BETWEEN 1990 AND 1999 ORDER BY estreno ASC;

-- 11. Listar los actores de la película más nueva. 

SELECT r.actor, p.pelicula, p.estreno FROM peliculas as p JOIN reparto AS r ON p.id = r.id_pelicula WHERE estreno = (SELECT MAX(estreno) FROM peliculas);  

-- 12. Inserte los datos de una nueva película solo en memoria, y otra película en el disco duro. 

BEGIN;
SAVEPOINT uno;
INSERT INTO peliculas VALUES(101, 'Joker: Folie à Deux', 2024, 'Todd Phillips');

SAVEPOINT dos;
INSERT INTO peliculas VALUES(102, 'Harry Potter', 2003, 'Director');

ROLLBACK TO dos; 
COMMIT;

-- 13 Actualice 5 directores utilizando ROLLBACK. 

BEGIN;
UPDATE peliculas SET director = 'Gonzalo Dieguez' WHERE id = 1;
UPDATE peliculas SET director = 'Catalina Arce' WHERE id = 2;
UPDATE peliculas SET director = 'Jaime Valdes' WHERE id = 3;
UPDATE peliculas SET director = 'Jorge Garces' WHERE id = 45;
UPDATE peliculas SET director = 'Hank' WHERE id = 10;
ROLLBACK;
-- 14. Inserte 3 actores a la película “Rambo” utilizando SAVEPOINT 



BEGIN;
SAVEPOINT uno;
INSERT INTO reparto VALUES
(72, 'Gonzalo'),
(72, 'Sofia'),
(72, 'Luis')
ROLLBACK TO uno;


-- 15. Elimina las películas estrenadas el año 2008 solo en memoria.

BEGIN;
ALTER TABLE reparto DROP CONSTRAINT fk_reparto_peliculas;
ALTER TABLE reparto DISABLE  TRIGGER ALL;
DELETE FROM peliculas WHERE estreno = 2008;

ALTER TABLE reparto ENABLE TRIGGER ALL;
ALTER TABLE peliculas ENABLE TRIGGER ALL;


ROLLBACK;

-- 16. Inserte 2 actores para cada película estrenada el 2001.

SELECT * FROM peliculas WHERE estreno = 2001;

13	"El Señor de los anillos: La comunidad del anillo"	2001	"Peter Jackson"
16	"Monstruos S.A."	2001	"Pete Docter"
55	"El viaje de Chihiro"	2001	"Hayao Miyazaki"
78	"Amélie"	2001	"Jean-Pierre Jeunet"
94	"Ocean's Eleven"	2001	"Steven Spielberg"
99	"Mouling Rouge"	2001	"Baz Luhrmann"

BEGIN;

INSERT INTO reparto VALUES
(13, 'Gonzalo'),
(13, 'Sofia'),
(16, 'Gonzalo'),
(16, 'Sofia'),
(55, 'Gonzalo'),
(55, 'Sofia'),
(78, 'Gonzalo'),
(78, 'Sofia'),
(94, 'Gonzalo'),
(94, 'Sofia'),
(99, 'Gonzalo'),
(99, 'Sofia')
ROLLBACK ;

-- 17. Actualice la película “King Kong” por el nombre de “Donkey Kong”, sin efectuar cambios en disco duro. 


BEGIN;
UPDATE peliculas SET pelicula = 'Donkey Kong' WHERE pelicula = 'King Kong';
ROLLBACK;