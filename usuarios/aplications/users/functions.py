""" Funciones extra de la aplicacion users """

import random
import string

def codec_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))