# Spanning Trees - Summary

## Key Definitions and Concepts

- **Spanning Tree**: A subgraph containing all vertices of a connected graph with exactly (n-1) edges, connected and acyclic
- **Minimum Spanning Tree (MST)**: A spanning tree with minimum total edge weight in a weighted graph
- **Cut Property**: The minimum weight edge crossing any cut belongs to some MST
- **Cycle Property**: The maximum weight edge in any cycle cannot belong to any MST

## Important Formulas and Theorems

- Number of edges in spanning tree: |V| - 1
- Cayley's Formula: Complete graph Kₙ has n^(n-2) spanning trees
- Kruskal's Complexity: O(E log V)
- Prim's Complexity: O(V²) naive, O(E log V) with heap

## Key Points

- Every connected graph with n vertices has at least one spanning tree
- Adding any edge to a spanning tree creates exactly one cycle
- Removing any edge from a spanning tree disconnects the graph
- Kruskal's builds MST by adding smallest edges that don't form cycles
- Prim's grows MST from an arbitrary vertex by adding minimum connecting edges
- Both are greedy algorithms guaranteed to produce optimal MST
- Cut and cycle properties form the theoretical foundation for MST algorithms

## Common Mistakes to Avoid

- Confusing spanning tree with minimum spanning tree (the latter requires weights)
- Forgetting that a spanning tree must include ALL vertices of the original graph
- Adding edges that create cycles when using Kruskal's algorithm
- Not checking if a vertex is already in the tree when using Prim's algorithm
- Incorrectly calculating total weight of MST (always double-check edge weights)

## Revision Tips

1. Practice both algorithms on at least 3-4 different graphs to gain speed
2. Memorize Cayley's formula and remember it's for complete graphs only
3. Know when to use Kruskal's (sparse graphs) vs Prim's (dense graphs)
4. Review cut and cycle properties as they frequently appear in 2-mark and 5-mark questions
