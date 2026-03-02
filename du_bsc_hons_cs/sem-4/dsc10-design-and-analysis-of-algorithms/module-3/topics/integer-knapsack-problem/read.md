# Integer Knapsack Problem (0/1 Knapsack)

## Introduction

The Integer Knapsack Problem, also known as the 0/1 Knapsack Problem, is one of the most fundamental problems in computer science and operations research. It serves as a classic example of dynamic programming and appears extensively in combinatorial optimization, resource allocation, and decision-making scenarios.

In simple terms, imagine you are a thief breaking into a jewelry store. You have a knapsack (bag) that can carry a maximum weight W. There are n items, each with a specific weight and profit (value). You cannot take partial items or multiple copies of the same item—you either take an item completely or leave it. Your goal is to maximize the total profit while ensuring the total weight does not exceed W.

This problem has numerous real-world applications: capital budgeting where you must select projects within a budget constraint; cargo loading problems in transportation; resource allocation in project management; and even in cryptography where it forms the basis of certain encryption schemes. The 0/1 Knapsack Problem is NP-hard, meaning there is no known polynomial-time algorithm to solve it for arbitrary inputs. However, dynamic programming provides a pseudo-polynomial time solution that is efficient for practical purposes.

## Key Concepts

### Problem Formulation

Given:
- n items, each with weight w[i] and profit p[i]
- Maximum knapsack capacity W

Find a subset of items to maximize total profit such that:
- Sum of weights of selected items ≤ W
- Each item can be selected at most once (0 or 1 choice)

### Dynamic Programming Approach

The dynamic programming solution uses the following recurrence relation:

**Let dp[i][w] represent the maximum profit achievable using the first i items with a knapsack capacity of w.**

Recurrence:
```
dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + p[i]) if w[i] ≤ w
dp[i][w] = dp[i-1][w] if w[i] > w
```

**Base Case:** dp[0][w] = 0 for all w (no items means zero profit)

**Time Complexity:** O(n × W)
**Space Complexity:** O(n × W), can be optimized to O(W)

### Space Optimization

We can reduce space from O(n×W) to O(W) by using a 1D array:

```python
dp = [0] × (W + 1)
for i in range(n):
    for w in range(W, w[i]-1, -1):
        dp[w] = max(dp[w], dp[w-w[i]] + p[i])
```

**Important:** The inner loop must run backwards (from W to w[i]) to ensure each item is used at most once.

### Types of Knapsack Problems

1. **0/1 Knapsack (Integer):** Each item can be taken at most once
2. **Unbounded Knapsack:** Each item can be taken unlimited times
3. **Fractional Knapsack:** Items can be taken fractionally (solved greedily)

## Examples

### Example 1: Basic 0/1 Knapsack

**Problem:**
Weights: [2, 3, 4, 5]
Profits: [3, 4, 5, 6]
Knapsack Capacity: 5

**Solution:**

| Item | Weight | Profit |
|------|--------|--------|
| 1    | 2      | 3      |
| 2    | 3      | 4      |
| 3    | 4      | 5      |
| 4    | 5      | 6      |

Using dynamic programming:

Initialize dp[0...5] = 0

For item 1 (weight=2, profit=3):
- w=5: max(0, dp[3]+3) = max(0, 0+3) = 3
- w=4: max(0, dp[2]+3) = max(0, 0+3) = 3
- w=3: max(0, dp[1]+3) = max(0, 0+3) = 3
- w=2: max(0, dp[0]+3) = max(0, 0+3) = 3

For item 2 (weight=3, profit=4):
- w=5: max(3, dp[2]+4) = max(3, 0+4) = 4
- w=4: max(3, dp[1]+4) = max(3, 0+4) = 4
- w=3: max(3, dp[0]+4) = max(3, 0+4) = 4

For item 3 (weight=4, profit=5):
- w=5: max(4, dp[1]+5) = max(4, 0+5) = 5
- w=4: max(4, dp[0]+5) = max(4, 5) = 5

For item 4 (weight=5, profit=6):
- w=5: max(5, dp[0]+6) = max(5, 6) = 6

**Answer:** Maximum Profit = 6 (select item 4 alone)

