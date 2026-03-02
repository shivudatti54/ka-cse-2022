# Iterative Deepening Depth-First Search

### Introduction

Iterative Deepening Depth-First Search (IDDFS) is a popular search algorithm used in Artificial Intelligence to find the shortest path between two nodes in a graph or a maze. In this study material, we will explore the concept of IDDFS, its advantages, and its implementation.

### Definition

Iterative Deepening Depth-First Search is a variant of Depth-First Search (DFS) that uses a combination of DFS and Breadth-First Search (BFS) to find the shortest path between two nodes.

### Key Concepts

- **Depth-First Search (DFS)**: A search algorithm that explores as far as possible along each branch before backtracking.
- **Breadth-First Search (BFS)**: A search algorithm that explores all the nodes at a given depth before moving to the next depth level.
- **Iterative Deepening**: A technique used to increase the depth of the search by incrementally increasing the maximum depth explored by the algorithm.
- **Graph**: A non-linear data structure consisting of nodes (or vertices) connected by edges.

### How IDDFS Works

1.  **Initialization**: Initialize a queue with the starting node and a maximum depth.
2.  **Exploration**: Explore the nodes in the queue using DFS.
3.  **Backtracking**: If the queue is empty, backtrack to the previous node and increase the maximum depth.
4.  **Termination**: The algorithm terminates when the destination node is found or the maximum depth is reached.

### Example

Suppose we have a graph with the following nodes and edges:

| Node | Edge |
| ---- | ---- |
| A    | B    |
| A    | C    |
| B    | D    |
| C    | D    |
| D    | E    |

We want to find the shortest path from node A to node E using IDDFS.

1.  **Initialization**: Initialize a queue with node A and a maximum depth of 1.
2.  **Exploration**: Explore the nodes in the queue using DFS. We visit nodes A, B, and C.
3.  **Backtracking**: Increase the maximum depth to 2 and explore the remaining nodes.
4.  **Exploration**: We visit nodes D and E.
5.  **Termination**: We find the shortest path from node A to node E, which is A -> B -> D -> E.

### Code Implementation

Here is a Python implementation of IDDFS:

```python
from collections import deque

def iddfs(graph, start, goal, max_depth):
    queue = deque([(start, [start], 0)])
    visited = set()

    while queue:
        node, path, depth = queue.popleft()
        if node == goal:
            return path

        if depth >= max_depth:
            continue

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], depth + 1))
                visited.add(neighbor)

    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

start = 'A'
goal = 'E'
max_depth = 2

path = iddfs(graph, start, goal, max_depth)
if path:
    print(f"Shortest path from {start} to {goal}: {path}")
else:
    print(f"No path from {start} to {goal}")
```

### Advantages

- **Guaranteed to find the shortest path**: IDDFS is guaranteed to find the shortest path between two nodes in an unweighted graph.
- **Efficient use of memory**: IDDFS uses a queue data structure to store the nodes to be explored, which makes it efficient in terms of memory usage.

### Disadvantages

- **Slow performance for large graphs**: IDDFS can be slow for large graphs due to its iterative deepening nature.
- **Not suitable for weighted graphs**: IDDFS is not suitable for weighted graphs, as it does not take into account the weights of the edges.

In conclusion, Iterative Deepening Depth-First Search is a powerful search algorithm that can be used to find the shortest path between two nodes in a graph or a maze. Its advantages include guaranteed shortest path and efficient use of memory. However, it may not be suitable for large graphs or weighted graphs.
