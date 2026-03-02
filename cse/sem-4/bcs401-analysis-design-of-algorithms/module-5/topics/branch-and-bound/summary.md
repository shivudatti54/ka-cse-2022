# Branch and Bound - Summary

## Key Definitions

- **Branch and Bound**: An exact optimization algorithm that systematically enumerates candidate solutions using branching, bounding, and pruning operations.

- **Branching**: The process of dividing a problem into subproblems, creating a decision tree where each node represents a partial solution space.

- **Bounding**: Computing upper or lower bounds on the optimal solution value within a subproblem to assess its promise.

- **Pruning**: Eliminating subproblems whose bounds indicate they cannot contain a solution better than the current best.

- **Admissible Bound**: A bound that never underestimates (for minimization) or overestimates (for maximization) the true optimal value.

- **Decision Tree**: A tree structure representing all possible solution paths, where Branch and Bound reduces size through pruning.

## Important Formulas

- **Pruning Condition (Maximization)**: Prune if LB ≥ Z* (current best solution)
- **Pruning Condition (Minimization)**: Prune if LB ≤ Z*
- **Knapsack Upper Bound**: UB = Σ(pᵢxᵢ) + (W - Σ(wᵢxᵢ)) × (pⱼ/wⱼ)
- **Worst-Case Complexity**: O(b^d) where b = branching factor, d = depth to optimal solution

## Key Points

1. Branch and Bound addresses NP-hard problems exactly without circumventing theoretical complexity bounds—it provides practical improvement over exhaustive search.

2. The algorithm's effectiveness depends critically on bounding function quality; tighter bounds enable more aggressive pruning.

3. Pruning is correct because if LB ≥ best known solution, no better solution exists in that subspace.

4. Search strategies trade off memory usage against speed of convergence to optimal solutions.

5. Depth-first (LIFO) uses minimal memory O(d); Best-first finds optimal solution fastest but requires O(b^d) space.

6. Branch and Bound reduces the decision tree from 2ⁿ nodes to a potentially much smaller subset, though worst-case remains exponential.

7. The algorithm guarantees optimality when using admissible bounds, unlike heuristic approaches that may yield suboptimal solutions.

## Common Mistakes

1. **Confusing Branch and Bound with heuristics**: B&B provides exact solutions; it is not a heuristic approximation algorithm.

2. **Incorrect pruning direction**: For maximization problems, prune when LB ≥ best solution; for minimization, when LB ≤ best solution.

3. **Using inadmissible bounds**: Bounds must be admissible (never underestimate/overestimate) to guarantee optimality—using tight but inadmissible bounds may prune optimal solutions.

4. **Ignoring the connection to NP-completeness**: Failing to recognize that B&B addresses limitations of algorithmic power by providing practical solutions to otherwise intractable problems.

5. **Assuming polynomial time**: Despite practical improvements, the worst-case complexity remains exponential; B&B does not solve the P vs NP problem.