import os
import sys

nombre_carpeta = "{{ cookiecutter.nombre_carpeta }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if nombre_carpeta.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {nombre_carpeta=} no es un nombre válido para esta plantilla.{RESET_ALL}")

   sys.exit(1)

print(f"{MESSAGE_COLOR}¡Vamos a hacerlo! ¡Vas a crear algo increíble!")
print(f"Creando proyecto en { os.getcwd() }{RESET_ALL}")