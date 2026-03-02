# Weighted Interval Scheduling

## Introduction

The Weighted Interval Scheduling Problem (WISP) is a fundamental optimization problem in computer science that extends the classic interval scheduling problem by associating a weight or profit with each interval. In real-world scenarios, not all tasks are equally valuable—some meetings generate more revenue, some bookings yield higher profits, and some projects deliver greater value. This problem captures such scenarios where we must select a subset of non-overlapping intervals to maximize the total weight.

The weighted interval scheduling problem appears extensively in resource allocation, scheduling, and planning applications. Consider a university timetable where different classes have varying enrollment numbers (weights), or a conference scheduling system where keynote sessions attract more attendees. A hospital might need to schedule surgeries of varying complexity and revenue potential in operating rooms. The problem also arises in investment planning, where different projects have different profit margins and cannot all be pursued simultaneously due to resource constraints.

This topic is crucial for the Design and Analysis of Algorithms course as it demonstrates how Dynamic Programming transforms an exponential-time exhaustive search into a polynomial-time solution. The problem showcases the power of preprocessing, the importance of optimal substructure, and the technique of memoization. Understanding this problem provides a foundation for solving numerous real-world optimization challenges.

## Key Concepts

### Problem Definition

Given n intervals, where each interval i has a start time s[i], finish time f[i], and a weight w[i], the goal is to select a subset of mutually non-overlapping intervals that maximizes the total weight. Two intervals are compatible if they do not overlap in time—typically, we consider intervals [s[i], f[i]) where the finish time of one equals the start time of another as non-overlapping.

The decision version asks whether there exists a feasible solution with total weight at least W, while the optimization version seeks the maximum possible total weight.

### Preprocessing: Sorting by Finish Time

The first critical step is to sort all intervals by their finish times in increasing order. This preprocessing creates a total order that enables efficient computation of compatibility. After sorting, we renumber the intervals from 1 to n, where f[1] ≤ f[2] ≤ ... ≤ f[n]. This indexing is essential for the dynamic programming recurrence.

### Finding Compatible Intervals: The p[j] Function

For each interval j (in the sorted order), we need to find p[j], the index of the last interval that finishes before interval j starts. Formally, p[j] = max{i < j : f[i] ≤ s[j]}, or p[j] = 0 if no such interval exists. This function helps us determine which intervals are compatible with interval j.

Computing p[j] efficiently can be done in O(n²) by brute force, or in O(n log n) using binary search on the sorted finish times. For binary search, we search for the rightmost interval with finish time ≤ s[j].

### Optimal Substructure

The problem exhibits optimal substructure, which is the key to the dynamic programming approach. Let OPT(j) represent the maximum total weight achievable using only intervals 1 through j. Then:

**OPT(j) = max(OPT(j-1), w[j] + OPT(p[j]))**

This recurrence considers two cases for the optimal solution involving intervals up to j:
1. Interval j is not selected: the optimal solution is the same as OPT(j-1)
2. Interval j is selected: we add its weight to the optimal solution for all intervals compatible with it, which is OPT(p[j])

### Dynamic Programming Solution

We compute an array dp[0...n] where dp[i] represents OPT(i), the maximum weight using intervals 1 through i. We initialize dp[0] = 0 (no intervals yields zero weight). For each i from 1 to n, we apply the recurrence:

```
dp[i] = max(dp[i-1], weight[i] + dp[p[i]])
```

After filling the dp array, dp[n] contains the maximum total weight. To recover the actual solution (which intervals were selected), we perform traceback starting from i = n, checking whether dp[i] came from dp[i-1] or from weight[i] + dp[p[i]].

### Time and Space Complexity

The algorithm runs in O(n log n) time when using binary search for computing p[j], as sorting takes O(n log n), computing all p[j] takes O(n log n), and the DP loop takes O(n). Space complexity is O(n) for storing the intervals, p array, and dp array.

## Examples

### Example 1: Basic Weighted Interval Scheduling

Consider the following intervals (already sorted by finish time):

| Index | Interval | Start | Finish | Weight |
|-------|----------|-------|--------|--------|
| 1 | A | 1 | 3 | 40 |
| 2 | B | 2 | 5 | 100 |
| 3 | C | 4 | 6 | 70 |
| 4 | D | 6 | 8 | 50 |
| 5 | E | 5 | 9 | 120 |

**Step 1: Compute p[j] values**

