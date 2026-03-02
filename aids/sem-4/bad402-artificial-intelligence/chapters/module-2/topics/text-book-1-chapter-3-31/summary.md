# **Revision Notes: Artificial Intelligence - Chapter 3.1**

**Key Definitions:**

- **Problem-Solving Agents:** Agents that can reason, solve problems, and make decisions.
- **Search Algorithm:** A method used to find a solution to a problem by exploring the search space.

**Key Formulas and Theorems:**

- **Breadth-First Search (BFS) Algorithm:**
  - `Q = {s, s1, s2, ... , s_n}`
  - `D = {d1, d2, ... , d_m}`
  - `QD = {s, d1, s1, d1s1, ... , s_d, d_m, s_md}`
- **Depth-First Search (DFS) Algorithm:**
  - `Q = {s, s1, s2, ... , s_n}`
  - `D = {d1, d2, ... , d_m}`
  - `QD = {s, d1, s1, d1s1, ... , s_d, d_m, s_md}`
- **Minimax Algorithm:**
  - `V(s) = max{V(s', r(s', s)) | s' in S}`
  - `V(s) = min{V(s', r(s', s)) | s' in S}`
- **Heuristics:** Functions that estimate the value of a node in the search space.

**Key Concepts:**

- **Search Trees:** Data structures used to represent the search space.
- **Graphs:** Representations of the search space as a network of nodes and edges.
- **States:** Representations of the current problem state.
- **Actions:** Possible moves in the search space.

**Important Examples:**

- **Tic-Tac-Toe:** A classic example of a problem-solving agent using Minimax Algorithm.
- **Robot Navigation:** A real-world example of using search algorithms to navigate through a space.
