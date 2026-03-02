# Travelling Salesman Problem - Summary

## Key Definitions and Concepts

- **Travelling Salesman Problem (TSP)**: Finding the minimum weight Hamiltonian cycle in a complete weighted graph that visits each city exactly once and returns to the starting point.

- **Hamiltonian Cycle**: A cycle that visits each vertex exactly once and returns to the starting vertex; TSP is the problem of finding the minimum weight Hamiltonian cycle.

- **Metric TSP**: Special case where triangle inequality holds: d(i,j) + d(j,k) ≥ d(i,k) for all cities.

- **Complete Graph**: A graph where every pair of vertices is connected by an edge; TSP is typically defined on complete graphs.

## Important Formulas and Theorems

- **Brute Force Complexity**: O(n!) - computationally infeasible for n > 15-20

- **Held-Karp Dynamic Programming**: O(n² × 2^n) - significantly better than brute force but still exponential

- **MST-based Approximation**: Provides solution ≤ 2 × optimal (for Metric TSP)

- **Christofides Algorithm**: Provides solution ≤ 1.5 × optimal (for Metric TSP)

## Key Points

- TSP is NP-hard; no polynomial-time exact algorithm is known for large instances

- For Metric TSP, triangle inequality simplifies the problem and enables approximation guarantees

- Heuristic methods (Nearest Neighbor, 2-Opt) run in polynomial time but don't guarantee optimality

- Dynamic programming provides exact solutions but requires exponential time and space

- Branch and bound can prune search space significantly for practical instances

- TSP has numerous practical applications in logistics, transportation, manufacturing, and bioinformatics

- The asymmetric TSP (different distances in each direction) and symmetric TSP are distinct variants

## Common Mistakes to Avoid

1. Confusing Hamiltonian cycles with Eulerian circuits - they are fundamentally different concepts

2. Forgetting that TSP requires returning to the starting city (complete cycle)

3. Assuming heuristic solutions are always optimal - they are approximations

4. Not accounting for the exponential growth in solution space when analyzing TSP algorithms

5. Misunderstanding the meaning of "approximation ratio" - a 2-approximation means at most twice optimal

## Revision Tips

1. Practice solving small TSP instances (3-4 cities) by hand using both dynamic programming and enumeration to understand the mechanics.

2. Memorize the time complexities of different approaches and understand the trade-offs between exact and heuristic methods.

3. Review the definition of NP-hardness and why it motivates approximation algorithms.

4. Go through previous university exam questions on TSP to understand the expected answer format and key points to include.
