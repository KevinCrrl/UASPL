# UASPL

UASPL es un proyecto libre que ayuda a automatizar tareas de escaneo y red, UASPL significa: Utilidad Automatizada para la Seguridad y la Protección de Linux.

# Ayuda y Uso

Dependencias que se deben instalar: clamav, ufw, rkhunter. El programa no los instala él mismo debido a que se debería manejar cada gestor de paquetes de cada distro.
En el código hay comentarios que ayudan a entender porque algo esta ahí y no simplemente es adorno, además que hay documentación en una url enlazada dentro del programa.

# Modo Gráfico

Este modo gráfico no usa la librería tkinter, usa customtkinter, además en el modo CLI se usa pyfiglet y colorama, todo esto son módulos externos, así que se deben instalar con un entorno virtual o directamente en el sistema usando el gestor de paquetes de la distro (No usar pip sin entorno virtual, destruirá las dependencias de la distro).
