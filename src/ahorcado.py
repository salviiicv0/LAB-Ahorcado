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

def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return(False)
        else:
            return(True)
        
def ejecutar_turno(palabra_secreta, letras_probadas):
    palabra_enmascarada = enmascarar_palabra(palabra_secreta, letras_probadas)
    print("Este es el estado actual de la palabra secreta: ", palabra_enmascarada)
    l_probada = pedir_letra(letras_probadas)
    is_letra = comprobar_letra(palabra_secreta, l_probada)
    letras_probadas.add(l_probada)
    return is_letra

def jugar(max_intentos, palabras):
    print("Bienvenido al juego del ahorcado.")
    palabra_secreta = elegir_palabra(palabras)
    letras_probadas = set(); intentos = 0
    while intentos < max_intentos:
        is_acierto = ejecutar_turno(palabra_secreta, letras_probadas)
        if is_acierto:
            palabra_completa = comprobar_palabra_completa(palabra_secreta, letras_probadas)
            if palabra_completa:
                break
        else:
            intentos += 1
    print("Fin del juego!")
    if intentos <= max_intentos:
        print("Enhorabuena, has conseguido descubrir la palabra secreta!")
        print(f"""
              Número de intentos: {intentos}
              Número de intentos máximos: {max_intentos}
              """)
        
#Iniciar el juego
if __name__ == "__main__":
    palabras = cargar_palabras("data\palabras_ahorcado.txt")
    jugar(250, palabras)


