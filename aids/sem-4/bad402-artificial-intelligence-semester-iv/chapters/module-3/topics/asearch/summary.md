# A* Search - Summary

## Key Definitions and Concepts

- A* Search: An informed search algorithm that combines path cost g(n) and heuristic estimate h(n) using the evaluation function f(n) = g(n) + h(n).

- g(n): The actual cost from the start state to node n along the path discovered by the search algorithm.

- h(n): A heuristic function that estimates the minimum cost from node n to any goal state. This is problem-specific knowledge.

- f(n): The estimated total cost of the solution path going through node n, computed as g(n) + h(n).

- Admissible Heuristic: A heuristic that never overestimates the true cost—h(n) ≤ h*(n) for all nodes n. Guarantees optimal solution.

- Consistent (Monotone) Heuristic: A heuristic satisfying h(n) ≤ c(n,a,n') + h(n') for all transitions. Implies admissibility and ensures efficient graph search.

## Important Formulas and Theorems

- Evaluation Function: f(n) = g(n) + h(n)

- Optimality Theorem: A* with an admissible heuristic is optimal. It never expands a node with f(n) > C*, where C* is the optimal solution cost.

- Complexity (Tree Search):
  - Time: O(b^d) worst case, O(d) with perfect heuristic
  - Space: O(b^d) worst case
  - Where b = branching factor, d = solution depth

- Dominance: Heuristic h1 dominates h2 if h1(n) ≥ h2(n) for all n, resulting in fewer node expansions.

## Key Points

- A* expands nodes in order of increasing f(n) value, ensuring systematic exploration.

- With an admissible heuristic, A* is guaranteed to find the optimal (minimum cost) solution.

- With a consistent heuristic, A*'s graph-search version never re-expands a node.

- The quality of the heuristic determines A*'s efficiency—better heuristics explore fewer nodes.

- A* is complete assuming finite branching factor and positive step costs.

- Space complexity is the primary limitation of A*, making it impractical for very large state spaces.

- Manhattan distance is a common admissible heuristic for grid-based movement problems.

- When h(n) = 0 for all n, A* degenerates to Dijkstra's algorithm.

## Common Mistakes to Avoid

1. CONFUSING g(n) AND h(n): Remember g(n) is actual accumulated cost (past), h(n) is estimated remaining cost (future).

2. USING NON-ADMISSIBLE HEURISTICS: This breaks optimality guarantee—A* may return suboptimal solutions.

3. IGNORING MEMORY CONSTRAINTS: Students often forget that A* requires storing all generated nodes, not just the current path.

4. NOT CHECKING CONSISTENCY: For graph search, consistency ensures efficiency by preventing unnecessary re-expansions.

5. OVERESTIMATING HEURISTICS: Using heuristics that "look good" but overestimate leads to suboptimal results.

## Revision Tips

1. PRACTICE computing Manhattan and Euclidean distances for grid problems—these appear frequently in exams.

2. MEMORIZE the optimality proof logic: With admissible h, any node with f > C* cannot be on optimal path.

3. WORK through the 8-puzzle example step-by-step to understand how A* expands nodes.

4. COMPARE A* with Greedy Best-First Search: Greedy uses only h(n) and is not optimal; A* uses both and guarantees optimality.

5. REMEMBER that admissibility is necessary for optimality—if the heuristic overestimates, the algorithm may choose a suboptimal path.