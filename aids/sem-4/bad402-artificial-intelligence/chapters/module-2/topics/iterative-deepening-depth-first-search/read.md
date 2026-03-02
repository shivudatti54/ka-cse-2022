# Iterative Deepening Depth-First Search

## Table of Contents

- [What is Iterative Deepening Depth-First Search?](#what-is-iterative-deepening-depth-first-search)
- [How Does Iterative Deepening Depth-First Search Work?](#how-does-iterative-deepening-depth-first-search-work)
- [Example Problem](#example-problem)
- [Advantages and Disadvantages](#advantages-and-disadvantages)
- [Implementation](#implementation)

## What is Iterative Deepening Depth-First Search?

Iterative Deepening Depth-First Search (IDDFS) is a variant of the depth-first search algorithm that uses a two-step process to find the shortest path between two nodes in a graph. The algorithm combines the benefits of iterative deepening and depth-first search to efficiently search large graphs.

## How Does Iterative Deepening Depth-First Search Work?

IDDFS works by incrementally increasing the search depth until the target node is found. The process involves the following steps:

- Initialize the search depth to 0
- Perform a depth-first search with the current search depth
- If the target node is not found, increment the search depth by 1 and repeat the process
- Continue incrementing the search depth until the target node is found

## Key Concepts

- **Search Depth**: The maximum distance a node can be from the current node in the search tree
- **Iterative Deepening**: A process of incrementally increasing the search depth until the target node is found
- **Depth-First Search**: A search algorithm that explores as far as possible along each branch before backtracking

## How IDDFS Works

Here's a step-by-step example of how IDDFS works:

1.  Initialize the search depth to 0
2.  Perform a depth-first search with search depth 0
3.  If the target node is not found, increment the search depth to 1 and repeat the process
4.  Perform a depth-first search with search depth 1
5.  If the target node is not found, increment the search depth to 2 and repeat the process
6.  Perform a depth-first search with search depth 2
7.  If the target node is found, return the path to the target node

## Example Problem

Consider a graph with the following nodes and edges:

| Node | Edge |
| ---- | ---- |
| A    | B    |
| A    | C    |
| B    | D    |
| C    | D    |
| D    | E    |
| E    | F    |

Find the shortest path from node A to node F using IDDFS.

## Implementation

Here's an example implementation of IDDFS in Python:

```python
from collections import deque

def iddfs(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, depth = queue.popleft()

        if node == target:
            return [node, start, target]

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))

    return None

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

# Find the shortest path from A to F
path = iddfs(graph, 'A', 'F')

if path:
    print("Shortest path:", path)
else:
    print("Target node not found")
```

## Advantages and Disadvantages

Advantages:

- **Efficient search**: IDDFS is efficient for searching large graphs because it uses a two-step process to find the shortest path.
- **Found shortest path**: IDDFS always finds the shortest path between two nodes.

Disadvantages:

- **Not suitable for unweighted graphs**: IDDFS is not suitable for unweighted graphs because it assumes that the graph has a weight function to guide the search.
- **High memory usage**: IDDFS requires a significant amount of memory to store the search queue, which can be a problem for large graphs.

## Conclusion

Iterative Deepening Depth-First Search (IDDFS) is a powerful algorithm for finding the shortest path between two nodes in a graph. Its two-step process of incrementally increasing the search depth and performing a depth-first search makes it efficient for searching large graphs. However, IDDFS may not be suitable for unweighted graphs and requires significant memory to store the search queue.
