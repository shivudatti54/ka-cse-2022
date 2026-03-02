# Coping with Limitations of Algorithmic Power: Backtracking, Branch-and-Bound, and Approximation

### Introduction

- Algorithmic power is limited by computational complexity, leading to the P vs NP problem.
- NP-complete problems are intractable, but approximations and heuristics can be used to cope with limitations.

### Backtracking

- **n-Queens Problem**:
  - Problem: Place n queens on an n x n chessboard such that no queen attacks any other.
  - Algorithm: Recursive backtracking to try all possible placements.
  - Time complexity: O(n!)
- **Subset-sum Problem**:
  - Problem: Determine if a subset of a given set of integers sums up to a target value.
  - Algorithm: Backtracking to try all possible subsets.
  - Time complexity: O(2^n)

### Branch-and-Bound

- **Knapsack Problem**:
  - Problem: Find the optimal subset of items with maximum value under a weight constraint.
  - Algorithm: Branch-and-bound to prune branches that are guaranteed to have a suboptimal solution.
  - Time complexity: O(nW log W)

### Approximation

- **Approximation Algorithms**:
  - Goal: Find a solution that is close to the optimal solution in polynomial time.
  - Techniques:
    - Greedy algorithms
    - Local search algorithms
  - Examples:
    - Approximation algorithms for the Traveling Salesman Problem and the Shortest Path Problem

### Important Formulas and Definitions

- **PSPACE**: The class of decision problems solvable in polynomial space.
- **NP**: The class of decision problems solvable in polynomial time by a deterministic Turing machine.
- **NP-Complete**: A problem that is at least as hard as the hardest problems in NP.

### Theorems

- **Cook-Levin Theorem**: P = NP if and only if every NP-complete problem has a polynomial-time algorithm.
- **Arora-Barak Theorem**: The hardness of approximation for NP problems.
