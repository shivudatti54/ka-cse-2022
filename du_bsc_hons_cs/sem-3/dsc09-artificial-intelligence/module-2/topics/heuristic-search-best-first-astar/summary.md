# Heuristic Search: Best‑First & A* (AI – DU B.Sc. (H) CS, NEP 2024)

## Introduction
Informed (heuristic) search uses domain‑specific knowledge to guide exploration, aiming to find a goal state with less effort than blind methods. The two most common informed strategies are **Greedy Best‑First Search** and **A* Search**, both of which are part of the Delhi University BSc (H) Computer Science syllabus (Unit III – Informed Search, NEP 2024).

## Core Ideas (Bullet Form)

- **Heuristic h(n)**
  - Estimate of the cheapest cost from node *n* to any goal.
  - *Admissible*: never overestimates true cost → guarantees solution if one exists.
  - *Consistent (monotonic)*: satisfies h(n) ≤ cost(n→n') + h(n') → guarantees optimality for A*.

- **Greedy Best‑First Search**
  - Expands node with lowest *h(n)* (purely heuristic).
  - Evaluation function f(n) = h(n).
  - Not guaranteed to be optimal; can get stuck in deep or expensive paths.
  - Time O(b^d), space O(b^d) in worst case.

- **A* Search**
  - Combines path‑cost *g(n)* and heuristic *h(n)*: f(n) = g(n) + h(n).
  - **Admissible h** → A* is *optimal* (finds least‑cost goal).
  - **Consistent h** → A* is *optimal* and never re‑expands a node (no need for closed list if using consistent heuristic).
  - Complexity:
    - *Time*: exponential in worst case, but best‑case practical speed‑up over uniform‑cost.
    - *Space*: main bottleneck – stores all generated nodes in the OPEN list (exponential).
  - **Algorithm sketch**
    1. Insert start node in priority queue (OPEN) with f‑value.
    2. Pop node with smallest f.
    3. If goal → return path.
    4. For each successor *n'*:
       - compute g = g(current) + cost(current→n').
       - if *n'* not visited or new g < previous g, update g, h, f and push into OPEN.
    5. Move popped node to CLOSED (or mark visited).

- **Comparison**
  | Feature               | Greedy Best‑First | A* |
  |-----------------------|-------------------|-----|
  | Evaluation function  | h(n)              | g(n)+h(n) |
  | Optimality            | No (may miss cheapest) | Yes (if h admissible) |
  | Completeness          | No (can get stuck) | Yes (finite graph) |
  | Memory usage          | Lower than A*   | Higher (needs full OPEN) |

- **Practical Tips (Exam‑focused)**
  - Remember the *f = g + h* formula; if h = 0, A* reduces to Uniform‑Cost Search.
  - For 8‑puzzle, Manhattan distance is a classic admissible heuristic.
  - If the problem graph is huge, consider *Iterative Deepening A** (IDA*) or *Recursive Best‑First Search* to save memory.

## Conclusion
Heuristic‑driven search, especially the Best‑First family, balances cost‑evaluation with domain knowledge. Greedy Best‑First is fast but sub‑optimal; A* provides optimal solutions when the heuristic is admissible (and consistent), making it a cornerstone technique in AI problem‑solving. Master the f‑function, heuristic properties, and the open/closed list mechanism—both are essential for the Delhi University exam.