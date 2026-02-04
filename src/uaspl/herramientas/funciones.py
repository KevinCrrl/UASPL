# KevinCrrl; LICENSE: GPL-3-or-later

import subprocess as sb
from uaspl.herramientas.avisoctk import avisoctk
from uaspl.herramientas.idioma import traductor
from uaspl.herramientas.gterminal import GTerminal
import customtkinter as ctk

class Servicio:
    def __init__(self, tipo):
        self.servicios = ["clamav-daemon", "clamav-clamonacc", "clamav-freshclam"]
        self.tipo = tipo

    def systemctl(self):
        try:
            sb.run(["pkexec", "systemctl", self.tipo] + self.servicios, check=True)
        except sb.CalledProcessError as e:
            print(traductor("Error ocurrido: ") + str(e))

def ayuda():
    print(traductor("""Argumentos disponibles:
escaneo: Escaneo ClamAV
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

Use el programa uasplc (no integrado directamente en UASPL, pero sí desarrollado en conjunto bajo distintas licencias) para ejecutar escaneos en la terminal."""))

def version():
    print(traductor("UASPL Versión 2.1.1"))

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
