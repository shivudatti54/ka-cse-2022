# Knapsack Problem

## Table of Contents

- [Knapsack Problem](#knapsack-problem)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Problem Formulation](#problem-formulation)
  - [Exhaustive Search Approach (Brute Force)](#exhaustive-search-approach-brute-force)
  - [Optimal Substructure Property](#optimal-substructure-property)
  - [Dynamic Programming Solution](#dynamic-programming-solution)
  - [Fractional Knapsack Problem](#fractional-knapsack-problem)
  - [NP-Hardness](#np-hardness)
- [Examples](#examples)
  - [Example 1: Exhaustive Search Execution](#example-1-exhaustive-search-execution)
  - [Example 2: Dynamic Programming Table Construction](#example-2-dynamic-programming-table-construction)
  - [Example 3: Fractional Knapsack Greedy Solution](#example-3-fractional-knapsack-greedy-solution)
- [Exam Tips](#exam-tips)

## Introduction

The Knapsack Problem is a fundamental combinatorial optimization problem that serves as a cornerstone in the study of algorithm design and computational complexity. Given a set of items, each with a weight and a value, the objective is to determine the most valuable combination of items that can be fit into a knapsack with a given weight capacity. This problem exemplifies the class of NP-hard problems for which no polynomial-time algorithm is known, making it a perfect candidate for studying both brute-force approaches and more sophisticated optimization techniques.

The problem derives its name from the practical scenario of a thief who must select items to steal, where each item has a specific value and weight. The thief's knapsack has a maximum weight capacity, and the goal is to maximize the total value of stolen items without exceeding this capacity. This problem appears prominently in resource allocation, budget management, project selection, and cargo loading applications.

Within the context of "Brute Force Approaches" and "Exhaustive Search," the Knapsack Problem serves as an ideal pedagogical example. The module expects coverage of the exhaustive search paradigm, where all possible combinations are examined to find the optimal solution. This brute-force approach, while theoretically important, has exponential time complexity and motivates the development of more efficient algorithms.

## Key Concepts

### Problem Formulation

Let us formally define the 0/1 Knapsack Problem. We are given:

- A set of n items, indexed from 1 to n
- For each item i, a weight w[i] and a value v[i]
- A knapsack with capacity W

We must select a subset S ⊆ {1, 2, ..., n} such that:

- Σ(i∈S) w[i] ≤ W (weight constraint)
- Σ(i∈S) v[i] is maximized (objective function)

Each item can either be included1 () or excluded (0) from the knapsack, hence the name "0/1 Knapsack."

### Exhaustive Search Approach (Brute Force)

The brute-force approach systematically enumerates all 2^n possible subsets of items and computes the total weight and value for each subset. For each valid subset (one whose total weight does not exceed W), we track the maximum value achieved.

```
BRUTE-FORCE-KNAPSACK(n, W, w[1...n], v[1...n]):
 maxValue = 0
 bestSet = ∅

 for subset from 0 to 2^n - 1:
 totalWeight = 0
 totalValue = 0
 currentSet = ∅

 for i from 1 to n:
 if subset's i-th bit is 1:
 totalWeight = totalWeight + w[i]
 totalValue = totalValue + v[i]
 currentSet = currentSet ∪ {i}

 if totalWeight ≤ W and totalValue > maxValue:
 maxValue = totalValue
 bestSet = currentSet

 return maxValue, bestSet
```

**Time Complexity Analysis**: The outer loop iterates through 2^n subsets, and for each subset, we examine all n items in the inner loop. This results in O(n × 2^n) time complexity. The space complexity is O(n) for storing the current subset and results.

**Proof of Correctness for Exhaustive Search**: We prove that the exhaustive search algorithm always returns an optimal solution. Let O be the optimal subset of items. Since the algorithm enumerates all 2^n possible subsets, O is certainly examined during the execution. When O is examined, its total weight is computed and found to be ≤ W, and its total value is compared against maxValue. Since maxValue is initialized to 0 and updated only when a strictly greater value is found, after processing all subsets, maxValue equals the maximum value among all feasible subsets, which is precisely the value of O. Therefore, the algorithm returns an optimal solution.

### Optimal Substructure Property

The 0/1 Knapsack Problem exhibits optimal substructure, a crucial property that enables dynamic programming solutions. We prove this property formally.

**Theorem (Optimal Substructure)**: For the 0/1 Knapsack Problem, let an optimal solution include item i. Then the remaining items (excluding i) must form an optimal solution to the subproblem with capacity W - w[i].

_Proof_: We prove by contradiction. Suppose the optimal solution includes item i, and the remaining items do not form an optimal solution to the subproblem. Then there exists a better solution S' to the subproblem with total value greater than that of the remaining items in the optimal solution. Adding item i to S' yields a feasible solution with total value greater than the original optimal solution—a contradiction. ∎

This optimal substructure property suggests that we can build optimal solutions from optimal solutions to subproblems, which is the foundation of the dynamic programming approach.

### Dynamic Programming Solution

Although the module focuses on brute-force approaches, understanding the DP solution provides essential context. The DP solution improves upon exhaustive search by avoiding recomputation of overlapping subproblems.

We define dp[i][w] as the maximum value achievable using the first i items with a knapsack capacity of w. The recurrence relation is:

```
dp[i][w] = dp[i-1][w] if w[i] > w
dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + v[i]) otherwise
```

The first case handles the situation where item i cannot be included due to weight constraints. The second case chooses the better option between excluding item i and including it.

**Proof of Correctness for DP Recurrence**: We prove by induction on i that dp[i][w] correctly computes the maximum value for the first i items.

_Base Case_: For i = 0 (no items), dp[0][w] = 0 for all w, which is clearly optimal.

_Inductive Hypothesis_: Assume dp[i-1][w] correctly represents the optimal value for the first i-1 items at capacity w.

_Inductive Step_: Consider item i. If w[i] > w, item i cannot be included, so dp[i][w] = dp[i-1][w] is optimal. If w[i] ≤ w, we have two choices: either exclude item i (value dp[i-1][w]) or include it (value v[i] + dp[i-1]w-w[i]]). Since the optimal solution must choose the better of these two options, dp[i][w] = max(dp[i-1][w], dp[i-1]w-w[i]] + v[i]) is correct.

Thus, by induction, the recurrence correctly computes optimal values. The time complexity is O(nW) and space complexity is O(nW), though space can be optimized to O(W).

### Fractional Knapsack Problem

In the Fractional Knapsack Problem, we can take fractions of items rather than making binary choices. This variant admits a greedy solution that is provably optimal.

**Greedy Algorithm**: Sort items by their value-to-weight ratio in descending order. Then, iterate through sorted items, taking each item completely if it fits, or taking a fractional part if only partial capacity remains.

The greedy choice property holds: always taking the highest value-to-weight ratio item first never leads to a suboptimal solution. This can be proven using an exchange argument.

**Proof of Greedy Choice Property**: Let items be sorted by decreasing v[i]/w[i]. Consider any optimal solution O. If the first item in O is not the highest ratio item, we can exchange it with the highest ratio item without violating feasibility (since we take at most as much weight) and without decreasing total value. Repeating this argument shows an optimal solution exists that follows the greedy order.

### NP-Hardness

The 0/1 Knapsack Problem is NP-hard, meaning there is no known polynomial-time algorithm to solve all instances unless P = NP. This complexity classification is fundamental to understanding why exhaustive search (O(2^n)) is the theoretical baseline and why we seek approximation schemes or pseudo-polynomial time algorithms (like dynamic programming with polynomial dependence on W).

## Examples

### Example 1: Exhaustive Search Execution

Consider n = 4 items with weights [2, 3, 4, 5], values [3, 4, 5, 8], and knapsack capacity W = 7.

Enumerating all subsets:

- {}: weight=0, value=0
- {1}: weight=2, value=3
- {2}: weight=3, value=4
- {3}: weight=4, value=5
- {4}: weight=5, value=8
- {1,2}: weight=5, value=7
- {1,3}: weight=6, value=8
- {1,4}: weight=7, value=11 ← Best so far
- {2,3}: weight=7, value=9
- {2,4}: weight=8 > 7 (infeasible)
- {3,4}: weight=9 > 7 (infeasible)
- {1,2,3}: weight=9 > 7 (infeasible)
- {1,2,4}: weight=10 > 7 (infeasible)
- {1,3,4}: weight=11 > 7 (infeasible)
- {2,3,4}: weight=12 > 7 (infeasible)
- {1,2,3,4}: weight=14 > 7 (infeasible)

The optimal solution is {item1, item4} with total weight 7 and total value 11.

### Example 2: Dynamic Programming Table Construction

Using the same instance, construct the dp table:

Initialize dp[0][w] = 0 for all w.

For i = 1 (item1: weight=2, value=3):

- dp[1][0..7]: [0, 0, 3, 3, 3, 3, 3, 3]

For i = 2 (item2: weight=3, value=4):

- dp[2]: [0, 0, 3, 4, 4, 7, 7, 7]

For i = 3 (item3: weight=4, value=5):

- dp[3]: [0, 0, 3, 4, 5, 7, 8, 9]

For i = 4 (item4: weight=5, value=8):

- dp[4]: [0, 0, 3, 4, 5, 8, 8, 11]

The final answer dp[4][7] = 11, confirming our exhaustive search result.

### Example 3: Fractional Knapsack Greedy Solution

Same items, but fractional allowed: weights [2, 3, 4, 5], values [3, 4, 5, 8], W = 7.

Ratios: item1=1.5, item2≈1.33, item3=1.25, item4=1.6

Sorted: item4 (1.6), item1 (1.5), item2 (1.33), item3 (1.25)

- Take item4 completely: weight=5, value=8, remaining capacity=2
- Take item1 fractionally: weight=2, value=3, capacity=0

Total value = 8 + 3 = 11. This equals the 0/1 optimal in this case, though this is not always true.

## Exam Tips

1. **Understand the exhaustive search complexity**: Remember that brute-force enumeration has O(n × 2^n) complexity and recognize when this approach becomes impractical.

2. **Prove optimal substructure**: Be able to formally prove the optimal substructure property for the 0/1 Knapsack Problem, as this is frequently tested in examinations.

3. **Master the DP recurrence**: The recurrence relation dp[i][w] = max(dp[i-1][w], dp[i-1]w-w[i]] + v[i]) must be memorized and understood thoroughly.

4. **Distinguish between variants**: Clearly understand that 0/1 Knapsack requires DP (or exhaustive search) while Fractional Knapsack admits a greedy solution.

5. **NP-hardness implications**: Understand that the NP-hard nature of 0/1 Knapsack means exhaustive search is the theoretical baseline and polynomial-time solutions are unlikely.

6. **Space optimization**: Remember that the 2D DP table can be optimized to 1D by processing capacities in reverse order to avoid overwriting needed values.

7. **Pseudo-polynomial time**: Recognize that DP runs in O(nW) time, which is pseudo-polynomial (polynomial in the numeric value of W but exponential in the input size).
