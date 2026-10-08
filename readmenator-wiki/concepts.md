# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `script` | 2 | 4 | `cli.py`, `script_animator.py` |
| `add` | 2 | 2 | `cli.py`, `script_animator.py` |
| `generate` | 2 | 2 | `cli.py`, `script_animator.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `add` | `depends_on` | `generate` | 1.00 |
| `add` | `depends_on` | `script` | 1.00 |
| `generate` | `depends_on` | `add` | 1.00 |
| `generate` | `depends_on` | `script` | 1.00 |
| `script` | `depends_on` | `add` | 1.00 |
| `script` | `depends_on` | `generate` | 1.00 |

## Dialectic Prompts

- Thesis: `add` centralizes 2 files; Antithesis: `generate` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `add` centralizes 2 files; Antithesis: `script` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `generate` centralizes 2 files; Antithesis: `script` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
