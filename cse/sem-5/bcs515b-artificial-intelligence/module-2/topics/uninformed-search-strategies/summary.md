# Uninformed Search Strategies - Summary

## Key Definitions and Concepts

- **Uninformed Search**: Search strategies that use no domain-specific knowledge; only the problem definition (initial state, goal state, operators) is used.
- **Frontier**: The set of nodes waiting to be expanded in the search process.
- **Branching Factor (b)**: Average number of successors generated from each node.
- **Depth (d)**: Distance from root node to the goal node in terms of number of edges.
- **Complete Search**: A strategy that guarantees finding a solution if one exists.
- **Optimal Search**: A strategy that finds the best (minimum cost) solution.

## Important Formulas and Theorems

- **BFS Time Complexity**: O(b^d)
- **BFS Space Complexity**: O(b^d)
- **DFS Time Complexity**: O(b^m) where m is maximum depth
- **DFS Space Complexity**: O(bm)
- **IDS Time Complexity**: O(b^d)
- **IDS Space Complexity**: O(bd)
- **Bidirectional Search Time**: O(b^(d/2))

## Key Points

- BFS uses FIFO queue, explores level by level, guarantees shortest path in unweighted graphs.
- DFS uses LIFO stack, goes deep before backtracking, memory efficient but not optimal.
- UCS uses priority queue ordered by path cost g(n), finds minimum-cost path when costs are positive.
- Depth-Limited Search imposes depth limit l to prevent infinite depth problem of DFS.
- Iterative Deepening Search combines BFS optimality with DFS space efficiency through repeated depth-limited searches.
- Bidirectional search reduces complexity by searching from both start and goal simultaneously.

## Common Mistakes to Avoid

1. Assuming DFS always finds a solution - it can get stuck in infinite loops without cycle detection.
2. Confusing BFS optimality - BFS is only optimal for unweighted graphs or when all edge costs are equal.
3. Neglecting space complexity - BFS can exhaust memory quickly even when solution exists.
4. Using UCS without checking that all costs are positive - UCS requires positive costs for completeness and optimality.

## Revision Tips

1. Practice tracing through BFS and DFS on small graphs by hand to understand the expansion order.
2. Memorize the properties (complete/optimal/complexities) of each algorithm in a comparative table.
3. Focus on when to use each strategy: BFS for shortest path, DFS for memory-limited scenarios, UCS for weighted costs.
4. Remember that Iterative Deepening is often preferred in practice as it combines the best properties of BFS and DFS.
