#!/bin/bash

# Nombre del entorno virtual
ENV_NAME="env"

# Ruta del script de Python
SCRIPT_NAME="cli.py"

# Crear un entorno virtual
python3 -m venv $ENV_NAME

# Activar el entorno virtual
source $ENV_NAME/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar las bibliotecas necesarias
pip install opencv-python Pillow moviepy groq signal argparse

# nos bajamos la ultima versión de la libreria para crear videos
wget --no-verbose --timestamping --output-document=script_animator.py https://raw.githubusercontent.com/grisuno/ScriptAnimator/main/script_animator.py


# Ejecutar el script de Python pasando el prompt de texto como parámetro del video que se quiere generar
python $SCRIPT_NAME "$1"

# Desactivar el entorno virtual
deactivate
