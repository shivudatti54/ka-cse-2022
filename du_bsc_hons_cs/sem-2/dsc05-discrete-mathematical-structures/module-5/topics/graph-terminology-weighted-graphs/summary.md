# Graph Terminology and Weighted Graphs - Summary

## Key Definitions and Concepts

- **Graph G = (V, E)**: Mathematical structure with vertices V and edges E connecting vertex pairs
- **Simple Graph**: No loops or parallel edges
- **Directed Graph (Digraph)**: Edges have direction, represented as ordered pairs (u, v)
- **Undirected Graph**: Edges have no direction, represented as unordered pairs {u, v}
- **Degree**: Number of edges incident to a vertex; in directed graphs, separate in-degree and out-degree
- **Complete Graph (Kₙ)**: Every pair of distinct vertices connected; has n(n-1)/2 edges
- **Bipartite Graph**: Vertices can be partitioned into two sets U and V with all edges between sets
- **Connected Graph**: Path exists between every pair of vertices
- **Tree**: Connected graph with no cycles; n vertices has n-1 edges
- **Weighted Graph**: Graph where each edge has an associated numerical weight/cost
- **Shortest Path**: Path between two vertices with minimum total edge weight

## Important Formulas and Theorems

- **Handshaking Lemma**: Σ deg(v) = 2|E| for undirected graphs
- **Complete Graph Edges**: |E| = n(n-1)/2 for Kₙ
- **Tree Edge Count**: |E| = |V| - 1
- **Eulerian Circuit**: Exists if connected and all vertices have even degree
- **Planar Graph Formula**: V - E + F = 2 (Euler's formula)

## Key Points

- Weighted graphs extend basic graphs by assigning costs to edges, enabling optimization problems
- Dijkstra's algorithm finds shortest paths in O(V²) or O(E log V) time with non-negative weights
- Minimum Spanning Tree (MST) connects all vertices with minimum total weight; Kruskal's sorts edges, Prim's grows from a vertex
- Complete graphs grow quadratically; K₅ is the smallest non-planar graph
- Bipartite graphs have no odd-length cycles and can be 2-colored
- Path length is counted in edges, not vertices
- In weighted graphs, path weight is sum of all edge weights

## Common Mistakes to Avoid

- Confusing "complete" with "connected" - they are different properties
- Forgetting that degree counts edges, not vertices in the neighborhood
- Applying Dijkstra's algorithm with negative edge weights (it won't work correctly)
- Counting path length in vertices instead of edges
- Not checking for cycles when building spanning trees or paths

## Revision Tips

1. Practice drawing different graph types (complete, bipartite, tree) to build visual intuition
2. Trace Dijkstra's algorithm multiple times until you can do it without errors
3. Memorize the conditions for Eulerian paths and circuits—they frequently appear in exams
4. Use the Handshaking Lemma as a quick check for degree sequence validity
5. Relate weighted graphs to real scenarios like road networks or flight routes for better understanding