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

import customtkinter as ctk
from uaspl.config.parser import config
from uaspl.herramientas.funciones import * # Esto también importa la función traductor()
from uaspl.herramientas.ctkui import ui
import sys
import os

# Verificar no-root antes que nada
if os.getuid() == 0:
    print(traductor("No use UASPL como root."))
    sys.exit(1)

# Definir tema para todas las interfaces desde el inicio
ctk.set_appearance_mode(config["tema"])

args = {
    traductor("red-estado"): firewall,
    "anti-rk": rkescaneo,
    "gui": ui,
    traductor("ayuda"): ayuda,
    "version": version,
    traductor("full-iniciar-servicios"): Servicio("enable --now").systemctl,
    traductor("full-detener-servicios"): Servicio("disable --now").systemctl,
    traductor("estado-servicios"): Servicio("status").systemctl,
    traductor("detener-servicios"): Servicio("stop").systemctl,
    traductor("iniciar-servicios"): Servicio("start").systemctl,
    traductor("activar-servicios"): Servicio("enable").systemctl,
    traductor("desactivar-servicios"): Servicio("disable").systemctl,
}

def main():
    try:
        for arg, funcion in args.items():
            if sys.argv[1] == arg:
                funcion()
                break # break para que cuando encuentre la función que no itere más y termine dando comportamientos raros en la consola.
    
        else: # else aquí y no dentro del bucle for porque sino al no encontrar el argumento el aviso del print termina saliendo más de una vez.
            print(traductor("Argumento no encontrado, use el argumento 'ayuda' para ver los comandos disponibles."))
    except IndexError: # Aquí controlo el error de que se ejecute el programa sin ingresar ni un solo argumento, se debe pasar un argumento siempre.
        print(traductor("No se ingresó ningún argumento."))
    except KeyboardInterrupt as e:
        print(e)

if __name__ == "__main__":
    main()
