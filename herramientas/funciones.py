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

import pyfiglet
import subprocess as sb
from herramientas.idioma import palabras
from herramientas.statusui import status_ventana
from colorama import init, Fore

init(autoreset=True) # Esto hace que la consola no quede toda del color que seleccioné para una sola línea. 

def color(texto):
    print(Fore.GREEN + pyfiglet.figlet_format(texto, "slant"))

def ayuda():
    print(palabras["me2"])

def version():
    print(palabras["version"])

def daemon():
    color(palabras["ac"])
    servicios = ["clamav-daemon", "clamav-clamonacc", "clamav-freshclam"]
    for servicio in servicios:
        # Aquí se ejecutan comandos usando shell=True porque es comando fijo y no ingresado por el usuario, así evito que nadie ingrese comandos malintencionados.
        sb.run(f"sudo systemctl enable --now {servicio}", shell=True)

def firewall():
    output = sb.run(["pkexec", "ufw", "status", "verbose"], capture_output=True)
    status_ventana(output.stdout)

def rkescaneo():
    color(palabras["re"])
    print(palabras["ac1"])
    sb.run(["sudo", "rkhunter", "--update"])
    print(palabras["ac2"])
    sb.run(["sudo", "rkhunter", "--propupd"])
    print(palabras["an1"])
    sb.run(["sudo", "rkhunter", "--check"])
