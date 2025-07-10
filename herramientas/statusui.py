import customtkinter as ctk

def status_ventana(output):
    statusui = ctk.CTk()
    statusui.title("UFW Status")
    statusui.geometry("500x300")

    consola = ctk.CTkScrollableFrame(statusui)
    consola.pack(fill="both", expand=True, padx=20, pady=20)

    texto = ctk.CTkLabel(consola, text=output, anchor="w", justify="left", wraplength=550)
    texto.pack(fill="both", expand=True, padx=10, pady=10)

    statusui.mainloop()
