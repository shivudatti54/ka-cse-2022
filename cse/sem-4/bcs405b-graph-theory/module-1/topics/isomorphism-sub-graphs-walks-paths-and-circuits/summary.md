# Isomorphism, Subgraphs, Walks, Paths and Circuits - Summary

## Key Definitions

- **Graph Isomorphism**: Graphs G₁ = (V₁, E₁) and G₂ = (V₂, E₂) are isomorphic if there exists a bijective function f: V₁ → V₂ preserving adjacency; denoted G₁ ≅ G₂.

- **Subgraph**: H = (V(H), E(H)) is a subgraph of G if V(H) ⊆ V(G) and E(H) ⊆ E(G).

- **Spanning Subgraph**: A subgraph containing all vertices of the original graph.

- **Induced Subgraph**: G[S] for S ⊆ V(G) contains exactly those edges of G with both endpoints in S.

- **Walk**: Sequence v₀, e₁, v₁, ..., e_k, v_k where each e_i connects v_{i-1} and v_i.

- **Trail**: A walk with all edges distinct.

- **Path**: A walk with all vertices distinct.

- **Circuit**: A closed trail (length ≥ 3) returning to its starting vertex.

- **Cycle**: A circuit with all vertices except the start/end distinct (simple closed path).

- **Distance d(u,v)**: Length of the shortest path between vertices u and v.

## Important Formulas

- Path of length k has k+1 vertices and k edges
- A cycle C_n has exactly n vertices and n edges
- Distance satisfies metric properties: d(u,v) ≥ 0, d(u,v) = d(v,u), d(u,v) ≤ d(u,w) + d(w,v)
- Diameter = max{d(u,v)} over all vertex pairs; Radius = min{ecc(v)} over all vertices
- Eccentricity ecc(v) = max{d(v,u)} for all u in the same component

## Key Points

1. Graph isomorphism preserves: number of vertices, number of edges, degree sequence, connectivity, and cycle structure.

2. Isomorphism is an equivalence relation, partitioning the set of all graphs into isomorphism classes.

3. Identical invariants (degree sequence, vertex count) are necessary but not sufficient for isomorphism.

4. Every path is a trail, and every trail is a walk; every cycle is a circuit but not vice versa.

5. An induced subgraph on S ⊆ V(G) includes ALL edges of G with both endpoints in S.

6. A spanning subgraph uses all vertices but may omit edges; essential for studying edge-dependent properties.

7. The distance function defines a metric on each connected component of a graph.

8. A graph is connected if and only if every pair of vertices has a finite distance between them.

9. The complement of a subgraph H in G contains all edges of G not in H.

10. Vertex repetitions in walks can be analyzed to extract paths, trails, or cycles as substructures.

## Common Mistakes

1. **Confusing isomorphism with equality**: Isomorphic graphs may have different vertex labels; the bijection maps one labeling to another.

2. **Omitting edges in induced subgraphs**: Students often forget that induced subgraphs must include ALL edges between selected vertices, not just a subset.

3. **Incorrectly classifying circuits as cycles**: A circuit may repeat vertices (other than the start/end), while a cycle never does.

4. **Forgetting that paths have distinct vertices**: A walk with repeated vertices is NOT a path, regardless of edge uniqueness.

5. **Assuming degree sequence equality implies isomorphism**: Counterexamples exist (e.g., certain regular graphs of the same degree can be non-isomorphic).