- For interval 1 (A): No interval ends before start (1), so p[1] = 0
- For interval 2 (B): No interval ends before start (2), so p[2] = 0
- For interval 3 (C): Interval 1 ends at 3 ≤ 4, so p[3] = 1
- For interval 4 (D): Interval 3 ends at 6 ≤ 6, so p[4] = 3
- For interval 5 (E): Interval 2 ends at 5 ≤ 5, so p[5] = 2

**Step 2: Compute dp array**

- dp[0] = 0
- dp[1] = max(dp[0], w[1] + dp[p[1]]) = max(0, 40 + 0) = 40
- dp[2] = max(dp[1], w[2] + dp[p[2]]) = max(40, 100 + 0) = 100
- dp[3] = max(dp[2], w[3] + dp[p[3]]) = max(100, 70 + dp[1]) = max(100, 70 + 40) = 110
- dp[4] = max(dp[3], w[4] + dp[p[4]]) = max(110, 50 + dp[3]) = max(110, 50 + 110) = 160
- dp[5] = max(dp[4], w[5] + dp[p[5]]) = max(160, 120 + dp[2]) = max(160, 120 + 100) = 220

**Maximum Weight: 220**

**Traceback to find intervals:**
- dp[5] = 220 came from w[5] + dp[2] = 120 + 100, so select E
- From dp[2] = 100, since dp[2] = w[2], select B
- Solution: Intervals B and E with total weight 100 + 120 = 220

### Example 2: With Zero-Weight Intervals

Consider intervals where some weights might be zero or negative:

| Index | Start | Finish | Weight |
|-------|-------|--------|--------|
| 1 | 1 | 4 | 50 |
| 2 | 3 | 5 | 20 |
| 3 | 0 | 6 | 100 |
| 4 | 5 | 7 | 30 |
| 5 | 7 | 8 | 25 |

After sorting by finish time: intervals become (1,4,50), (3,5,20), (0,6,100), (5,7,30), (7,8,25)

Compute p[j]: p[1]=0, p[2]=0, p[3]=0 (none end before 0), p[4]=1 (4≤5), p[5]=4 (7≤7)

DP computation:
- dp[0] = 0
- dp[1] = max(0, 50+0) = 50
- dp[2] = max(50, 20+0) = 50
- dp[3] = max(50, 100+0) = 100
- dp[4] = max(100, 30+dp[1]) = max(100, 30+50) = 100
- dp[5] = max(100, 25+dp[4]) = max(100, 25+100) = 125

Maximum weight: 125, selecting intervals 3 and 5 (weights 100 + 25).

### Example 3: Real-World Application

A freelance consultant has the following project offers (each project is an interval with the shown payment):

| Project | Start Week | End Week | Payment (₹) |
|---------|------------|----------|-------------|
| P1 | 1 | 3 | 50,000 |
| P2 | 2 | 5 | 80,000 |
| P3 | 4 | 7 | 60,000 |
| P4 | 6 | 9 | 90,000 |
| P5 | 8 | 10 | 40,000 |

Sorted by finish time maintains this order. Computing p values:
- p[1]=0 (no project before week 1)
- p[2]=0 (week 2 starts, no project finishes before week 2)
- p[3]=1 (project P1 ends at week 3 ≤ 4)
- p[4]=2 (P2 ends at week 5 ≤ 6)
- p[5]=3 (P3 ends at week 7 ≤ 8)

DP: dp[1]=50000, dp[2]=80000, dp[3]=max(80000, 60000+50000)=110000, dp[4]=max(110000, 90000+80000)=170000, dp[5]=max(170000, 40000+110000)=170000

Optimal selection: Projects P2 and P4 (₹80,000 + ₹90,000 = ₹1,70,000)

## Exam Tips

1. **Always sort first**: Remember that the DP recurrence requires intervals sorted by finish time. Many students lose marks by forgetting this preprocessing step.

2. **Understand p[j] thoroughly**: The p[j] function is crucial. Practice computing it using both O(n²) and binary search methods. In exams, you may need to show your work for p[j] calculation.

3. **Base case matters**: Initialize dp[0] = 0. This represents the case with no intervals and zero weight, forming the foundation of the recurrence.

4. **Traceback technique**: After computing dp[n], traceback by comparing dp[i] with dp[i-1] to determine if interval i was selected in the optimal solution.

5. **Time complexity analysis**: Be prepared to justify O(n log n) complexity. Sorting dominates when using binary search for p[j].

6. **Connection to other problems**: Understand how this relates to the 0/1 Knapsack problem—the weighted interval scheduling can be seen as a special case with compatibility constraints.

7. **Edge cases**: Handle cases where all weights are equal, all intervals overlap, no intervals exist (n=0), or p[j] = 0 for all j.