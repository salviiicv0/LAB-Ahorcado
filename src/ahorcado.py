import random

def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res
    
def elegir_palabra(palabras):
    return random.choice(palabras)

def enmascarar_palabra(palabra, letras_probadas):
    res = []
    for letras in palabra:
        if letras in letras_probadas:
            res.append(letras)
        else:
            res.append("_")
    return "".join(res)


def pedir_letra(letras_probadas):
    n_letra = input("Introduce una nueva letra: ")
    while n_letra.lower() in letras_probadas:
        n_letra = input("Ya has probado con esa letra. Intente con otra: ")
    return n_letra.lower()

def comprobar_letra(palabra_secreta, letra):
    if letra in palabra_secreta:
        print("La letra está en la palabra secreta")
        return(True)
    else:
        print("La letra no está en la palabra secreta")
        return(False)
