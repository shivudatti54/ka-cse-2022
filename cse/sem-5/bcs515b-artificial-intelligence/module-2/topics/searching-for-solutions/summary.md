# Searching for Solutions - Summary

## Key Definitions and Concepts

- **Search**: Problem-solving technique exploring possible states to find a path from initial to goal state
- **Problem Formulation**: Four components - Initial state, Goal state, Successor function, Path cost
- **Search Space**: Set of all states reachable from the initial state
- **Branching Factor**: Average number of successors from any state
- **Heuristic Function h(n)**: Estimates cost from node n to goal state
- **Evaluation Function f(n) = g(n) + h(n)**: Used in A\* search to prioritize nodes

## Important Formulas and Theorems

- **BFS Complexity**: Time O(b^d), Space O(b^d)
- **DFS Complexity**: Time O(b^m), Space O(bm)
- **A\* Optimality**: Finds optimal solution if heuristic h(n) is admissible (never overestimates true cost)
- **Consistent Heuristic**: h(n) ≤ c(n,n') + h(n') for all edges
- **Greedy Best-First**: Expands node with lowest h(n) value

## Key Points

1. Problem formulation requires defining initial state, goal state, successor function, and path cost precisely.

2. Uninformed search (BFS, DFS, UCS) uses no problem-specific knowledge; informed search (Greedy, A\*) uses heuristics.

3. BFS guarantees shortest path when all costs are equal; DFS is memory-efficient but not complete in infinite spaces.

4. A\* combines path cost g(n) and heuristic h(n) for optimal search when using admissible heuristics.

5. Heuristic admissibility is critical - admissible heuristics never overestimate true cost to goal.

6. A good heuristic significantly reduces search effort compared to uninformed methods.

7. The choice of search algorithm depends on whether completeness, optimality, or efficiency is prioritized.

## Common Mistakes to Avoid

1. Confusing DFS with BFS data structures - BFS uses queue (FIFO), DFS uses stack (LIFO)

2. Forgetting that A\* requires an admissible heuristic for optimality

3. Assuming DFS always finds the shortest path (it doesn't)

4. Not understanding that a heuristic can be admissible without being consistent

5. Confusing the goal test (checking if current state is goal) with the evaluation function

## Revision Tips

1. Practice formulating problems with the four components for various scenarios.

2. Trace through BFS, DFS, and A\* manually on small graphs to understand the execution flow.

3. Remember: BFS = queue (FIFO), DFS = stack (LIFO), UCS/A\* = priority queue (by cost)

4. For A\* problems, always verify heuristic admissibility before claiming optimality.

5. Focus on understanding when each algorithm is appropriate rather than just memorizing formulas.
