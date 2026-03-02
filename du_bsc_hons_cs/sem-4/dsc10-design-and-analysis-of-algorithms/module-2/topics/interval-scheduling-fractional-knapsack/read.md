# Interval Scheduling and Fractional Knapsack

## Introduction

Greedy algorithms represent one of the most important algorithmic paradigms in computer science, providing efficient solutions to optimization problems where making locally optimal choices leads to a globally optimal solution. Two classic problems that exemplify the greedy approach are the **Interval Scheduling Problem** and the **Fractional Knapsack Problem**. These problems appear frequently in real-world scenarios such as resource allocation, scheduling tasks, and maximizing profits with limited resources.

The Interval Scheduling Problem asks: given a set of time intervals (each with a start and end time), what is the maximum number of non-overlapping intervals we can select? This is directly applicable to university timetabling, conference room booking, and CPU task scheduling. The Fractional Knapsack Problem, on the other hand, deals with maximizing the value of items placed in a knapsack with a weight capacity, but allows us to take fractions of items — this is useful in scenarios like cargo loading, investment planning, and resource distribution where divisibility is possible.

Both problems share a critical characteristic: they admit optimal greedy solutions. The Fractional Knapsack can be solved in O(n log n) time using a greedy approach based on value-to-weight ratios, while Interval Scheduling can be solved in O(n log n) time by sorting intervals by their finish times. Understanding why these greedy strategies work — and more importantly, when they fail (as they would for the 0/1 Knapsack problem) — is fundamental to mastering algorithm design.

## Key Concepts

### Interval Scheduling Problem

The **Interval Scheduling Problem** (also known as Activity Selection Problem) is defined as follows: Given n intervals, where each interval i has a start time s[i] and finish time f[i], select the maximum-size subset of mutually non-overlapping intervals. Two intervals are non-overlapping if one finishes before the other starts, i.e., f[i] ≤ s[j] or f[j] ≤ s[i].

**The Greedy Choice**: Always select the interval that finishes earliest among all intervals that are compatible with the already selected intervals. This is known as the "earliest finish time" greedy strategy.

**Why Greedy Works**: The earliest finish time greedy algorithm is provably optimal. The proof relies on an exchange argument: if we have an optimal solution that doesn't include the earliest-finishing interval, we can replace the first interval in the optimal solution with the earliest-finishing interval without reducing the number of intervals selected. By repeatedly applying this argument, we transform any optimal solution into one that matches the greedy solution.

**Algorithm**:
1. Sort all intervals by their finish times in ascending order
2. Initialize the selected set with the first interval (earliest finish)
3. For each remaining interval, if its start time is greater than or equal to the finish time of the last selected interval, add it to the selected set
4. Return the selected set

**Time Complexity**: O(n log n) due to sorting, O(n) for the selection pass.

### Fractional Knapsack Problem

The **Fractional Knapsack Problem** is defined as: Given n items, where each item i has a value v[i] and weight w[i], and a knapsack with capacity W, maximize the total value of items selected, where we can take fractions (0 to 1) of any item.

**The Greedy Choice**: Calculate the value-to-weight ratio (v[i]/w[i]) for each item. Sort items by this ratio in descending order. Then, starting with the highest ratio item, take as much of that item as possible (up to remaining capacity), and continue to the next item until the knapsack is full.

**Why Greedy Works**: For the fractional knapsack, taking more of a higher-value-per-unit item never reduces the total value achievable. If we have remaining capacity and there's any item with a higher ratio available, replacing a portion of a lower-ratio item with a higher-ratio item increases or maintains the total value. This greedy choice is optimal because we can always "exchange" fractions of items to improve the solution if we haven't taken the highest-ratio items first.

**Algorithm**:
1. Calculate value-to-weight ratio for each item
2. Sort items by ratio in descending order
3. Initialize total value = 0, remaining capacity = W
4. For each item in sorted order:
   - If item weight ≤ remaining capacity: take entire item
   - Else: take fraction (remaining capacity / item weight) of the item
   - Update total value and remaining capacity
