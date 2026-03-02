# Greedy Algorithm Principles

## Introduction to Greedy Algorithms

Greedy algorithms are a class of algorithmic techniques that make locally optimal choices at each step with the hope of finding a global optimum. The fundamental principle is to make the choice that seems best at the moment, without considering future consequences or revisiting previous decisions. This "greedy" approach is simple, intuitive, and often leads to efficient solutions for optimization problems.

Unlike dynamic programming, which solves subproblems and combines their solutions, greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. While not universally applicable, greedy algorithms are particularly effective for problems that exhibit two key properties: the greedy choice property and optimal substructure.

## Key Properties of Greedy Algorithms

### Greedy Choice Property

The greedy choice property states that a globally optimal solution can be arrived at by making a locally optimal (greedy) choice. This means that at each decision point, we can make a choice that looks best for the current situation, and this will lead to an optimal solution overall.

**Example**: In the activity selection problem, always choosing the activity that finishes earliest (a greedy choice) leads to an optimal schedule of non-overlapping activities.

### Optimal Substructure

A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. This property is shared with dynamic programming, but greedy algorithms exploit it differently by making a greedy choice and then solving a single subproblem.

**Example**: In the fractional knapsack problem, after choosing the item with the highest value-to-weight ratio, the remaining problem is a smaller knapsack problem with reduced capacity.

## Comparison with Other Paradigms

| Feature        | Greedy Algorithms            | Dynamic Programming            | Divide and Conquer                 |
| -------------- | ---------------------------- | ------------------------------ | ---------------------------------- |
| **Approach**   | Make locally optimal choices | Solve overlapping subproblems  | Break into independent subproblems |
| **Optimality** | Not always optimal           | Always optimal (if applicable) | Always optimal                     |
| **Efficiency** | Usually O(n log n) or O(n)   | Usually polynomial time        | Usually O(n log n)                 |
| **Storage**    | Minimal                      | Requires table storage         | Recursion stack                    |
| **Examples**   | Dijkstra, Huffman coding     | Fibonacci, LCS                 | Merge sort, Quick sort             |

## Common Greedy Algorithm Problems

### Activity Selection Problem

The activity selection problem involves selecting the maximum number of activities that don't overlap, given a set of activities with start and finish times.

**Greedy Approach**: Sort activities by finish time and always select the next activity that doesn't conflict with the previously selected ones.

```
Activities: (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)

Sorted by finish time: (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)

Selected activities: (1,4) → (5,7) → (8,11) → (12,16)
```

### Huffman Coding

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to characters based on their frequencies, with more frequent characters getting shorter codes.

**Greedy Approach**: Repeatedly combine the two least frequent nodes into a new node until only one node remains.

```
Step-by-step building of Huffman tree:

Characters: A(5), B(9), C(12), D(13), E(16), F(45)

Step 1: Combine A(5) and B(9) → Node(14)
Step 2: Combine C(12) and Node(14) → Node(26)
Step 3: Combine D(13) and E(16) → Node(29)
Step 4: Combine Node(26) and Node(29) → Node(55)
Step 5: Combine F(45) and Node(55) → Root(100)
```

### Fractional Knapsack Problem

Given items with weights and values, and a knapsack with limited capacity, the goal is to maximize the total value by taking fractions of items.

**Greedy Approach**: Sort items by value-to-weight ratio in descending order and take as much as possible of each item.

```
Items: (weight, value)
Item1: (10, 60), Item2: (20, 100), Item3: (30, 120)
Knapsack capacity: 50

Value/weight ratios: Item1: 6, Item2: 5, Item3: 4

Solution: Take all of Item1 (10kg, $60), all of Item2 (20kg, $100),
and 20/30 of Item3 (20kg, $80) → Total: 50kg, $240
```

### Job Scheduling Problem

Given jobs with deadlines and profits, schedule jobs to maximize profit such that each job is completed by its deadline.

**Greedy Approach**: Sort jobs by profit in descending order and schedule each job as late as possible without missing its deadline.

```
Jobs: (deadline, profit)
J1: (2, 100), J2: (1, 19), J3: (2, 27), J4: (1, 25), J5: (3, 15)

Sorted by profit: J1(100), J3(27), J4(25), J2(19), J5(15)

Schedule:
Time 1: J1 (deadline 2, can schedule later)
Time 1: J4 (deadline 1, must schedule now)
Time 2: J1
Time 3: J5
Total profit: 100 + 25 + 15 = 140
```

## Algorithm Design Steps

1. **Problem Analysis**: Determine if the problem has greedy choice property and optimal substructure.
2. **Greedy Selection**: Identify what makes a choice "greedy" (e.g., earliest finish time, highest ratio).
3. **Sorting**: Often the first step is to sort the input based on the greedy criterion.
4. **Iterative Selection**: Process elements in sorted order, making greedy choices.
5. **Solution Construction**: Build the solution incrementally based on these choices.
6. **Correctness Proof**: Prove that the greedy choice leads to an optimal solution.

## When to Use Greedy Algorithms

Greedy algorithms are appropriate when:

- The problem has the greedy choice property
- The problem has optimal substructure
- A globally optimal solution can be achieved through local optimizations
- The problem doesn't require reconsidering previous choices

## Limitations of Greedy Algorithms

- Not all problems can be solved optimally with greedy approaches
- May get stuck in local optima instead of finding global optimum
- Require careful proof of correctness
- The 0/1 knapsack problem cannot be solved optimally with a greedy approach (though fractional can)

## Exam Tips

1. **Identify Greedy Problems**: Look for optimization problems where local optimal choices lead to global optimum.
2. **Prove Correctness**: Always be prepared to prove that your greedy choice is safe (leads to optimal solution).
3. **Sorting is Key**: Most greedy algorithms begin with sorting - know the appropriate sorting criterion.
4. **Counterexamples**: For problems where greedy doesn't work (like 0/1 knapsack), be ready to provide a counterexample.
5. **Complexity Analysis**: Greedy algorithms are usually efficient - often dominated by sorting (O(n log n)).
6. **Compare with DP**: Understand when to use greedy vs dynamic programming (greedy when local choices are sufficient, DP when need to consider all possibilities).
