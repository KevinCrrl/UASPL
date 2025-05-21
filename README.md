# UASPL

UASPL es un acrónimo recursivo como el del proyecto GNU (GNU's No Unix) por lo que UASPL significa: UASPL Automatizado para la Seguridad y la Protección de Linux.

# ¿Ayuda y Uso?

Dependencias que se deben instalar: clamav, ufw, rkhunter. El programa no los instala él mismo.
En el código hay comentarios que ayudan a entender porque algo esta ahí y no simplemente es adorno.

# Modo Gráfico

Este modo gráfico no usa la librería tkinter, usa customtkinter, además en el modo CLI se usa pyfiglet y colorama, todo esto son módulos externos, así que se deben instalar con un entorno virtual o directamente en el sistema usando el gestor de paquetes de la distro (No usar pip sin entorno virtual, destruirá las dependencias de la distro).