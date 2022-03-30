def encripto(cadena, n=1):
    """ Esta funcion retorna a partir de un string, su equivalente
        en cifrado cesar, segun su variacion de desplazamiento expresado en n
    """
    c = []
    for ch in cadena:
        c.append(ch)
    c = list(map(lambda x: ord(x) + n, c))
    c = list(map(lambda x: chr(x), c))
    c = ''.join(c)
    return c


cadena_encriptada = encripto('hola como estas')
print(cadena_encriptada)
