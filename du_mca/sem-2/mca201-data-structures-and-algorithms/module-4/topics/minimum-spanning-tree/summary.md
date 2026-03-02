# Minimum Spanning Tree - Summary

## Key Definitions and Concepts

- **Spanning Tree**: A connected, acyclic subgraph containing all n vertices of a graph; always has exactly n-1 edges
- **Minimum Spanning Tree (MST)**: A spanning tree with minimum total edge weight in a weighted connected graph
- **Cut Property**: The lightest edge crossing any cut belongs to some MST
- **Cycle Property**: The heaviest edge in any cycle cannot belong to any MST

## Important Formulas and Theorems

- **Number of edges in MST**: n-1 edges (for n vertices)
- **Prim's Algorithm**: O(E log V) with binary heap, O(E + V log V) with Fibonacci heap
- **Kruskal's Algorithm**: O(E log E) or O(E log V)
- **Union-Find with path compression + union by rank**: Amortized O(α(n)) ≈ O(1)
- **MST Uniqueness**: If all edge weights are distinct, MST is unique

## Key Points

1. MST is a greedy algorithm solution—the greedy choice at each step leads to global optimum
2. Both Prim's and Kruskal's algorithms are greedy approaches but differ in edge selection strategy
3. Prim's grows the MST from a single vertex; Kruskal's builds forest and merges components
4. Cut property proves correctness of Prim's; cycle property proves correctness of Kruskal's
5. For dense graphs (E ≈ V²), Prim's with array is optimal; for sparse graphs, Kruskal's works well
6. Union-Find data structure is essential for efficient cycle detection in Kruskal's algorithm
7. MST has applications in network design, clustering, image segmentation, and approximation algorithms

## Common Mistakes to Avoid

1. Confusing spanning tree with minimum spanning tree—MST requires minimum total weight
2. Forgetting that MST exists only for connected graphs; use minimum spanning forest for disconnected graphs
3. Not handling edge weights correctly—algorithm must consider edge weights, not just connectivity
4. Adding edges that form cycles, especially in Kruskal's without proper cycle detection

## Revision Tips

1. Practice implementing both Prim's and Kruskal's algorithms from scratch
2. Work through at least 3-4 complete examples of each algorithm by hand
3. Memorize the time complexities and understand when to apply each algorithm
4. Review Union-Find operations as they're crucial for Kruskal's implementation
5. Understand the proof of cut property and cycle property for theoretical questions