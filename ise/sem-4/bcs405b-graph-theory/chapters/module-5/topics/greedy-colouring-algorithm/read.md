# Greedy Algorithms

## Introduction to Greedy Algorithms

Greedy algorithms are a fundamental class of algorithms in combinatorial optimization that make a sequence of choices, each of which looks best at the moment. At each decision point, the algorithm chooses the locally optimal option without reconsidering previous decisions. This "greedy" approach is simple to implement and often efficient, but doesn't always yield globally optimal solutions.

Greedy algorithms are particularly useful for optimization problems where we need to make a series of choices to arrive at an optimal solution. They work well when a problem exhibits two key properties: the greedy-choice property and optimal substructure.

## Key Properties of Greedy Algorithms

### Greedy-Choice Property

A problem has the greedy-choice property if a globally optimal solution can be reached by making a locally optimal (greedy) choice. This means that at each step, we can make a choice that looks best without considering the overall problem, and this series of choices will lead to an optimal solution.

### Optimal Substructure

A problem exhibits optimal substructure if an optimal solution to the problem contains within it optimal solutions to subproblems. This property allows us to solve the problem recursively by breaking it down into smaller subproblems.

## When to Use Greedy Algorithms

Greedy algorithms are appropriate when:

1. The problem has the greedy-choice property
2. The problem has optimal substructure
3. We need a fast, approximate solution (when exact optimization is computationally expensive)

## Classic Greedy Algorithm Examples

### Activity Selection Problem

**Problem Statement**: Given a set of activities with start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on one activity at a time.

```
Activities:
A1: (1, 4)
A2: (3, 5)
A3: (0, 6)
A4: (5, 7)
A5: (3, 8)
A6: (5, 9)
```

**Greedy Approach**: Sort activities by finish time and always select the activity that finishes earliest and doesn't conflict with previously selected activities.

```
Sorted by finish time: A1, A2, A4, A5, A6
Solution: A1, A4
```

### Huffman Coding

**Problem Statement**: Given a set of characters and their frequencies, construct a prefix-free binary code that minimizes the expected length of the encoded message.

**Greedy Approach**: Repeatedly combine the two least frequent nodes into a new node until only one node remains.

```
Characters: A(5), B(9), C(12), D(13), E(16), F(45)

Step 1: Combine A(5) and B(9) → AB(14)
Step 2: Combine C(12) and AB(14) → CAB(26)
Step 3: Combine D(13) and E(16) → DE(29)
Step 4: Combine CAB(26) and DE(29) → CABDE(55)
Step 5: Combine F(45) and CABDE(55) → Root(100)
```

### Fractional Knapsack Problem

**Problem Statement**: Given items with weights and values, and a knapsack with limited capacity, determine the maximum value that can be carried, allowing fractions of items to be taken.

**Greedy Approach**: Sort items by value-to-weight ratio in descending order and take as much as possible of each item.

```
Items:
Item1: weight=10, value=60, ratio=6.0
Item2: weight=20, value=100, ratio=5.0
Item3: weight=30, value=120, ratio=4.0
Knapsack capacity: 50

Solution: Take all of Item1 (10), all of Item2 (20), and 20/30 of Item3
Total value: 60 + 100 + (20/30)*120 = 60 + 100 + 80 = 240
```

## Greedy vs Dynamic Programming

| Aspect          | Greedy Algorithms                    | Dynamic Programming                   |
| --------------- | ------------------------------------ | ------------------------------------- |
| Decision Making | Makes locally optimal choice         | Considers all possible choices        |
| Optimality      | Not always optimal                   | Always finds optimal solution         |
| Efficiency      | Usually more efficient               | Can be computationally expensive      |
| Problem Types   | Problems with greedy-choice property | Problems with overlapping subproblems |
| Memory Usage    | Lower memory requirements            | Higher memory requirements            |

## Implementation Framework

The general structure of a greedy algorithm follows this pattern:

1. **Sort** the input according to some criterion
2. **Initialize** the solution set
3. **Iterate** through the sorted input
4. **Select** elements that satisfy the constraints
5. **Add** selected elements to the solution set

```python
def greedy_algorithm(items, constraints):
    # Sort items based on some greedy criterion
    sorted_items = sort(items, key=criterion)

    solution = []
    for item in sorted_items:
        if satisfies_constraints(solution, item, constraints):
            solution.append(item)

    return solution
```

## Limitations of Greedy Algorithms

Greedy algorithms don't always produce optimal solutions. A classic example is the 0-1 Knapsack Problem, where the greedy approach (based on value-to-weight ratio) fails to find the optimal solution:

```
Items:
Item1: weight=5, value=50, ratio=10
Item2: weight=10, value=60, ratio=6
Item3: weight=20, value=140, ratio=7
Knapsack capacity: 30

Greedy solution: Item1 + Item3 = 50 + 140 = 190
Optimal solution: Item2 + Item3 = 60 + 140 = 200
```

## Proving Greedy Algorithm Correctness

To prove that a greedy algorithm produces an optimal solution, we typically use one of these methods:

1. **Greedy stays ahead**: Show that the greedy algorithm is always at least as good as any other algorithm at each step
2. **Exchange argument**: Show that any solution can be transformed to the greedy solution without worsening the objective
3. **Mathematical induction**: Prove correctness by induction on the problem size

## Real-World Applications

Greedy algorithms are used in various domains:

1. **Networking**: Dijkstra's algorithm for shortest path routing
2. **Data Compression**: Huffman coding for file compression
3. **Scheduling**: Task scheduling in operating systems
4. **Finance**: Coin change problem (for certain coin systems)
5. **Machine Learning**: Decision tree construction (ID3, C4.5 algorithms)

## Exam Tips

1. **Identify greedy-choice property**: Look for problems where local optimal choices lead to global optimum
2. **Check optimal substructure**: Verify that the problem can be broken down into smaller subproblems
3. **Consider sorting**: Many greedy algorithms begin by sorting input data
4. **Watch for pitfalls**: Remember that greedy algorithms don't always yield optimal solutions
5. **Practice proof techniques**: Be prepared to prove why a greedy approach works for a given problem
6. **Compare with DP**: Understand when to use greedy vs dynamic programming approaches
