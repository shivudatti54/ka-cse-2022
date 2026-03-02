# **Coping with Limitations of Algoritmic Power: Backtracking, Branch-and-Bound, Approximation**

### I. Backtracking

- **n-Queens problem**: Find a configuration of queens on an n x n chessboard such that no two queens attack each other
- **Subset-sum problem**: Determine if a subset of integers can sum up to a given target value
- **Key concepts**:
  - Recursion
  - Backtracking
  - Pruning (early termination of search space)
- **Formulas**:
  - n-Queens problem: no known efficient algorithm
  - Subset-sum problem: 2^n - 2^(n/2) time complexity
- **Important theorems**:
  - Cook-Levin theorem: P ≠ NP

### II. Branch-and-Bound

- **Knapsack problem**: Find the optimal subset of items to include in a knapsack of limited capacity
- **Key concepts**:
  - Branching and bounding
  - Pruning (early termination of search space)
  - Lower bounding functions
- **Formulas**:
  - Knapsack problem: O(nW) time complexity
- **Important theorems**:
  - Held-Karp theorem: branch-and-bound is optimal for Knapsack problem

### III. Approximation

- **Definition**: A solution that is close to the optimal solution, but may not be optimal
- **Key concepts**:
  - Greedy algorithms
  - Local search
  - Metaheuristics
- **Formulas**:
  - Approximation ratio (e.g. 3-approximation)
- **Important theorems**:
  - Garey-Hakimi theorem: approximation algorithms can be more efficient than exact algorithms for certain problems

**Revision Tips**

- Backtracking and Branch-and-Bound can be used to solve NP-complete problems
- Approximation algorithms can provide good solutions in polynomial time
- Understand the trade-offs between exact and approximate algorithms
- Practice implementing algorithms to optimize performance
