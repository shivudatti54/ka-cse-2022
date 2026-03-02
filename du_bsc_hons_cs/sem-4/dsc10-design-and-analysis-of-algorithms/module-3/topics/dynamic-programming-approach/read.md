# Dynamic Programming Approach

## Introduction

Dynamic Programming (DP) is one of the most powerful algorithmic design techniques in computer science, essential for solving optimization problems efficiently. Unlike the divide-and-conquer approach, which breaks problems into independent subproblems, dynamic programming applies when subproblems share smaller subproblems—a property known as overlapping subproblems. The technique was pioneered by Richard Bellman in the 1950s and remains foundational in algorithm design for competitive programming, resource allocation, string processing, and many real-world applications.

In the context of the University of Delhi's DSC10 course, dynamic programming represents a critical topic that frequently appears in both internal assessments and end-semester examinations. Understanding DP is not merely about memorizing formulas; it requires developing algorithmic thinking to recognize when a problem exhibits optimal substructure and overlapping subproblems. This approach transforms exponential-time algorithms into polynomial-time solutions, making it indispensable for solving complex computational problems within reasonable time constraints.

## Key Concepts

### Characteristics of Dynamic Programming Problems

A problem is suitable for dynamic programming solution if it exhibits two fundamental properties:

1. **Optimal Substructure**: The optimal solution to the problem can be constructed from optimal solutions to its subproblems. This means that if we know the optimal solution for smaller instances, we can build the optimal solution for larger instances. For example, in the shortest path problem, the shortest path from source to destination can be decomposed into shorter paths.

2. **Overlapping Subproblems**: The same subproblems are solved multiple times during the computation. Consider the recursive computation of Fibonacci numbers—F(n) requires computing F(n-1) and F(n-2), which in turn require computing F(n-2) again, leading to exponential redundant calculations.

### Approaches to Dynamic Programming

There are two primary methodologies for implementing dynamic programming:

**Top-Down Approach (Memoization)**: This is the recursive approach where we store the results of expensive function calls in a table (memoization cache). When we need a solution to a subproblem, we first check if it's already computed; if yes, we return the cached result; otherwise, we compute it and store it. Memoization transforms a recursive algorithm with exponential complexity into one with polynomial complexity.

**Bottom-Up Approach (Tabulation)**: This approach builds the solution iteratively starting from the smallest subproblems and progressively builds up to the solution of the original problem. We create a table and fill it systematically. This method typically has better space optimization and avoids recursion overhead.

### Steps to Formulate a Dynamic Programming Solution

1. Characterize the structure of an optimal solution
2. Define the value of an optimal solution recursively
3. Compute the value of an optimal solution (either top-down or bottom-up)
4. Construct the optimal solution from the computed information

### Common Dynamic Programming Patterns

The field has developed several recurring patterns that appear across different problem types. The **Linear DP** pattern involves problems where the state depends on the previous state only, such as in Fibonacci-like sequences. The **2D DP** pattern emerges in problems involving two dimensions, such as grid traversal or string matching. The **Knapsack DP** pattern handles problems with binary choices or selection from multiple items. The **Interval DP** pattern addresses problems where we need to combine solutions from intervals, such as matrix chain multiplication or optimal binary search trees.

## Examples

### Example 1: Fibonacci Number Calculation

**Problem**: Compute the nth Fibonacci number where F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n ≥ 2.

**Naive Recursive Approach**:
```
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This has time complexity O(2^n), which is exponential.

**Dynamic Programming Solution (Bottom-Up)**:
```
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
Time Complexity: O(n), Space Complexity: O(n)

**Space-Optimized Solution**:
```
def fib_optimized(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1
```
Time Complexity: O(n), Space Complexity: O(1)

### Example 2: 0/1 Knapsack Problem

**Problem**: Given n items with weights w1, w2, ..., wn and values v1, v2, ..., vn, and a knapsack with capacity W, find the maximum value that can be obtained by selecting items such that the total weight does not exceed W. Each item can be selected at most once.

**Solution using Dynamic Programming**:

Let dp[i][w] represent the maximum value achievable using the first i items with knapsack capacity w.

Recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w - wi] + vi) if wi ≤ w, else dp[i-1][w]

```
def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]
```

**Example**: values = [60, 100, 120], weights = [10, 20, 30], W = 50
- Solution: Maximum value = 220 (items with weights 10 and 20)
- Time Complexity: O(nW), Space Complexity: O(nW)

### Example 3: Longest Common Subsequence (LCS)

**Problem**: Given two strings str1 and str2, find the length of the longest subsequence present in both strings. A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

**Solution using Dynamic Programming**:

Let dp[i][j] represent the length of LCS of str1[0:i] and str2[0:j].

Recurrence:
- If str1[i-1] == str2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
- Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

```
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

**Example**: str1 = "AGGTAB", str2 = "GXTXAYB"
- LCS = "GTAB" (length 4)
- Time Complexity: O(mn), Space Complexity: O(mn)

## Exam Tips

For students appearing in DU semester examinations, the following points are critical:

1. **Identify DP Problems**: The first step in solving any DP problem is recognizing that it exhibits optimal substructure and overlapping subproblems. This identification is often tested in objective questions.

2. **Define State Clearly**: Clearly define what each state (dp[i] or dp[i][j]) represents. This is essential for both deriving the recurrence relation and for partial credit in examination.

3. **Establish Base Cases**: Always identify and implement base cases correctly. Errors in base cases lead to incorrect solutions or index out of bounds errors.

4. **Recurrence Relation**: Focus on deriving the recurrence relation. This is the core of any DP solution and typically carries the highest weight in mark allocation.

5. **Space Optimization**: For questions asking for optimal space complexity, remember that many 2D DP problems can be reduced to 1D arrays. Understand when this optimization is valid.

6. **Choice of Approach**: Know when to use memoization (top-down) versus tabulation (bottom-up). Memoization is often easier to implement from a recursive solution, while tabulation provides better performance.

7. **Time-Space Tradeoff**: Be prepared to discuss the time and space complexity of your DP solution. This is a common examination question component.

8. **Practice Standard Problems**: Master classic DP problems including Fibonacci, Knapsack, LCS, Edit Distance, Longest Increasing Subsequence, and Matrix Chain Multiplication, as these frequently appear in examinations.