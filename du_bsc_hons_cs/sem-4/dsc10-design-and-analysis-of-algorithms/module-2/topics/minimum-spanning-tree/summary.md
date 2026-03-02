# Minimum Spanning Tree - Summary

## Key Definitions and Concepts

- **Spanning Tree**: A connected, acyclic subgraph containing all n vertices of a graph; has exactly n-1 edges
- **Minimum Spanning Tree (MST)**: A spanning tree with minimum total edge weight
- **Cut Property**: The minimum weight edge crossing any cut (partition of vertices) belongs to some MST
- **Cycle Property**: The maximum weight edge in any cycle cannot be part of any MST

## Important Formulas and Theorems

- **Number of edges in MST**: n-1 (where n is number of vertices)
- **Kruskal's Complexity**: O(E log V) using Union-Find with path compression
- **Prim's Complexity**: O(V²) with arrays, O(E log V) with binary heap
- **MST Uniqueness**: If all edge weights are distinct, MST is unique

## Key Points

- Both Kruskal's and Prim's are greedy algorithms that always produce optimal solutions
- Kruskal's is edge-centric: adds edges in increasing order, uses Union-Find
- Prim's is vertex-centric: grows tree from one vertex, uses Priority Queue
- Kruskal's better for sparse graphs (E ≈ V), Prim's better for dense graphs (E ≈ V²)
- Start vertex in Prim's can be arbitrary—all MSTs are equivalent in weight
- The cut property provides the theoretical foundation for both algorithms

## Common Mistakes to Avoid

1. **Continuing after n-1 edges**: Stop as soon as MST has n-1 edges; adding more creates cycles
2. **Confusing the algorithms**: Kruskal's builds from multiple components, Prim's from one
3. **Ignoring cycle detection**: In Kruskal's, skipping edges that would create cycles is critical
4. **Forgetting to update priority queue**: In Prim's, add new edges when vertices are added to MST

## Revision Tips

1. Practice drawing both algorithms step-by-step on small graphs (5-6 vertices)
2. Memorize the time complexities and understand when each algorithm is preferred
3. Review Union-Find data structure as it's essential for Kruskal's
4. Solve previous year DU exam questions on MST for pattern familiarity