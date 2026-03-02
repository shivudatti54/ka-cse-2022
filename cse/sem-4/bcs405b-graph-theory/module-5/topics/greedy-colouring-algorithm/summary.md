# Greedy Colouring Algorithm - Summary

## Key Definitions and Concepts

- **Greedy Colouring:** A vertex colouring algorithm that processes vertices in a specific order and assigns the smallest available colour not used by adjacent neighbours.
- **Chromatic Number χ(G):** The minimum number of colours needed to colour a graph G properly.
- **Maximum Degree Δ(G):** The highest degree of any vertex in graph G.
- **Saturation Degree:** The number of distinct colours used on neighbours of a vertex (used in DSATUR algorithm).
- **Perfect Graph:** A graph where χ(H) = ω(H) for every subgraph H (ω is clique number).

## Important Formulas and Theorems

- **Trivial Bound:** χ(G) ≤ Δ(G) + 1
- **Greedy Bound:** With any vertex ordering, greedy colouring uses at most 1 + max_i deg_i colours
- **Brook's Theorem:** For connected G that is not Kₙ or odd cycle: χ(G) ≤ Δ(G); for Kₙ: χ(G) = n; for odd cycle C₂ₙ₊₁: χ(G) = 3

## Key Points

1. Greedy colouring always produces a proper colouring (no adjacent vertices share a colour).
2. The quality of greedy colouring depends entirely on the vertex ordering chosen.
3. Welsh-Powell algorithm uses descending degree ordering for better results.
4. DSATUR uses saturation degree heuristic for more intelligent vertex selection.
5. For perfect graphs (chordal, interval, bipartite), any ordering yields optimal colouring.
6. Complete graphs and odd cycles require Δ(G) + 1 colours regardless of ordering.
7. Time complexity of greedy colouring is O(V + E).
8. The algorithm is polynomial-time but does not guarantee optimal (minimum) colouring.

## Common Mistakes to Avoid

1. **Forgetting to update neighbours:** When colouring a vertex, always check ALL already-coloured neighbours, not just the first one found.
2. **Ignoring vertex ordering:** Many students apply greedy colouring without considering the order, leading to non-optimal results.
3. **Confusing degree and saturation:** Degree is the number of neighbours; saturation is the number of different colours on neighbours.
4. **Misapplying Brook's Theorem:** Remember it only applies to connected graphs and has exceptions for complete graphs and odd cycles.

## Revision Tips

1. Practice greedy colouring on small graphs (5-7 vertices) with different orderings to see how results vary.
2. Memorize the Welsh-Powell algorithm steps: sort by degree descending, then assign colours by scanning.
3. Remember: worst case = complete graph requires n colours; best case = bipartite graphs require 2 colours.
4. For exams, always write down vertex degrees first, determine ordering, then systematically apply the algorithm.
5. Review Brook's Theorem conditions carefully - know the exceptions for Kₙ and odd cycles.
