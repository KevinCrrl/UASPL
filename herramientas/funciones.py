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

import subprocess as sb
from herramientas.printlet import color

def daemon():
    color("Activar ClamAV")
    # Aquí se ejecuta un comando usando shell=True porque es comando fijo y no ingresado por el usuario, así evito que nadie ingrese comandos malintencionados.
    sb.run("sudo systemctl enable clamav-daemon --now && sudo systemctl start clamav-daemon --now", shell=True)


def firewall():
    color("UFW Status")
    sb.run(["sudo", "ufw", "status", "verbose"])

def rkescaneo():
    color("RKHUNTER Escaneo")
    print("Actualizando bases de datos...\n")
    sb.run(["sudo", "rkhunter", "--update"])
    print("Actualizando base local de propiedades...\n")
    sb.run(["sudo", "rkhunter", "--propupd"])
    print("Ejecutando análisis completo...\n")
    sb.run(["sudo", "rkhunter", "--check"])