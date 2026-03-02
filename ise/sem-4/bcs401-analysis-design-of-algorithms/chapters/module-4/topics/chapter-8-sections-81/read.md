# **Chapter 8: Analysis & Design of Algorithms**

## **Dynamic Programming: A Brief Overview**

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the results to avoid redundant computation. This technique is particularly useful for problems with overlapping subproblems and optimal substructure.

**Key Concepts:**

- **Optimal Substructure:** A problem has optimal substructure if the optimal solution to the problem can be constructed from the optimal solutions of its subproblems.
- **Overlapping Subproblems:** A problem has overlapping subproblems if the subproblems are identical or have similar solutions.

**Three Basic Examples of Dynamic Programming:**

### 1. Fibonacci Series

The Fibonacci series is a classic example of a dynamic programming problem. The problem is to find the `n`-th Fibonacci number, where each Fibonacci number is the sum of the two preceding ones, usually starting with 0 and 1.

**Naive Recursive Solution:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Dynamic Programming Solution:**

```python
def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
```

### 2. Longest Common Subsequence (LCS)

The LCS problem is to find the longest common subsequence between two sequences. This problem has overlapping subproblems and optimal substructure.

**Naive Recursive Solution:**

```python
def lcs(str1, str2):
    if not str1 or not str2:
        return ""
    if str1[0] == str2[0]:
        return str1[0] + lcs(str1[1:], str2[1:])
    else:
        return max(lcs(str1, str2[1:]), lcs(str1[1:], str2), key=len)
```

**Dynamic Programming Solution:**

```python
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_str.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(lcs_str))
```

### 3. Knapsack Problem

The knapsack problem is a classic problem in computer science and operations research. The problem is to find the optimal subset of items with a given weight capacity that maximizes the total value.

**Naive Recursive Solution:**

```python
def knapsack(capacity, weights, values):
    if capacity == 0 or len(values) == 0:
        return 0
    if weights[0] > capacity:
        return knapsack(capacity, weights[1:], values[1:])
    else:
        return max(values[0] + knapsack(capacity-weights[0], weights[1:], values[1:]),
                   knapsack(capacity, weights[1:], values[1:]))
```

**Dynamic Programming Solution:**

```python
def knapsack(capacity, weights, values):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]],
                               dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]
```

**Memory Optimization:**

In the dynamic programming solutions, we use a 2D array `dp` to store the results of subproblems. However, this can lead to high memory usage for large inputs. To optimize memory usage, we can use a 1D array and store the last row of the `dp` array in a separate array.

```python
def knapsack(capacity, weights, values):
    n = len(values)
    dp = [0] * (capacity + 1)
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j:
                dp[j] = max(values[i-1] + dp[j-weights[i-1]],
                             dp[j])
            else:
                dp[j] = dp[j]
    return dp[capacity]
```

In this optimized solution, we only store the last row of the `dp` array, which reduces memory usage significantly.

By using dynamic programming, we can solve these complex problems efficiently and with minimal memory usage.
