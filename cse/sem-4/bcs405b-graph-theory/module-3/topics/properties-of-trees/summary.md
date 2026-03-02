# Properties of Trees - Summary

## Key Definitions and Concepts

- **Tree**: A connected acyclic graph (no cycles)
- **Forest**: An acyclic graph (may be disconnected); each component is a tree
- **Leaf/Pendant Vertex**: A vertex of degree 1 in a tree
- **Internal/Branch Vertex**: A vertex with degree greater than 1
- **Spanning Tree**: A subgraph that is a tree containing all vertices of the original graph
- **Rooted Tree**: A tree with a distinguished vertex designated as the root
- **Binary Tree**: A rooted tree where each vertex has at most two children
- **Center of Tree**: Vertex(s) minimizing maximum distance to all other vertices
- **Minimum Spanning Tree (MST)**: A spanning tree with minimum total edge weight

## Important Formulas and Theorems

- **Edge Count**: A tree with n vertices has exactly (n - 1) edges
- **Leaf Count**: A tree with more than 2 vertices has at least 2 leaves
- **Cayley's Formula**: Complete graph Kₙ has n^(n-2) distinct spanning trees
- **Spanning Tree Edges**: For connected graph with n vertices and m edges, spanning tree has (n - 1) edges; remove (m - n + 1) edges
- **Center Property**: Tree center is 1 vertex if diameter is even, 2 adjacent vertices if diameter is odd
- **Binary Tree Formula**: For proper binary tree with n vertices, i internal vertices, l leaves: n = 2i + 1 and l = i + 1
- **Radius-Diameter**: For any tree: radius ≤ diameter ≤ 2 × radius

## Key Points

1. A graph is a tree if and only if it is connected and has (n-1) edges (for n vertices)
2. Every edge in a tree is a bridge—removing it disconnects the graph
3. Between any two vertices in a tree, exactly one unique path exists
4. The leaf pruning method finds the tree center by iteratively removing all leaves
5. Every connected graph has at least one spanning tree
6. Adding any edge to a tree creates exactly one cycle
7. Trees are minimally connected graphs—they have maximum vertices with minimum edges
8. The complete graph Kₙ provides the maximum possible spanning trees (n^(n-2))

## Common Mistakes to Avoid

1. Confusing forests with trees—remember trees must be connected
2. Forgetting that a single vertex graph (K₁) is also a tree
3. Incorrectly counting edges—always verify: |E| = |V| - 1 for trees
4. Confusing the number of children with degree in rooted trees (parent edge counts as 1 in degree)
5. Applying Cayley's Formula to incomplete graphs—it only works for complete graphs

## Revision Tips

1. Practice identifying trees vs. non-trees using the characterization theorems
2. Solve multiple problems on finding tree centers using the pruning method
3. Memorize Cayley's Formula and practice its application to Kₙ
4. Understand the relationship: connected graph → spanning tree → remove edges
5. Review the leaf and internal vertex relationships in binary trees
6. Draw various tree types (path, star, binary) to visualize properties
7. Solve previous year university exam questions on tree properties
