# Kruskal's Algorithm - Summary

## Key Definitions and Concepts

- **Spanning Tree**: A subgraph containing all vertices with exactly V-1 edges and no cycles
- **Minimum Spanning Tree (MST)**: The spanning tree with minimum total edge weight
- **Kruskal's Algorithm**: A greedy algorithm that builds MST by adding edges in increasing order of weight, skipping those that create cycles
- **Union-Find (DSU)**: Data structure supporting Find (cycle detection) and Union (merge sets) operations in near-constant amortized time

## Important Formulas and Theorems

- **Time Complexity**: O(E log V) where E = edges, V = vertices
- **Space Complexity**: O(V) for the Union-Find data structure
- **Cut Property**: The minimum weight edge crossing any cut belongs to some MST
- **Cycle Property**: The maximum weight edge in any cycle does not belong to any MST

## Key Points

- Algorithm sorts all edges by weight, then iteratively adds the smallest edge that doesn't form a cycle
- Union-Find with path compression and union by rank achieves near-O(1) operations
- Algorithm stops when MST has V-1 edges
- Works on disconnected graphs but produces a Minimum Spanning Forest
- Greedy approach is justified by the cut property of MSTs
- Better suited for sparse graphs compared to Prim's algorithm

## Common Mistakes to Avoid

1. Forgetting to stop after V-1 edges are added (continuing unnecessarily)
2. Not initializing each vertex as a separate set in Union-Find
3. Confusing Kruskal's (edge-based) with Prim's (vertex-based) approach
4. Failing to check if endpoints are in the same set before adding an edge
5. Incorrectly handling graphs with disconnected components

## Revision Tips

1. Practice tracing Kruskal's algorithm on at least 3-4 different graphs
2. Memorize the implementation of Union-Find with path compression and union by rank
3. Know the comparison: Kruskal = O(E log V), Prim = O(V²) or O(E log V)
4. Remember that Kruskal processes edges (good for sparse graphs), Prim processes vertices (good for dense graphs)
5. Revise the cut property and cycle property as they form the theoretical basis for correctness