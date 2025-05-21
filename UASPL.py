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

from herramientas.funciones import *
from herramientas.ctkui import ui
import sys

args = {
    "activar": daemon,
    "red-estado": firewall,
    "anti-rk": rkescaneo,
    "modo-ui": ui,
}

try:
    for arg, funcion in args.items():
        if sys.argv[1] == arg:
            funcion()
            break # break para que cuando encuentre la función que no itere más y termine dando comportamientos que no quiero en la consola.
    
    else: # else aquí y no dentro del bucle for porque sino al no encontrar el argumento el aviso del print termina saliendo más de una vez.
        print("""Argumento no encontrado
Argumentos disponibles:
activar: Activa el daemon de ClamAV.
red-estado: Consulta y muestra el estado y las reglas del firewall UFW.
anti-rk: Realiza un escaneo en busca de modificaciones malintencionadas y rootkits.
modo-ui: Activa la interfaz gráfica del programa, aún así se necesita de la terminal para ver las salidas de los comandos.

Si se desea realizar un escaneo antivirus con ClamAV, se debe usar el modo gráfico para dar la ruta a escanear.""")

except IndexError: # Aquí controlo el error de que se ejecute el programa sin ingresar ni un solo argumento, sí o sí se debe dar un argumento.
    print("No se ingresó ningún argumento.")
