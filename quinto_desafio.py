def encripto(cadena, n=1):
    """ Esta funcion retorna a partir de un string, su equivalente
        en cifrado cesar, segun su variacion de desplazamiento expresado en n
    """
    c = list(map(lambda x: chr(ord(x) + n), cadena))
    c = ''.join(c)
    return c


cadena_encriptada = encripto('hola como estas')
print(cadena_encriptada)
