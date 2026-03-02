# Knapsack Problem - Summary

## Key Definitions

- **0/1 Knapsack Problem**: An optimization problem where each item must be either taken completely or left behind; items cannot be divided.

- **Fractional Knapsack Problem**: A variant where fractions of items can be taken, allowing more flexible combinations.

- **Optimal Substructure**: A property where an optimal solution to a problem contains optimal solutions to its subproblems.

- **NP-hardness**: A classification indicating that no polynomial-time algorithm exists unless P = NP.

## Important Formulas

- **Exhaustive Search Complexity**: O(n × 2^n) time, O(n) space

- **DP Recurrence**: 
  - dp[i][w] = dp[i-1][w] if w[i] > w
  - dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + v[i]) otherwise

- **DP Complexity**: O(nW) time, O(nW) space (or O(W) with optimization)

## Key Points

1. The Knapsack Problem requires selecting items with given weights and values to maximize total value under a weight capacity constraint.

2. Exhaustive search examines all 2^n possible subsets, guaranteeing optimality but having exponential time complexity.

3. The optimal substructure property enables dynamic programming solutions by building optimal solutions from optimal subproblems.

4. Dynamic programming improves exhaustive search by avoiding recomputation through memoization, achieving O(nW) complexity.

5. The 0/1 Knapsack is NP-hard, meaning no polynomial-time algorithm is known; DP is pseudo-polynomial.

6. Fractional Knapsack admits a greedy solution by selecting items in decreasing order of value-to-weight ratio.

7. The greedy algorithm for Fractional Knapsack is provably optimal due to the greedy choice property.

8. Space optimization in DP uses a 1D array by processing capacities in reverse order.

9. For large n, exhaustive search becomes impractical, motivating approximation algorithms and pseudo-polynomial DP.

## Common Mistakes

1. **Confusing 0/1 and Fractional variants**: Applying greedy to 0/1 Knapsack (incorrect) or DP to Fractional (unnecessary).

2. **Incorrect DP initialization**: Forgetting to initialize the base case (dp[0][w] = 0) leads to incorrect results.

3. **Forward iteration in space-optimized DP**: Processing capacities in forward order causes items to be reused multiple times.

4. **Ignoring the weight constraint**: Selecting items whose total weight exceeds W, resulting in infeasible solutions.

5. **Misunderstanding pseudo-polynomial time**: O(nW) is polynomial in W but exponential in input size (log W), hence NP-hard.