PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling> ls


    Directorio: C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        05-11-2024     21:35                book_


PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling> cd book_                                                                                                                                             
PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_> cd site_django                                                                                                                                 
PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django> ls


    Directorio: C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        05-11-2024     20:25                book
d-----        05-11-2024     20:25                site_django
-a----        05-11-2024     20:02         139264 db.sqlite3
-a----        17-10-2024     19:55            689 manage.py


PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django> pip list
Package          Version
---------------- -------
asgiref          3.8.1
Django           5.1.2
multipledispatch 1.0.0
pip              24.2
sqlparse         0.5.1
tzdata           2024.2
PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django> pip list > requirements.txt
PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django> ls


    Directorio: C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        05-11-2024     20:25                book
d-----        05-11-2024     20:25                site_django
-a----        05-11-2024     20:02         139264 db.sqlite3
-a----        17-10-2024     19:55            689 manage.py
-a----        06-11-2024     20:17            394 requirements.txt


PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django> pip freeze > requirements.txt
PS C:\Users\gonza\OneDrive\Escritorio\Python\Modulo 6\S11\Reboundy Drilling\book_\site_django> 