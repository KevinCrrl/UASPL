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

from uaspl.herramientas.idioma import traductor
import customtkinter as ctk

def avisoctk(mensaje, parent=None, traducir=True):
    if parent:
        dialogo = ctk.CTkToplevel(parent)
        # Hacer la ventana modal respecto al parent
        dialogo.transient(parent)
        dialogo.grab_set()
    else:
        # Si no hay parent, crear una ventana raíz
        dialogo = ctk.CTk()

    dialogo.title(traductor("Aviso de UASPL"))
    dialogo.geometry("350x150")
    dialogo.resizable(False, False)

    if traducir:
        label = ctk.CTkLabel(dialogo, text=traductor(mensaje), wraplength=330)
    else:
        label = ctk.CTkLabel(dialogo, text=mensaje, wraplength=330)
    label.pack(padx=20, pady=20, expand=True, fill="both")

    boton = ctk.CTkButton(dialogo, text="OK", command=dialogo.destroy)
    boton.pack(pady=(0, 20))

    if parent:
        parent.wait_window(dialogo)
    else:
        dialogo.mainloop()
