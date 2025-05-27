import json
import os

ruta = os.path.expanduser("~/.config/uaspl/config.json") # Esto permite que Python entienda que ~ es la carpeta del usuario, así el programa no tiene que andar adivinando como se llama la carpeta del usuario
if os.path.exists(ruta): # Verifico que la ruta exista porque si no existe y el programa asume que está, da error y adiós inicio del programa
    with open(ruta, "r", encoding="utf-8") as archivo:
        idioma = json.load(archivo)

    if idioma["idioma"] == "english":
        from idiomas.english import palabras
            
    else:
        from idiomas.espanol import palabras

else:
    from idiomas.espanol import palabras
    print("""No se cargó ningún idioma, se usará español por defecto, para cambiar el idioma o dejar de ver este mensaje, cree el archivo config.json de acuerdo a las instrucciones dadas en https://wiki.archlinux.org/title/User:KevinCrrl/Uaspl-bin_(Espa%C3%B1ol)
No language loaded, Spanish will be used by default, to change the language or stop seeing this message, create the config.json file according to the instructions given at https://wiki.archlinux.org/title/User:KevinCrrl/Uaspl-bin_(Espa%C3%B1ol)""")