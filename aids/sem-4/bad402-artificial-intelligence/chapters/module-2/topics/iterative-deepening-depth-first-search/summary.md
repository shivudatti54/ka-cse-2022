# Iterative Deepening Depth-First Search

### Definition

Iterative Deepening Depth-First Search (IDDFS) is a graph search algorithm that combines the benefits of Breadth-First Search (BFS) and Depth-First Search (DFS).

### Key Points

- **Algorithm**:
  - Start with DFS and set a maximum depth
  - If the goal is not found, increase the maximum depth and repeat the DFS
- **Pseudocode**:

```markdown
function IDDFS(graph, start, goal):
max_depth = 0
while true:
result = dfs(graph, start, goal, max_depth)
if result != null:
return result
max_depth += 1
```

- **Properties**:
  - **Optimality**: IDDFS is optimal because it explores all nodes at each depth before moving on to the next depth
  - **Completeness**: IDDFS is complete because it guarantees to find the goal if it exists
- **Time and Space Complexity**:
  - Time: O(b^d) where b is the branching factor and d is the maximum depth
  - Space: O(b^d)
- **Theorem**: IDDFS is guaranteed to find the shortest path to the goal if the graph is unweighted and the goal is reachable.

### Important Formulas

- **Depth-First Search**:

```markdown
function dfs(graph, start, goal, max_depth):
if max_depth <= 0 or start == goal:
return start
for neighbor in graph[start]:
if neighbor == goal:
return neighbor
result = dfs(graph, neighbor, goal, max_depth - 1)
if result != null:
return result
return null
```

- **Iterative Deepening**:

```markdown
function iterative_deepening_dfs(graph, start, goal):
max_depth = 1
while true:
result = dfs(graph, start, goal, max_depth)
if result != null:
return result
max_depth += 1
```

### Notes

- IDDFS is often used for solving mazes and other types of graph-based problems
- It can be implemented using a queue to keep track of the maximum depth to explore at each step
