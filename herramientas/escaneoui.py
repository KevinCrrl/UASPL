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
import subprocess as sb
from time import sleep
from herramientas.funciones import color
from herramientas.idioma import palabras
from colorama import Fore

def ventana():
    def escaneo():
        ruta = entrada.get()
        color(palabras["ti1"])
        print(palabras["ti2"])
        sleep(3)
        sb.run(["sudo", "freshclam"])
        print(palabras["ti3"])
        sleep(3)
        sb.run(["sudo", "clamscan", ruta]) # sin shell=True porque aquí si se maneja una entrada de usuario y peor aún con sudo que es el riesgo total de todo Linux.
        print(Fore.BLUE + palabras["final"])

    vent = ctk.CTk()
    vent.title(palabras["ti1"])
    vent.geometry("220x120")
    vent.resizable(False, False)

    texto1 = ctk.CTkLabel(vent, text=palabras["gr1"])
    texto1.pack()

    entrada = ctk.CTkEntry(vent)
    entrada.pack(pady=5)

    boton1 = ctk.CTkButton(vent, text=palabras["bu1"], command=escaneo)
    boton1.pack()

    vent.mainloop()