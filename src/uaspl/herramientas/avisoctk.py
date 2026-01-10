# KevinCrrl; LICENSE: GPL-3-or-later

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
