# Elementary Graph Operations - Summary

## Key Definitions and Concepts

- **Adjacency Matrix:** A V × V array where matrix[i][j] = 1 indicates an edge from i to j. Space: O(V²). Edge lookup: O(1).

- **Adjacency List:** An array of lists where index i contains all neighbors of vertex i. Space: O(V + E). Edge lookup: O(degree).

- **BFS (Breadth-First Search):** Traverses level by level using a queue. Guarantees shortest path in unweighted graphs. Time: O(V + E).

- **DFS (Depth-First Search):** Explores deeply before backtracking, using stack or recursion. Used for cycle detection, topological sort. Time: O(V + E).

## Important Formulas and Theorems

- **Space Complexity - Adjacency Matrix:** O(V²)
- **Space Complexity - Adjacency List:** O(V + E)
- **Time Complexity - Add Edge (Matrix):** O(1)
- **Time Complexity - Add Edge (List):** O(1)
- **Time Complexity - Remove Vertex (Matrix):** O(V²)
- **Time Complexity - Remove Vertex (List):** O(V + E)
- **BFS/DFS Time Complexity:** O(V + E) for adjacency list, O(V²) for matrix

## Key Points

- For sparse graphs (E << V²), adjacency list is preferred; for dense graphs, matrix may be better.

- BFS uses a queue and visits all neighbors at current depth before moving deeper.

- DFS can be implemented recursively (uses call stack) or iteratively (explicit stack).

- In undirected graphs with adjacency matrix, the matrix is always symmetric.

- Removing a vertex is the most expensive operation in both representations.

- Edge existence check is O(1) in matrix but O(degree) in adjacency list.

- In-degree and out-degree are computed differently for directed graphs.

## Common Mistakes to Avoid

- Confusing when to use BFS versus DFS—they serve different purposes.

- Forgetting that adjacency matrix requires O(V²) space regardless of edge count.

- Not marking vertices as visited during traversal, leading to infinite loops.

- Assuming undirected graph edge removal is the same as directed—must remove from both adjacency lists.

- Using recursive DFS for very large graphs may cause stack overflow.

## Revision Tips

- Practice implementing both BFS and DFS on paper with small graphs.

- Create a comparison table of all operations with their time/space complexities.

- Trace through traversal algorithms step-by-step to understand the order of vertex visits.

- Remember: BFS = Queue (first in, first out), DFS = Stack (last in, first out) or recursion.