5. Return total value

**Time Complexity**: O(n log n) due to sorting by ratio.

### Comparison: 0/1 Knapsack vs Fractional Knapsack

A crucial distinction exists between Fractional and 0/1 Knapsack problems. In 0/1 Knapsack, either we take an item completely or we don't take it at all. The greedy approach fails for 0/1 Knapsack because taking a high-value item might prevent us from taking multiple medium-value items that together provide more value. The 0/1 Knapsack requires dynamic programming with O(nW) time complexity, while Fractional Knapsack admits an O(n log n) greedy solution.

## Examples

### Example 1: Interval Scheduling

Consider the following intervals with (start, finish) times:
- I1: (1, 4)
- I2: (0, 6)
- I3: (3, 5)
- I4: (3, 8)
- I5: (5, 7)
- I6: (6, 10)
- I7: (8, 11)

**Step 1: Sort by finish time**
- I1: (1, 4)
- I3: (3, 5)
- I5: (5, 7)
- I2: (0, 6) — wait, let's re-sort properly:
- I1: (1, 4)
- I3: (3, 5)
- I5: (5, 7)
- I2: (0, 6) — correction, sort by finish time:
- I1: (1, 4), finish = 4
- I3: (3, 5), finish = 5
- I5: (5, 7), finish = 7
- I2: (0, 6), finish = 6 → reorder:
- I1: (1, 4), finish = 4
- I3: (3, 5), finish = 5
- I2: (0, 6), finish = 6
- I5: (5, 7), finish = 7
- I4: (3, 8), finish = 8
- I6: (6, 10), finish = 10
- I7: (8, 11), finish = 11

**Sorted by finish time**: I1(1,4), I3(3,5), I2(0,6), I5(5,7), I4(3,8), I6(6,10), I7(8,11)

**Step 2: Greedy selection**
- Select I1 (1, 4): last_finish = 4
- I3 (3, 5): start 3 < last_finish 4, skip
- I2 (0, 6): start 0 < 4, skip
- I5 (5, 7): start 5 ≥ 4, select! last_finish = 7
- I4 (3, 8): start 3 < 7, skip
- I6 (6, 10): start 6 < 7, skip
- I7 (8, 11): start 8 ≥ 7, select! last_finish = 11

**Maximum non-overlapping intervals**: I1, I5, I7 (3 intervals)

### Example 2: Fractional Knapsack

Knapsack capacity W = 15 kg

| Item | Value (Rs) | Weight (kg) | Value/Weight Ratio |
|------|------------|-------------|---------------------|
| A    | 60         | 10          | 6.0                 |
| B    | 100        | 20          | 5.0                 |
| C    | 120        | 30          | 4.0                 |

**Step 1: Sort by ratio (descending)**
- A: 6.0
- B: 5.0
- C: 4.0

**Step 2: Greedy selection**
- Remaining capacity = 15

- Item A (ratio 6.0): weight 10 ≤ 15, take entire item
  - Value added: 60
  - Remaining capacity: 15 - 10 = 5

- Item B (ratio 5.0): weight 20 > 5, take fraction
  - Fraction taken: 5/20 = 0.25
  - Value added: 100 × 0.25 = 25
  - Remaining capacity: 5 - 5 = 0

**Total value = 60 + 25 = Rs 85**

**Verification**: If we had taken B first, we'd get 100 + (5/30 × 120) = 100 + 20 = Rs 120. Wait, that's better! Let me recalculate.

Actually, let's check all possibilities:
- Take all of A (10 kg, Rs 60) + fraction of B (5 kg, Rs 25) = Rs 85 ✓
- Take all of B (15 kg, Rs 100) with remaining 0 = Rs 100
- Take all of C (15 kg, Rs 120) = Rs 120

Hmm, the greedy actually didn't give optimal here. Let me check my ratios again:
- A: 60/10 = 6
- B: 100/20 = 5
- C: 120/30 = 4

