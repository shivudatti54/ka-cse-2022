# **Coping with Limitations of Algorithmic Power: Backtracking, Branch-and-Bound, and Approximation**

## **Introduction**

Algorithms are designed to solve problems efficiently, but there are certain limitations to their power. In this section, we will explore three techniques to cope with these limitations: Backtracking, Branch-and-Bound, and Approximation.

## **Backtracking**

Backtracking is a technique used to solve problems that involve search and exploration of possible solutions. It works by recursively trying different solutions and backtracking when a dead-end is reached.

### Key Concepts:

- **Recursion**: A method where a function calls itself to solve a problem.
- **Branching**: Trying different solutions and exploring their consequences.
- **Backtracking**: When a dead-end is reached, the algorithm backtracks to a previous point and tries an alternative solution.

### Problem: n-Queens Problem

Given an n x n chessboard, place n queens such that no two queens attack each other.

**Example:**

```
n = 4

  . Q . .
  . . . .
  . . . .
  . . . .
```

**Solution:**

```
n = 4

  Q . . .
  . . . .
  . . . .
  . . Q .
```

**Code:**

```python
def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)

    result = []
    place_queens(n, 0, [-1]*n)
    return result

print(solve_n_queens(4))
```

## **Subset-Sum Problem**

Given a subset of integers and a target sum, find a subset that sums up to the target.

### Problem:

```
subset = [3, 34, 4, 12, 5, 2]
target = 9

subset = [3, 4, 2]
target = 9
```

**Code:**

```python
def subset_sum(numbers, target):
    def backtrack(start, path, target):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(numbers)):
            backtrack(i + 1, path + [numbers[i]], target - numbers[i])

    result = []
    backtrack(0, [], target)
    return result

print(subset_sum([3, 34, 4, 12, 5, 2], 9))
```

## **Branch-and-Bound**

Branch-and-bound is a technique used to prune branches that cannot lead to a solution.

### Key Concepts:

- **Pruning**: Removing branches that cannot lead to a solution.
- **Bound**: An upper or lower limit on the value of the solution.

### Problem: Knapsack Problem

Given a set of items, each with a weight and value, determine the subset of items to include in a knapsack of limited capacity.

**Example:**

```
items = [(2, 6), (2, 3), (6, 5), (5, 4), (4, 6)]
capacity = 10

items = [(2, 6), (2, 3), (6, 5), (4, 6)]
capacity = 10
```

**Code:**

```python
def knapsack(items, capacity):
    def backtrack(start, weight, value, path):
        if weight > capacity:
            return
        if value > 0:
            result.append((path, value))
        for i in range(start, len(items)):
            backtrack(i + 1, weight + items[i][0], value + items[i][1], path + [items[i]])

    result = []
    backtrack(0, 0, 0, [])
    return result

print(knapsack([(2, 6), (2, 3), (6, 5), (5, 4), (4, 6)], 10))
```

## **Approximation**

Approximation algorithms are designed to find a near-optimal solution in a reasonable amount of time.

### Key Concepts:

- **Approximation ratio**: A measure of the ratio between the approximation and the optimal solution.
- **Greedy algorithm**: A simple algorithm that makes the locally optimal choice at each step.

### Problem: 0/1 Knapsack Problem

Given a set of items, each with a weight and value, determine the subset of items to include in a knapsack of limited capacity.

**Example:**

```
items = [(2, 6), (2, 3), (6, 5), (5, 4), (4, 6)]
capacity = 10

items = [(2, 6), (2, 3), (6, 5), (4, 6)]
capacity = 10
```

**Code:**

```python
def approximation_knapsack(items, capacity):
    def greedy_algorithm(items, capacity):
        items.sort(key=lambda x: x[1] / x[0], reverse=True)
        result = []
        for item in items:
            if capacity >= item[0]:
                capacity -= item[0]
                result.append(item)
        return result

    return greedy_algorithm(items, capacity)

print(approximation_knapsack([(2, 6), (2, 3), (6, 5), (5, 4), (4, 6)], 10))
```

## **Conclusion**

In this section, we explored three techniques to cope with limitations of algorithmic power: Backtracking, Branch-and-Bound, and Approximation. These techniques can be used to solve a wide range of problems, from the n-Queens problem to the Knapsack problem. By understanding these techniques, you can develop more efficient algorithms and solve complex problems in computer science.
