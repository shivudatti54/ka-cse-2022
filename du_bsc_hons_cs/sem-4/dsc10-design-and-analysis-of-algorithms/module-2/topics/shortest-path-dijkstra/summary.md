# Dijkstra's Algorithm - Summary

## Key Definitions and Concepts

- **Single-Source Shortest Path**: Finding the minimum weight path from a source vertex to all other vertices in a weighted graph.
- **Relaxation**: The operation of updating a vertex's distance if a shorter path through another vertex is discovered.
- **Greedy Choice Property**: Selecting the unvisited vertex with minimum tentative distance at each step leads to globally optimal solutions.
- **Priority Queue**: Data structure (typically min-heap) used to efficiently extract the vertex with minimum distance.

## Important Formulas and Theorems

- **Relaxation condition**: if dist[u] + w(u,v) < dist[v], then dist[v] = dist[u] + w(u,v)
- **Array implementation**: O(V²) time complexity
- **Binary heap implementation**: O((V + E) log V) time complexity
- **Fibonacci heap implementation**: O(E + V log V) time complexity

## Key Points

- Dijkstra's algorithm ONLY works for graphs with non-negative edge weights (w ≥ 0)
- The algorithm uses a greedy approach: always extract the vertex with minimum distance
- When a vertex is extracted, its shortest distance is final (proven by contradiction)
- Space complexity is O(V) for all implementations
- For dense graphs (E ≈ V²), simple array implementation may be faster
- For sparse graphs, binary heap is preferred due to O(E log V) performance
- The algorithm can be paused and resumed; distances persist
- A parent array is needed to reconstruct actual shortest paths

## Common Mistakes to Avoid

1. **Forgetting non-negative weight constraint**: Never apply Dijkstra to graphs with negative weights
2. **Not marking visited vertices**: Can cause infinite loops or incorrect results
3. **Ignoring updates in priority queue**: Binary heap requires re-insertion, not in-place update
4. **Assuming adjacency matrix**: Always consider graph representation for complexity analysis
5. **Confusing with minimum spanning tree**: Dijkstra finds shortest paths, not minimum spanning tree

## Revision Tips

- Practice tracing through at least 3-4 different graphs by hand
- Memorize the time complexity formulas for different implementations
- Remember the comparison with Bellman-Ford: Dijkstra is faster but less general
- Keep the relaxation operation formula on fingertips
- Focus on understanding why the greedy choice works, not just memorizing steps
- Review the correctness proof argument for exam questions on proof techniques