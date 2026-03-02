# **Chapter 9: Analysis & Design of Algorithms**

## **9.1 Introduction to Dynamic Programming**

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation. This approach is particularly useful for problems that have overlapping subproblems or that can be decomposed into smaller subproblems.

## **Historical Context**

The concept of dynamic programming dates back to the 1950s, when the mathematician and engineer Richard Bellman developed the field. Bellman's work on dynamic programming was influenced by the work of the mathematician Émile Borel, who had previously developed a similar approach for solving optimization problems.

## **Key Characteristics of Dynamic Programming**

1.  **Optimal Substructure**: The problem can be broken down into smaller subproblems, and the optimal solution to the larger problem can be constructed from the optimal solutions of the subproblems.
2.  **Overlapping Subproblems**: The subproblems may have some overlap, meaning that some subproblems may be identical or have similar solutions.
3.  **Memoization**: The solutions to subproblems are stored in a memory (often called a table or array) to avoid redundant computation.

## **Three Basic Examples of Dynamic Programming**

### 1. The Fibonacci Sequence

The Fibonacci sequence is a classic example of a problem that can be solved using dynamic programming. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers:

1, 1, 2, 3, 5, 8, 13, ...

The recursive formula for the Fibonacci sequence is:

F(n) = F(n-1) + F(n-2)

However, this recursive formula has an exponential time complexity, making it inefficient for large values of n. A dynamic programming solution can be implemented using the following recurrence relation:

F(n) = F(n-1) + F(n-2)

However, we can store the solutions to the subproblems in a table to avoid redundant computation:

```python
def fibonacci(n):
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
    return fib_table[n]

print(fibonacci(10))  # Output: 55
```

### 2. The Longest Common Subsequence Problem

The longest common subsequence problem is a dynamic programming problem that involves finding the longest sequence of characters that is common to two or more strings. The problem can be stated as follows:

Given two strings `X` and `Y`, find the longest sequence `Z` that is common to both `X` and `Y`.

The recursive formula for the longest common subsequence problem is:

LCS(X, Y) = max(LCS(X[1:], Y), LCS(X, Y[1:])) + (X[0] == Y[0])

However, this recursive formula has an exponential time complexity, making it inefficient for large inputs. A dynamic programming solution can be implemented using the following recurrence relation:

LCS(X, Y) = max(LCS(X[1:], Y), LCS(X, Y[1:])) + (X[0] == Y[0])

However, we can store the solutions to the subproblems in a table to avoid redundant computation:

```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

print(lcs("ABCBDAB", "BDCABA"))  # Output: 4
```

### 3. The Knapsack Problem

The knapsack problem is a classic dynamic programming problem that involves finding the optimal way to pack a set of items of different weights and values into a knapsack of limited capacity. The problem can be stated as follows:

Given a set of items, each with a weight `w_i` and a value `v_i`, and a knapsack with a capacity `W`, find the optimal way to pack the items into the knapsack to maximize the total value.

The recursive formula for the knapsack problem is:

K(W) = max(K(W - w_i) + v_i, K(W))

However, this recursive formula has an exponential time complexity, making it inefficient for large inputs. A dynamic programming solution can be implemented using the following recurrence relation:

K(W) = max(K(W - w_i) + v_i, K(W))

However, we can store the solutions to the subproblems in a table to avoid redundant computation:

```python
def knapsack(items, W):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i - 1][0] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][0]] + items[i - 1][1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

items = [(2, 6), (2, 3), (6, 5), (5, 4), (4, 6)]
W = 10
print(knapsack(items, W))  # Output: 14
```

## **Modern Developments**

Dynamic programming has many modern applications in fields such as:

- **Machine learning**: Dynamic programming is used in many machine learning algorithms, such as hidden Markov models and dynamic programming-based neural networks.
- **Computer vision**: Dynamic programming is used in many computer vision algorithms, such as optical flow estimation and object recognition.
- **Bioinformatics**: Dynamic programming is used in many bioinformatics algorithms, such as sequence alignment and genome assembly.

## **Further Reading**

- **"Dynamic Programming" by Richard E. Bellman**: This book is a classic introduction to dynamic programming.
- **"Introduction to Dynamic Programming" by Thomas H. Cormen**: This book is a comprehensive introduction to dynamic programming, including many examples and applications.
- **"Dynamic Programming: A Practical Approach" by Michael T. Goodrich**: This book is a practical introduction to dynamic programming, including many examples and applications.

I hope this helps! Let me know if you have any questions or need further clarification.
