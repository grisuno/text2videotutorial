# Concepts

Nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

- `script` | files=2 | mentions=4 | `cli.py`, `script_animator.py`
- `add` | files=2 | mentions=2 | `cli.py`, `script_animator.py`
- `generate` | files=2 | mentions=2 | `cli.py`, `script_animator.py`

## Verb Edges

- `add` --depends_on--> `generate` (strength 1.00)
- `add` --depends_on--> `script` (strength 1.00)
- `generate` --depends_on--> `add` (strength 1.00)
- `generate` --depends_on--> `script` (strength 1.00)
- `script` --depends_on--> `add` (strength 1.00)
- `script` --depends_on--> `generate` (strength 1.00)

## Dialectic

- Thesis: `add` centralizes 2 files; Antithesis: `generate` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `add` centralizes 2 files; Antithesis: `script` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `generate` centralizes 2 files; Antithesis: `script` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
