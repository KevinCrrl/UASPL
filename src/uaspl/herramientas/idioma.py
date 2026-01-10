# KevinCrrl; LICENSE: GPL-3-or-later

from uaspl.idiomas.diccionario import frases
from uaspl.config.parser import config

idioma = "espanol"

if config["idioma"] == "english":
    idioma = "english"

def traductor(frase):
    if idioma == "english":
        return frases[frase]
    return frase
