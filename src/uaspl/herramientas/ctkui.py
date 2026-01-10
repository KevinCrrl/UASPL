# KevinCrrl; LICENSE: GPL-3-or-later

import customtkinter as ctk
from uaspl.herramientas.extensiones import ventana_extensiones
from tkinter import PhotoImage
from uaspl.herramientas.ufwui import ventanaufw
from uaspl.herramientas.funciones import *
from uaspl.herramientas.idioma import traductor

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
