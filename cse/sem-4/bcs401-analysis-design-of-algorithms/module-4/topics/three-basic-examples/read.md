# Three Basic Examples in Dynamic Programming

## Table of Contents

- [Three Basic Examples in Dynamic Programming](#three-basic-examples-in-dynamic-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Overlapping Subproblems](#overlapping-subproblems)
  - [Optimal Substructure](#optimal-substructure)
  - [Top-Down Approach (Memoization)](#top-down-approach-memoization)
  - [Bottom-Up Approach (Tabulation)](#bottom-up-approach-tabulation)
  - [State Transition](#state-transition)
- [Example 1: Fibonacci Number Calculation](#example-1-fibonacci-number-calculation)
- [Example 2: Binomial Coefficient](#example-2-binomial-coefficient)
- [Example 3: Minimum Coin Change Problem](#example-3-minimum-coin-change-problem)
- [Comparison: Memoization vs Tabulation](#comparison-memoization-vs-tabulation)
- [Summary](#summary)

## Introduction

Dynamic Programming (DP) is an algorithmic paradigm that solves complex problems by breaking them into simpler subproblems, storing the results of these subproblems to avoid redundant computations. The concept was formally introduced by Richard Bellman in the 1950s and has since become a fundamental technique in algorithm design.

The foundation of dynamic programming rests on two key properties: **Optimal Substructure** (the optimal solution to a problem can be constructed from optimal solutions to its subproblems) and **Overlapping Subproblems** (the same subproblems are solved multiple times). When both these properties hold, dynamic programming can transform exponential-time algorithms into polynomial-time solutions.

This chapter introduces three fundamental examples that demonstrate the core concepts of dynamic programming: the Fibonacci sequence calculation, the Binomial Coefficient problem, and the Minimum Coin Change problem. These examples illustrate both the top-down (memoization) and bottom-up (tabulation) approaches to implementing dynamic programming solutions.

## Key Concepts

### Overlapping Subproblems

A problem exhibits overlapping subproblems when recursive solutions involve solving the same subproblem multiple times. Consider the recursive computation of Fibonacci numbers where F(5) requires F(4) and F(3), but F(3) is also required when computing F(4), leading to redundant calculations.

### Optimal Substructure

A problem has optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems. For instance, the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers, which are themselves optimal solutions to smaller subproblems.

### Top-Down Approach (Memoization)

The top-down approach starts with the original problem and recursively breaks it into subproblems. When a subproblem is solved, its result is stored in a table (memoized) to avoid recomputation. This approach directly follows the recursive structure but may have overhead from recursive calls.

### Bottom-Up Approach (Tabulation)

The bottom-up approach solves the smallest subproblems first and builds up to the original problem. This eliminates recursion overhead and typically results in better space utilization. The solution is stored in a table (tabulated) as we progress from smaller to larger subproblems.

### State Transition

The core of any DP solution is defining the state and the transition between states. The state represents what information we need to solve a particular subproblem, and the transition defines how to compute the solution for a state from previously computed states.

## Example 1: Fibonacci Number Calculation

The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n ≥ 2.

**Proof of Optimal Substructure**: The Fibonacci sequence exhibits optimal substructure because the nth Fibonacci number can be expressed as the sum of two smaller Fibonacci numbers. Specifically, F(n) = F(n-1) + F(n-2). This means the optimal solution to computing F(n) can be constructed from the optimal solutions of its subproblems F(n-1) and F(n-2).

**Proof of Overlapping Subproblems**: When computing F(n) recursively, the same subproblems are solved multiple times. For example, computing F(5) requires computing F(4) and F(3). Computing F(4) requires F(3) and F(2). Thus, F(3) is computed twice, F(2) is computed three times, demonstrating overlapping subproblems.

**Naive Recursive Approach (Exponential Time)**:

```
function fib(n):
 if n ≤ 1:
 return n
 return fib(n-1) + fib(n-2)
```

Time Complexity: O(2^n), Space Complexity: O(n) recursion stack depth.

**Top-Down DP with Memoization**:

```
function fibMemo(n, memo):
 if n ≤ 1:
 return n
 if memo[n] is not null:
 return memo[n]
 memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
 return memo[n]
```

Time Complexity: O(n), Space Complexity: O(n) for memo table + O(n) for recursion stack.

**Bottom-Up DP with Tabulation**:

```
function fibTab(n):
 if n ≤ 1:
 return n
 dp[0] = 0
 dp[1] = 1
 for i from 2 to n:
 dp[i] = dp[i-1] + dp[i-2]
 return dp[n]
```

Time Complexity: O(n), Space Complexity: O(n).

**Space-Optimized Bottom-Up**:

```
function fibOptimized(n):
 if n ≤ 1:
 return n
 prev2 = 0
 prev1 = 1
 for i from 2 to n:
 current = prev1 + prev2
 prev2 = prev1
 prev1 = current
 return prev1
```

Time Complexity: O(n), Space Complexity: O(1).

## Example 2: Binomial Coefficient

The Binomial Coefficient C(n, k) represents the number of ways to choose k elements from n elements, calculated as n!/(k!(n-k)!). It satisfies Pascal's Triangle identity: C(n, k) = C(n-1, k-1) + C(n-1, k).

**Proof of Optimal Substructure**: The optimal substructure property follows from Pascal's identity. To choose k elements from n, we can either include a specific element (and choose k-1 from n-1) or exclude it (and choose k from n-1). Thus, C(n,k) = C(n-1,k-1) + C(n-1,k), where the optimal solutions to the subproblems yield the optimal solution to the main problem.

**Proof of Overlapping Subproblems**: Computing C(n,k) recursively requires computing C(n-1,k-1) and C(n-1,k). These in turn share common subproblems, such as C(n-2,k-2), C(n-2,k-1), and C(n-2,k). The recursion tree exhibits significant overlap.

**Recursive Formula**:

- Base cases: C(n, 0) = 1, C(n, n) = 1, C(n, 1) = n
- Recursive case: C(n, k) = C(n-1, k-1) + C(n-1, k)

**Top-Down DP with Memoization**:

```
function binomMemo(n, k, memo):
 if k == 0 or k == n:
 return 1
 if k == 1:
 return n
 if memo[n][k] is not null:
 return memo[n][k]
 memo[n][k] = binomMemo(n-1, k-1, memo) + binomMemo(n-1, k, memo)
 return memo[n][k]
```

Time Complexity: O(n×k), Space Complexity: O(n×k) for memo table + O(n) recursion stack.

**Bottom-Up DP Implementation**:

```
function binomialCoeff(n, k):
 C = 2D array of size (n+1) × (k+1)

 // Base cases: C(i, 0) = 1 for all i
 for i from 0 to n:
 C[i][0] = 1

 // Fill the table using the recurrence relation
 for i from 1 to n:
 for j from 1 to min(i, k):
 if i == j:
 C[i][j] = 1
 else:
 C[i][j] = C[i-1][j-1] + C[i-1][j]

 return C[n][k]
```

Time Complexity: O(n×k), Space Complexity: O(n×k).

**Space-Optimized Version**:

```
function binomialCoeffOptimized(n, k):
 C = array of size (k+1)
 C[0] = 1

 for i from 1 to n:
 for j from min(i, k) down to 1:
 C[j] = C[j] + C[j-1]

 return C[k]
```

Time Complexity: O(n×k), Space Complexity: O(k).

## Example 3: Minimum Coin Change Problem

Given a set of coin denominations and a target amount, find the minimum number of coins needed to make up that amount. If impossible, return -1.

**Problem Definition**:

- Input: Array of coin denominations coins[], target amount N
- Output: Minimum number of coins to make amount N, or -1 if impossible

**Proof of Optimal Substructure**: Let dp[i] be the minimum number of coins needed to make amount i. For the optimal solution to make amount i, consider the last coin used. If the last coin has denomination c, then the remaining amount i-c must be solved optimally. Thus, dp[i] = min(dp[i-c] + 1) for all valid coins c, demonstrating optimal substructure.

**State Definition**: Let dp[i] represent the minimum number of coins needed to make amount i.

**State Transition**: dp[i] = min(dp[i - coin_j] + 1) for all coins where coin_j ≤ i, with dp[0] = 0.

**Base Cases**:

- dp[0] = 0 (zero coins needed for amount 0)
- dp[i] = ∞ for i > 0 initially (unreachable state)

**Top-Down DP with Memoization**:

```
function minCoinsMemo(amount, coins, memo):
 if amount == 0:
 return 0
 if amount < 0:
 return -1
 if memo[amount] is not null:
 return memo[amount]

 minCount = Infinity
 for coin in coins:
 result = minCoinsMemo(amount - coin, coins, memo)
 if result != -1:
 minCount = min(minCount, result + 1)

 memo[amount] = (minCount == Infinity) ? -1 : minCount
 return memo[amount]
```

Time Complexity: O(n×k) where n = amount, k = number of coins, Space Complexity: O(n).

**Bottom-Up DP Implementation**:

```
function minCoins(coins, amount):
 if amount == 0:
 return 0

 dp = array of size (amount + 1) initialized to Infinity
 dp[0] = 0

 for i from 1 to amount:
 for coin in coins:
 if coin <= i and dp[i - coin] != Infinity:
 dp[i] = min(dp[i], dp[i - coin] + 1)

 return (dp[amount] == Infinity) ? -1 : dp[amount]
```

Time Complexity: O(n×k), Space Complexity: O(n).

**Proof of Correctness**: We prove by induction that dp[i] after the algorithm completes equals the minimum number of coins needed to make amount i. Base case: dp[0] = 0 is correct. Inductive step: assume dp[j] is correct for all j < i. When computing dp[i], we consider all coins that could be the last coin. If coin c is the last coin, then we need dp[i-c] coins for the remaining amount. Taking the minimum over all valid coins gives the optimal solution. By induction, dp[i] is correct for all i.

## Comparison: Memoization vs Tabulation

| Aspect      | Memoization (Top-Down)                  | Tabulation (Bottom-Up)            |
| ----------- | --------------------------------------- | --------------------------------- |
| Approach    | Recursive, starts from main problem     | Iterative, starts from base cases |
| Order       | Natural problem decomposition           | Fixed order of computation        |
| Memory      | Only stores visited subproblems         | Stores all subproblems            |
| Speed       | May have recursion overhead             | Generally faster                  |
| When to Use | When few subproblems are needed         | When all subproblems are needed   |
| Space       | More space-efficient if few subproblems | O(n) space typically              |

## Summary

Dynamic Programming transforms exponential-time recursive solutions into polynomial-time solutions by exploiting optimal substructure and overlapping subproblems. The three examples demonstrated:

- **Fibonacci**: Simple 1D DP with O(n) time and O(1) space optimization
- **Binomial Coefficient**: 2D DP with O(n×k) complexity and space optimization to O(k)
- **Minimum Coin Change**: Unbounded knapsack variant with O(n×k) complexity

The key to solving DP problems lies in correctly identifying the state definition and deriving the state transition equation.
