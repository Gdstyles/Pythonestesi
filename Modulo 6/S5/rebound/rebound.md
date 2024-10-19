# ir al archivo urls.py ubicado dentro de la carpeta del aplicativo (book)
book/urls.py

# agregar el path para capturar la petición /palindromo/<str:palabra>

# crear funcion en views que reciba un requesty un parametro de entrada para procesar la palabra y verificar si es palindromo o no
    
    def palindromo(request, palabra): # yo habgo yoga hoy
        es_palindromo = ''
    
        palabra_sin_espacios = palabra.replace(' ', '') # yohagoyogahoy
        if palabra_sin_espacios == palabra_sin_espacios[::-1]:
            es_palindromo = 'ES PALÍNDROMO'
        else:
            es_palindromo = 'NO ES PALINDROMO'
    
        context = {'es_palindromo': es_palindromo, 'palabra':   palabra}
    
        return render(request, 'espalindromo.html', context)

# crear espalindromo.html en la carpeta book/templates/


       <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    <!-- utilizar notacion de llaves  {{key}} para acceder a los elementos del constexto existenes en el response -->
    <h2> {{palabra}} {{es_palindromo}}</h2>




    </body>
    </html>