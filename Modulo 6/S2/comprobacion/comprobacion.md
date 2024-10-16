-- Version -- 

PS C:\Users\gonza\OneDrive\Escritorio\Python> python --version
Python 3.12.5


-- PIP --

PS C:\Users\gonza\OneDrive\Escritorio\Python> PIP list
Package          Version
---------------- -------
multipledispatch 1.0.0
pip              24.2


-- ejecutar instalador de paqqyetes --

PS C:\Users\gonza\OneDrive\Escritorio\Python> pip --version
pip 24.2 from C:\Users\gonza\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)

-- crear un entorno virtual

PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\comprobacion> python -m venv proyecto_django

-- mostrar paquetes --

(proyecto_django) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\comprobacion> pip list
Package Version
------- -------
pip     24.2


-- instalar django --

(proyecto_django) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\comprobacion> pip install Django
Collecting Django
  Downloading Django-5.1.2-py3-none-any.whl.metadata (4.2 kB)
Collecting asgiref<4,>=3.8.1 (from Django)
  Downloading asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django)
  Downloading sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from Django)
  Downloading tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading Django-5.1.2-py3-none-any.whl (8.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 16.0 MB/s eta 0:00:00
Downloading asgiref-3.8.1-py3-none-any.whl (23 kB)
Downloading sqlparse-0.5.1-py3-none-any.whl (44 kB)
Downloading tzdata-2024.2-py2.py3-none-any.whl (346 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-5.1.2 asgiref-3.8.1 sqlparse-0.5.1 tzdata-2024.2


-- verificar que version de Django se instalo -- 

(proyecto_django) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\comprobacion> pip list
Package  Version
-------- -------
asgiref  3.8.1
Django   5.1.2
pip      24.2
sqlparse 0.5.1
tzdata   2024.2

-- mostrar comando de ayuda PIP

(proyecto_django) PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S2\comprobacion> pip help