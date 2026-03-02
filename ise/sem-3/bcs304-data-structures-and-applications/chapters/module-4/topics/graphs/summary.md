# GRAPHS - Summary

## Key Definitions and Concepts

- **Graph**: An ordered pair G = (V, E) where V is a set of vertices and E is a set of edges connecting pairs of vertices.
- **Directed Graph (Digraph)**: Graph where edges have a specific direction, represented as ordered pairs (u, v).
- **Undirected Graph**: Graph where edges have no direction; (u, v) is identical to (v, u).
- **Weighted Graph**: Graph where each edge carries a numerical weight representing cost, distance, or time.
- **Adjacent Vertices**: Two vertices connected by an edge.
- **Path**: Sequence of vertices where consecutive vertices are connected by edges.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected Graph**: Undirected graph with a path between every pair of vertices.
- **Strongly Connected**: Directed graph with directed paths between all vertex pairs.

## Important Formulas and Theorems

- **Complete Graph (Kn)**: Number of edges = n(n-1)/2 (undirected)
- **Tree with n vertices**: Exactly n-1 edges
- **BFS/DFS Time Complexity**: O(V + E) using adjacency list
- **Adjacency Matrix Space**: O(V²) regardless of edges
- **Adjacency List Space**: O(V + E)
- **Dijkstra's Algorithm**: O((V + E) log V) with priority queue
- **Kruskal's/Prim's MST**: O(E log V)
- **Floyd-Warshall**: O(V³) for all-pairs shortest path

## Key Points

1. Graphs model pairwise relationships and are fundamental to solving complex computational problems.

2. Choice between adjacency matrix and adjacency list depends on graph density - matrix for dense, list for sparse graphs.

3. BFS finds shortest path (by edges) in unweighted graphs and explores level by level using a queue.

4. DFS explores depth-first using recursion or explicit stack, essential for cycle detection and topological sort.

5. Topological sort orders vertices in DAG such that all edges point from earlier to later vertices.

6. Minimum spanning tree connects all vertices with minimum total edge weight; Kruskal's uses Union-Find, Prim's grows from a vertex.

7. Trees are connected acyclic graphs; forests are disjoint unions of trees.

8. Strongly connected components in directed graphs can be found using Kosaraju's or Tarjan's algorithm.

## Common Mistakes to Avoid

1. Confusing undirected and directed graph properties - direction matters for connectivity and path existence.

2. Using Dijkstra's algorithm with negative edge weights - it produces incorrect results; use Bellman-Ford instead.

3. Forgetting that adjacency matrix always uses O(V²) space even for sparse graphs with few edges.

4. Not checking for cycles before topological sort - topological ordering exists only for DAGs.

5. In BFS/DFS implementations, failing to mark vertices as visited leads to infinite loops.

## Revision Tips

1. Practice drawing both adjacency matrix and adjacency list representations for small graphs.

2. Manually trace BFS and DFS on sample graphs, recording the state of queue/stack at each step.

3. Memorize time and space complexities for all major graph operations and algorithms.

4. Solve previous year DU examination questions on graph representations and traversals.

5. Create a comparison table of graph algorithms with their time complexities, use cases, and constraints.