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

from tkinter import LEFT
import customtkinter as ctk 
import subprocess as sb
from herramientas.funciones import color
from herramientas.idioma import palabras

def ventanaufw():
    def nueva_regla():
        regla = entrada.get()
        color(palabras["ti5"])
        sb.run(["sudo", "ufw"] + regla.split())

    ufwui = ctk.CTk()
    ufwui.title(palabras["ti1"])
    ufwui.geometry("280x100")
    ufwui.resizable(False, False)

    doble = ctk.CTkFrame(ufwui, width=260, height=30)
    doble.pack(pady=3)

    texto1 = ctk.CTkLabel(doble, text="sudo ufw")
    texto1.pack(side=LEFT)

    entrada = ctk.CTkEntry(doble)
    entrada.pack(side=LEFT)

    boton1 = ctk.CTkButton(ufwui, text=palabras["bu2"], command=nueva_regla)
    boton1.pack(pady=3)

    ufwui.mainloop()