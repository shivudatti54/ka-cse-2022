# Cut-Sets and Cut-Vertices - Summary

## Key Definitions and Concepts

- **Cut-Vertex (Articulation Point)**: A vertex v in a connected graph G such that G - v (removing v and its incident edges) becomes disconnected. The removal increases the number of connected components.

- **Bridge (Cut-Edge)**: An edge e whose removal disconnects the graph. An edge is a bridge if and only if it does not belong to any cycle.

- **Cut-Set (Edge Cut)**: A minimal set of edges whose removal disconnects the graph. A set S is a cut-set if G - S is disconnected but G - S' is connected for any proper subset S'.

- **Biconnected Graph**: A graph with no cut-vertices (also called 2-vertex-connected).

- **Block**: A maximal biconnected subgraph (no cut-vertices within it).

## Important Formulas and Theorems

- **Edge Connectivity**: λ(G) = minimum number of edges whose removal disconnects G
- **Vertex Connectivity**: κ(G) = minimum number of vertices whose removal disconnects G
- **Key Inequality**: κ(G) ≤ λ(G) ≤ δ(G), where δ(G) is the minimum degree
- **Bridge Condition**: Edge e = (u,v) is a bridge iff it lies on no cycle

## Key Points

1. All bridges in a graph are edges of its spanning trees; removing any non-bridge edge maintains connectivity.

2. In a tree, every edge is a bridge, and every non-leaf vertex is a cut-vertex.

3. Complete graphs Kn have no cut-vertices or bridges (κ = λ = n-1).

4. The DFS algorithm finds cut-vertices using discovery times (disc[]) and lowest reachability (low[]).

5. Root of DFS tree is a cut-vertex if it has ≥2 children; non-root v is cut-vertex if ∃ child c with low[c] ≥ disc[v].

6. A block-cut graph is bipartite, connecting biconnected components to their articulation points.

7. Edge connectivity λ(G) equals the number of edges in a minimum cut-set.

## Common Mistakes to Avoid

1. **Confusing bridges with cut-vertices**: Remember bridges are edges, cut-vertices are vertices.

2. **Forgetting leaf nodes in trees**: Leaf nodes (degree 1) are NOT cut-vertices even in trees.

3. **Ignoring edge direction**: In undirected graphs, edges have no direction; always consider both endpoints.

4. **Incorrect low value calculation**: Low[v] must consider back edges to ancestors, not descendants.

## Revision Tips

1. Practice identifying cut-vertices and bridges by inspection for small graphs.

2. Memorize the inequality κ(G) ≤ λ(G) ≤ δ(G) - this is frequently tested.

3. For DFS-based problems, practice the algorithm with at least 3-4 examples.

4. Remember: "Bridge = no cycle" is the fastest way to identify bridges in simple graphs.
