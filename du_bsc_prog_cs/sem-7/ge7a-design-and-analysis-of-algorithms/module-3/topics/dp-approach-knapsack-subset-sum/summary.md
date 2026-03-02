# Dynamic Programming Approach: Knapsack and Subset Sum - Summary

## Key Definitions and Concepts

- **Dynamic Programming**: An algorithmic paradigm that solves complex problems by breaking them into overlapping subproblems and storing their solutions to avoid recomputation.

- **Optimal Substructure**: Property where an optimal solution can be constructed from optimal solutions of its subproblems.

- **Overlapping Subproblems**: Property where the same subproblems are solved multiple times during the algorithm's execution.

- **0/1 Knapsack Problem**: Given n items with weights and values, find maximum value with weight limit W, where each item can be taken at most once.

- **Subset Sum Problem**: Given a set of numbers and target sum S, determine if a subset exists that sums exactly to S.

## Important Formulas and Theorems

**0/1 Knapsack Recurrence**:
```
dp[i][w] = dp[i-1][w]                                    if w_i > w
dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)         if w_i ≤ w
```

**Subset Sum Recurrence**:
```
dp[i][s] = dp[i-1][s] OR dp[i-1][s-arr[i-1]]             if s ≥ arr[i-1]
dp[i][s] = dp[i-1][s]                                    otherwise
```

**Time Complexity**: O(n × W) for both problems, where n = number of items/elements, W = capacity/target sum.

**Space Complexity**: O(n × W) for table-based, O(W) for space-optimized versions.

## Key Points

- Greedy approach fails for 0/1 Knapsack because decisions about items depend on future choices; DP is necessary.

- The DP table's cell dp[i][w] represents the optimal solution considering first i items with weight limit w.

- For space optimization in 0/1 Knapsack, iterate weight from W down to w_i to prevent using the same item twice.

- Subset Sum is a special case of 0/1 Knapsack where all values equal weights (or we ask about existence rather than optimization).

- Both problems are NP-complete in general, but DP provides pseudo-polynomial time solution.

- Base cases are essential: dp[0][w] = 0 for Knapsack; dp[0][0] = true, dp[0][s>0] = false for Subset Sum.

- To reconstruct the solution, trace backwards from dp[n][W], checking which decision (include/exclude) led to the current value.

## Common Mistakes to Avoid

1. **Forward iteration in space optimization**: Using forward loop (0 to W) instead of reverse causes items to be used multiple times incorrectly.

2. **Confusing 0/1 and Fractional Knapsack**: Remember 0/1 requires DP, Fractional can use greedy.

3. **Incorrect base case initialization**: Setting wrong base values leads to completely wrong answers.

4. **Forgetting boundary conditions**: Not checking if w_i ≤ w before accessing dp[i-1][w-w_i].

5. **Not considering empty set**: For Subset Sum, always remember sum 0 is always achievable with empty set.

## Revision Tips

1. Practice tracing through small examples by hand—write out the complete DP table for at least 2-3 examples.

2. Memorize the recurrence relations and understand the logic behind each term (include vs. exclude decisions).

3. Remember the space optimization trick: reverse iteration is the key to using 1D arrays correctly.

4. Review the time-space tradeoff: understand when optimization is possible and when it's not worth the complexity.

5. Solve previous year DU examination questions on this topic to familiarize with exam patterns and difficulty levels.