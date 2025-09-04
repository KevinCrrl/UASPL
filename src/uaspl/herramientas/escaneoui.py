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
from herramientas.idioma import traductor
from herramientas.gterminal import GTerminal

def ventana():
    def escaneo():
        ruta = entrada.get()
        GTerminal(traductor("ClamAV Escaneo"), ["pkexec", "uasplc", "clam", ruta], True).crear_interfaz()

    vent = ctk.CTk()
    vent.title(traductor("ClamAV Escaneo"))
    vent.geometry("220x120")
    vent.resizable(False, False)

    texto1 = ctk.CTkLabel(vent, text=traductor("Ingresa la ruta a escanear:"))
    texto1.pack()

    entrada = ctk.CTkEntry(vent)
    entrada.pack(pady=5)

    boton1 = ctk.CTkButton(vent, text=traductor("Escanear"), command=escaneo)
    boton1.pack()

    vent.mainloop()
