# **Chapter 8: Dynamic Programming - Three Basic Examples and The Knapsack Problem**

### 8.1 Introduction to Dynamic Programming

---

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation. This approach is particularly useful for problems that have overlapping subproblems or that can be decomposed into smaller subproblems.

### 8.2 Key Concepts

---

### **Definition:** Dynamic Programming

Dynamic programming is a method for solving problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation.

### **Key Characteristics:**

- **Optimal substructure:** The problem can be broken down into smaller subproblems, and the optimal solution to the larger problem can be constructed from the optimal solutions of the subproblems.
- **Overlapping subproblems:** The subproblems may have some overlap, meaning that some subproblems may be identical or have similar solutions.

### 8.3 Three Basic Examples

---

### **Example 1: Fibonacci Sequence**

The Fibonacci sequence is a classic example of a problem that can be solved using dynamic programming. The sequence is defined recursively as:

F(n) = F(n-1) + F(n-2)

where F(n) is the nth Fibonacci number.

**Dynamic Programming Solution:**

```python
def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
```

### **Example 2: Longest Common Subsequence**

The longest common subsequence problem is a classic example of a problem that can be solved using dynamic programming. The problem is defined as follows:

Given two sequences X and Y, find the longest common subsequence of the two sequences.

**Dynamic Programming Solution:**

```python
def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### **Example 3: Matrix Chain Multiplication**

The matrix chain multiplication problem is a classic example of a problem that can be solved using dynamic programming. The problem is defined as follows:

Given a sequence of matrices X1, X2, ..., Xn, find the most efficient way to multiply the matrices together.

**Dynamic Programming Solution:**

```python
def matrix_chain_multiplication(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    for L in range(1, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]
```

### 8.4 The Knapsack Problem

---

The knapsack problem is a classic example of a problem that can be solved using dynamic programming. The problem is defined as follows:

Given a set of items, each with a weight and a value, and a knapsack with a limited capacity, find the optimal way to fill the knapsack so as to maximize the total value.

**Dynamic Programming Solution:**

```python
def knapsack(capacity, weights, values):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
```

### 8.5 Memory Considerations

---

Dynamic programming can be memory-intensive, especially for large problems. There are several strategies that can be used to reduce memory usage:

- **Tabulation:** Instead of storing the entire table in memory, only the most recent row or column is stored.
- **Memoization:** Instead of recomputing the same subproblem multiple times, the solution to the subproblem is stored and reused.
- **Dynamic memory allocation:** The amount of memory allocated for the table can be adjusted dynamically based on the size of the problem.

### 8.6 Conclusion

---

Dynamic programming is a powerful method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation. The knapsack problem is a classic example of a problem that can be solved using dynamic programming. By understanding the key concepts, including optimal substructure and overlapping subproblems, and by applying dynamic programming to three basic examples, we can develop a deeper understanding of this method and its applications.
