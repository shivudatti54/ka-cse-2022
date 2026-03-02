# Vertex Connectivity - Summary

## Key Definitions and Concepts

- **Vertex Cut (Separating Set):** A set of vertices S ⊆ V(G) whose removal disconnects the graph G or reduces it to a trivial graph (single vertex). The removal creates G-S.

- **Vertex Connectivity (κ(G)):** The minimum number of vertices that must be removed to disconnect the graph or reduce it to a trivial graph. For Kₙ, κ(Kₙ) = n-1.

- **Cut Vertex (Articulation Point):** A vertex whose removal increases the number of connected components. Graphs with κ(G) = 1 have cut vertices.

- **Edge Connectivity (λ(G)):** The minimum number of edges whose removal disconnects the graph.

- **Minimum Degree (δ(G)):** The smallest degree among all vertices in the graph.

## Important Formulas and Theorems

- **Whitney's Theorem:** For any graph G with n ≥ 2: κ(G) ≤ λ(G) ≤ δ(G)

- **Complete Graph:** κ(Kₙ) = λ(Kₙ) = δ(Kₙ) = n-1

- **Cycle Graph:** κ(Cₙ) = 2 for n ≥ 3

- **Complete Bipartite Graph:** κ(Kₘ,ₙ) = min(m, n)

- **Path Graph:** κ(Pₙ) = 1 for n ≥ 2

- **Disconnected Graph:** κ(G) = 0

## Key Points

- Vertex connectivity measures graph resilience against vertex removal
- κ(G) ≤ λ(G) always holds; removing vertices is more disruptive than removing edges
- Minimum degree δ(G) provides an upper bound on both κ(G) and λ(G)
- Higher vertex connectivity indicates more robust network structures
- Complete graphs are the most connected simple graphs for their size
- The gap between κ(G) and λ(G) can be arbitrarily large in certain graphs
- Vertex connectivity cannot exceed n-1 for a graph with n vertices
- For regular graphs, vertex and edge connectivity often coincide with minimum degree

## Common Mistakes to Avoid

1. **Confusing vertex and edge connectivity:** Remember vertex cuts remove vertices and their incident edges; edge cuts only remove edges.

2. **Forgetting disconnected graphs:** Always check if the graph is connected first—disconnected graphs have κ(G) = 0.

3. **Incorrect minimum vertex cut:** The vertex cut must disconnect the graph or leave a trivial graph; removing vertices that don't achieve this doesn't count.

4. **Ignoring complete graphs:** Complete graphs require removal of (n-1) vertices to become trivial, which is a common exam trap.

## Revision Tips

1. **Practice with graph families:** Memorize connectivity values for paths, cycles, complete graphs, and complete bipartite graphs as these appear frequently.

2. **Apply Whitney's theorem first:** When solving problems, start with κ(G) ≤ λ(G) ≤ δ(G) to establish bounds.

3. **Draw small examples:** For exam questions, sketch the graph and physically remove vertices to find the minimum cut.

4. **Understand the inequality chain:** Remember the order—vertex connectivity is always ≤ edge connectivity, which is ≤ minimum degree.
