# Dijkstra's Algorithm - Summary

## Key Definitions

- **Shortest Path Distance:** The minimum total weight path from source vertex s to vertex v
- **Relaxation:** The operation of updating a vertex's distance through a newly discovered path
- **Tentative Distance:** The current best-known distance from source to a vertex (may not be final)
- **Priority Queue:** A data structure (typically min-heap) that extracts the vertex with minimum distance

## Important Formulas

- **Relaxation Condition:** if dist[u] + w(u,v) < dist[v] then dist[v] = dist[u] + w(u,v)
- **Time Complexity (Binary Heap):** O((V + E) log V)
- **Time Complexity (Array):** O(V² + E)
- **Time Complexity (Fibonacci Heap):** O(V log V + E)

## Key Points

1. Dijkstra's Algorithm is a GREEDY algorithm that finds shortest paths from a single source
2. Works ONLY with non-negative edge weights; fails with negative weights
3. Maintains set S of finalized vertices; extracts minimum distance vertex iteratively
4. The invariant: when vertex u is extracted, dist[u] equals the true shortest path distance
5. Uses relaxation to progressively improve distance estimates
6. Priority queue operations determine overall time complexity
7. Predecessor array π[] enables path reconstruction
8. Superior to Bellman-Ford for non-negative weights due to better complexity

## Common Mistakes

1. **Applying to negative weights:** Using Dijkstra when edge weights can be negative (should use Bellman-Ford)
2. **Forgetting initialization:** Setting dist[s]=0 while leaving all other vertices at ∞
3. **Missing relaxation:** Not checking all neighbors of the extracted vertex
4. **Incorrect complexity:** Confusing O(V²) with O((V+E) log V) without specifying the data structure