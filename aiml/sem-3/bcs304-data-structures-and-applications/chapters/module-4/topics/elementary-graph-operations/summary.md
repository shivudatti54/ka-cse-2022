# Elementary Graph Operations - Summary

## Key Definitions and Concepts

- **Adjacency Matrix:** 2D array representation where matrix[i][j] = 1 indicates an edge from i to j. Space: O(V²), edge lookup: O(1).

- **Adjacency List:** Array of lists where each list contains neighbors of a vertex. Space: O(V+E), edge lookup: O(degree).

- **BFS (Breadth-First Search):** Traverses level by level using a queue. Finds shortest path in unweighted graphs. Time: O(V+E).

- **DFS (Depth-First Search):** Explores depth-wise using a stack or recursion. Used for cycle detection, topological sort. Time: O(V+E).

## Important Formulas and Theorems

- For undirected graphs: Sum of all degrees = 2 × |E|
- For directed graphs: Sum of in-degrees = Sum of out-degrees = |E|
- BFS/DFS time complexity: O(V + E) for adjacency list, O(V²) for adjacency matrix
- Space complexity for BFS: O(V) for queue and visited array
- Space complexity for DFS: O(V) for stack (recursive) or visited array

## Key Points

- BFS uses FIFO queue; DFS uses LIFO stack or recursion
- Adjacency matrix suits dense graphs; adjacency list suits sparse graphs
- Always mark vertices as visited when enqueued (BFS) or before exploring neighbors (DFS)
- In-degree = count of edges pointing TO a vertex; out-degree = count of edges pointing FROM a vertex
- Adding/removing vertices in adjacency matrix requires O(V²) reconstruction
- Edge removal in adjacency list requires searching the linked list: O(degree)
- Both BFS and DFS visit each vertex exactly once when graph is connected

## Common Mistakes to Avoid

- Forgetting to mark vertices as visited, leading to infinite loops in traversal
- Confusing in-degree and out-degree calculations in directed graphs
- Using BFS for problems requiring deep exploration where DFS is more suitable
- Not considering the graph representation when determining operation complexity
- Attempting to add edges between non-existent vertices

## Revision Tips

1. Practice implementing BFS and DFS on paper with small graphs to understand the step-by-step execution.

2. Memorize the key differences between adjacency matrix and adjacency list through comparison tables.

3. Remember the relationship between vertices, edges, and degrees using the handshaking lemma.

4. Solve previous year DU examination questions on graph traversals to understand the exam pattern.