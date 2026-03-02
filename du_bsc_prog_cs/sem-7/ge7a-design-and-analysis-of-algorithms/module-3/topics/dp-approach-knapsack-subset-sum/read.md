# Dynamic Programming Approach: Knapsack and Subset Sum Problems

## Introduction

Dynamic Programming (DP) is one of the most powerful algorithmic paradigms in computer science, serving as a cornerstone technique for solving optimization problems. In this topic, we explore two classic problems—**0/1 Knapsack** and **Subset Sum**—through the lens of dynamic programming. These problems appear frequently in real-world scenarios such as resource allocation, inventory management, financial portfolio optimization, and load balancing.

The 0/1 Knapsack problem derives its name from a scenario where a thief must choose items to steal, with each item having a weight and value, but can only take each item at most once (hence "0/1" - either take it or don't). The Subset Sum problem asks whether a subset of given numbers can sum to a target value, with applications in cryptography, currency systems, and decision-making scenarios.

Understanding these problems through dynamic programming not only helps solve them efficiently but also develops your ability to recognize optimal substructure and overlapping subproblems—the two key properties that make DP applicable. For University of Delhi's Computer Science program, these problems form a significant portion of algorithmic analysis questions in end-semester examinations.

## Key Concepts

### 1. Properties of Dynamic Programming

Before diving into specific problems, it's essential to understand why DP works:

- **Optimal Substructure**: An optimal solution can be constructed from optimal solutions of its subproblems. This means if we know the best solution for smaller instances, we can build up to the solution for larger instances.

- **Overlapping Subproblems**: The same subproblems are solved multiple times. Instead of recomputing, we store results in a table (memoization or tabulation) to avoid redundant computation.

### 2. 0/1 Knapsack Problem

**Problem Statement**: Given n items with weights w₁, w₂, ..., wₙ and values v₁, v₂, ..., vₙ, and a knapsack with capacity W, find the maximum value that can be obtained by selecting a subset of items such that total weight does not exceed W. Each item can be taken at most once.

**Why Greedy Fails**: A common misconception is that a greedy approach (taking items by value/weight ratio) works. However, greedy fails because the decision about an item depends on future choices. Consider: weights = [10, 20, 30], values = [60, 100, 120], W = 50. Greedy by ratio picks items with value/weight = 6 (item 1) but cannot add item 2 (weight 20) or item 3 (weight 30) alone. Optimal solution: items 2 + 3 = 220.

**DP Formulation**:

Let `dp[i][w]` represent the maximum value achievable using first i items with weight limit w.

**Recurrence Relation**:
```
dp[i][w] = dp[i-1][w]                           if w_i > w (cannot include item i)
dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)  if w_i ≤ w (either don't include or include item i)
```

**Base Case**: `dp[0][w] = 0` for all w (no items means zero value)
**Answer**: `dp[n][W]`

**Time Complexity**: O(n × W)
**Space Complexity**: O(n × W), can be optimized to O(W) using 1D array

### 3. Subset Sum Problem

**Problem Statement**: Given a set of n numbers and a target sum S, determine whether there exists a subset whose elements sum to exactly S.

**DP Formulation**:

Let `dp[i][s]` be true if a subset of the first i elements can sum to s.

**Recurrence Relation**:
```
dp[i][s] = dp[i-1][s]                              (don't include element i)
         OR dp[i-1][s-arr[i-1]]                   (include element i, if s ≥ arr[i-1])
```

**Base Cases**:
- `dp[0][0] = true` (empty set sums to 0)
- `dp[0][s] = false` for s > 0 (non-empty sum with no elements)

**Answer**: `dp[n][S]`

**Time Complexity**: O(n × S)
**Space Complexity**: O(n × S), can be optimized to O(S)

### 4. Space Optimization

For both problems, we can reduce space from O(n×W) to O(W) by using a 1D array processed in reverse order:

```python
# 0/1 Knapsack - Space Optimized
dp = [0] * (W + 1)
for i in range(n):
    for w in range(W, weights[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
```

The reverse iteration ensures we use values from the previous iteration (i-1) since we overwrite from right to left.

## Examples

### Example 1: 0/1 Knapsack

**Problem**: Given items with weights [2, 3, 4, 5] and values [3, 4, 5, 8], find maximum value with knapsack capacity 5.

**Solution**:

Let's build the DP table:

Initialize: dp[0][w] = 0 for all w

For item 1 (weight=2, value=3):
- w=0 to 1: dp[1][w] = dp[0][w] = 0
- w=2 to 5: dp[1][w] = max(dp[0][w], dp[0][w-2] + 3)
  - dp[1][2] = max(0, 0+3) = 3
  - dp[1][3] = max(0, 0+3) = 3
  - dp[1][4] = max(0, 0+3) = 3
  - dp[1][5] = max(0, 0+3) = 3

For item 2 (weight=3, value=4):
- w=0 to 2: dp[2][w] = dp[1][w]
  - dp[2][0]=0, dp[2][1]=0, dp[2][2]=3
- w=3: dp[2][3] = max(dp[1][3]=3, dp[1][0]+4=4) = 4
- w=4: dp[2][4] = max(dp[1][4]=3, dp[1][1]+4=4) = 4
- w=5: dp[2][5] = max(dp[1][5]=3, dp[1][2]+4=3+4=7) = 7

For item 3 (weight=4, value=5):
- w=0 to 3: carry forward previous values
- w=4: dp[3][4] = max(dp[2][4]=4, dp[2][0]+5=5) = 5
- w=5: dp[3][5] = max(dp[2][5]=7, dp[2][1]+5=5) = 7

For item 4 (weight=5, value=8):
- w=5: dp[4][5] = max(dp[3][5]=7, dp[3][0]+8=8) = 8

**Answer**: Maximum value = 8 (taking only item 4)

### Example 2: Subset Sum

**Problem**: Given set [3, 34, 4, 12, 5, 2] and target sum S = 9, determine if a subset sums to 9.

**Solution**:

Build dp table where dp[i][s] indicates if sum s is achievable using first i elements:

Elements considered: [] → [3] → [3,34] → [3,34,4] → ...

Initialize row 0: dp[0][0] = true, dp[0][s>0] = false

Row 1 (include 3):
- dp[1][0] = true (don't include 3)
- dp[1][3] = true (include 3: dp[0][0] + 3 = 3)
- dp[1][other] = false

Row 2 (include 34): No new sums possible (34 > 9)

Row 3 (include 4):
- dp[3][4] = true (include 4)
- dp[3][7] = true (3+4)
- dp[3][3] = true (from before)
- dp[3][0] = true

Row 4 (include 12): No new sums (12 > 9)

Row 5 (include 5):
- dp[5][5] = true
- dp[5][8] = true (3+5)
- dp[5][9] = true (4+5)
- dp[5][7] = true (from 3+4)

Row 6 (include 2):
- dp[6][2] = true
- dp[6][5] = true (from 3+2 or 5 alone)
- dp[6][6] = true (4+2)
- dp[6][7] = true (from before)
- dp[6][8] = true (from 3+5)
- **dp[6][9] = true** (4+5 or 3+4+2)

**Answer**: Yes, subset exists. One solution: {4, 5} or {3, 4, 2}

### Example 3: Space-Optimized Knapsack

**Problem**: Same as Example 1, using space optimization.

**Solution**:

```
weights = [2, 3, 4, 5]
values = [3, 4, 5, 8]
W = 5
```

Initialize: dp = [0, 0, 0, 0, 0, 0]

Item 1 (w=2, v=3): iterate w from 5 to 2
- dp[5] = max(0, dp[3]+3) = max(0, 0+3) = 3
- dp[4] = max(0, dp[2]+3) = max(0, 0+3) = 3
- dp[3] = max(0, dp[1]+3) = max(0, 0+3) = 3
- dp[2] = max(0, dp[0]+3) = max(0, 0+3) = 3

dp = [0, 0, 3, 3, 3, 3]

Item 2 (w=3, v=4): iterate w from 5 to 3
- dp[5] = max(3, dp[2]+4) = max(3, 3+4=7) = 7
- dp[4] = max(3, dp[1]+4) = max(3, 0+4=4) = 4
- dp[3] = max(3, dp[0]+4) = max(3, 0+4=4) = 4

dp = [0, 0, 3, 4, 4, 7]

Item 3 (w=4, v=5): iterate w from 5 to 4
- dp[5] = max(7, dp[1]+5) = max(7, 0+5=5) = 7
- dp[4] = max(4, dp[0]+5) = max(4, 0+5=5) = 5

dp = [0, 0, 3, 4, 5, 7]

Item 4 (w=5, v=8): iterate w from 5 to 5
- dp[5] = max(7, dp[0]+8) = max(7, 0+8=8) = 8

dp = [0, 0, 3, 4, 5, 8]

**Answer**: Maximum value = 8

## Exam Tips

1. **Understand the recurrence relation**: For 0/1 Knapsack, remember the max() function—either exclude or include the current item. For Subset Sum, remember the OR operation—either we can form the sum without or with the current element.

2. **Table construction matters**: When solving manually in exams, clearly define what rows and columns represent. Typically, rows represent items and columns represent weight/sum capacity.

3. **Base cases are crucial**: Always state and use base cases correctly. For Knapsack, dp[0][w] = 0. For Subset Sum, dp[0][0] = true and dp[0][s>0] = false.

4. **Space optimization technique**: Remember to iterate in reverse order when using 1D array optimization to avoid using the same item twice.

5. **Difference between 0/1 and Fractional Knapsack**: Don't confuse them! 0/1 requires DP, while Fractional Knapsack can be solved greedily by value/weight ratio.

6. **Trace through small examples**: In exams, always trace through the algorithm with a small example to verify your recurrence and table construction.

7. **Time and Space analysis**: Know that both problems have O(n×W) time complexity, and understand when space can be optimized.

8. **Variations**: Be prepared for variations like "find the items selected" (backtracking through the table) or "minimum knapsack" (initializing with infinity instead of 0).