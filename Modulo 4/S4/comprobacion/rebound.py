class Libro:
    def __init__(self, autor= None, titulo= None, anio_publicacion= None):
        self.autor = autor
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion


libro_uno = Libro()
libro_dos = Libro()

libro_uno.autor = "Dan Brown"
libro_uno.titulo = "Infierno"
libro_dos.autor = "Dan Brown"
libro_dos.titulo = "El Código Da Vinci"
libro_dos.anio_publicacion = 2003       
        
print(libro_uno.__dict__)

print(libro_dos.__dict__)
     