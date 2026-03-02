# Bellman-Ford Algorithm - Summary

## Key Definitions and Concepts

- **Single-Source Shortest Path**: Finding the shortest path from one source vertex to all other vertices in a weighted graph
- **Relaxation**: The operation of updating vertex distances when a shorter path is discovered through an intermediate vertex
- **Negative Weight Edge**: An edge with a weight less than zero; Bellman-Ford handles these correctly
- **Negative Weight Cycle**: A cycle whose total edge weight is negative, making shortest paths undefined

## Important Formulas and Theorems

- **Relaxation Formula**: `if dist[u] + w(u,v) < dist[v]: dist[v] = dist[u] + w(u,v)`
- **Iteration Count**: The algorithm performs |V| - 1 iterations over all edges
- **Time Complexity**: O(|V| × |E|)
- **Space Complexity**: O(|V|)
- **Negative Cycle Detection**: If any edge can be relaxed after |V| - 1 iterations, a negative weight cycle exists

## Key Points

- Bellman-Ford algorithm works with negative edge weights (unlike Dijkstra's)
- Initialization sets source distance to 0 and all others to infinity
- Each iteration relaxes all edges, progressively improving distance estimates
- After |V| - 1 iterations, shortest paths (if they exist) are finalized
- Additional pass detects negative weight cycles reachable from source
- Algorithm is based on dynamic programming principles
- Works on both directed and undirected graphs
- Unreachable vertices retain infinite distance

## Common Mistakes to Avoid

- Confusing the number of iterations (|V| - 1, not |V|)
- Forgetting to check for negative cycles after the main iterations
- Using Dijkstra's algorithm when negative weights are present
- Not handling the case where the source vertex cannot reach all vertices
- Forgetting to initialize the source vertex distance to 0

## Revision Tips

1. Practice tracing Bellman-Ford on at least 3-4 different graphs
2. Focus on understanding why |V| - 1 iterations are sufficient
3. Memorize the comparison between Bellman-Ford and Dijkstra
4. Review negative cycle detection carefully—it's frequently tested
5. Solve previous year DU question papers for pattern familiarity