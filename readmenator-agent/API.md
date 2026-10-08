# API

## cli.py

### signal_handler (function) `def signal_handler(sig, frame)`
- Defined: `cli.py:61`
- Depends on: `script_animator.py`

### show_help (function) `def show_help(message)`
- Defined: `cli.py:67`
- Depends on: `script_animator.py`

### check_api_key (function) `def check_api_key()`
- Defined: `cli.py:71`
- Depends on: `script_animator.py`

### configure_logging (function) `def configure_logging(debug)`
- Defined: `cli.py:79`
- Depends on: `script_animator.py`

### parse_args (function) `def parse_args()`
- Defined: `cli.py:83`
- Depends on: `script_animator.py`

### create_complex_prompt (function) `def create_complex_prompt(base_prompt, history, knowledge_base, error_message)`
- Defined: `cli.py:90`
- Depends on: `script_animator.py`

### load_knowledge_base (function) `def load_knowledge_base(file_path)`
- Defined: `cli.py:116`
- Depends on: `script_animator.py`

### save_knowledge_base (function) `def save_knowledge_base(knowledge_base, file_path)`
- Defined: `cli.py:122`
- Depends on: `script_animator.py`

### add_to_knowledge_base (function) `def add_to_knowledge_base(prompt, command, file_path)`
- Defined: `cli.py:126`
- Depends on: `script_animator.py`

### get_relevant_knowledge (function) `def get_relevant_knowledge(prompt)`
- Defined: `cli.py:131`
- Depends on: `script_animator.py`

### transform_knowledge_base (function) `def transform_knowledge_base(client)`
- Defined: `cli.py:139`
- Depends on: `script_animator.py`

### save_script (function) `def save_script(script, script_name)`
- Defined: `cli.py:162`
- Depends on: `script_animator.py`

### generate_video_from_script (function) `def generate_video_from_script(script_path)`
- Defined: `cli.py:170`
- Depends on: `script_animator.py`

### main (function) `def main()`
- Defined: `cli.py:185`
- Depends on: `script_animator.py`

## script_animator.py

### add_text_to_image (function) `def add_text_to_image(draw, text, position, font, color)`
- Defined: `script_animator.py:15`
- Imported by: `cli.py`

### generate_frames (function) `def generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path, audio_path)`
- Defined: `script_animator.py:27`
- Imported by: `cli.py`

### main (function) `def main()`
- Defined: `script_animator.py:97`
- Imported by: `cli.py`
