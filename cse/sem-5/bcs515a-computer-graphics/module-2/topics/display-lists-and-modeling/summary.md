# Display Lists and Modeling - Summary

## Key Definitions and Concepts

- **Display List**: A pre-compiled, named group of OpenGL commands stored on the GPU for efficient repeated execution.
- **Hierarchical Modeling**: Building complex objects from simpler sub-objects organized in a parent-child tree structure.
- **Instance Transformation**: A transformation (translate, rotate, scale) applied to a prototype object to create a positioned copy in the scene.
- **Scene Graph**: A DAG representing the spatial and logical hierarchy of objects in a scene.
- **Matrix Stack**: An OpenGL stack mechanism for saving and restoring transformation states during hierarchical rendering.

## Important Formulas and Functions

- `glGenLists(range)` — Generates unique display list identifiers
- `glNewList(id, mode)` — Begins display list definition (mode: `GL_COMPILE` or `GL_COMPILE_AND_EXECUTE`)
- `glEndList()` — Ends display list definition
- `glCallList(id)` — Executes a single display list
- `glCallLists(n, type, lists)` — Executes multiple display lists
- `glDeleteLists(id, range)` — Deletes display lists
- `glPushMatrix()` / `glPopMatrix()` — Save/restore transformation matrix on stack

## Key Points

- Display lists are **immutable** — once created, they cannot be modified, only deleted and recreated.
- `GL_COMPILE` stores commands without executing; `GL_COMPILE_AND_EXECUTE` does both simultaneously.
- Display lists improve performance by reducing CPU-GPU communication overhead.
- Hierarchical modeling uses a tree structure where child transformations are relative to their parent.
- The matrix stack depth is limited (minimum 32 for modelview matrix) — excessive nesting can cause stack overflow.
- Display lists can be nested — one display list can call another using `glCallList()`.
- Shared geometry in a DAG allows memory-efficient reuse (e.g., one wheel used for four instances).
- Changing a parent's transformation automatically affects all descendants in the hierarchy.
- Display lists can store state changes (color, material, lighting) along with geometry.
- Not all OpenGL commands can be stored in display lists (list management commands are excluded).

## Common Mistakes to Avoid

- **Forgetting `glEndList()`**: Every `glNewList()` must have a matching `glEndList()`, otherwise undefined behavior occurs.
- **Mismatched Push/Pop**: Every `glPushMatrix()` must have a corresponding `glPopMatrix()`. Missing one corrupts the entire transformation hierarchy.
- **Trying to modify display lists**: Students often attempt to change display list contents. Remember, they must be deleted and recreated.
- **Wrong transformation order**: In OpenGL, transformations are applied in reverse order of code. Apply scale, then rotate, then translate in code to get T·R·S effect.

## Revision Tips

- Practice drawing the matrix stack state step-by-step for hierarchical code — this is a common exam exercise.
- Memorize the robot arm example thoroughly; it covers all key concepts (display lists, matrix stack, hierarchical transformations).
- Create a comparison table: Display List vs. Immediate Mode — covering performance, flexibility, memory, and use cases.
- Write and run at least 2-3 OpenGL programs using display lists and hierarchical modeling before the exam for hands-on understanding.
