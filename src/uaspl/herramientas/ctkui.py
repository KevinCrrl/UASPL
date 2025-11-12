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
from herramientas.extensiones import ventana_extensiones
from tkinter import PhotoImage
from herramientas.ufwui import ventanaufw
from herramientas.funciones import *
from herramientas.idioma import traductor

nombres = {
    traductor("Escaneo ClamAV"): escaneo,
    traductor("Reglas UFW"): firewall,
    traductor("RKESCANEO"): rkescaneo,
    traductor("Nueva Regla UFW"): ventanaufw,
    traductor("Mis Extensiones"): ventana_extensiones
}

def ui():
    root = ctk.CTk()
    root.title("UASPL GUI")
    # True para que sea el ícono en todas las demás ventanas
    root.iconphoto(True, PhotoImage(file='/usr/share/icons/hicolor/48x48/apps/UASPL.png'))

    root.geometry("300x220")
    root.resizable(False, False)

    texto = ctk.CTkLabel(root, text=traductor("Menú de UASPL:"))
    texto.pack()

    for nombre, funcion in nombres.items(): # for y dict usado para no tener que estar reescribiendo la función CTkButton para crear tantos botones (DRY)
        boton = ctk.CTkButton(root, text=nombre, command=funcion)
        boton.pack(pady=5)

    root.mainloop()
