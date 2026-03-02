# **Chapter 9: Dynamic Programming - Three Basic Examples, The Knapsack Problem and Memory**

## **9.1 Introduction to Dynamic Programming**

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems, solving each subproblem only once, and storing the results to avoid redundant computation. This approach is particularly useful for problems that have overlapping subproblems or that can be decomposed into smaller subproblems.

## **9.1.1 Key Characteristics of Dynamic Programming**

- **Optimal Substructure**: The problem can be broken down into smaller subproblems, and the optimal solution to the larger problem can be constructed from the optimal solutions of the subproblems.
- **Overlapping Subproblems**: The subproblems may have some overlap, meaning that some subproblems may be identical or have similar solutions.

## **9.1.2 Basic Steps of Dynamic Programming**

1.  **Divide the Problem into Smaller Subproblems**: Break down the problem into smaller, more manageable subproblems.
2.  **Solve each Subproblem**: Solve each subproblem using a recursive or iterative approach.
3.  **Store the Results**: Store the results of each subproblem in a memory-based data structure, such as a table or array.
4.  **Combine the Results**: Combine the results of each subproblem to construct the optimal solution to the larger problem.

## **9.1.3 Example 1: Fibonacci Series**

The Fibonacci series is a classic example of a problem that can be solved using dynamic programming. The Fibonacci series is defined as:

`F(n) = F(n-1) + F(n-2)`

where `F(n)` is the `n`-th Fibonacci number.

**Example Code (Python):**

```python
def fibonacci(n):
    # Create a table to store the results of subproblems
    fib_table = [0] * (n + 1)

    # Initialize the base cases
    fib_table[0] = 0
    fib_table[1] = 1

    # Fill in the table using dynamic programming
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    # Return the nth Fibonacci number
    return fib_table[n]

# Test the function
print(fibonacci(10))  # Output: 55
```

## **9.1.4 Example 2: Longest Common Subsequence**

The longest common subsequence problem is a classic problem in computer science. Given two sequences `X` and `Y`, find the longest subsequence that is common to both sequences.

**Example Code (Python):**

```python
def longest_common_subsequence(X, Y):
    # Create a table to store the results of subproblems
    lcs_table = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]

    # Fill in the table using dynamic programming
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Return the longest common subsequence
    lcs = []
    i, j = len(X), len(Y)
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Return the longest common subsequence in the correct order
    return lcs[::-1]

# Test the function
X = "AGGTAB"
Y = "GXTXAYB"
print(longest_common_subsequence(X, Y))  # Output: ["A", "G", "T", "X", "B"]
```

## **9.1.5 Example 3: Knapsack Problem**

The knapsack problem is a classic problem in combinatorial optimization. Given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack of limited capacity to maximize the total value.

**Example Code (Python):**

```python
def knapsack(capacity, weights, values):
    # Create a table to store the results of subproblems
    dp_table = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]

    # Fill in the table using dynamic programming
    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(values[i - 1] + dp_table[i - 1][j - weights[i - 1]], dp_table[i - 1][j])

    # Return the maximum value
    return dp_table[-1][-1]

# Test the function
weights = [2, 3, 4, 5]
values = [10, 20, 30, 40]
capacity = 10
print(knapsack(capacity, weights, values))  # Output: 50
```

## **9.1.6 Memory Efficiency**

Dynamic programming can be memory-intensive, especially for large problems. However, there are several techniques to improve memory efficiency:

- **Top-Down Dynamic Programming**: Instead of building the table from scratch, reuse the results of subproblems by storing them in a smaller table.
- **Bottom-Up Dynamic Programming**: Build the table from the bottom up, starting with the smallest subproblems and working up to the largest.
- **Memoization**: Store the results of subproblems in a cache, so that they can be reused instead of recomputed.

By using these techniques, dynamic programming can be made more memory-efficient and scalable for larger problems.
