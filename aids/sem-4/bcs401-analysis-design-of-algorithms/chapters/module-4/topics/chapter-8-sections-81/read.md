# **Chapter 8: Dynamic Programming - Three Basic Examples and Memory**

## **8.1 Introduction to Dynamic Programming**

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation. This technique is particularly useful for problems that have overlapping subproblems or that can be decomposed into smaller subproblems.

**Key Concepts:**

- **Optimal Substructure**: A problem has optimal substructure if the optimal solution to the problem can be constructed from the optimal solutions of its subproblems.
- **Overlapping Subproblems**: A problem has overlapping subproblems if the subproblems are similar or have some common characteristics.
- **Memoization**: The process of storing the solutions to subproblems in a memory to avoid redundant computation.

## **3 Basic Examples of Dynamic Programming**

### 1. Fibonacci Series

The Fibonacci series is a classic example of a dynamic programming problem. The problem is to find the `n`-th Fibonacci number, where each number is the sum of the two preceding numbers (1, 1, 2, 3, 5, 8, ...).

**Naive Recursive Solution:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

**Dynamic Programming Solution:**

```python
def fibonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result
```

**2. Longest Common Subsequence (LCS)**

The LCS problem is to find the longest common subsequence between two sequences. For example, given the sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA".

**Naive Recursive Solution:**

```python
def lcs(str1, str2):
    if not str1 or not str2:
        return ""
    else:
        if str1[0] == str2[0]:
            return str1[0] + lcs(str1[1:], str2[1:])
        else:
            return max(lcs(str1, str2[1:]), lcs(str1[1:], str2), key=len)
```

**Dynamic Programming Solution:**

```python
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_str = str1[i-1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs_str
```

### 3. Knapsack Problem

The knapsack problem is a classic problem in combinatorial optimization. Given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack of limited capacity to maximize the total value.

**Naive Recursive Solution:**

```python
def knapsack(capacity, weights, values):
    if not weights or not values or not capacity:
        return 0
    else:
        if weights[0] > capacity:
            return knapsack(capacity, weights[1:], values[1:])
        else:
            return max(values[0] + knapsack(capacity-weights[0], weights[1:], values[1:]), knapsack(capacity, weights[1:], values[1:]))
```

**Dynamic Programming Solution:**

```python
def knapsack(capacity, weights, values):
    m, n = len(weights), len(values)
    dp = [[0] * (capacity+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, capacity+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j])
    return dp[m][capacity]
```

## **Memory Considerations**

Dynamic programming often requires significant memory to store the solutions to subproblems. However, with the use of memoization, we can avoid redundant computation and reduce the memory requirements.

**Memoization Techniques:**

- **Top-Down Memoization**: Store the solutions to subproblems in a table and reuse them as needed.
- **Bottom-Up Memoization**: Store the solutions to subproblems in a table and reuse them as needed.

By using memoization techniques, we can efficiently solve complex dynamic programming problems with limited memory.
