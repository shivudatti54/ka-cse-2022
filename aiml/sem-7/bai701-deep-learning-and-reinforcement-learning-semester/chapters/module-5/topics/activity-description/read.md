# Activity Selection Problem

## Introduction to Greedy Algorithms

Greedy Algorithms are a class of algorithms that make the best local choice at each step with the hope of finding a global optimum. They are particularly useful for optimization problems where we need to find the best solution from a set of choices. The key characteristic of greedy algorithms is that they never reconsider their choices once made.

The Activity Selection Problem is a classic example that demonstrates the greedy algorithmic paradigm. It involves selecting the maximum number of activities that can be performed by a single person or machine, assuming that only one activity can be done at a time.

## Problem Statement

Given a set `S = {a₁, a₂, ..., aₙ}` of `n` activities, where each activity `aᵢ` has:
- A start time `sᵢ`
- A finish time `fᵢ` (with `sᵢ < fᵢ`)

The objective is to select the **maximum number of non-overlapping activities** that can be performed by a single person.

### Key Constraints:
- Only one activity can be performed at a time
- Once started, an activity must run to completion
- Activities are sorted by their finish times (typically)

## Greedy Approach for Activity Selection

The optimal solution for this problem can be found using a greedy algorithm that always selects the activity with the earliest finish time that doesn't conflict with previously selected activities.

### Algorithm Steps:

1. **Sort activities** by their finish times in ascending order
2. **Initialize** the solution set with the first activity (the one with earliest finish time)
3. **Iterate** through the remaining activities:
   - For each activity, if its start time is greater than or equal to the finish time of the last selected activity
   - **Select** this activity and add it to the solution set

### Pseudocode:

```
Activity-Selection(S, f, s)
1. Sort S by finish time f
2. A = {a₁}  // Select first activity
3. k = 1     // Index of last selected activity
4. for m = 2 to n do
5.   if s[m] >= f[k] then
6.     A = A ∪ {aₘ}
7.     k = m
8. return A
```

## Example with Step-by-Step Solution

Let's consider a set of activities with their start and finish times:

| Activity | Start Time | Finish Time |
|----------|------------|-------------|
| A₁       | 1          | 3           |
| A₂       | 2          | 5           |
| A₃       | 4          | 7           |
| A₄       | 1          | 8           |
| A₅       | 5          | 9           |
| A₆       | 8          | 10          |

### Step 1: Sort by Finish Time

After sorting by finish time:

| Activity | Start Time | Finish Time |
|----------|------------|-------------|
| A₁       | 1          | 3           |
| A₂       | 2          | 5           |
| A₃       | 4          | 7           |
| A₄       | 1          | 8           |
| A₅       | 5          | 9           |
| A₆       | 8          | 10          |

### Step 2: Initialize Solution

Select A₁ (earliest finish time)
- Current solution: {A₁}
- Last finish time: 3

### Step 3: Iterate Through Remaining Activities

Check A₂: Start time (2) < last finish time (3) → Skip (overlaps)
Check A₃: Start time (4) ≥ last finish time (3) → Select
- Current solution: {A₁, A₃}
- Last finish time: 7

Check A₄: Start time (1) < last finish time (7) → Skip
Check A₅: Start time (5) < last finish time (7) → Skip
Check A₆: Start time (8) ≥ last finish time (7) → Select
- Current solution: {A₁, A₃, A₆}
- Last finish time: 10

### Final Solution: {A₁, A₃, A₆} (3 activities)

## Time Complexity Analysis

- **Sorting**: O(n log n) - Using efficient sorting algorithm
- **Selection**: O(n) - Single pass through sorted activities
- **Total Complexity**: O(n log n)

This is optimal as sorting is the most expensive operation.

## Why the Greedy Approach Works

### Greedy Choice Property
The activity with the earliest finish time leaves the maximum remaining time for subsequent activities, making it the optimal choice for the first step.

### Optimal Substructure
Once we make the greedy choice (selecting the activity with earliest finish time), the remaining problem reduces to finding the optimal solution for the subproblem of activities that start after the finish time of the selected activity.

## Proof of Correctness

**Theorem**: The greedy algorithm always produces an optimal solution for the activity selection problem.

**Proof by contradiction**:
1. Assume the greedy solution is not optimal
2. Let the greedy solution be {a₁, a₂, ..., aₖ} and an optimal solution be {b₁, b₂, ..., bₘ} with m > k
3. Since we choose activities with earliest finish times, we can show that for each i, f(aᵢ) ≤ f(bᵢ)
4. This leads to a contradiction as we could replace bᵢ with aᵢ and potentially add more activities

## Comparison with Other Approaches

| Approach | Time Complexity | Space Complexity | Optimal? |
|----------|-----------------|------------------|----------|
| Greedy (finish time) | O(n log n) | O(1) | Yes |
| Dynamic Programming | O(n²) | O(n) | Yes |
| Brute Force | O(2ⁿ) | O(n) | Yes |

The greedy approach is more efficient than dynamic programming for this problem.

## Variations of the Problem

1. **Weighted Activity Selection**: Each activity has a weight/value, and we want to maximize the total value (requires DP approach)
2. **Multiple Resources**: Select activities that can be performed with k persons/machines
3. **Time Constraints**: Activities with deadlines and durations

## Implementation Example

```python
def activity_selection(start, finish):
    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    selected = [0]  # First activity always selected
    last_finish = activities[0][1]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish:
            selected.append(i)
            last_finish = activities[i][1]
    
    return selected

# Example usage
start_times = [1, 2, 4, 1, 5, 8]
finish_times = [3, 5, 7, 8, 9, 10]
result = activity_selection(start_times, finish_times)
print("Selected activities:", result)  # Output: [0, 2, 5]
```

## Real-World Applications

1. **Scheduling classes** in a classroom
2. **CPU scheduling** in operating systems
3. **Resource allocation** in cloud computing
4. **Meeting room scheduling** in office buildings
5. **Tournament scheduling** in sports

## Exam Tips

1. **Always sort by finish time** - This is the key step that makes the greedy approach work
2. **Prove optimality** - Be prepared to explain why the greedy choice leads to global optimum
3. **Time complexity** - Remember it's O(n log n) due to sorting
4. **Counter examples** - Understand why sorting by start time or duration doesn't work
5. **Practice variations** - Be familiar with weighted activity selection and multiple resources
6. **Comparison** - Be able to compare greedy approach with DP solution
7. **Implementation** - Practice writing the algorithm pseudocode or code