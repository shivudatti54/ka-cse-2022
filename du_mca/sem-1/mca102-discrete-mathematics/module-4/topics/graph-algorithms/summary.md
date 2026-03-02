# Graph Algorithms - Summary

## Key Definitions and Concepts
- **Adjacency Matrix**: 2D array where matrix[i][j] = weight of edge i-j
- **Bipartite Graph**: Graph whose vertices can be divided into two disjoint sets
- **Relaxation**: Process of updating better path estimates in shortest-path algorithms
- **Union-Find**: Data structure for tracking connected components

## Important Formulas and Theorems
- **Dijkstra's Algorithm**: dist[v] = min(dist[v], dist[u] + weight(u,v))
- **Kruskal's MST**: Total weight = Σ(selected edges), uses Union-Find with path compression
- **Prim's Algorithm**: MST grows by adding minimum edge connecting tree to non-tree vertex
- **Handshaking Lemma**: Σ(degrees) = 2|E|

## Key Points
- BFS is optimal for unweighted shortest paths
- DFS helps find strongly connected components
- Dijkstra's requires non-negative edge weights
- Kruskal's works better for sparse graphs
- Topological sort only exists for DAGs
- Adjacency lists are space-efficient for sparse graphs
- Negative cycles make shortest-path problems undefined

## Common Mistakes to Avoid
- Confusing BFS (queue) with DFS (stack) implementation
- Forgetting to check for cycles in MST algorithms
- Applying Dijkstra's to graphs with negative weights
- Missing updates in relaxation steps
- Assuming topological order is unique

## Revision Tips
1. Practice tracing algorithms on Indian city connectivity maps
2. Create comparison tables for algorithms' time/space complexity
3. Implement BFS using both adjacency matrix and list
4. Solve previous years' DU questions on MST construction
5. Use visualization tools like Graph Online for better intuition

Length: 650 words