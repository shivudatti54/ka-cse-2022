# Algorithm Design Strategies - Summary

## Key Definitions and Concepts
- Divide and Conquer: Recursive problem decomposition
- Greedy Choice: Locally optimal decision with global impact
- Optimal Substructure: Optimal solution contains optimal sub-solutions
- Memoization: Storing intermediate results in DP
- Backtracking: Depth-first search with pruning
- Amortized Analysis: Average-case complexity over operations

## Important Formulas and Theorems
- Master Theorem: T(n) = aT(n/b) + O(n^k)
- Bellman Equation: V(s) = maxₐ[R(s,a) + γV(s')]
- Huffman Coding: H = Σp_i log₂(1/p_i)
- Knapsack DP: max(val[n-1] + K(n-1,w-wt[n-1]), K(n-1,w))

## Key Points
- Divide and Conquer works best when subproblems are independent
- Greedy algorithms require proof of correctness
- DP solves problems with overlapping subproblems
- Backtracking has exponential time but works for NP-hard problems
- Randomized algorithms trade determinism for speed
- Space-time tradeoff is crucial in strategy selection
- Real-world applications include VLSI design and genome sequencing

## Common Mistakes to Avoid
- Applying Greedy to problems without optimal substructure
- Confusing memoization (top-down) with tabulation (bottom-up)
- Missing base cases in recurrence relations
- Overlooking space complexity in DP implementations

## Revision Tips
- Practice deriving time complexities using Master Theorem
- Create strategy comparison charts with example problems
- Solve previous years' DU questions on Knapsack variations
- Implement all strategies in Python/Java for better retention
- Focus on proof techniques for Greedy algorithms

Length: 600 words