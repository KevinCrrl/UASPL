# KevinCrrl; LICENSE: GPL-3-or-later

from uaspl.herramientas.idioma import traductor
from uaspl.herramientas.confirmacion import ventana_confirmacion
from uaspl.herramientas.avisoctk import avisoctk
from subprocess import Popen, PIPE, STDOUT, run, CalledProcessError
from customtkinter import filedialog
import customtkinter as ctk
import threading as thd

class GTerminal:
    def __init__(self, titulo, comando: list, isclam: bool):
        self.titulo = titulo
        self.comando = comando
        self.isclam = isclam
        self.salida_acumulada = ""
        self.maliciosos = []
        self.found = False

    def guardar_salida(self, salida):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if archivo:
            with open(archivo, "w", encoding="utf-8") as archivo:
                archivo.write(salida)

    def eliminar_virus(self):
        def eliminar():
            try:
                run(["pkexec", "rm"] + self.maliciosos, check=True)
            except CalledProcessError as e:
                avisoctk(traductor("Error ocurrido") + "\n" + str(e), traducir=False)
            if self.found:
                avisoctk("Todos los archivos maliciosos han sido eliminados.\nSe recomienda verificar.")
            else:
                avisoctk("No se encontraron archivos maliciosos.")
        
        for linea in self.salida_acumulada.split("\n"):
            if "FOUND" in linea:
                self.found = True
                malicioso = linea.split(":")[0] # Eliminar la etiqueta de malware para quedarse solo con el archivo
                self.maliciosos.append(malicioso)

        ventana_confirmacion("UASPL: ClamAV",
        traductor("Seguro de que deseas eliminar todos los archivos detectados como maliciosos?") + "\n" + str(self.maliciosos),
        traductor("Sí"),
        "No",
        eliminar)

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
            eliminar = ctk.CTkButton(root, text=traductor("Eliminar Virus Detectados"), command=self.eliminar_virus)
            eliminar.pack(pady=10, side="left")

        root.mainloop()
