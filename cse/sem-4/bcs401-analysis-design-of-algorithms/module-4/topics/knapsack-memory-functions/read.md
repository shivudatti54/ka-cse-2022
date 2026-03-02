# The Knapsack Problem and Memory Functions

## Table of Contents

- [The Knapsack Problem and Memory Functions](#the-knapsack-problem-and-memory-functions)
- [Introduction](#introduction)
- [1. Mathematical Formulation of the 0/1 Knapsack Problem](#1-mathematical-formulation-of-the-01-knapsack-problem)
  - [Problem Definition](#problem-definition)
  - [Mathematical Formulation](#mathematical-formulation)
- [2. Proof of Optimal Substructure and Derivation of Recurrence](#2-proof-of-optimal-substructure-and-derivation-of-recurrence)
  - [Theorem: Optimal Substructure Property](#theorem-optimal-substructure-property)
  - [Derivation of the Recurrence Relation](#derivation-of-the-recurrence-relation)
- [3. Dynamic Programming Algorithm](#3-dynamic-programming-algorithm)
  - [Standard Bottom-Up Approach](#standard-bottom-up-approach)
  - [Space-Optimized Implementation](#space-optimized-implementation)
- [4. The Fractional Knapsack Problem](#4-the-fractional-knapsack-problem)
  - [Problem Distinction](#problem-distinction)
  - [Greedy Algorithm](#greedy-algorithm)
- [5. Memory Functions: Top-Down Dynamic Programming](#5-memory-functions-top-down-dynamic-programming)
  - [Concept and Motivation](#concept-and-motivation)
  - [Why Memory Functions?](#why-memory-functions)
  - [Implementation](#implementation)
  - [Comparison: Memory Functions vs. Bottom-Up DP](#comparison-memory-functions-vs-bottom-up-dp)
  - [When Memory Functions Outperform Bottom-Up](#when-memory-functions-outperform-bottom-up)
- [6. Worked Numerical Examples](#6-worked-numerical-examples)
  - [Example 1: Standard DP Table Construction](#example-1-standard-dp-table-construction)
  - [Example 2: Memory Function Trace](#example-2-memory-function-trace)
  - [Edge Case Analysis](#edge-case-analysis)
- [7. Assessment Questions](#7-assessment-questions)
  - [Multiple Choice Questions](#multiple-choice-questions)
  - [Flashcard](#flashcard)

## Introduction

The Knapsack Problem stands as one of the most quintessential combinatorial optimization problems in computer science and operations research. First formulated mathematically in the early 20th century, it has since become a cornerstone problem for understanding dynamic programming, greedy algorithms, and the theory of NP-completeness. The problem derives its name from the practical scenario of a thief who must select items to steal, constrained by the limited capacity of a knapsack.

The significance of the Knapsack Problem extends far beyond its anecdotal origin. It serves as a fundamental model for resource allocation scenarios including capital budgeting, cargo loading, inventory management, and portfolio optimization. In computer science, it provides an excellent pedagogical vehicle for understanding algorithmic paradigms including dynamic programming, greedy choice, and memoization. The problem's NP-hard nature for the general case makes it particularly interesting from a computational complexity perspective, as it admits efficient pseudo-polynomial solutions through dynamic programming.

This study material examines three interconnected solution approaches: the dynamic programming solution to the 0/1 Knapsack Problem, the greedy algorithm for the Fractional Knapsack Problem, and the memory function technique (top-down dynamic programming with memoization) that provides an alternative implementation strategy.

## 1. Mathematical Formulation of the 0/1 Knapsack Problem

### Problem Definition

Given a set of n items, where each item i (1 ≤ i ≤ n) has:

- A weight w[i] (positive integer)
- A value v[i] (positive integer)

And given a knapsack with capacity W (positive integer), the objective is to select a subset of items such that:

- The total weight of selected items does not exceed W
- The total value of selected items is maximized

Each item can be selected at most once (binary decision), hence the name "0/1" — we either take the entire item (1) or leave it completely (0).

### Mathematical Formulation

The problem is formally expressed as:

**Maximize:** Z = Σ\_{i=1}^{n} v[i] · x[i]

**Subject to:** Σ\_{i=1}^{n} w[i] · x[i] ≤ W

**Where:** x[i] ∈ {0, 1} for all i = 1, 2, ..., n

The binary constraint x[i] ∈ {0, 1} distinguishes the 0/1 Knapsack Problem from its fractional variant and fundamentally changes the problem's computational complexity.

## 2. Proof of Optimal Substructure and Derivation of Recurrence

### Theorem: Optimal Substructure Property

The 0/1 Knapsack Problem exhibits optimal substructure, meaning that an optimal solution to the problem contains within it optimal solutions to subproblems.

**Proof by Construction:**

Consider an optimal solution S for the original problem with n items and capacity W. Let item n (arbitrarily ordered) be either included or excluded in S:

**Case 1: Item n ∉ S (item not selected)**

- Then S is also an optimal solution to the subproblem containing only items 1 to n-1 with the same capacity W
- If there existed a better solution S' for this subproblem, replacing S with S'∪{ } would yield a better solution for the original problem — contradiction

**Case 2: Item n ∈ S (item selected)**

- Let w[n] be the weight of item n and v[n] be its value
- Then S \ {n} is an optimal solution to the subproblem with items 1 to n-1 and capacity W - w[n]
- If there existed a better solution S' for this subproblem with higher value, then S'∪{n} would yield a higher value for the original problem — contradiction

Thus, any optimal solution contains optimal solutions to subproblems, establishing optimal substructure. ∎

### Derivation of the Recurrence Relation

Let dp[i][w] denote the maximum value obtainable using the first i items (items 1 through i) with a knapsack capacity w.

For each state (i, w), we have two choices:

1. **Exclude item i:** If we do not include item i, the value remains dp[i-1][w]

2. **Include item i:** If w[i] ≤ w (item fits), we can include it, gaining v[i] plus the optimal value from the remaining capacity: dp[i-1]w - w[i]] + v[i]

Taking the maximum of these choices:

```
dp[i][w] = dp[i-1][w] if w[i] > w
dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + v[i]) if w[i] ≤ w
```

This recurrence is the foundation of the dynamic programming solution.

## 3. Dynamic Programming Algorithm

### Standard Bottom-Up Approach

The algorithm constructs a table of size (n+1) × (W+1) where dp[i][w] represents the optimal value for the first i items with capacity w.

**Algorithm:**

```
function KNAPSACK(n, W, w[1..n], v[1..n]):
 // Initialize dp table with zeros
 for w_cap from 0 to W:
 dp[0][w_cap] = 0

 // Fill table row by row
 for i from 1 to n:
 dp[i][0] = 0
 for w_cap from 0 to W:
 if w[i] > w_cap:
 // Cannot include item i
 dp[i][w_cap] = dp[i-1][w_cap]
 else:
 // Can either include or exclude
 dp[i][w_cap] = max(dp[i-1][w_cap],
 dp[i-1][w_cap - w[i]] + v[i])

 return dp[n][W]
```

**Complexity Analysis:**

- **Time Complexity:** O(n × W) — we compute each of the (n+1)(W+1) table entries once, with O(1) work per entry
- **Space Complexity:** O(n × W) — storing the complete DP table

The algorithm is pseudo-polynomial because the complexity depends on the numeric value of W, not its binary representation length.

### Space-Optimized Implementation

We can reduce space complexity to O(W) by recognizing that row i only depends on row i-1.

**Algorithm:**

```
function KNAPSACK_OPTIMIZED(n, W, w[1..n], v[1..n]):
 dp[0..W] = 0

 for i from 1 to n:
 // Iterate backwards to prevent using item i more than once
 for w_cap from W down to w[i]:
 dp[w_cap] = max(dp[w_cap],
 dp[w_cap - w[i]] + v[i])

 return dp[W]
```

**Critical Observation:** The backward iteration (W → w[i]) is essential. Forward iteration would allow the same item to be counted multiple times because dp[w_cap - w[i]] would already include the current item's contribution.

## 4. The Fractional Knapsack Problem

### Problem Distinction

Unlike the 0/1 variant, the Fractional Knapsack Problem permits taking arbitrary fractions of items. This seemingly minor relaxation fundamentally changes the problem's nature — it becomes solvable by a greedy algorithm and attains polynomial time complexity.

### Greedy Algorithm

The optimal strategy selects items based on their value-to-weight ratio (benefit per unit weight), always taking the highest-ratio remaining item first.

**Algorithm:**

```
function FRACTIONAL_KNAPSACK(n, W, w[1..n], v[1..n]):
 // Calculate value-to-weight ratios
 for i from 1 to n:
 ratio[i] = v[i] / w[i]

 // Sort items by ratio in descending order
 sort items by ratio descending

 total_value = 0
 remaining_capacity = W

 for i in sorted_order:
 if w[i] ≤ remaining_capacity:
 // Take entire item
 total_value += v[i]
 remaining_capacity -= w[i]
 else:
 // Take fraction
 fraction = remaining_capacity / w[i]
 total_value += v[i] * fraction
 remaining_capacity = 0
 break

 return total_value
```

**Proof of Greedy Optimality:**

The greedy algorithm is optimal for the fractional knapsack due to the matroid structure of the problem. Suppose an optimal solution O differs from the greedy solution G. Let item k be the first item where they differ. Since greedy selects items in descending ratio order, ratio[k] ≥ ratio of any item in O not selected by greedy. By exchanging items appropriately, we can transform O into G without decreasing total value, proving G is optimal.

**Time Complexity:** O(n log n) dominated by the sorting step

## 5. Memory Functions: Top-Down Dynamic Programming

### Concept and Motivation

The memory function approach (also called memoization or top-down dynamic programming) provides an alternative to the bottom-up tabular method. Instead of computing all subproblems systematically, it solves only those subproblems that are actually needed during recursion, storing results for future reference.

### Why Memory Functions?

The standard bottom-up DP computes all n×W states, even though many may be unnecessary for a specific instance. When:

- The capacity W is large but specific inputs require exploration of only a small subset
- The solution path is shallow (few items actually considered)

The memory function can be more efficient by avoiding computation of irrelevant subproblems.

### Implementation

```
function MEMORY_KNAPSACK(n, W, w[1..n], v[1..n]):
 // Initialize memoization table with -1 (indicating uncomputed)
 for i from 0 to n:
 for j from 0 to W:
 memo[i][j] = -1

 return MF(i = n, w = W)

function MF(i, w):
 // Base case: no items or no capacity
 if i == 0 or w == 0:
 return 0

 // Check if already computed
 if memo[i][w] != -1:
 return memo[i][w]

 // Compute the value
 if w[i] > w:
 memo[i][w] = MF(i-1, w)
 else:
 memo[i][w] = max(MF(i-1, w),
 MF(i-1, w - w[i]) + v[i])

 return memo[i][w]
```

### Comparison: Memory Functions vs. Bottom-Up DP

| Aspect               | Bottom-Up DP              | Memory Functions                       |
| -------------------- | ------------------------- | -------------------------------------- |
| **Approach**         | Tabulation                | Memoization                            |
| **Order**            | Systematic (iterative)    | Recursive (lazy evaluation)            |
| **Subproblems**      | All computed              | Only as needed                         |
| **Time Complexity**  | O(nW) worst case          | O(nW) worst case; better when sparse   |
| **Space Complexity** | O(nW) or O(W)             | O(nW) for memo table + recursion stack |
| **Overhead**         | No function call overhead | Recursive call overhead                |
| **Debugging**        | Harder to trace           | More intuitive recursion               |
| **When Preferred**   | All subproblems needed    | Sparse subproblem exploration          |

### When Memory Functions Outperform Bottom-Up

Memory functions excel in scenarios where:

1. The search space is not a complete grid (some states unreachable)
2. The solution path doesn't require all table entries
3. The recursive structure maps naturally to the problem
4. Early termination is possible

**Theorem:** In the worst case, both approaches have identical time complexity O(nW). However, the average case for random instances often favors memory functions due to reduced constant factors from avoiding unnecessary computation.

## 6. Worked Numerical Examples

### Example 1: Standard DP Table Construction

**Problem:** Given n=4 items with weights [2, 3, 4, 5] and values [3, 4, 5, 6], and knapsack capacity W=5, find the maximum value.

**Solution:**

Step 1: Initialize dp[0][w] = 0 for all w

Step 2: Process each item:

**Item 1 (w=2, v=3):**

- w=0,1: w[1] > w → dp[1][w] = 0
- w=2,3,4,5: dp[1][w] = max(dp[0][w], dp[0][w-2]+3) = 3

**Item 2 (w=3, v=4):**

- w=0,1,2: w[2] > w → dp[2][w] = dp[1][w]
- w=3: max(dp[1][3]=3, dp[1][0]+4=4) = 4
- w=4: max(dp[1][4]=3, dp[1][1]+4=4) = 4
- w=5: max(dp[1][5]=3, dp[1][2]+4=4) = 4

**Item 3 (w=4, v=5):**

- w=0,1,2,3: dp[3][w] = dp[2][w]
- w=4: max(dp[2][4]=4, dp[2][0]+5=5) = 5
- w=5: max(dp[2][5]=4, dp[2][1]+5=5) = 5

**Item 4 (w=5, v=6):**

- w=0,1,2,3,4: dp[4][w] = dp[3][w]
- w=5: max(dp[3][5]=5, dp[3][0]+6=6) = 6

**Result:** dp[4][5] = 6 (select item 4 only)

### Example 2: Memory Function Trace

Using the same problem, trace MEMORY_KNAPSACK(4, 5):

The function first checks memo[4][5] = -1, computes recursively:

- MF(4,5) calls MF(3,5) and MF(3,0)+6
- MF(3,5) calls MF(2,5) and MF(2,1)+5
- MF(2,5) calls MF(1,5) and MF(1,2)+4
- MF(1,5) computes 3, stores in memo[1][5]

Rather than computing all 20 table entries like bottom-up, the memory function computes only those states actually reached during recursion, in this case 12 states.

### Edge Case Analysis

**Case 1: All items too heavy**

- If w[i] > W for all i, dp[n][W] = 0
- Algorithm correctly returns 0

**Case 2: Single item fitting exactly**

- If one item has w[i] = W, it will be selected if v[i] > 0
- Correct due to recurrence: dp[i][W] = max(dp[i-1][W], dp[i-1][0]+v[i]) = v[i]

**Case 3: Zero capacity**

- dp[i][0] = 0 for all i (base case initialization)

**Case 4: All items with zero weight**

- If w[i] = 0 and v[i] > 0, algorithm can include infinite value
- This is the pseudo-polynomial limitation — requires integer weights

## 7. Assessment Questions

### Multiple Choice Questions

**Question 1 (Hard - Analytical):**
Consider a 0/1 Knapsack with n=5 items, weights [1, 2, 3, 4, 5], values [10, 15, 40, 30, 60], and capacity W=7. What is the maximum value achievable?

A) 65
B) 70
C) 75
D) 80

**Answer: C (75)** — Items 1(w=1,v=10), 3(w=3,v=40), 5(w=5,v=60) exceed capacity. Optimal: Items 3(w=3,v=40) + 2(w=2,v=15) + 1(w=1,v=10) = 65; or Items 5(w=5,v=60) + 1(w=1,v=10) = 70; or Items 3(w=3,v=40) + 4(w=4,v=30) = 70; Best is Items 3(w=3,v=40) + 4(w=4,v=30) + 1(w=1,v=10) exceeds 7. Actual optimal: Items 3(v=40) + 5(v=60) but weights 3+5=8>7. Items 2(v=15)+3(v=40)+4(v=30) weights 2+3+4=9>7. Items 1+2+3 = 1+2+3=6, values 10+15+40=65. Items 3+4=7, values 40+30=70. Items 2+5=7, values 15+60=75. Items 1+3+4=8>7. Items 1+2+5=8>7. Answer: 75.

**Question 2 (Hard - Proof-based):**
In the space-optimized knapsack, if we iterate w from w[i] to W (forward) instead of W to w[i] (backward), what happens?

A) Same result but slower
B) Incorrect result due to using item multiple times
C) Stack overflow error
D) Time complexity reduces

**Answer: B** — Forward iteration allows the current item to be reused because dp[w-w[i]] already includes the current item's contribution, violating the 0/1 constraint.

**Question 3 (Hard - Complexity Analysis):**
For the memory function approach, what is the minimum number of distinct subproblems that must be computed for any instance with n items and capacity W?

A) n + W
B) min(n, W)
C) nW/2
D) Cannot be determined

**Answer: D** — The number depends on the specific weights and values; some instances may compute more or fewer subproblems than others.

### Flashcard

**Front:** What is the key distinction between memory functions and bottom-up dynamic programming in terms of computation strategy?

**Back:** Memory functions use lazy evaluation (memoization) — computing subproblems only when needed during recursion. Bottom-up DP uses eager evaluation (tabulation) — systematically computing all subproblems regardless of necessity. This gives memory functions advantage when solution space is sparse, while bottom-up avoids recursion overhead.
