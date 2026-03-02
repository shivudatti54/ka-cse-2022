# Kruskal's Algorithm - Summary

## Key Definitions
- **Spanning Tree**: A subgraph that includes all vertices of a connected graph without forming cycles, containing exactly n-1 edges
- **Minimum Spanning Tree (MST)**: The spanning tree with minimum total edge weight
- **Cut Property**: For any cut in a graph, the minimum weight edge crossing the cut belongs to some MST
- **Disjoint Set Union (DSU)**: A data structure maintaining disjoint sets with Find and Union operations

## Important Formulas
- **Time Complexity**: O(E log V) = O(E log E)
- **Space Complexity**: O(V + E)
- **DSU amortized cost per operation**: O(α(n)), where α is the inverse Ackermann function
- **MST edges required**: n-1 edges for n vertices

## Key Points
- Kruskal's Algorithm is a greedy algorithm that sorts edges by weight and adds them if they don't create cycles
- The algorithm uses the cut property to guarantee optimality—the minimum edge crossing any cut is safe to add
- The DSU (Union-Find) data structure efficiently tracks connected components with near-constant time operations
- Union-by-rank and path compression optimizations achieve amortized O(α(n)) per operation
- The algorithm produces a Minimum Spanning Forest for disconnected graphs
- Unlike Prim's Algorithm which grows one tree, Kruskal's builds a forest that merges into one tree

## Common Mistakes
- Confusing Kruskal's with Prim's—Kruskal uses edges sorted globally, Prim uses a priority queue from a growing tree
- Forgetting to check cycle condition before adding edges; adding an edge connecting vertices in same component creates invalid cycles
- Incorrectly calculating complexity—sorting E edges dominates, giving O(E log E), not O(V log E)
- Not understanding that DSU operations are not truly O(1) but O(α(n)), though practically constant
- Assuming MST is unique—it is only unique when all edge weights are distinct