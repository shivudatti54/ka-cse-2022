# Graph Representations, BFS and DFS - Summary

## Key Definitions and Concepts

- **Graph:** A non-linear data structure G = (V, E) where V is a set of vertices and E is a set of edges connecting vertex pairs.
- **Adjacency Matrix:** A V × V 2D array where adj[i][j] = 1 indicates an edge between vertices i and j.
- **Adjacency List:** An array of lists where each list contains the neighbors of a vertex.
- **BFS (Breadth-First Search):** A traversal technique that explores vertices level by level using a FIFO queue.
- **DFS (Depth-First Search):** A traversal technique that explores as deep as possible along each branch before backtracking using a LIFO stack.

## Important Formulas and Theorems

- **Adjacency Matrix Space:** O(V²)
- **Adjacency List Space:** O(V + E)
- **BFS Time Complexity:** O(V + E)
- **DFS Time Complexity:** O(V + E)
- **BFS Space Complexity:** O(V)
- **DFS Space Complexity:** O(V)

## Key Points

- BFS uses a queue and visits all neighbors at distance d before visiting vertices at distance d+1.
- DFS uses recursion (stack) and explores as far as possible before backtracking.
- For unweighted graphs, BFS finds the shortest path from source to any reachable vertex.
- Adjacency list is preferred for sparse graphs (E << V²); adjacency matrix for dense graphs.
- Always initialize visited array before starting traversal.
- Handle disconnected graphs by iterating through all vertices and starting new traversals from unvisited vertices.
- BFS marks vertices visited when enqueuing; DFS marks vertices visited before recursive calls.

## Common Mistakes to Avoid

- Forgetting to mark a vertex as visited before adding to queue (causes infinite loops in BFS).
- Not handling disconnected graphs in exam questions.
- Confusing adjacency matrix row iteration (O(V)) with adjacency list iteration (O(degree)).
- Using BFS for problems requiring deep exploration or DFS for shortest path (when incorrect).
- Forgetting to add reverse edges in undirected graph implementations.

## Revision Tips

1. Practice implementing both BFS and DFS from memory - this is a common exam question.
2. Memorize the time-space complexity table for all representations and traversals.
3. Understand when to use BFS (shortest path, level order) vs DFS (cycle detection, topological sort).
4. Solve at least 3-4 graph problems covering connected components, path finding, and traversal variations.
5. Draw diagrams for graph traversals to visualize the order of vertex visits.