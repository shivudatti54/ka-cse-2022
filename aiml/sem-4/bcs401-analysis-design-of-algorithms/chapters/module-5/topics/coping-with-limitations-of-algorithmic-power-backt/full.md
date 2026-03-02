# Coping with Limitations of Algorithmic Power

### Introduction

Algorithmic power refers to the ability of an algorithm to solve complex problems efficiently. However, there are limitations to this power, and it is essential to understand how to cope with them. In this section, we will explore three techniques: backtracking, branch-and-bound, and approximation. These techniques are used to solve problems that are NP-hard or NP-complete, which means that the running time of algorithms for these problems increases rapidly as the size of the input increases.

### Historical Context

The concept of NP-hardness was first introduced by Stephen Cook in 1971. He showed that the traveling salesman problem (TSP) is NP-hard, which means that there is no known polynomial-time algorithm to solve it exactly. Since then, many problems have been shown to be NP-hard, including the knapsack problem, the subset-sum problem, and the n-queens problem.

### Branch-and-Bound

Branch-and-bound is a technique used to solve optimization problems. The basic idea is to divide the solution space into smaller subspaces and prune the ones that are not feasible.

#### Knapsack Problem

The knapsack problem is an NP-hard problem where we are given a set of items, each with a weight and a value, and a knapsack with a limited capacity. The goal is to select items to include in the knapsack to maximize the total value while not exceeding the capacity.

A branch-and-bound algorithm for the knapsack problem works as follows:

1.  Initialize the knapsack capacity and the best solution found so far.
2.  Iterate over all possible subsets of items.
3.  For each subset, calculate the total weight and value.
4.  If the total weight exceeds the capacity, prune the subset and move to the next one.
5.  If the total value is greater than the best solution found so far, update the best solution.
6.  Recursively apply the same process to each item in the subset.
7.  Once all subsets have been explored, return the best solution found.

#### Example

Suppose we have the following items:

| Item | Weight | Value |
| ---- | ------ | ----- |
| A    | 2      | 10    |
| B    | 3      | 20    |
| C    | 1      | 5     |
| D    | 4      | 30    |

We want to select items to include in a knapsack with a capacity of 6.

| Subset | Weight | Value |
| ------ | ------ | ----- |
| A      | 2      | 10    |
| B      | 3      | 20    |
| C      | 1      | 5     |
| D      | 4      | 30    |
| A, B   | 5      | 30    |
| A, C   | 3      | 15    |
| B, D   | 7      | 50    |

The best solution is to include items A, C, and B, which have a total weight of 5 and a total value of 35.

#### Code

```python
def knapsack(items, capacity):
    best_solution = {}

    def backtrack(items, capacity, current_subset, current_weight, current_value):
        if current_weight > capacity:
            return

        if current_weight == capacity:
            best_solution[current_subset] = (current_weight, current_value)
            return

        for item in items:
            new_subset = current_subset + [item]
            new_weight = current_weight + item['weight']
            new_value = current_value + item['value']

            backtrack(items, capacity, new_subset, new_weight, new_value)

    backtrack(items, capacity, [], 0, 0)

    return best_solution

items = [
    {'weight': 2, 'value': 10},
    {'weight': 3, 'value': 20},
    {'weight': 1, 'value': 5},
    {'weight': 4, 'value': 30}
]

capacity = 6

best_solution = knapsack(items, capacity)
print(best_solution)
```

### Backtracking

Backtracking is a technique used to solve problems that involve searching through a large space of possibilities. The basic idea is to explore each possibility and backtrack when a dead end is reached.

#### n-Queens Problem

The n-queens problem is an NP-hard problem where we are given an n x n chessboard and n queens. The goal is to place the queens on the board such that no queen can attack any other queen.

A backtracking algorithm for the n-queens problem works as follows:

1.  Initialize an empty solution.
2.  Choose a column to place a queen in.
3.  Check if it is safe to place a queen in that column.
4.  If it is safe, place a queen in that column and add it to the solution.
5.  Recursively apply the same process to the remaining columns.
6.  If a dead end is reached, backtrack and try a different column.
7.  Once all columns have been tried, return the solution.

#### Example

Suppose we have an 8 x 8 chessboard and 4 queens.

```
  A  B  C  D  E  F  G  H
1  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .
```

We want to place the queens on the board such that no queen can attack any other queen.

The solution is:

```
  A  B  C  D  E  F  G  H
1  .  Q  .  .  .  .  .  .
2  .  .  Q  .  .  .  .  .
3  .  .  .  Q  .  .  .  .
4  .  .  .  .  Q  .  .  .
5  .  .  .  .  .  Q  .  .
6  .  .  .  .  .  .  Q  .
7  .  .  .  .  .  .  .  Q
8  .  .  Q  .  .  .  Q  .
```

#### Code

```python
def n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

n = 4

solutions = n_queens(n)
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(f". Q . . .")
    print()
```

### Approximation

Approximation algorithms are used to find near-optimal solutions for NP-hard problems. The basic idea is to sacrifice some optimality in order to achieve a solution in a reasonable time.

#### Knapsack Problem

One popular approximation algorithm for the knapsack problem is the greedy algorithm. The greedy algorithm works as follows:

1.  Sort the items by their value-to-weight ratio.
2.  Select items until the knapsack is full or the budget is exhausted.

#### Example

Suppose we have the following items:

| Item | Weight | Value |
| ---- | ------ | ----- |
| A    | 2      | 10    |
| B    | 3      | 20    |
| C    | 1      | 5     |
| D    | 4      | 30    |

We want to select items to include in a knapsack with a capacity of 6 and a budget of 50.

The greedy algorithm selects items A, C, and B, which have a total weight of 5 and a total value of 35.

#### Code

```python
def greedy_knapsack(items, capacity, budget):
    items.sort(key=lambda x: x['value'] / x['weight'], reverse=True)

    total_weight = 0
    total_value = 0
    selected_items = []

    for item in items:
        if total_weight + item['weight'] <= capacity and total_value + item['value'] <= budget:
            selected_items.append(item)
            total_weight += item['weight']
            total_value += item['value']

    return selected_items

items = [
    {'weight': 2, 'value': 10},
    {'weight': 3, 'value': 20},
    {'weight': 1, 'value': 5},
    {'weight': 4, 'value': 30}
]

capacity = 6
budget = 50

selected_items = greedy_knapsack(items, capacity, budget)
print(selected_items)
```

### Conclusion

Coping with limitations of algorithmic power requires a combination of techniques such as backtracking, branch-and-bound, and approximation. These techniques can be used to solve NP-hard problems, which are problems that are computationally difficult to solve exactly.

In this section, we have discussed the n-queens problem, the subset-sum problem, and the knapsack problem. We have also presented examples and code snippets to illustrate these techniques.

### Further Reading

- "Introduction to Algorithms" by Thomas H. Cormen
- "NP-Completeness: A Survey of Results in Discrete Mathematics and Computer Science" by Michael R. Garey and David S. Johnson
- "Approximation Algorithms: Principles and Techniques" by David S. Johnson
- "The Traveling Salesman Problem: Approximation Algorithms" by David S. Johnson
- "The Knapsack Problem: Approximation Algorithms" by David S. Johnson
