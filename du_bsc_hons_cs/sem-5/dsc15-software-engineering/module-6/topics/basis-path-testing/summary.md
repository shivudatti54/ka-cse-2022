# Basis Path Testing - Summary

## Key Definitions and Concepts

- **Basis Path Testing**: A white-box testing technique that uses the control flow graph to identify a minimum set of linearly independent paths that must be tested to ensure complete branch coverage.

- **Control Flow Graph (CFG)**: A directed graph where nodes represent statements/decision points and edges represent flow of control between them.

- **Cyclomatic Complexity (M)**: A quantitative measure of program complexity equal to the number of independent paths in the program.

- **Independent Path**: A path through the CFG that introduces at least one new edge not traversed by any other independent path.

- **Basic Block**: A sequence of statements with a single entry point and single exit point.

## Important Formulas and Theorems

- **Primary Formula**: M = E - N + 2P (where E = edges, N = nodes, P = components)
- **Simplified Formula**: M = D + 1 (where D = number of decision points)
- **Basis Set**: Contains exactly M independent paths
- **Testing Guarantee**: Testing all M basis paths ensures branch (edge) coverage

## Key Points

1. Basis path testing was developed by Tom McCabe in 1976 as a mathematically rigorous testing approach.

2. Cyclomatic complexity directly indicates the number of test cases needed for basis path testing.

3. M ≤ 10 indicates low-risk, testable code; M > 20 indicates high complexity requiring redesign.

4. Decision points (if, while, for, case) each add 1 to cyclomatic complexity.

5. Nested decision structures exponentially increase the number of possible paths but linearly increase cyclomatic complexity.

6. Basis path testing does NOT test all possible paths—only the independent basis set.

7. The basis set is not unique; multiple valid sets of independent paths can exist.

8. This technique is most effective for unit testing individual functions/methods.

## Common Mistakes to Avoid

1. **Confusing nodes and edges**: Remember that statements are nodes, and transitions between statements are edges.

2. **Forgetting to add 1**: The formula M = D + 1 requires adding 1 to the number of decision points.

3. **Incorrect CFG construction**: Not accounting for merge points where multiple paths converge.

4. **Assuming all paths must be tested**: Basis path testing tests M paths, not all possible paths.

5. **Ignoring case statements**: Switch/case statements contribute (number of cases) to decision count.

## Revision Tips

1. Practice drawing CFGs from code snippets until it becomes automatic.

2. Memorize the two cyclomatic complexity formulas and know when to use each.

3. Solve at least 3-4 CFG problems from previous year question papers to understand marking patterns.

4. Remember: Independent paths = Cyclomatic Complexity = Minimum test cases required.

5. Focus on understanding the relationship between decision points, complexity, and test paths rather than rote memorization.