# Heuristic Functions - Summary

## Key Definitions and Concepts

- **Heuristic Function h(n):** Estimates the cost from node n to the goal state. Provides domain-specific knowledge to guide search.
- **Admissible Heuristic:** Never overestimates true cost; h(n) ≤ h*(n) for all nodes. Guarantees optimal solution with A*.
- **Consistent Heuristic:** Satisfies triangle inequality: h(n) ≤ c(n,n') + h(n'). Implies f-values never decrease along any path.
- **Heuristic Evaluation f(n):** f(n) = g(n) + h(n), where g(n) = cost from start, h(n) = estimated cost to goal.

## Important Formulas and Theorems

- **Evaluation Function:** f(n) = g(n) + h(n)
- **Admissibility:** h(n) ≤ h\*(n) for all n
- **Consistency:** h(n) ≤ c(n,n') + h(n') for all edges
- **A\* Optimality:** A\* with admissible h(n) finds optimal solution
- **Dominance:** If h₁(n) ≥ h₂(n) for all n, h₁ dominates h₂

## Key Points

1. Heuristic functions make search "informed" by using problem-specific knowledge.
2. Zero heuristic (h=0) converts A\* to uniform-cost search.
3. Manhattan distance is admissible for 4-directional grid movement.
4. Tile count and Manhattan distance are common heuristics for 8-puzzle.
5. Stronger heuristics explore fewer nodes but require more computation.
6. Consistent heuristics guarantee optimality and efficient search.
7. Relaxed problems provide a systematic method to derive admissible heuristics.
8. A\* with admissible heuristic is both complete and optimal.

## Common Mistakes to Avoid

1. **Confusing admissibility with consistency:** All consistent heuristics are admissible, but admissible heuristics may not be consistent.
2. **Using non-admissible heuristics:** This can cause A\* to miss the optimal solution.
3. **Ignoring computational cost:** Stronger heuristics may cost more to compute, potentially negating benefits.
4. **Forgetting that h(n)=0 is admissible:** Some students incorrectly think heuristic must be positive.

## Revision Tips

1. Memorize the f(n) = g(n) + h(n) formula - it appears in every exam question.
2. Practice computing Manhattan distance and tile count heuristics for 8-puzzle.
3. Remember: admissible = never overestimate, consistent = triangle inequality.
4. Review solved examples of A\* search trace to understand heuristic application.
5. Know the relationship: stronger heuristic → fewer nodes expanded → faster search.
