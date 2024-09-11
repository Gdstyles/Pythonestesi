usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'} 
 
id_usuario = '004' 

def ver_diccionario():
    try:
        print(usuarios[id_usuario])
    except:
        KeyError
        print(f"La clave {id_usuario} no está en el diccionario. Añadiendo clave..") 
        usuarios[id_usuario] = "Ninguno"

def rev_diccionario():
    print(usuarios)    

ver_diccionario()
rev_diccionario()
