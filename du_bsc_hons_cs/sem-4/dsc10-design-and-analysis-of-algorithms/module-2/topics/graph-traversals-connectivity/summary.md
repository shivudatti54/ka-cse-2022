# Graph Traversals and Connectivity - Summary

## Key Definitions and Concepts

- **Graph Traversal**: Systematic process of visiting all vertices and edges in a graph exactly once.
- **BFS (Breadth-First Search)**: Level-by-level exploration using a FIFO queue; finds shortest path in unweighted graphs.
- **DFS (Depth-First Search)**: Goes deep along branches before backtracking; uses stack (explicit or recursion).
- **Connected Graph**: Undirected graph where a path exists between every pair of vertices.
- **Connected Component**: Maximal connected subgraph; cannot reach vertices outside the component.
- **Strongly Connected Component**: In directed graphs, a subset where every vertex can reach every other vertex.
- **Articulation Point**: Vertex whose removal disconnects the graph.
- **Bridge (Cut Edge)**: Edge whose removal disconnects the graph.

## Important Formulas and Theorems

- **BFS/DFS Time Complexity**: O(V + E) using adjacency list
- **BFS/DFS Space Complexity**: O(V) for queue/stack and visited array
- **Adjacency Matrix Space**: O(V²)
- **Adjacency List Space**: O(V + E)
- **Connected Graph Property**: For n vertices, at least n-1 edges required; complete graph K_n is maximally connected.

## Key Points

- BFS uses Queue (FIFO); DFS uses Stack (LIFO) or recursion
- BFS guarantees shortest path in unweighted graphs; DFS does not
- Both traversals visit each vertex and edge exactly once → O(V + E)
- Traversal is foundation for: cycle detection, topological sort, connected components, SCC finding
- A graph can have multiple connected components (disconnected graph)
- Strong connectivity only applies to directed graphs; regular connectivity applies to undirected graphs
- Choice between BFS/DFS depends on problem requirements (shortest path → BFS; topological sort → DFS)

## Common Mistakes to Avoid

1. **Forgetting to mark vertices as visited**: Leads to infinite loops, especially with cycles.
2. **Confusing BFS and DFS applications**: Using DFS for shortest path (incorrect) instead of BFS.
3. **Ignoring disconnected vertices**: Always iterate over ALL vertices, not just from one source.
4. **Wrong graph representation choice**: Using adjacency matrix for very sparse graphs wastes memory.
5. **Stack overflow with recursion**: Deep graphs (10⁴+ vertices) may cause stack overflow; use iterative version.

## Revision Tips

1. **Trace by hand**: Practice running BFS and DFS on paper for small graphs (5-7 vertices) until you can predict the visit order.
2. **Compare and contrast**: Make a table comparing BFS vs. DFS on parameters like data structure, applications, path properties.
3. **Code implementation**: Write both BFS and DFS from scratch multiple times until you can code them without参考.
4. **Focus on connectivity**: Understand how traversal helps determine components—this is frequently tested.
5. **Previous year questions**: Solve DU past papers on graph traversals to understand exam patterns and important topics.