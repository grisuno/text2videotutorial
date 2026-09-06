# API

## cli.py

### signal_handler `def signal_handler(sig, frame)`
- Defined: `cli.py:61`
- Depends on: `script_animator.py`

### show_help `def show_help(message)`
- Defined: `cli.py:67`
- Depends on: `script_animator.py`

### check_api_key `def check_api_key()`
- Defined: `cli.py:71`
- Depends on: `script_animator.py`

### configure_logging `def configure_logging(debug)`
- Defined: `cli.py:79`
- Depends on: `script_animator.py`

### parse_args `def parse_args()`
- Defined: `cli.py:83`
- Depends on: `script_animator.py`

### create_complex_prompt `def create_complex_prompt(base_prompt, history, knowledge_base, error_message)`
- Defined: `cli.py:90`
- Depends on: `script_animator.py`

### load_knowledge_base `def load_knowledge_base(file_path)`
- Defined: `cli.py:116`
- Depends on: `script_animator.py`

### save_knowledge_base `def save_knowledge_base(knowledge_base, file_path)`
- Defined: `cli.py:122`
- Depends on: `script_animator.py`

### add_to_knowledge_base `def add_to_knowledge_base(prompt, command, file_path)`
- Defined: `cli.py:126`
- Depends on: `script_animator.py`

### get_relevant_knowledge `def get_relevant_knowledge(prompt)`
- Defined: `cli.py:131`
- Depends on: `script_animator.py`

### transform_knowledge_base `def transform_knowledge_base(client)`
- Defined: `cli.py:139`
- Depends on: `script_animator.py`

### save_script `def save_script(script, script_name)`
- Defined: `cli.py:162`
- Depends on: `script_animator.py`

### generate_video_from_script `def generate_video_from_script(script_path)`
- Defined: `cli.py:170`
- Depends on: `script_animator.py`

### main `def main()`
- Defined: `cli.py:185`
- Depends on: `script_animator.py`

## script_animator.py

### add_text_to_image `def add_text_to_image(draw, text, position, font, color)`
- Defined: `script_animator.py:15`
- Imported by: `cli.py`

### generate_frames `def generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path, audio_path)`
- Defined: `script_animator.py:27`
- Imported by: `cli.py`

### main `def main()`
- Defined: `script_animator.py:97`
- Imported by: `cli.py`
