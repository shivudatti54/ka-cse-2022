# Graphs: Types and Representations - Summary

## Key Definitions and Concepts

- **Graph G = (V, E)**: Consists of vertices V (nodes) and edges E (connections between vertex pairs)
- **Directed Graph**: Edges have direction; edges are ordered pairs (u,v)
- **Undirected Graph**: Edges have no direction; edges are unordered sets {u,v}
- **Simple Graph**: No loops and no multiple edges
- **Multigraph**: May have multiple edges between vertices
- **Adjacent Vertices**: Two vertices connected by an edge
- **Degree of Vertex**: Number of edges incident to the vertex
- **Isolated Vertex**: Degree = 0
- **Pendant Vertex**: Degree = 1 (leaf)

## Important Formulas and Theorems

- **Handshaking Lemma**: Σdeg(v) = 2|E| for any undirected graph
- **Complete Graph Kₙ**: n(n-1)/2 edges
- **Complete Bipartite Kₘ,ₙ**: m × n edges
- **Tree with n vertices**: Exactly n-1 edges
- **Adjacency Matrix Space**: O(V²)
- **Adjacency List Space**: O(V + E)

## Key Points

1. Graphs model pairwise relationships between objects in diverse applications
2. Complete graphs (Kₙ) have maximum edges; cycle graphs (Cₙ) form simple loops
3. Bipartite graphs can be 2-colored with no adjacent vertices sharing colors
4. Trees are connected acyclic graphs; forests are collections of trees
5. DAGs (Directed Acyclic Graphs) are essential for topological ordering
6. Planar graphs can be drawn without edge crossings; Euler's formula: V - E + F = 2
7. Adjacency matrices provide O(1) edge lookup but consume O(V²) space
8. Adjacency lists are space-efficient for sparse graphs O(V + E)
9. The choice of representation depends on graph density and required operations
10. In-degree and out-degree apply to directed graphs; sum equals number of edges

## Common Mistakes to Avoid

1. Forgetting that loops contribute 1 to degree (not 2) in undirected graphs
2. Confusing complete bipartite Kₘ,ₙ with complete graph Kₙ—they have different edge counts
3. Using adjacency matrix for very large sparse graphs (wastes memory)
4. Assuming all graphs are connected—always check connectivity when required
5. Mixing up directed and undirected graph properties (e.g., degree calculations differ)

## Revision Tips

1. Practice drawing different graph types: Kₙ, Cₙ, Pₙ, Wₙ, Qₙ
2. Memorize the number of edges in complete and complete bipartite graphs
3. Always apply Handshaking Lemma first when solving degree problems
4. Remember: sparse graphs → adjacency lists; dense graphs → adjacency matrices
5. Create a comparison table of all graph types with their properties for quick revision