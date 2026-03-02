# Weighted Interval Scheduling - Summary

## Key Definitions and Concepts

- **Weighted Interval Scheduling Problem**: Given n intervals with start times, finish times, and weights, select a subset of non-overlapping intervals that maximizes total weight.

- **p[j] Function**: For interval j (sorted by finish time), p[j] is the index of the last interval that finishes before interval j starts, or 0 if no such interval exists.

- **Compatible Intervals**: Two intervals are compatible if they do not overlap; typically, [s[i], f[i]) and [s[j], f[j]) are compatible if f[i] ≤ s[j] or f[j] ≤ s[i].

- **Optimal Substructure**: The optimal solution for first j intervals can be constructed from optimal solutions of smaller subproblems.

## Important Formulas and Theorems

**Recurrence Relation:**
```
OPT(j) = max(OPT(j-1), w[j] + OPT(p[j]))
```

**Time Complexity:** O(n log n) with binary search for p[j], or O(n²) with linear search
**Space Complexity:** O(n) for dp array and auxiliary structures

## Key Points

1. Always sort intervals by finish time before applying dynamic programming
2. p[j] can be computed efficiently using binary search on sorted finish times
3. The DP solution considers two cases: include interval j or exclude interval j
4. Traceback starting from dp[n] recovers the selected intervals
5. The problem exhibits optimal substructure, enabling polynomial-time solution
6. Without DP, exhaustive search would require checking 2^n subsets (exponential)
7. Initialization: dp[0] = 0 serves as the base case

## Common Mistakes to Forget

- Sorting intervals before computing p[j] values
- Incorrectly computing p[j] when intervals have equal finish times
- Forgetting to initialize dp[0] = 0
- Not understanding that intervals with f[i] = s[j] are considered non-overlapping

## Revision Tips

1. Practice computing p[j] manually with at least 5 different examples
2. Draw the interval timeline to visualize compatibility relationships
3. Write out the traceback process step-by-step for different inputs
4. Memorize the recurrence relation—it forms the core of the algorithm
5. Understand the connection between this problem and 0/1 Knapsack