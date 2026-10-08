# root

*Community 0 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `add_text_to_image`, `add_to_knowledge_base`, `check_api_key`, `configure_logging`, `create_complex_prompt`, `generate_frames`, `generate_video_from_script`, `get_relevant_knowledge`. Core file: `cli.py` (14 symbols). Documented purpose: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: 09/06/2024 Licencia: GPL v3  Descripción: Asistente de investigaci.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `cli.py` | py | utility | 14 | yes |
| `script_animator.py` | py | utility | 3 | no |

## Key Symbols

- `signal_handler` (function, `cli.py:61`) `def signal_handler(sig, frame)`
- `show_help` (function, `cli.py:67`) `def show_help(message)`
- `check_api_key` (function, `cli.py:71`) `def check_api_key()`
- `configure_logging` (function, `cli.py:79`) `def configure_logging(debug)`
- `parse_args` (function, `cli.py:83`) `def parse_args()`
- `create_complex_prompt` (function, `cli.py:90`) `def create_complex_prompt(base_prompt, history, knowledge_base, error_message)`
- `load_knowledge_base` (function, `cli.py:116`) `def load_knowledge_base(file_path)`
- `save_knowledge_base` (function, `cli.py:122`) `def save_knowledge_base(knowledge_base, file_path)`
- `add_to_knowledge_base` (function, `cli.py:126`) `def add_to_knowledge_base(prompt, command, file_path)`
- `get_relevant_knowledge` (function, `cli.py:131`) `def get_relevant_knowledge(prompt)`
- `transform_knowledge_base` (function, `cli.py:139`) `def transform_knowledge_base(client)`
- `save_script` (function, `cli.py:162`) `def save_script(script, script_name)`
- `generate_video_from_script` (function, `cli.py:170`) `def generate_video_from_script(script_path)`
- `main` (function, `cli.py:185`) `def main()`
- `add_text_to_image` (function, `script_animator.py:15`) `def add_text_to_image(draw, text, position, font, color)`
- `generate_frames` (function, `script_animator.py:27`) `def generate_frames(text, bg_image_path, font_path, output_resolution, fps, char`
- `main` (function, `script_animator.py:97`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 1
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (layer utility) with no import path between community 0 (root) and community 1 (orphans).

## Risks

- [dataflow UNCHECKED_ALLOC] `script_animator.py:29` `generate_frames` `bg_image`: Result of allocator stored in `bg_image` is never checked against NULL.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `script_animator.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `cli.py`
- `script_animator.py`
