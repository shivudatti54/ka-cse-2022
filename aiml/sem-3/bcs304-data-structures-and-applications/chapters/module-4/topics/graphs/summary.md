# GRAPHS - Summary

## Key Definitions and Concepts

- GRAPH: An ordered pair G = (V, E) where V is a set of vertices and E is a set of edges connecting vertex pairs.
- VERTEX: A fundamental unit representing an entity in a graph.
- EDGE: A connection between two vertices, can be directed (ordered pair) or undirected (unordered pair).
- DEGREE: In undirected graphs, the number of edges incident to a vertex. In directed graphs, separate in-degree and out-degree.
- PATH: A sequence of vertices where consecutive vertices are connected by edges.
- CYCLE: A path that starts and ends at the same vertex.
- CONNECTED GRAPH: An undirected graph where a path exists between every pair of vertices.

## Important Formulas and Theorems

- HANDSHAKING LEMMA: Σ deg(v) = 2|E| for any undirected graph
- For directed graphs: Σ indeg(v) = Σ outdeg(v) = |E|
- Adjacency Matrix Space: O(V²)
- Adjacency List Space: O(V + E)
- BFS Time Complexity: O(V + E) using adjacency list
- DFS Time Complexity: O(V + E) using adjacency list

## Key Points

- GRAPHS MODEL pairwise relationships between objects in non-linear fashion
- Undirected graphs represent symmetric relationships; directed graphs represent asymmetric relationships
- Adjacency matrix provides O(1) edge lookup but requires O(V²) space
- Adjacency list provides O(V + E) space and is preferred for sparse graphs
- BFS uses a queue and visits vertices level-by-level, useful for shortest paths in unweighted graphs
- DFS uses recursion/stack and explores depth-first, useful for cycle detection and topological sort
- A graph with no cycles is called an ACYCLIC graph
- A directed acyclic graph is called a DAG

## Common Mistakes to Confusing adjacency matrix row and column indices when representing edges

- Forgetting that adjacency matrix for undirected graphs is symmetric
- Not initializing the queue in BFS implementation
- Getting infinite recursion in DFS due to not marking vertices as visited
- Confusing weak connectivity with strong connectivity in directed graphs

## Revision Tips

1. DRAW sample graphs and practice converting between adjacency matrix and adjacency list representations manually.
2. MEMORIZE the time and space complexities for both representations.
3. PRACTICE implementing BFS and DFS on paper for small graphs to understand the traversal order.
4. REMEMBER key properties: BFS for shortest path in unweighted graphs, DFS for topological sorting and cycle detection.