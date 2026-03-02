# Iterative Deepening Depth-First Search

### Definition

Iterative Deepening Depth-First Search (IDDFS) is a variant of the Depth-First Search (DFS) algorithm that combines the benefits of both Breadth-First Search (BFS) and DFS.

### Key Points

- **Algorithm**:
  - Start with DFS and set a limit (max depth) to explore only a certain depth.
  - If the goal is not found at the current depth, increase the depth limit and retry DFS.
- **Pseudocode**:
  ```python
  function IDDFS(graph, goal, max_depth):
  explored = set()
  for depth in range(1, max_depth + 1):
  result = dfs(graph, goal, depth, explored)
  if result != None:
  return result
  return None

```
*   **Time Complexity**:
    *   O(b^d) in the worst case, where b is the branching factor and d is the depth of the goal.
*   **Space Complexity**:
    *   O(b^d) due to the recursive call stack.

### Important Formulas and Theorems

*   **Depth-First Search (DFS) Formula**:
    *   d = |V| + |E| - n, where d is the depth of the goal, |V| is the number of vertices, |E| is the number of edges, and n is the number of nodes.
*   **A* Search Theorem**:
    *   IDDFS is equivalent to A* search with a heuristic function that returns 0 when the goal is found.

### Key Theorems

*   **IDDFS Completeness**:
    *   IDDFS is complete if the graph is connected and the goal is reachable from any node.
*   **IDDFS Optimality**:
    *   IDDFS is optimal if the heuristic function is admissible and consistent.

### Important Definitions

*   **Breadth-First Search (BFS)**: A search algorithm that explores all nodes at a given depth before moving on to the next depth level.
*   **Depth-First Search (DFS)**: A search algorithm that explores as far as possible along each branch before backtracking.
*   **Branching Factor**: The average number of edges incident on a node in the graph.
```
