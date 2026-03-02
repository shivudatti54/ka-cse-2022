# Chapter 9 (Sections 9.1) Dynamic Programming: Three Basic Examples

### Key Concepts

- **Dynamic Programming (DP)**: A method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the results to avoid redundant computation.
- **Optimal Substructure**: A property of problems that can be broken down into smaller subproblems, where the optimal solution to the larger problem can be constructed from the optimal solutions of the subproblems.
- **Overlapping Subproblems**: A common occurrence in DP problems, where the same subproblem is solved multiple times, resulting in redundant computation.

### Important Formulas and Definitions

- **Bellman's Principle of Optimality**: "An optimal solution to a problem can be constructed from the optimal solutions of its subproblems."
- **Memoization**: A technique used to store the results of subproblems in a memory (e.g., table, array), so that they can be quickly retrieved and reused instead of recomputed.
- **Recurrence Relation**: An equation that defines a problem in terms of smaller instances of the same problem.

### The Three Basic Examples

- **Fibonacci Series**: A classic DP problem where we calculate the `n`-th Fibonacci number, where `F(n) = F(n-1) + F(n-2)`.
- **Shortest Path Problem**: A DP problem where we find the shortest path between two nodes in a graph.
- **Knapsack Problem**: A classic DP problem where we maximize the value of items in a knapsack of limited capacity.

### Important Theorems

- **Knapsack Unbounded Knapsack Problem**: NP-Complete
- **Fibonacci Series**: NP-Complete
- **Shortest Path Problem**: NP

### Quick Revision Points

- Break down complex problems into smaller subproblems
- Store results of subproblems in memory (memoization)
- Use recurrence relations to define problems in terms of smaller instances
- Identify optimal substructure and overlapping subproblems
- Use Bellman's Principle of Optimality to construct optimal solutions
