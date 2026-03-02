# Chapter 9: Dynamic Programming - Three Basic Examples and The Knapsack Problem

===========================================================

### 9.1 Introduction to Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation. This approach is particularly useful for problems that have overlapping subproblems or that can be decomposed into smaller subproblems.

### Key Concepts

- **Optimal Substructure**: A problem has optimal substructure if the optimal solution to the problem can be constructed from the optimal solutions of its subproblems.
- **Overlapping Subproblems**: Subproblems that have some common elements and can be solved once and reused in other subproblems.
- **Memoization**: Storing the solutions to subproblems in a memory (e.g., an array or a table) to avoid redundant computation.

### Three Basic Examples of Dynamic Programming

#### 1. Fibonacci Series

The Fibonacci series is a classic example of an optimal substructure problem. The series is defined as:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n-1) + F(n-2)` for `n >= 2`

A naive recursive solution to this problem would have an exponential time complexity due to the repeated computation of the same subproblems. However, using dynamic programming, we can solve this problem in linear time complexity by storing the solutions to subproblems in an array:

```markdown
| n   | F(n) |
| --- | ---- |
| 0   | 0    |
| 1   | 1    |
| 2   | 1    |
| 3   | 2    |
| 4   | 3    |
| 5   | 5    |
```

#### 2. Longest Common Subsequence

The longest common subsequence problem is another example of an optimal substructure problem. Given two sequences `X` and `Y`, we need to find the longest subsequence that is common to both sequences.

A naive recursive solution to this problem would have an exponential time complexity due to the repeated computation of the same subproblems. However, using dynamic programming, we can solve this problem in linear time complexity by storing the lengths of the longest common subsequences in a table:

```markdown
| | | | |
| X | Y | | | |
| --- | --- | | | |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 2 | 2 |
```

#### 3. Matrix Chain Multiplication

The matrix chain multiplication problem is an example of a problem with overlapping subproblems. Given a sequence of matrices, we need to find the most efficient way to multiply them together.

A naive recursive solution to this problem would have an exponential time complexity due to the repeated computation of the same subproblems. However, using dynamic programming, we can solve this problem in linear time complexity by storing the minimum number of scalar multiplications required to multiply the matrices in each subchain:

```markdown
| | | | | | |
| M1 | M2 | M3 | M4 | M5 | M6 |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| M1M2M3 | M1M2M4 | M1M2M5 | M1M2M6 |
| | | | | | |
| M1M3M4 | M1M3M5 | M1M3M6 |
| | | | | | |
| M2M4M5 | M2M4M6 |
| | | | | | |
| M3M5M6 |
```

### The Knapsack Problem

The knapsack problem is a classic example of a problem that can be solved using dynamic programming. Given a set of items, each with a weight and a value, we need to find the subset of items that maximizes the total value while not exceeding the capacity of a knapsack.

A naive recursive solution to this problem would have an exponential time complexity due to the repeated computation of the same subproblems. However, using dynamic programming, we can solve this problem in linear time complexity by storing the maximum value that can be obtained with each possible weight from 0 to `W`:

```markdown
| Weight | Maximum Value |
| ------ | ------------- |
| 0      | 0             |
| 1      | 0             |
| 2      | 2             |
| 3      | 4             |
| 4      | 6             |
| 5      | 7             |
| 6      | 10            |
| 7      | 11            |
| 8      | 13            |
```

### Conclusion

Dynamic programming is a powerful technique for solving complex problems by breaking them down into smaller subproblems and storing the solutions to subproblems. By using dynamic programming, we can solve problems like the Fibonacci series, the longest common subsequence, and the knapsack problem in linear time complexity, rather than exponential time complexity.

### References

- [1] "Introduction to Algorithms" by Thomas H. Cormen
- [2] "Dynamic Programming" by Robert Sedgewick and Kevin Wayne
- [3] "The Knapsack Problem" by Ronald L. Graham, Ronald J. Lueker, and Victor Y. Quek
