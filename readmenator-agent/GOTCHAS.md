# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `cli.py` (score: 3.40)
- `script_animator.py` (score: 2.30)
- `install.sh` (score: 0.00)

## Hotspots (complexity + centrality)

- `cli.py` -- complexity: 1.0, centrality: 1.0, combined: 1.0
- `script_animator.py` -- complexity: 0.2, centrality: 0.5, combined: 0.4
- `install.sh` -- complexity: 0.0, centrality: 0.0, combined: 0.0

## Dataflow Issues (INFERRED, review each lead)

- `script_animator.py:29` `generate_frames` [UNCHECKED_ALLOC] `bg_image`: Result of allocator stored in `bg_image` is never checked against NULL.
