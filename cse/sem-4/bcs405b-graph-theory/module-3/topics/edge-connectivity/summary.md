# Edge-Connectivity - Summary

## Key Definitions and Concepts

- **Edge Cut:** A set of edges whose removal disconnects the graph
- **Edge-Connectivity λ(G):** Minimum number of edges needed to disconnect the graph; λ(G) = min{|S| : S ⊆ E(G) and G - S is disconnected}
- **Bridge (Cut-Edge):** An edge whose removal disconnects the graph; λ(G) = 1 for bridges
- **k-edge-connected Graph:** A graph with λ(G) ≥ k

## Important Formulas and Theorems

- **Inequality Chain:** κ(G) ≤ λ(G) ≤ δ(G)
- **Complete Graph:** λ(Kₙ) = n - 1
- **Complete Bipartite:** λ(Kₘ,ₙ) = min(m, n)
- **Cycle Graphs:** λ(Cₙ) = 2 (for n ≥ 3)
- **Tree Graphs:** λ(T) = 1
- **Bridge Characterization:** An edge is a bridge iff it does not lie on any cycle
- **Menger's Theorem (Edge Version):** Minimum edge cut size equals maximum number of edge-disjoint paths
- **Max-Flow Min-Cut:** Maximum flow equals minimum cut capacity

## Key Points

- Edge-connectivity measures network robustness against edge failures
- λ(G) is always at least κ(G) and at most δ(G)
- Complete graphs are maximally edge-connected with λ(Kₙ) = n-1
- Cycles have edge-connectivity 2 because they have no bridges
- The complete bipartite graph Kₘ,ₙ has edge-connectivity equal to the smaller part size
- Local edge-connectivity λ(s,t) between vertices is the minimum edges to separate them
- For any graph, λ(G) = min{λ(s,t) : s,t are distinct vertices}

## Common Mistakes to Avoid

- Confusing vertex connectivity with edge connectivity—they are different measures
- Forgetting that λ(G) ≤ δ(G); you cannot disconnect a graph by removing fewer edges than the minimum degree
- Not recognizing that a single edge can only be a bridge if it's not part of any cycle
- Assuming edge-connectivity is the same as vertex connectivity—they are related but not equal

## Revision Tips

1. Memorize the inequality chain κ(G) ≤ λ(G) ≤ δ(G)—this is the most frequently tested concept
2. Practice identifying bridges quickly using the cycle test: if an edge is on a cycle, it's not a bridge
3. Remember key values: λ(Kₙ) = n-1, λ(Kₘ,ₙ) = min(m,n), λ(Cₙ) = 2
4. Use Max-Flow Min-Cut algorithm for computing edge-connectivity between specific vertex pairs
5. Review how edge-connectivity applies to network reliability problems
