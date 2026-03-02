# Ford-Fulkerson Maximum Flow Algorithm - Summary

## Key Definitions and Concepts

- **Flow Network**: Directed graph G = (V, E) with source s, sink t, and capacity function c(u, v)
- **Flow f**: Function satisfying capacity constraint (0 ≤ f ≤ c), skew symmetry (f(u,v) = -f(v,u)), and flow conservation at intermediate vertices
- **Value of Flow |f|**: Total flow leaving source = Σ f(s, v)
- **Residual Graph G_f**: Graph showing remaining capacity; forward edges have capacity c(u,v) - f(u,v), backward edges have capacity f(u,v)
- **Augmenting Path**: Path from s to t in residual graph; bottleneck capacity is the minimum residual capacity along the path
- **s-t Cut (S, T)**: Partition of V where s ∈ S, t ∈ T; capacity is sum of c(u,v) for edges from S to T

## Important Formulas and Theorems

- **Residual Capacity (Forward)**: c_f(u, v) = c(u, v) - f(u, v)
- **Residual Capacity (Backward)**: c_f(v, u) = f(u, v)
- **Flow Update**: f'(u, v) = f(u, v) + bottleneck (forward) or f(u, v) - bottleneck (backward)
- **Max-Flow Min-Cut Theorem**: Maximum flow value = Minimum cut capacity
- **Time Complexity**: O(E × |f|) for basic Ford-Fulkerson; O(VE²) for Edmonds-Karp

## Key Points

- Ford-Fulkerson iteratively finds augmenting paths and increases flow until no augmenting path exists
- When algorithm terminates, flow is maximum (proved by Max-Flow Min-Cut theorem)
- Path reversal (using backward edges) allows adjusting previously assigned flow
- For integer capacities, algorithm always terminates (flow value increases by at least 1 each iteration)
- Minimum cut can be found from final residual graph: vertices reachable from s form set S
- Maximum flow equals capacity of minimum cut
- BFS-based approach (Edmonds-Karp) guarantees polynomial time complexity

## Common Mistakes to Avoid

1. Forgetting to include backward edges in residual graph construction
2. Not checking residual capacity before using an edge in augmenting path
3. Incorrectly calculating bottleneck capacity (must be minimum, not sum)
4. Confusing flow value with total capacity used
5. Not updating flow conservation at all intermediate vertices
6. Drawing residual edges incorrectly (direction matters!)

## Revision Tips

1. Practice drawing residual graphs manually - this is the most important skill
2. Memorize the three flow properties and be able to state them precisely
3. Understand the Max-Flow Min-Cut theorem proof - it's frequently asked
4. Solve at least 5-6 complete examples with step-by-step execution
5. Know the difference between Ford-Fulkerson and Edmonds-Karp
6. Review bipartite matching reduction to maximum flow