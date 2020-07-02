""" Funciones útiles para la base de datos. """

from unidecode import unidecode

def clear_txt(txt, delallspaces=False, uni_decode=True):
    if txt:
        txt = txt.upper().strip()
        if delallspaces:
            txt = txt.replace(' ', '')
        if uni_decode:
            txt = unidecode(txt)
    return txt
