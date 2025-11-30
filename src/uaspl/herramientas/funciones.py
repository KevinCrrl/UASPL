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
from uaspl.herramientas.avisoctk import avisoctk
from uaspl.herramientas.idioma import traductor
from uaspl.herramientas.gterminal import GTerminal
import customtkinter as ctk

class Servicio:
    def __init__(self, tipo):
        self.nombres = ["clamav-daemon", "clamav-clamonacc", "clamav-freshclam"]
        self.tipo = tipo

    def systemctl(self):
        for servicio in self.nombres:
            try:
                sb.run(["pkexec", "systemctl"] + self.tipo.split() + [servicio], check=True)
            except sb.CalledProcessError:
                print(f"Error ocurrido durante el servicio {servicio}")

def ayuda():
    print(traductor("""Argumentos disponibles:
red-estado: Consulta y muestra el estado y las reglas del firewall UFW en una interfaz gráfica.
anti-rk: Realiza un escaneo en busca de modificaciones malintencionadas y rootkits en una interfaz gráfica.
gui: Muestra el menú principal del programa donde se pueden llamar otras interfaces.
version: Muestra la versión que se está usando de UASPL.
full-iniciar-servicios: Activa e inicia inmediatamente los servicios de ClamAV.
full-detener-servicios: Desactiva y detiene inmediatamente los servicios de ClamAV.
estado-servicios: Muestra el estado de los servicios de ClamAV.
detener-servicios: Detiene los servicios de ClamAV en la sesión actual.
iniciar-servicios: Inicia los servicios de ClamAV en la sesión actual.
activar-servicios: Activa los servicios de ClamAV para que inicien con el sistema.
desactivar-servicios: Desactiva los servicios de ClamAV para que no inicien con el sistema.

Si se desea realizar un escaneo antivirus con ClamAV, se debe usar el modo gráfico para dar la ruta a escanear.

Use el programa uasplc (no integrado directamente en UASPL, pero sí desarrollado en conjunto bajo distintas licencias) para ejecutar escaneos en la terminal."""))

def version():
    print(traductor("UASPL Versión 2.0.0"))

def firewall():
    GTerminal("UFW Status", ["pkexec", "ufw", "status", "verbose"], False).crear_interfaz()

def rkescaneo():
    GTerminal("RKHUNTER", ["pkexec", "sh", "uasplc", "rk"], False).crear_interfaz()

def escaneo():
    ruta = ctk.filedialog.askdirectory()
    if ruta == ():  # askdirectory() retorna una tupla cuando se cancela la acción
        avisoctk("No se ingresó ninguna ruta.")
    else:
        GTerminal(traductor("ClamAV Escaneo"), ["pkexec", "sh", "uasplc", "clam", ruta], True).crear_interfaz()
