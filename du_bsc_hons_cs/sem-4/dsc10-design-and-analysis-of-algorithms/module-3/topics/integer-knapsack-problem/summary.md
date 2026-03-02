# Integer Knapsack Problem - Summary

## Key Definitions and Concepts

- **0/1 Knapsack Problem:** A combinatorial optimization problem where each item can be taken at most once (binary decision), maximizing total profit subject to weight capacity constraint W.

- **Dynamic Programming State:** dp[i][w] = maximum profit achievable using first i items with capacity w

- **Recurrence Relation:** 
  - dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + p[i]) if w[i] ≤ w
  - dp[i][w] = dp[i-1][w] if w[i] > w

- **Base Case:** dp[0][w] = 0 and dp[i][0] = 0 for all i, w

## Important Formulas and Theorems

- **Time Complexity:** O(n × W) where n = number of items, W = knapsack capacity
- **Space Complexity:** O(n × W), optimized to O(W) with 1D array
- **0/1 Knapsack:** Iterate capacity backwards (W → w[i])
- **Unbounded Knapsack:** Iterate capacity forwards (w[i] → W)

## Key Points

- The 0/1 Knapsack is NP-hard; dynamic programming provides pseudo-polynomial solution
- Each item has exactly two choices: include or exclude (hence "0/1")
- Space optimization works because we only need dp[w-w[i]] from previous iteration
- Fractional Knapsack can be solved greedily; 0/1 requires dynamic programming
- The algorithm finds maximum profit, not necessarily minimum weight usage
- Backtracking through the DP table reveals which items form the optimal solution

## Common Mistakes to Avoid

1. **Forgetting backward iteration** in space-optimized 0/1 knapsack—this causes items to be counted multiple times
2. **Not checking weight constraint** before including an item in the recurrence
3. **Confusing 0/1 with Unbounded**—they use opposite iteration directions
4. **Ignoring base cases**—starting with incorrect initialization leads to wrong answers

## Revision Tips

1. Practice drawing complete DP tables for small examples (3-4 items, capacity 5-10)
2. Memorize the recurrence relation and understand why it works
3. Remember: 0/1 = backwards iteration, Unbounded = forwards iteration
4. Review how to backtrack to find selected items from the DP table
5. Compare with Fractional Knapsack to understand why greedy works there but not for 0/1