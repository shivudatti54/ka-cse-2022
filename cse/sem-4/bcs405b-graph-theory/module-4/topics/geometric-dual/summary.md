# Geometric Dual - Summary

## Key Definitions and Concepts

- **Geometric Dual (G\*)**: Given a connected planar graph G with a fixed planar embedding, the geometric dual G* is constructed by placing one vertex in each face of G, and connecting two vertices in G* if their corresponding faces share a common edge in G.

- **Self-Dual Graph**: A graph G is self-dual if G ≅ G\*. For such graphs with n vertices and e edges, the condition e = 2n - 2 must hold.

- **Face Counting**: A connected planar graph with n vertices, e edges, and f faces satisfies Euler's formula: n - e + f = 2.

## Important Formulas and Theorems

- **Vertex-Face Correspondence**: |V(G\*)| = number of faces in G = f
- **Edge Preservation**: |E(G\*)| = |E(G)| = e
- **Degree Relationship**: Degree of vertex v* in G* equals number of edges bounding the corresponding face in G
- **Euler's Formula for Dual**: |V(G*)| - |E(G*)| + |F(G\*)| = 2
- **Self-Dual Condition**: For self-dual graphs: e = 2n - 2
- **Duality Property**: (G*)* ≅ G for connected planar graphs without bridges

## Key Points

1. The geometric dual depends on the specific planar embedding; different embeddings yield different duals.

2. Bridges in the original graph create loops in the dual graph.

3. Multiple edges in the original graph may create multiple edges between vertices in the dual.

4. The dual of any planar graph is always planar.

5. The dual of a connected planar graph is always connected.

6. Common self-dual graphs include wheel graphs W₄, W₅, W₆,... and the complete graph K₂.

7. Each edge in G corresponds to exactly one edge in G*, but a vertex in G* may correspond to multiple edges in G (the boundary edges of a face).

8. The geometric dual is always defined for connected planar graphs; disconnected graphs require separate treatment for each component.

## Common Mistakes to Avoid

1. **Forgetting the Outer Face**: Always count the exterior region as a face when constructing the dual.

2. **Ignoring Edge Multiplicity**: When two faces share more than one edge (like in graphs with multiple edges), ensure multiple edges appear in the dual.

3. **Incorrect Loop Handling**: Edges on bridges or boundary edges create loops in the dual - do not forget to include them.

4. **Confusing Geometric and Combinatorial Duals**: Remember geometric dual requires a specific embedding, while combinatorial dual is more general.

## Revision Tips

1. Practice drawing duals for at least 5 different planar graphs to build confidence.

2. Always verify your constructed dual using Euler's formula as a sanity check.

3. Memorize the correspondence: vertices ↔ faces, edges ↔ edges, faces ↔ vertices.

4. Review wheel graphs Wₙ for n ≥ 4 as common examples of self-dual graphs.

5. Solve previous year university examination questions on geometric dual to understand the question patterns and marking schemes.
