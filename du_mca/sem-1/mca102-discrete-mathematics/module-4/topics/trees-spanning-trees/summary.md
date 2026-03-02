# Trees and Spanning Trees - Summary

## Key Definitions and Concepts
- **Tree**: Acyclic connected graph with n vertices and (n-1) edges
- **Spanning Tree**: Subgraph containing all vertices of original graph with minimal edges
- **MST**: Spanning tree with minimum total edge weight
- **Cut**: Partition of vertices into two disjoint sets
- **Light Edge**: Minimum weight edge in a cut

## Important Formulas and Theorems
- **Edges in Tree**: |E| = |V| - 1
- **Kruskal's Complexity**: O(E log E)
- **Prim's Complexity**: O(E + V log V)
- **Cayley's Formula**: Complete graph Kₙ has nⁿ⁻² spanning trees
- **Cut Property**: Lightest edge across any cut belongs to MST
- **Cycle Property**: Heaviest edge in any cycle not in MST

## Key Points
- Trees are minimally connected (removing any edge disconnects)
- Any connected graph has at least one spanning tree
- MST is unique if all edge weights are distinct
- Kruskal's better for sparse graphs, Prim's for dense graphs
- Union-Find data structure efficiently detects cycles
- Fibonacci heaps optimize Prim's algorithm
- MSTs have applications in network design and clustering

## Common Mistakes to Avoid
- Confusing spanning trees with shortest path trees
- Forgetting to check for cycles in Kruskal's algorithm
- Incorrectly sorting edges in descending order
- Assuming MST is unique in graphs with duplicate weights
- Missing edge cases in proof-based questions

## Revision Tips
1. Practice visual identification of spanning trees in sample graphs
2. Implement both MST algorithms from scratch
3. Solve at least 5 different weight configuration problems
4. Memorize proof structures for cut and cycle properties
5. Use adjacency matrices for Prim's and edge lists for Kruskal's practice