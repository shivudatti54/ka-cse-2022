# Informed Search Strategies - Summary

## Key Definitions and Concepts

- **Heuristic Function h(n)**: Estimates the cost from node n to the goal state. Provides domain-specific knowledge to guide search.
- **Greedy Best-First Search**: Expands node with lowest h(n) value. Fast but neither complete nor optimal.
- **A\* Search**: Uses f(n) = g(n) + h(n) to balance actual cost and estimated cost. Combines completeness with optimality.
- **Admissible Heuristic**: Never overestimates true cost; h(n) ≤ h\*(n) for all nodes.
- **Consistent (Monotone) Heuristic**: Satisfies h(n) ≤ c + h(n') for all successors. Implies admissibility.
- **Dominance**: Heuristic h1 dominates h2 if h1(n) ≥ h2(n) for all states; explores fewer nodes.

## Important Formulas and Theorems

- **A\* Evaluation Function**: f(n) = g(n) + h(n)
  - g(n): actual cost from start to node n
  - h(n): estimated cost from n to goal
- **Optimality Theorem**: A\* with admissible h(n) finds optimal solution
- **Completeness**: A\* is complete if b is finite and costs are bounded
- **Complexity**: O(b^d) time and space where b is branching factor, d is solution depth

## Key Points

1. Informed search uses problem-specific knowledge (heuristic) to reduce search effort
2. Greedy Best-First Search is fast but can miss optimal solutions
3. A\* guarantees optimal solution with admissible heuristics
4. Manhattan Distance dominates Misplaced Tiles heuristic in 8-puzzle
5. A* expands all nodes with f(n) ≤ f*(goal), making it memory-intensive
6. Consistent heuristics prevent node re-expansion in graph search
7. Better heuristics explore fewer nodes but may cost more to compute

## Common Mistakes to Avoid

1. Confusing g(n) and h(n) in the f(n) formula
2. Forgetting that Greedy is not optimal even with good heuristics
3. Using non-admissible heuristics with A\* and expecting optimal results
4. Not checking for duplicate states in graph search
5. Confusing admissibility with consistency—they are different properties

## Revision Tips

1. Memorize f(n) = g(n) + h(n) as the defining formula of A\*
2. Remember: Greedy = h(n) only, A\* = g(n) + h(n)
3. Practice computing Manhattan Distance for 8-puzzle states
4. Review the conditions for A\* optimality (admissible heuristic)
5. Compare properties of Greedy vs A\* in tabular form for quick recall
