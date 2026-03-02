# **Chapter 9: Dynamic Programming - Basics and Examples**

## **9.1 Introduction to Dynamic Programming**

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation. This technique is particularly useful for problems that have overlapping subproblems or that can be decomposed into smaller subproblems.

**Key Concepts:**

- **Overlapping subproblems:** Subproblems that have some common characteristics or that can be mapped to each other.
- **Optimal substructure:** The property that the optimal solution to a problem can be constructed from the optimal solutions of its subproblems.
- **Memoization:** The process of storing the solutions to subproblems in a memory-based data structure to avoid redundant computation.

## **Why Dynamic Programming?**

Dynamic programming is useful for solving several types of problems, including:

- **Optimization problems:** Problems that seek to minimize or maximize a function subject to certain constraints.
- **Counting problems:** Problems that require counting the number of ways to achieve a certain goal.
- **String problems:** Problems that involve manipulating strings, such as finding the longest common subsequence.

## **Three Basic Examples of Dynamic Programming**

### Example 1: Fibonacci Sequence

The Fibonacci sequence is a classic example of dynamic programming. The sequence is defined recursively as follows:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n-1) + F(n-2)`, for `n > 1`

A naive recursive implementation of the Fibonacci sequence would involve redundant computation, as each recursive call would compute the same subproblem multiple times. A dynamic programming solution avoids this redundancy by storing the solutions to subproblems in an array:

```python
def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
```

### Example 2: Longest Common Subsequence

The longest common subsequence (LCS) problem is a classic problem in computer science. Given two sequences, find the longest subsequence that is common to both. A naive recursive implementation would involve redundant computation, as each recursive call would compute the same subproblem multiple times. A dynamic programming solution avoids this redundancy by storing the solutions to subproblems in a 2D array:

```python
def lcs(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

### Example 3: Knapsack Problem

The knapsack problem is a classic problem in computer science. Given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack of limited capacity to maximize the total value. A naive recursive implementation would involve redundant computation, as each recursive call would compute the same subproblem multiple times. A dynamic programming solution avoids this redundancy by storing the solutions to subproblems in a 2D array:

```python
def knapsack(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]
```

## **Memory Considerations**

Dynamic programming solutions can be memory-intensive, particularly when dealing with large inputs. To mitigate this, several techniques can be used:

- **Memoization:** Store the solutions to subproblems in a memory-based data structure to avoid redundant computation.
- **Tabulation:** Store the solutions to subproblems in a table or array to avoid redundant computation.
- **Dynamic memory allocation:** Allocate memory dynamically to store the solutions to subproblems.

## **Conclusion**

Dynamic programming is a powerful technique for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation. By applying dynamic programming to a wide range of problems, we can develop efficient and scalable solutions that can handle large inputs.