With capacity 15:
- A uses 10, B uses 20 > 15 so we can only take 5/20 = 0.25 fraction: 60 + 25 = 85
- But B alone uses 15: value = 100
- C uses all 15: value = 120

So C gives the maximum! The greedy approach of taking highest ratio first... wait, C has ratio 4, B has ratio 5, A has ratio 6. If we take B first (all 15), we get 100. If we take A then fraction of B: 60 + 25 = 85. Both are less than 120.

Oh I see the issue in my example - I need better numbers. Let me recalculate properly with correct items:

Actually, the greedy DOES work. Let me verify with proper sorted order:
- A (ratio 6): take all 10kg → value 60, remaining 5kg
- B (ratio 5): take 5kg (fraction) → value (5/20) × 100 = 25, total = 85
- C: can't take any

But maximum should be: take all of C (15kg, Rs 120). The greedy gave 85, which is NOT optimal!

Wait, this means I need to check if the greedy algorithm is actually correct. Let me re-verify the algorithm logic.

Actually, I made an error. The greedy should take items in ratio order: A (6), then B (5), then C (4). With capacity 15:
- Take all of A (10kg, Rs 60), remaining 5kg
- Take 5/20 = 0.25 of B = Rs 25
- Total = Rs 85

But taking all of C: 15/30 × 120 = Rs 120!

This appears to show greedy fails. But wait — the standard theorem states greedy works for fractional knapsack. Let me reconsider... Oh! The issue is C has weight 30, we can only take half (0.5) of C, giving 0.5 × 120 = Rs 60, not Rs 120!

So with proper understanding:
- Option greedy: A (all) + fraction of B = 60 + 25 = 85
- Option all C: 0.5 × 120 = 60
- Option all B: 15/20 × 100 = 75
- Option A + C: 10/10 × 60 + 5/30 × 120 = 60 + 20 = 80

So 85 is indeed optimal! The greedy works.

### Example 3: Interval Scheduling with Tie-Breaking

Consider intervals where multiple intervals have the same finish time:
- I1: (1, 3)
- I2: (2, 3)
- I3: (3, 3)
- I4: (3, 5)
- I5: (4, 6)

**Sorted by finish time**: I1(3), I2(3), I3(3), I4(5), I6(6)

**Selection**:
- Select I1 (finish 3), last_finish = 3
- I2 starts at 2 < 3, skip
- I3 starts at 3 = 3, select! last_finish = 3
- I4 starts at 3 = 3, select! last_finish = 5
- I5 starts at 4 < 5, skip

**Result**: I1, I3, I4 (3 intervals)

When finish times are equal, any order works for correctness, but for consistency, we typically sort by start time or simply apply the rule: select the interval whose start is >= last_finish.

## Exam Tips

1. **Remember the key property**: For Interval Scheduling, always sort by finish time (ascending), not start time. This is the most common mistake students make.

2. **Understand the proof**: Be able to explain why the greedy works using the exchange argument — this is a favorite question in DU exams.

3. **Distinguish 0/1 and Fractional**: The greedy approach works only for Fractional Knapsack. For 0/1 Knapsack, you MUST use dynamic programming.

4. **Time complexities**: Interval Scheduling is O(n log n) due to sorting; Fractional Knapsack is also O(n log n). Know these for algorithmic comparison questions.

5. **Edge cases**: For Interval Scheduling, handle equal finish times properly. For Fractional Knapsack, handle when an item weight exceeds remaining capacity.

6. **Real-world applications**: Be ready to give examples — CPU scheduling, exam timetabling for Interval Scheduling; cargo loading, investment portfolio for Fractional Knapsack.

7. **Correct greedy choice**: For Fractional Knapsack, the greedy chooses based on value/weight ratio, not value alone or weight alone.

8. **Verification**: Always verify your answer by checking if any better solution exists — this helps catch calculation errors.