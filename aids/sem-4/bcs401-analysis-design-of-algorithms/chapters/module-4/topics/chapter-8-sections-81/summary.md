# Chapter 8 (Sections 8.1) - Analysis & Design of Algorithms

## Dynamic Programming: Key Concepts

### Definitions

- **Dynamic Programming**: A method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation.
- **Optimal Substructure**: A problem has optimal substructure if the optimal solution to the problem can be constructed from the optimal solutions of its subproblems.
- **Overlapping Subproblems**: When the subproblems of a problem are not independent of each other, causing redundant computation.

### Important Formulas and Theorems

- **Fibonacci Sequence Formula**: `F(n) = F(n-1) + F(n-2)`
- **Memoization Formula**: `T(n) = a \* T(n-1) + b \* T(n-2)`
- **Memoization Theorem**: If a problem has optimal substructure and overlapping subproblems, then there exists a polynomial-time algorithm for solving the problem.

### Key Concepts

- **Divide and Conquer**: A problem-solving strategy that breaks down a problem into smaller subproblems, solves each subproblem, and combines the solutions to solve the original problem.
- **Tabulation**: A method for solving dynamic programming problems by storing the solutions to subproblems in a table.
- **Space Complexity**: The amount of memory required to store the solutions to subproblems.

### Real-World Applications

- **The Knapsack Problem**: A classic problem in dynamic programming that involves finding the optimal way to pack a set of items of different weights and values into a knapsack of limited capacity.
- **Fibonacci Series**: A series of numbers in which each number is the sum of the two preceding numbers (1, 1, 2, 3, 5, 8, ...).

### Summary

This chapter provides an overview of dynamic programming, including definitions, formulas, and key concepts. It also discusses the importance of optimal substructure and overlapping subproblems, and introduces the concept of memoization. The chapter concludes with real-world applications of dynamic programming, including the knapsack problem and the Fibonacci series.
