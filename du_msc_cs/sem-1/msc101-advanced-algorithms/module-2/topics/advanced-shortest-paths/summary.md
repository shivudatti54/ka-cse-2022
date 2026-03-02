# Advanced Shortest-Path Algorithms - Summary

## Key Definitions and Concepts
- **Reweighting**: Technique to eliminate negative weights while preserving shortest paths
- **Relaxation**: Fundamental operation updating distance estimates
- **Negative Cycle**: Path returning to start with total weight < 0
- **Transitive Closure**: Matrix representation of reachability

## Important Formulas and Theorems
- Floyd-Warshall Recurrence: d(k)[i,j] = min(d(k-1)[i,j], d(k-1)[i,k] + d(k-1)[k,j])
- Johnson's Potential: h(v) = shortest path from virtual source to v
- Bellman-Ford Termination: After V-1 iterations, additional relaxation detects negative cycles

## Key Points
- Johnson's algorithm is asymptotically best for sparse graphs with negative weights
- Floyd-Warshall's Θ(V³) time makes it suitable only for dense graphs
- Contraction hierarchies reduce query times by 3-4 orders of magnitude
- Yen's modification reduces Bellman-Ford's average case complexity
- K-shortest path algorithms require O(KV²) time using deviation paths
- Dynamic graphs require incremental algorithms like Dynamic Floyd-Warshall
- Quantum algorithms offer O(√V) speedup for adjacency matrix implementations

## Common Mistakes to Avoid
- Forgetting to check for negative cycles in Bellman-Ford implementations
- Incorrect initialization of distance matrices in Floyd-Warshall
- Misapplying Dijkstra's algorithm to graphs with negative weights
- Overlooking space complexity in massive graphs
- Confusing edge relaxation with path relaxation in proofs

## Revision Tips
1. Practice matrix updates for Floyd-Warshall with different graph sizes
2. Compare algorithm pseudocode side-by-side in tabular form
3. Implement Johnson's algorithm with both binary and Fibonacci heaps
4. Study real-world case studies from Uber's route optimization system
5. Explore recent papers on GPU-accelerated shortest-path algorithms

Length: 650 words