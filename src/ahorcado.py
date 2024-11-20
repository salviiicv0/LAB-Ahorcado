import random

def cargar_palabras(ruta):
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
        return res
    
def elegir_palabra(palabras):
    return random.choice(palabras)

def enmascarar_palabra(palabra, letras_probadas):
    res = []
    for letra in palabra:
        if letra in letras_probadas:
            res.append(letra)
        else:
            res.append("_")
    return res

def pedir_letra(letras_probadas):
    letra = input("Adivina una letra: ")
    while letra in letras_probadas:
        letra = input("Ya has probado con esa letra. Intenta con otra: ")
    return letra

def comprobar_letra(palabra_secreta, letra):
    if letra in palabra_secreta:
        return True
    else:
        return False
    
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    for l in letras_probadas:
        if l in palabra_secreta:
            return True
        else:
            return False
        
def ejecutar_turno(palabra_secreta, letras_probadas):
    enmascarar_palabra(palabra_secreta, letras_probadas)
    letra = pedir_letra(letras_probadas)
    if comprobar_letra(palabra_secreta, letra) == True:
        return True
    else:
        return False