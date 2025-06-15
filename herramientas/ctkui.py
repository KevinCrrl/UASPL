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
from herramientas.escaneoui import ventana
from herramientas.ufwui import ventanaufw
from herramientas.funciones import *
from herramientas.idioma import palabras

nombres = {
    palabras["ventana"]: ventana,
    palabras["firewall"]: firewall,
    palabras["rkescaneo"]: rkescaneo,
    palabras["regla"]: ventanaufw
}

def ui():
    root = ctk.CTk()
    root.title("UASPL GUI")
    root.geometry("300x200")
    root.resizable(False, False)

    texto = ctk.CTkLabel(root, text=palabras["ti4"])
    texto.pack()

    for nombre, funcion in nombres.items(): # for y dict usado para no tener que estar reescribiendo la función CTkButton para crear tantos botones (DRY)
        boton = ctk.CTkButton(root, text=nombre, command=funcion)
        boton.pack(pady=5)

    root.mainloop()