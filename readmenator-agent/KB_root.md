# Subsystem: root

## cli.py
- Layer: utility
- Doc: main.py  Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: 09/06/2024 Licenc
- Language: py
- Symbols:
  - `signal_handler` (function, line 61) `def signal_handler(sig, frame)`
  - `show_help` (function, line 67) `def show_help(message)`
  - `check_api_key` (function, line 71) `def check_api_key()`
  - `configure_logging` (function, line 79) `def configure_logging(debug)`
  - `parse_args` (function, line 83) `def parse_args()`
  - `create_complex_prompt` (function, line 90) `def create_complex_prompt(base_prompt, history, knowledge_base, error_message)`
  - `load_knowledge_base` (function, line 116) `def load_knowledge_base(file_path)`
  - `save_knowledge_base` (function, line 122) `def save_knowledge_base(knowledge_base, file_path)`
  - `add_to_knowledge_base` (function, line 126) `def add_to_knowledge_base(prompt, command, file_path)`
  - `get_relevant_knowledge` (function, line 131) `def get_relevant_knowledge(prompt)`
  - `transform_knowledge_base` (function, line 139) `def transform_knowledge_base(client)`
  - `save_script` (function, line 162) `def save_script(script, script_name)`
  - `generate_video_from_script` (function, line 170) `def generate_video_from_script(script_path)`
  - `main` (function, line 185) `def main()`
- Depends on: `script_animator.py`

## install.sh
- Layer: utility
- Doc: Nombre del entorno virtual
- Language: sh

## script_animator.py
- Layer: utility
- Language: py
- Symbols:
  - `add_text_to_image` (function, line 15) `def add_text_to_image(draw, text, position, font, color)`
  - `generate_frames` (function, line 27) `def generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path, audio_path)`
  - `main` (function, line 97) `def main()`
- Imported by: `cli.py`
