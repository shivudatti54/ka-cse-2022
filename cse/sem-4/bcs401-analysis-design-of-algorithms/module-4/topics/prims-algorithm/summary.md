# Prim's Algorithm - Summary

## Key Definitions
- **Minimum Spanning Tree (MST)**: A spanning tree with minimum total edge weight in a connected, weighted, undirected graph
- **Cut Property**: The minimum weight edge crossing any cut (partition of vertices) belongs to some MST
- **Greedy Choice Property**: Selecting the minimum weight edge connecting the tree to a new vertex preserves optimality
- **Spanning Tree**: A connected acyclic subgraph containing all vertices of the original graph

## Important Formulas
- **Array Implementation**: T(n) = O(V²) — optimal for dense graphs where E ≈ V²
- **Binary Heap Implementation**: T(n) = O(E log V) — efficient for sparse graphs
- **Fibonacci Heap Implementation**: T(n) = O(E + V log V) — theoretical optimum

## Key Points
- Prim's Algorithm is a greedy algorithm that builds MST by adding one vertex at a time
- The algorithm starts from an arbitrary vertex and grows the tree outward
- The cut property guarantees correctness: minimum edge crossing any cut belongs to MST
- Three implementations exist with different time complexities suited for different graph types
- For dense graphs (E ≈ V²), the simple O(V²) array implementation outperforms heap-based approaches
- The algorithm produces a single connected tree unlike Kruskal's which builds a forest
- Space complexity varies: O(V) for arrays, O(V+E) for heap implementations

## Common Mistakes
- Confusing Prim's with Dijkstra's (though similar, Dijkstra's finds shortest paths, not MST)
- Selecting the wrong implementation for the graph type, leading to suboptimal performance
- Forgetting that Prim's requires a connected graph; disconnected graphs have no spanning tree
- Mishandling edges when both endpoints are already in the tree (such edges are skipped)
- Assuming equal edge weights simplifies only the result, not the algorithmic steps