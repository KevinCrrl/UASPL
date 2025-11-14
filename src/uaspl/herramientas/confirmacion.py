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

def ventana_confirmacion(titulo:str, texto:str, texto_si:str, texto_no:str, funcion_si,):
    def ejecutar_si():
        ventana.destroy()
        funcion_si()

    ventana = ctk.CTk()
    ventana.title(titulo)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_rowconfigure(0, weight=1)
    ventana.geometry("500x300")

    textbox = ctk.CTkTextbox(ventana, wrap="word", corner_radius=10)
    textbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    textbox.insert("0.0", texto)

    textbox.configure(state="disabled")

    si = ctk.CTkButton(ventana, text=texto_si, command=ejecutar_si)
    si.grid()

    no = ctk.CTkButton(ventana, text=texto_no, command=ventana.destroy)
    no.grid(pady=10)

    ventana.mainloop()
