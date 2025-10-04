from xdg.BaseDirectory import xdg_config_home, xdg_data_home
from herramientas.idioma import traductor
from herramientas.funciones import avisoctk
import customtkinter as ctk
import subprocess as sb
import os

def ventana_extensiones():
    ruta_extensiones = os.path.join(xdg_data_home, "uaspl")
    ruta_config_extensiones = os.path.join(xdg_config_home, "uaspl", "extensiones.txt")

    if os.path.exists(ruta_config_extensiones):
        with open(ruta_config_extensiones, "r", encoding="utf-8") as extensiones:
            lista = extensiones.read()

        vext = ctk.CTk()
        vext.title(traductor("Mis Extensiones"))
        vext.geometry("300x400")

        scroll = ctk.CTkScrollableFrame(vext, width=290, height=390)
        scroll.pack(padx=10, pady=10, fill="both", expand=True)

        for extension in lista.split("\n"):
            if extension == "":
                continue
            ctk.CTkButton(scroll, text=extension, command=lambda ext=extension: sb.run(["python", os.path.join(ruta_extensiones, f"{ext}.py")], check=False)).pack(pady=5, padx=10, fill="x")
        
    else:
        avisoctk("No existe el archivo de extensiones.")
