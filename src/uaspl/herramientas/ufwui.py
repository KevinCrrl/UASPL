# KevinCrrl; LICENSE: GPL-3-or-later

import customtkinter as ctk
from uaspl.herramientas.idioma import traductor
from uaspl.herramientas.gterminal import GTerminal

def ventanaufw():
    regla = ctk.CTkInputDialog(text="pkexec ufw", title=traductor("UFW Regla"))
    GTerminal(traductor("UFW Regla"), ["pkexec", "ufw"] + regla.get_input().split(), False).crear_interfaz()
