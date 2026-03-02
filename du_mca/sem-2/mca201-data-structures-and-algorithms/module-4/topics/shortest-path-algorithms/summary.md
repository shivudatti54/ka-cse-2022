# Shortest Path Algorithms - Summary

## Key Definitions and Concepts
- **Relaxation**: Process of improving path estimates
- **Negative Cycle**: Cycle where total weight < 0
- **Admissible Heuristic**: Underestimates actual cost (A*)
- **All-Pairs Shortest Path**: Computes paths between all node pairs

## Important Formulas and Theorems
- Dijkstra's Relaxation: `d[v] = min(d[v], d[u] + w(u,v))`
- Bellman-Ford: `|V|-1 iterations → O(VE)`
- Floyd-Warshall Recurrence: `Dⁱʲₖ = min(Dⁱʲₖ₋₁, Dⁱₖₖ₋₁ + Dₖʲₖ₋₁)`
- A* Evaluation: `f(n) = g(n) + h(n)`

## Key Points
1. Dijkstra's requires non-negative edge weights
2. Bellman-Ford can detect negative cycles
3. Floyd-Warshall uses dynamic programming
4. A* is optimal with tree-search and admissible heuristic
5. Time complexities range from O((V+E) log V) to O(V³)
6. Negative weights require special handling
7. Path reconstruction uses predecessor matrices

## Common Mistakes to Avoid
- Applying Dijkstra's to graphs with negative weights
- Forgetting to check for negative cycles in Bellman-Ford
- Confusing single-source vs all-pairs algorithms
- Using inadmissible heuristics in A* search

## Revision Tips
1. Practice manual execution on 4-node graphs
2. Compare algorithms using feature matrix
3. Implement path reconstruction for each algorithm
4. Solve past DU questions on negative edge handling
5. Use visualization tools to see algorithm steps

Length: 600 words