# Different Representations of Planar Graphs - Summary

## Key Definitions and Concepts

- **Planar Graph**: A graph that can be drawn on a plane without edge crossings. A specific drawing is called a plane graph.
- **Face**: A region bounded by edges in a planar embedding. The unbounded region is the outer face.
- **Planar Embedding**: A particular way of drawing a planar graph without edge crossings.
- **Dual Graph (G\*)**: A graph where vertices represent faces of the original graph, and edges exist between faces sharing a common boundary.
- **Half-Edge (DCEL)**: A data structure with vertices, half-edges, and faces for efficient planar subdivision representation.

## Important Formulas and Theorems

- **Euler's Formula**: n - m + f = 2 (for connected planar graphs)
- **Edge Bound**: m ≤ 3n - 6 (for simple planar graphs with n ≥ 3)
- **Face Bound**: f ≤ 2n - 4
- **Minimum Degree**: δ(G) ≤ 5 for any planar graph with n ≥ 3
- **Fáry's Theorem**: Every planar graph has a straight-line embedding

## Key Points

1. Planar graphs can be represented geometrically (visual embeddings) or combinatorially (data structures).

2. Adjacency matrix provides O(1) edge lookup but requires O(n²) space, unsuitable for large sparse planar graphs.

3. Adjacency list is space-efficient with O(n + m) complexity and ideal for graph traversal operations.

4. Half-edge (DCEL) structure is optimal for face-related operations and planar subdivisions.

5. The dual of a connected planar graph (G*) has the property that (G*)\* ≅ G.

6. For planar graphs, m ≤ 3n - 6 provides a necessary condition to verify planarity.

7. Geometric representations include straight-line, radial, circular, and grid embeddings.

8. Fáry's theorem guarantees that any planar graph can be drawn with straight-line edges.

9. Face adjacency list stores cyclic order of edges for each face, enabling efficient face traversal.

10. The choice of representation depends on the operations to be performed on the graph.

## Common Mistakes to Avoid

- Confusing a planar graph (the abstract graph) with a plane graph (a specific embedding)
- Applying m ≤ 3n - 6 for graphs with n < 3 or for non-simple graphs
- Forgetting that the outer face counts in the face count for Euler's formula
- Assuming the dual of a disconnected graph preserves all properties

## Revision Tips

1. Practice drawing different representations for the same planar graph to build intuition.

2. Memorize Euler's formula and the edge bound - these are most frequently tested.

3. For each representation type, remember one advantage and one disadvantage.

4. When solving problems, first check the necessary condition (m ≤ 3n - 6) before attempting complex planarity testing.

5. Understand the dual graph construction through examples - draw a simple planar graph and its dual side by side.
