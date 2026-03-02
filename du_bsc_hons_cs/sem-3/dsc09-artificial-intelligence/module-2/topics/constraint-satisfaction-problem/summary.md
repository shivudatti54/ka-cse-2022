# Constraint Satisfaction Problems (CSP) - Summary

## Key Definitions and Concepts

- **CSP Definition**: A Constraint Satisfaction Problem is a triple (X, D, C) where X is a set of variables, D is a set of domains (possible values), and C is a set of constraints.

- **Solution**: A complete assignment where all variables have values from their domains and all constraints are satisfied.

- **Constraint Graph**: A graph where nodes represent variables and edges represent binary constraints between variables.

## Important Formulas and Theorems

- **Backtracking Complexity**: O(d^n) worst-case, where d = domain size, n = number of variables

- **AC-3 Complexity**: O(ed³), where e = number of arcs, d = maximum domain size

- **Arc Consistency**: For binary constraint between X and Y, arc (X→Y) is consistent if for every value in D(X), there exists some value in D(Y) that satisfies the constraint.

## Key Points

- CSPs formalize problems requiring assignment of values to variables under constraints - fundamental in AI problem-solving.

- Unary constraints involve one variable; binary constraints involve two; global constraints (like Alldiff) can involve many variables.

- Backtracking is the basic algorithm - assign variables recursively, backtrack on failure.

- Forward checking removes incompatible values from neighboring variables after each assignment.

- AC-3 enforces arc consistency by repeatedly removing values that have no support in neighboring domains.

- MRV (Minimum Remaining Values) heuristic selects the variable with fewest domain values - fails early to save computation.

- LCV (Least Constraining Value) heuristic prefers values that restrict least choices for neighbors - preserves flexibility.

- Constraint propagation dramatically reduces search space before and during search.

- Real-world applications include scheduling, timetabling, resource allocation, and puzzle solving.

## Common Mistakes to Ignore

- Confusing constraint satisfaction with optimization - CSPs are decision problems (find any valid solution).

- Forgetting that arc consistency does not guarantee a solution - it only removes impossible values.

- Applying heuristics incorrectly - MRV chooses variable with fewest values; LCV orders values for a variable.

- Not checking forward after assignment - always update neighbor domains in backtracking.

## Revision Tips

1. Practice drawing constraint graphs for problems like map coloring and n-Queens.

2. Trace AC-3 algorithm on simple 2-variable problems to understand arc consistency.

3. Solve at least 3-4 CSP examples using backtracking with MRV heuristic by hand.

4. Memorize the complexity formulas - they frequently appear in DU exams.

5. Focus on understanding when and why each heuristic improves performance.