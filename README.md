# DSA-Vault

Structured DSA problem solutions: problem statement, intuition, approach, animated GIF diagram, and Python code.

## Structure

```
templates/problem_template.md   # copy for every new problem
tools/array_gif.py               # reusable frame -> gif renderer
topics/<topic>/<problem-slug>/
  README.md                      # problem write-up (from template)
  solution.py                    # solution
  generate_gif.py                # builds diagram.gif
  diagram.gif                    # generated animation
```

## Adding a new problem

1. `mkdir topics/<topic>/<problem-slug>`
2. Copy `templates/problem_template.md` to `topics/<topic>/<problem-slug>/README.md`, fill it in.
3. Write `solution.py`.
4. Write `generate_gif.py` — record array snapshots as frames, call `tools/array_gif.render(frames, "diagram.gif")`.
5. Run `python generate_gif.py` to produce `diagram.gif`, embed it in the README.

See `topics/array/merge-sorted-array/` for a full worked example.
