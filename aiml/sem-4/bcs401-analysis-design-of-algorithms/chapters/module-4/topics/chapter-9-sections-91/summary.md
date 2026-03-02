# **Chapter 9: Dynamic Programming**

### 9.1 Introduction

- Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems.
- It uses memoization to store the solutions to subproblems to avoid redundant computation.

### Key Concepts

- **Optimal Substructure**: The problem can be broken down into smaller subproblems, and the optimal solution to the larger problem can be constructed from the optimal solutions of the subproblems.
- **Overlapping Subproblems**: The subproblems may have some overlap, i.e., some subproblems may be identical or have similar solutions.

### Important Formulas and Definitions

- **Dynamic Programming Formulation**:
  - Define a function `f(i)` that represents the optimal solution to the problem up to index `i`.
  - The function `f(i)` is defined recursively as:
    - `f(i) = min(f(i-1), f(i-2), ..., f(j)) + c`
    - where `j` is the index of the last element in the array, and `c` is the cost of the current element.

- **Memoization**:
  - Store the solutions to subproblems in an array `dp` of size `n+1`, where `dp[i]` represents the optimal solution to the problem up to index `i`.
  - Use the formula `dp[i] = min(dp[i-1], dp[i-2], ..., dp[j]) + c` to compute the optimal solution to the problem up to index `i`.

- **The Knapsack Problem**:
  - Given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack of limited capacity to maximize the total value.
  - The Knapsack Problem can be solved using dynamic programming by defining a function `f(i, w)` that represents the optimal solution to the problem up to index `i` and weight `w`.

### Important Theorems

- **Theorem 1**: If a problem has optimal substructure and overlapping subproblems, then it can be solved using dynamic programming.

### Important Algorithms

- **The Knapsack Problem Algorithm**:
  - Initialize an array `dp` of size `(n+1) x (w+1)`, where `dp[i][j]` represents the optimal solution to the problem up to index `i` and weight `j`.
  - Fill the array using the recurrence relation `dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v[i])`, where `v[i]` is the value of the `i`-th item.
  - The optimal solution is stored in `dp[n][w]`.
