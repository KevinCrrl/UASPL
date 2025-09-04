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

from herramientas.idioma import traductor
from subprocess import Popen, PIPE, STDOUT, run, CalledProcessError
from customtkinter import filedialog
from colorama import Fore, init
import customtkinter as ctk
import threading as thd

init(autoreset=True)

class GTerminal:
    def __init__(self, titulo, comando: list, isclam: bool):
        self.titulo = titulo
        self.comando = comando
        self.isclam = isclam
        self.salida_acumulada = ""

    def guardar_salida(self, salida):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if archivo:
            with open(archivo, "w", encoding="utf-8") as archivo:
                archivo.write(salida)

    def eliminar_virus(self, salida_clam):
        confirmacion = input(traductor("Seguro de que deseas eliminar todos los archivos detectados como maliciosos? (s/n): "))
        if confirmacion.strip().lower() == "s" or confirmacion.strip().lower() == "y":
            for linea in salida_clam.split("\n"):
                if "FOUND" in linea:
                    malicioso = linea.split()[0][:-1]
                    try:
                        run(["pkexec", "rm", malicioso], check=True) # [:-1] quita el : al final de la ruta del archivo
                    except CalledProcessError:
                        print(Fore.RED + traductor("ERROR: NO SE PUDO ELIMINAR EL ARCHIVO:") + malicioso)

    def crear_interfaz(self):
        def tarea():
            process = Popen(self.comando, stdout=PIPE, stderr=STDOUT, text=True)

            for linea in process.stdout:
                text_box.configure(state="normal")  # Permitir a la interfaz mostrar en tiempor real
                text_box.insert("end", linea)
                text_box.see("end")
                text_box.update()  # Actualizar antes de hacer disabled para evitar el lag visual
                text_box.configure(state="disabled")  # Impedir que un usuario manipule la salida
                self.salida_acumulada += linea

        root = ctk.CTk()
        root.geometry("700x400")
        root.title(self.titulo)

        text_box = ctk.CTkTextbox(root, font=("DejaVu Sans Mono", 14))
        text_box.pack(fill="both", expand=True, padx=10, pady=10)
        text_box.configure(state="disabled")

        proceso = thd.Thread(target=tarea)
        proceso.start()

        root.update()

        guardar = ctk.CTkButton(root, text=traductor("Guardar"), command=lambda: self.guardar_salida(self.salida_acumulada))
        guardar.pack(pady=10, padx=10, side="left")

        if self.isclam:
            eliminar = ctk.CTkButton(root, text=traductor("Eliminar Virus Detectados"), command=lambda: self.eliminar_virus(self.salida_acumulada))
            eliminar.pack(pady=10, side="left")

        root.mainloop()
