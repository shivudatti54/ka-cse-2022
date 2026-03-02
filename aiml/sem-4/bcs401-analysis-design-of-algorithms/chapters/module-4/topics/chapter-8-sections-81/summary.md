# **Revision Notes: Dynamic Programming - Chapter 8 (Sections 8.1)**

## **Key Concepts**

- **Definition of Dynamic Programming**: A method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation.
- **Memoization**: The process of storing the results of expensive function calls so that they can be reused instead of recalculated.
- **Tabulation**: A technique for solving dynamic programming problems by building a table of solutions to subproblems.

## **Theorems and Formulas**

- **Optimal Substructure**: If the problem can be broken down into smaller subproblems, and the optimal solution to the larger problem can be constructed from the optimal solutions of the subproblems, then the problem can be solved using dynamic programming.
- **Overlapping Subproblems**: If the problem has overlapping subproblems, meaning that some subproblems are identical or have similar solutions, then dynamic programming can be used to avoid redundant computation.

## **Important Formulas**

- **Knapsack Problem Formula**: `dp[i][w] = max(dp[i-1][w], dp[i-1][w-x[i]] + v[i])`, where `dp[i][w]` is the maximum value that can be obtained with `i` items and maximum weight `w`.
- **Fibonacci Formula**: `F(n) = F(n-1) + F(n-2)`, where `F(n)` is the `n`-th Fibonacci number.

## **Three Basic Examples**

- **0/1 Knapsack Problem**: A classic problem where we have a set of items, each with a weight and a value, and we need to select a subset of items to put in a knapsack of limited capacity.
- **Longest Common Subsequence (LCS)**: A problem where we have two sequences and we need to find the longest subsequence that is common to both sequences.
- **Shortest Path Problem**: A problem where we have a graph and we need to find the shortest path between two nodes.

## **Important Techniques**

- **Bottom-up Approach**: A technique where we start with the smallest subproblems and build up to the largest problem.
- **Top-down Approach**: A technique where we start with the largest problem and break it down into smaller subproblems.
