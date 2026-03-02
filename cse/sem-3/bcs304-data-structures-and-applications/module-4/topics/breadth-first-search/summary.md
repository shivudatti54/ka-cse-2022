# Breadth First Search

## Overview

Breadth First Search (BFS) is a graph traversal algorithm that explores vertices level by level, visiting all neighbors of a vertex before moving on to neighbors of those neighbors. BFS uses a queue to process vertices in the order they are discovered and maintains a visited array to prevent revisiting vertices.

## Key Points

- BFS explores vertices level by level, starting from the source vertex.
- Uses a queue to process vertices in the order they are discovered.
- Maintains a visited array to prevent revisiting vertices.
- Guarantees the shortest path in unweighted graphs.
- Time complexity: O(V + E) for adjacency list representation.
- Space complexity: O(V) for the visited array and queue.

## Important Definitions

- **BFS Tree**: The tree formed by the tree edges discovered during BFS.
- **Level**: The distance from the source vertex to a vertex in the BFS tree.
- **Shortest Path**: The minimum number of edges between two vertices.

## Key Formulas / Syntax

- BFS Algorithm:
  1. Start at the source vertex, mark it as visited, and enqueue it.
  2. Dequeue a vertex from the front of the queue.
  3. For each unvisited neighbor of this vertex, mark it as visited and enqueue it.
  4. Repeat until the queue is empty.

## Comparisons

| Feature              | BFS                      | DFS                         |
| -------------------- | ------------------------ | --------------------------- |
| Data structure       | Queue (FIFO)             | Stack (LIFO) / Recursion    |
| Exploration strategy | Level by level (breadth) | As deep as possible (depth) |
| Shortest path        | Yes (unweighted graphs)  | No                          |

## Exam Tips

- Trace BFS carefully, showing the queue state at each step and the visited set.
- Explain the shortest path property of BFS and why DFS does not guarantee it.
- Remember that BFS must use a queue, and using a stack would change it to DFS.
- State the time complexity as O(V + E) for adjacency list representation.
- Mark a vertex as visited when you enqueue it, not when you dequeue it.
- Recall that the level of a vertex in the BFS tree equals the shortest distance from the source.
