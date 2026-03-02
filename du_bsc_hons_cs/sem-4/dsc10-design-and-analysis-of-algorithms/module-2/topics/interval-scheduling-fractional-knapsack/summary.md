# Interval Scheduling and Fractional Knapsack - Summary

## Key Definitions and Concepts

- **Interval Scheduling Problem**: Given n intervals with start and finish times, find the maximum-size subset of mutually non-overlapping intervals.

- **Activity Selection**: Another name for Interval Scheduling; the greedy approach selects the interval that finishes earliest.

- **Fractional Knapsack Problem**: Given n items with values and weights, and a knapsack of capacity W, maximize total value where fractions (0 to 1) of any item can be taken.

- **0/1 Knapsack Problem**: Unlike Fractional, either the entire item is taken or none of it; requires dynamic programming, not greedy.

- **Greedy Algorithm**: An algorithmic paradigm that makes locally optimal choices at each step, hoping for a global optimum.

## Important Formulas and Theorems

- **Interval Scheduling**: Sort intervals by finish time f[i] in ascending order. Select interval i if s[i] ≥ last_finish.

- **Fractional Knapsack**: Calculate ratio r[i] = v[i]/w[i] for each item. Sort by r[i] in descending order. Take items entirely if w[i] ≤ remaining capacity; otherwise take fractional amount.

- **Exchange Argument**: Proof technique showing that if an optimal solution doesn't contain the greedy choice, we can exchange the first interval/item with the greedy choice without reducing optimality.

## Key Points

- Interval Scheduling greedy: Always select the interval that ends earliest and is compatible with previously selected intervals.

- Fractional Knapsack greedy: Sort by value-to-weight ratio and take as much as possible of the highest-ratio items first.

- Both problems have O(n log n) time complexity due to sorting.

- The greedy approach FAILS for 0/1 Knapsack — must use dynamic programming (O(nW)).

- For Interval Scheduling with equal finish times, any interval can be selected as long as it's compatible.

- For Fractional Knapsack, the greedy solution is always optimal because we can "exchange" fractions of items.

## Common Mistakes to Avoid

1. Sorting Interval Scheduling by start time instead of finish time — this produces incorrect results.

2. Confusing Fractional Knapsack with 0/1 Knapsack and attempting greedy solution for 0/1 — it doesn't work.

3. Forgetting to check if the current interval's start time is >= last selected finish time.

4. In Fractional Knapsack, not handling the case where item weight exceeds remaining capacity (take fraction, not entire item).

5. Not recalculating remaining capacity after each selection in both algorithms.

## Revision Tips

1. Practice at least 3 problems of each type to solidify the algorithm steps.

2. Memorize why greedy works for these problems — the exchange argument is frequently asked.

3. Create a comparison table between Interval Scheduling, Fractional Knapsack, and 0/1 Knapsack.

4. Remember: Sort first, then apply greedy selection — this pattern applies to both algorithms.

5. Focus on understanding the proof of optimality, not just the algorithm steps.