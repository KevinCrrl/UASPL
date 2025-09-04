"""
    Copyright (C) 2025 KevinCrrl

    Este programa es software libre: puedes redistribuirlo y/o modificarlo
    está bajo los términos de la Licencia Pública General GNU publicada por
    la Free Software Foundation, ya sea la versión 3 de la Licencia, o
    (a su elección) cualquier versión posterior.

    Este programa se distribuye con la esperanza de que sea útil,
    pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
    COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Véase la
    Licencia Pública General GNU para más detalles.

    Debería haber recibido una copia de la Licencia Pública General GNU
    junto con este programa. Si no, consulte <https://www.gnu.org/licenses/>."""

from xdg.BaseDirectory import xdg_config_home
import jsonschema
import json
import sys
import os

uaspl_schema = {
    "type": "object",
    "properties": {
        "idioma": {"type": "string"},
        "tema": {"type": "string"}
    },
    "required": [],
}

config_uaspl = {
    "idioma": "espanol",
    "tema": "dark"
}

config_usuario = config_uaspl # copia para realizar comparación

ruta = os.path.join(xdg_config_home, "uaspl", "config.json")
if os.path.exists(ruta): # Verifico que la ruta exista porque si no existe y el programa asume que está, da error y el programa no inicia.
    with open(ruta, "r", encoding="utf-8") as archivo:
        config_usuario = json.load(archivo)
else:
    print("""No se cargó ninguna configuración, se usará la configuración interna por defecto, para cambiar características como el idioma o dejar de ver este mensaje, cree el archivo config.json de acuerdo a las instrucciones dadas en https://KevinCrrl.github.io/KevinCrrl/documentacion/uaspl.html
No configuration loaded, default internal configuration will be used. To change features such as language or stop seeing this message, create the config.json file according to the instructions given at https://KevinCrrl.github.io/KevinCrrl/documentacion/uaspl.html""")

try:
    jsonschema.validate(instance=config_usuario, schema=uaspl_schema)
except jsonschema.ValidationError as e:
    print(f">> ERROR: La validación de configuración de UASPL encontró un error en tu archivo config.json: {e}")
    print(f">> ERROR: The UASPL configuration validation found an error in your config.json file: {e}")
    sys.exit(1)

config = {}

for configuracion, valor in config_uaspl.items():
    try:
        config[configuracion] = config_usuario[configuracion]
    except KeyError:
        config[configuracion] = valor
