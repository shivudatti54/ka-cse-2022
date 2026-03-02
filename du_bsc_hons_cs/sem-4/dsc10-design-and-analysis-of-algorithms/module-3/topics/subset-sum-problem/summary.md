# Subset Sum Problem - Summary

## Key Definitions and Concepts

- **Subset Sum Problem:** Given a set S of n positive integers and target T, determine if a subset of S sums exactly to T
- **NP-Complete:** A class of problems for which no polynomial-time algorithm is known; if one can be solved in polynomial time, all NP-complete problems can
- **Pseudo-polynomial:** Algorithm whose runtime is polynomial in the numeric value of input (T), but exponential in input size (log T)

## Important Formulas and Theorems

- **Brute Force:** Time O(n × 2ⁿ), Space O(n)
- **DP Solution:** Time O(n × T), Space O(n × T) or O(T) optimized
- **Number of possible subsets:** 2ⁿ

## Key Points

- Subset Sum is Karp's original NP-complete problem (1972)
- DP solution is pseudo-polynomial; not truly polynomial for large T
- Always iterate backward in space-optimized 1D DP to avoid reusing elements
- Base case: dp[0] = true (empty subset achieves sum 0)
- Subset Sum is a special case of 0/1 Knapsack (when values = weights)
- Partition Problem is a special case where target = total_sum/2
- FPTAS exists for the optimization version of Subset Sum

## Common Mistakes to Avoid

- Forgetting to initialize dp[0] = true as the base case
- Iterating forward in 1D DP, causing elements to be counted multiple times
- Confusing pseudo-polynomial with polynomial complexity
- Not handling the case when element > target sum in DP transition

## Revision Tips

1. Practice drawing complete DP tables for small examples by hand
2. Remember the backward iteration rule for space optimization
3. Know the exact recurrence: dp[i][j] = dp[i-1][j] OR dp[i-1][j - S[i-1]]
4. Understand that pseudo-polynomial depends on numeric value, not input size
5. Review the connection between Subset Sum, Partition, and Knapsack problems