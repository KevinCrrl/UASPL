#!/bin/sh

# UASPL Comandos, Autor: KevinCrrl, LICENCIA: MIT
# El software se proporciona "tal cual", sin garantía de ningún tipo. 
# El autor no se hace responsable de daños derivados de su uso. (Vea la licencia MIT para más detalles)
# Este archivo se puede usar de manera individual o junto a UASPL (Para ser usado por UASPL se debe ubicar este archivo en /usr/bin con el nombre uasplc sin extensión)
# No lleva la licencia GPLv3 de UASPL ya que UASPL lo llama a través de subprocess.Popen, por ende no aplica el copyleft, además su creador (KevinCrrl) considera la licencia MIT más apta para un script pequeño como este.

clam() {
    case "$1" in
        /|~|/*|~/*)
            cat <<'EOF'
  ____ _                    ___     __
 / ___| | __ _ _ __ ___    / \ \   / /
| |   | |/ _` | '_ ` _ \  / _ \ \ / / 
| |___| | (_| | | | | | |/ ___ \ V /  
 \____|_|\__,_|_| |_| |_/_/   \_\_/

EOF
            freshclam
            clamscan -r "$1"
            ;;
        *)
            echo "Por favor revise la ruta ingresada, parece no tener estilo de ruta válida."
            echo "Please review the path you entered, it doesn't appear to have a valid path style."
            ;;
    esac
}

rk() {
    cat <<'EOF'
      _    _                 _            
 _ __| | _| |__  _   _ _ __ | |_ ___ _ __ 
| '__| |/ / '_ \| | | | '_ \| __/ _ \ '__|
| |  |   <| | | | |_| | | | | ||  __/ |   
|_|  |_|\_\_| |_|\__,_|_| |_|\__\___|_|

EOF
    sleep 2
    rkhunter --update --nocolors --skip-keypress
    rkhunter --propupd --nocolors --skip-keypress
    rkhunter --check --nocolors --skip-keypress
}

if [ "$1" = "clam" ]; then
    clam "$2"
elif [ "$1" = "rk" ]; then
    rk
else
    echo "Argumento desconocido... Comandos válidos:"
    echo "Unknown argument... Valid commands:"
    echo "uasplc clam"
    echo "uasplc rk"
fi