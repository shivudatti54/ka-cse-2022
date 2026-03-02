# BFS, DFS, and Hill Climbing Search Algorithms - Summary

## Key Definitions and Concepts

- **Search Algorithm:** A procedure that systematically explores a problem space to find a solution state from an initial state.
- **BFS (Breadth-First Search):** Uninformed search that explores all nodes at depth d before moving to depth d+1; uses FIFO queue.
- **DFS (Depth-First Search):** Uninformed search that explores as far as possible along each branch before backtracking; uses LIFO stack or recursion.
- **Hill Climbing:** Local search algorithm that iteratively moves to neighboring states with better objective function values.
- **Branching Factor (b):** Average number of children generated from each node.
- **Goal State:** The target state that satisfies problem constraints and represents a solution.

## Important Formulas and Theorems

- **BFS Time Complexity:** O(b^d) where b = branching factor, d = depth of shallowest goal
- **BFS Space Complexity:** O(b^d) — must store all frontier nodes
- **DFS Time Complexity:** O(b^m) where m = maximum depth
- **DFS Space Complexity:** O(bm) — stores only current path
- **Completeness:** BFS guarantees solution if one exists; DFS does not
- **Optimality:** BFS finds shortest path; DFS and Hill Climbing do not guarantee optimal solutions

## Key Points

- BFS uses Queue data structure; DFS uses Stack or recursion
- BFS is complete and optimal; DFS is neither complete nor optimal in infinite spaces
- BFS is memory-intensive; DFS is memory-efficient but may explore unnecessary paths
- Hill Climbing is a greedy local search that climbs the "hill" toward better solutions
- Hill Climbing fails at local maxima, plateaus, and ridges
- Random-restart Hill Climbing improves chances of finding global optimum
- Choice of algorithm depends on problem: BFS for shortest path, DFS for deep search, Hill Climbing for optimization
- All three are fundamental to AI problem-solving and frequently tested in examinations

## Common Mistakes to Avoid

1. Confusing BFS queue order (FIFO) with DFS stack order (LIFO)
2. Assuming DFS always finds optimal solution—it does not
3. Forgetting that Hill Climbing is not complete—it can get stuck permanently
4. Not considering memory constraints when choosing BFS for large state spaces
5. Using Hill Climbing without a good heuristic—will likely get stuck in local optima

## Revision Tips

1. Practice tracing BFS and DFS on small graphs manually to internalize the order of node expansion.
2. Memorize the time and space complexities with the parameters b, d, and m.
3. Remember: BFS = Breadth (wide) = Queue; DFS = Depth (deep) = Stack.
4. For Hill Climbing, always consider the heuristic quality—it makes or breaks the algorithm.
5. Review previous year DU exam questions on search algorithms to understand the pattern and depth of questions asked.