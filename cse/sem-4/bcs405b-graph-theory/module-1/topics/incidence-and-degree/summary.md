# Incidence and Degree in Graph Theory - Summary

## Key Definitions and Concepts

- **Graph G = (V, E)**: A mathematical structure with vertices (V) and edges (E) connecting pairs of vertices
- **Incidence**: An edge is incident to its endpoint vertices; a vertex is incident to edges connecting to it
- **Degree of vertex v (deg(v))**: Number of edges incident to v; loops count twice
- **Isolated vertex**: Degree zero; no connections
- **Pendant vertex**: Degree one; leaf node
- **Maximum degree Δ(G)**: Largest vertex degree in the graph
- **Minimum degree δ(G)**: Smallest vertex degree in the graph

## Important Formulas and Theorems

- **Handshaking Lemma**: Σ\_{v∈V} deg(v) = 2|E|
- **Corollary**: Number of odd-degree vertices is always even
- **Complete graph K_n**: n vertices, n(n-1)/2 edges, degree (n-1) for each vertex
- **Complete bipartite K\_{m,n}**: m+n vertices, mn edges, degrees m and n
- **k-regular graph edges**: nk/2 (nk must be even)
- **Maximum edges in simple graph**: n(n-1)/2

## Key Points

1. The Handshaking Lemma is fundamental: sum of all vertex degrees equals twice the number of edges

2. Every graph has an even number of odd-degree vertices—this is always true

3. Complete graphs are (n-1)-regular; K_n has maximum possible edges for n vertices

4. Complete bipartite graphs K\_{m,n} have vertices in two sets with no edges within each set

5. Regular graphs have uniform degree; used extensively in network design

6. Degree sequence determines many graph properties but doesn't uniquely identify a graph

7. The Havel-Hakimi algorithm systematically checks if a sequence is graphical

8. Bipartite graphs contain no odd cycles; useful for modeling relationships between two distinct groups

## Common Mistakes to Avoid

1. Forgetting that loops contribute 2 to degree (not 1) when graphs aren't simple

2. Not verifying answers with Handshaking Lemma—always check your work

3. Confusing K*n (complete) with K*{m,n} (complete bipartite)—they are different structures

4. Forgetting that degree sequence must be non-negative integers

5. Incorrectly applying the formula for edges in regular graphs—nk/2 must be integer

## Revision Tips

1. Practice computing degrees for various graph configurations until automatic

2. Memorize the Handshaking Lemma formula and its corollary—they appear in every exam

3. Work through at least 3-4 Havel-Hakimi examples to master the algorithm

4. Create comparison tables for special graph types: complete, regular, bipartite

5. Solve previous year university questions on this topic to understand exam patterns
