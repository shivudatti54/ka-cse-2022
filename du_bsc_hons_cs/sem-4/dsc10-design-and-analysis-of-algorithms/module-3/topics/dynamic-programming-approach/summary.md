# Dynamic Programming Approach - Summary

## Key Definitions and Concepts

- **Dynamic Programming**: An algorithmic technique for solving optimization problems by breaking them into overlapping subproblems and computing each subproblem only once.
- **Optimal Substructure**: A property where the optimal solution to a problem can be constructed from optimal solutions to its subproblems.
- **Overlapping Subproblems**: A property where the same subproblems are solved multiple times during the computation.
- **Memoization (Top-Down)**: A technique where recursive solutions store computed results to avoid redundant calculations.
- **Tabulation (Bottom-Up)**: An iterative approach that builds solutions starting from the smallest subproblems.
- **State**: A subproblem's solution, typically represented as dp[i] or dp[i][j].
- **Recurrence Relation**: The equation that expresses the solution to a problem in terms of solutions to smaller subproblems.

## Important Formulas and Theorems

- **Fibonacci DP**: dp[i] = dp[i-1] + dp[i-2], with dp[0] = 0, dp[1] = 1
- **0/1 Knapsack**: dp[i][w] = max(dp[i-1][w], dp[i-1][w - wi] + vi) if wi ≤ w
- **LCS**: If str1[i-1] == str2[j-1]: dp[i][j] = dp[i-1][j-1] + 1; else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- **Time Complexity**: Typically O(nW) for knapsack, O(mn) for LCS/Filbonacci
- **Space Complexity**: Can often be reduced from O(n²) to O(n) or O(1) through optimization

## Key Points

- Dynamic programming transforms exponential time complexity O(2^n) to polynomial time O(n^c) for suitable problems.
- Not all problems have optimal substructure—dynamic programming cannot be applied universally.
- Memoization automatically computes subproblems only as needed but has recursion overhead.
- Tabulation requires defining the computation order but avoids recursion stack issues.
- Space optimization is often possible by recognizing that only previous states are needed.
- The recurrence relation is the heart of any DP solution—master deriving it.
- Backtracking through the DP table reconstructs the actual solution, not just its value.

## Common Mistakes to Avoid

- Confusing dynamic programming with divide-and-conquer—DP requires overlapping subproblems.
- Forgetting base cases, which leads to incorrect solutions or runtime errors.
- Incorrect recurrence relations due to misunderstanding problem requirements.
- Failing to handle boundary conditions in array access (index out of bounds).
- Using mutable default arguments in Python implementations (common in recursion).
- Not considering space optimization opportunities when applicable.

## Revision Tips

1. Practice deriving recurrence relations from problem statements before implementing code.
2. Trace through DP tables manually with small examples to understand the flow.
3. Memorize the standard problem patterns: Fibonacci, Knapsack, LCS, LIS, Edit Distance.
4. Review previous years' DU examination questions on dynamic programming.
5. Focus on understanding why DP works, not just how to implement it—this helps in new problems.