### Example 2: Finding Selected Items

**Problem:**
n = 3, W = 6
Items: (w1=2, p1=10), (w2=2, p2=10), (w3=3, p3=12)

**Solution:**

Build DP table:

| i\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|-----|---|---|---|---|---|---|---|
| 0   | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1   | 0 | 0 | 10| 10| 10| 10| 10|
| 2   | 0 | 0 | 10| 10| 20| 20| 20|
| 3   | 0 | 0 | 10| 12| 20| 22| 22|

**Backtracking to find items:**
- dp[3][6] = 22 ≠ dp[2][6] = 20 → Item 3 selected
- Remaining capacity: 6 - 3 = 3
- Check dp[2][3] = 12 = dp[1][3] = 10 → Item 2 not selected (but wait, dp[2][3]=12 > dp[1][3]=10, so item 2 IS selected)
- Remaining capacity: 3 - 2 = 1
- dp[1][1] = 0 = dp[0][1] → Item 1 not selected

**Selected Items:** Item 2 and Item 3
**Total Weight:** 2 + 3 = 5 ≤ 6
**Total Profit:** 10 + 12 = 22

### Example 3: Unbounded Knapsack Comparison

**Problem:**
Weights: [1, 2, 3]
Profits: [10, 15, 40]
Capacity: 5

**(a) 0/1 Knapsack:**

DP Table:
| i\w | 0 | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|---|
| 0   | 0 | 0 | 0 | 0 | 0 | 0 |
| 1   | 0 | 10| 10| 10| 10| 10|
| 2   | 0 | 10| 15| 25| 25| 25|
| 3   | 0 | 10| 15| 40| 50| 50|

**Answer:** Maximum Profit = 50 (Items: 1 and 3)

**(b) Unbounded Knapsack (each item unlimited):**

DP:
- w=1: max(0, 0+10) = 10
- w=2: max(10, dp[1]+15) = max(10, 10+15) = 25
- w=3: max(25, dp[2]+40) = max(25, 25+40) = 65
- w=4: max(50, dp[3]+10) = max(50, 50+10) = 60
- w=5: max(60, dp[4]+15) = max(60, 50+15) = 65

**Answer:** Maximum Profit = 65 (Five items of weight 1: 5×10 = 50 OR Item 3 + Item 2: 40+15=55... wait, let me recalculate)

Actually for unbounded:
- w=1: 10 (item 1)
- w=2: max(10, 10+15) = 25 (item 1 + item 1 OR item 2)
- w=3: max(25, 10+40) = 50 (item 1 + item 2 OR item 3 alone=40)
- w=4: max(50, 25+10) = 60 (2×item1 + 1×item2 OR 2×item2)
- w=5: max(60, 50+10) = 65 (3×item1 + 1×item2)

**Answer:** Maximum Profit = 65

## Exam Tips

1. **Understand the difference between 0/1 and Unbounded:** The key distinction is that in 0/1, each item can be used once, so iterate backwards in space-optimized version. In Unbounded, iterate forwards.

2. **Remember the recurrence relation:** dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + p[i]) - this is crucial for both solving problems and explaining the approach.

3. **Space optimization technique:** For 0/1 knapsack, always iterate the capacity from W down to weight[i] to prevent using the same item multiple times.

4. **Handle base cases properly:** Initialize dp array with zeros. The first row and column should always be zero.

5. **Backtracking to find selected items:** After computing the DP table, trace back from dp[n][W] to determine which items were selected.

6. **Time complexity analysis:** Remember O(n×W) is pseudo-polynomial because W can be exponential in the input size (number of bits).

7. **Practice with small examples:** Draw complete DP tables for small inputs to understand the algorithm thoroughly—this helps in exams where you may need to show the table.

8. **Compare with Greedy for Fractional Knapsack:** Note that fractional knapsack can be solved greedily by taking items in decreasing order of value/weight ratio, but 0/1 cannot.

9. **Handle edge cases:** Consider cases where no item fits, or when items have zero weight/profit.

10. **Write clean pseudocode:** Be able to write both the 2D and space-optimized versions of the algorithm.