# 0/1 Knapsack with Branch and Bound

## Introduction

The **0/1 Knapsack Problem** is a classic optimization problem in computer science. Given a set of items, each with a weight and a value, the goal is to determine the most valuable combination of items that can fit into a knapsack of fixed capacity without exceeding its weight limit. The "0/1" designation means that each item is either entirely included or not included—no fractional items are allowed.

While Dynamic Programming provides an efficient solution for the 0/1 Knapsack problem with pseudo-polynomial time complexity O(nW), it can be inefficient when the knapsack capacity (W) is large. **Branch and Bound** offers an alternative approach that can be more efficient in many practical scenarios, especially for large capacity values, by systematically exploring the solution space and pruning branches that cannot lead to an optimal solution.

## Understanding Branch and Bound

**Branch and Bound** is a state-space search algorithm that explores candidate solutions systematically. It consists of two main operations:

1. **Branching**: Dividing the problem into smaller subproblems.
2. **Bounding**: Calculating an upper bound for the best possible solution in each branch and pruning branches that cannot yield a better solution than the best one found so far.

```
+---------------------+
| Initial Problem     |
+---------------------+
         |
         | Branch
         v
+---------------------+    +---------------------+
| Subproblem 1        |    | Subproblem 2        |
| (Include Item)      |    | (Exclude Item)      |
+---------------------+    +---------------------+
         |                           |
         | Bound                     | Bound
         v                           v
+---------------------+    +---------------------+
| Prune if bound <    |    | Prune if bound <    |
| current best        |    | current best        |
+---------------------+    +---------------------+
```

## Key Concepts for 0/1 Knapsack with B&B

### 1. Problem Representation

Each node in the state space tree represents a decision made about an item: either including it or excluding it. The root node represents no decisions made. As we traverse down the tree, we make decisions about each item sequentially.

### 2. Bounding Function

The critical component of Branch and Bound is the bounding function, which provides an estimate of the best possible solution achievable from a given node. For the 0/1 Knapsack problem, we typically use a relaxation of the problem where fractional items are allowed (similar to the Fractional Knapsack problem).

**Upper Bound Calculation:**

1. Sort items by value-to-weight ratio in descending order
2. For a given node, items already decided (included/excluded) contribute fixed value/weight
3. For remaining items, add them fractionally until knapsack is full

```
Upper Bound = (Value of fixed items) +
              (Fractional value of remaining capacity filled with best remaining items)
```

### 3. State Space Tree

```
                        Root (No decisions)
                             /\
                            /  \
                           /    \
                      Include   Exclude
                      Item 1    Item 1
                         /\        /\
                        /  \      /  \
                 Include   Excl Include Excl
                 Item 2    Item2 Item2 Item2
```

Each level represents a decision about a specific item. The tree has depth n (number of items).

## Implementation Steps

### Step 1: Preprocessing

1. Calculate value-to-weight ratio for each item
2. Sort items in descending order of value-to-weight ratio
3. Initialize global best value = 0

### Step 2: Node Representation

Each node should store:

- Level (current item index being considered)
- Current profit
- Current weight
- Upper bound

### Step 3: Algorithm

```python
def branch_and_bound_knapsack(items, capacity):
    # Sort items by value/weight ratio descending
    sorted_items = sorted(items, key=lambda x: x.value/x.weight, reverse=True)

    # Initialize queue with root node
    queue = PriorityQueue()  # Prioritized by upper bound (max priority)
    root = Node(level=-1, profit=0, weight=0)
    root.bound = calculate_bound(root, sorted_items, capacity)
    queue.put((-root.bound, root))  # Negative for max priority

    best_profit = 0

    while not queue.empty():
        _, current = queue.get()

        # If leaf node, update best
        if current.level == len(items)-1:
            continue

        # Consider including next item
        next_level = current.level + 1
        next_item = sorted_items[next_level]

        # Include next item
        if current.weight + next_item.weight <= capacity:
            include_node = Node(level=next_level,
                              profit=current.profit + next_item.value,
                              weight=current.weight + next_item.weight)
            include_node.bound = calculate_bound(include_node, sorted_items, capacity)

            if include_node.profit > best_profit:
                best_profit = include_node.profit

            if include_node.bound > best_profit:
                queue.put((-include_node.bound, include_node))

        # Exclude next item
        exclude_node = Node(level=next_level,
                          profit=current.profit,
                          weight=current.weight)
        exclude_node.bound = calculate_bound(exclude_node, sorted_items, capacity)

        if exclude_node.bound > best_profit:
            queue.put((-exclude_node.bound, exclude_node))

    return best_profit
```

### Step 4: Bound Calculation Function

```python
def calculate_bound(node, sorted_items, capacity):
    if node.weight >= capacity:
        return 0

    bound = node.profit
    remaining_capacity = capacity - node.weight
    next_level = node.level + 1

    # Add items fractionally until capacity is filled
    while next_level < len(sorted_items) and sorted_items[next_level].weight <= remaining_capacity:
        bound += sorted_items[next_level].value
        remaining_capacity -= sorted_items[next_level].weight
        next_level += 1

    # Add fraction of next item if capacity remains
    if next_level < len(sorted_items):
        bound += remaining_capacity * (sorted_items[next_level].value / sorted_items[next_level].weight)

    return bound
```

## Example Walkthrough

Let's solve a concrete example with 4 items and capacity W = 10:

| Item | Value | Weight | Value/Weight |
| ---- | ----- | ------ | ------------ |
| 1    | 40    | 2      | 20.0         |
| 2    | 30    | 5      | 6.0          |
| 3    | 50    | 10     | 5.0          |
| 4    | 10    | 5      | 2.0          |

**Sorted by value/weight ratio:** Items 1, 2, 3, 4

**Root Node (Level -1):**

- Profit = 0, Weight = 0
- Bound = 0 + (40) + (30) + fraction of item 3 (10-2-5=3 → 3\*5=15) = 85

**Include Item 1 (Level 0):**

- Profit = 40, Weight = 2
- Bound = 40 + (30) + fraction of item 3 (10-2-5=3 → 3\*5=15) = 85

**Exclude Item 1 (Level 0):**

- Profit = 0, Weight = 0
- Bound = 0 + (30) + (50) = 80 (but weight 5+10=15 > 10, so actually: 0 + 30 + fraction of item 3 (5) = 35)

The algorithm continues exploring nodes with the best bounds first, eventually finding the optimal solution.

## Comparison with Other Approaches

| Method              | Time Complexity        | Space Complexity  | Advantages                          | Disadvantages             |
| ------------------- | ---------------------- | ----------------- | ----------------------------------- | ------------------------- |
| Dynamic Programming | O(nW)                  | O(nW)             | Guaranteed optimal, straightforward | Inefficient for large W   |
| Greedy (Fractional) | O(n log n)             | O(1)              | Very fast                           | Not optimal for 0/1       |
| Branch and Bound    | Exponential worst-case | O(2^n) worst-case | Often prunes large portions         | Implementation complexity |
| Backtracking        | O(2^n)                 | O(n)              | Simple to implement                 | No pruning, inefficient   |

## Optimization Techniques

1. **Best-First Search**: Always expand the node with the best upper bound
2. **Depth-First Search with Bounding**: Can use less memory
3. **Initial Solution**: Use greedy solution as initial best to prune more
4. **Dominance Rules**: Prune nodes that are dominated by others

## Real-World Applications

- Resource allocation in project management
- Portfolio optimization in finance
- Cutting stock problems in manufacturing
- Resource-constrained scheduling

## Exam Tips

1. **Understand the Bound Calculation**: Be able to compute upper bounds manually for given problem instances
2. **Trace the Algorithm**: Practice tracing through small examples to understand node expansion and pruning
3. **Compare Approaches**: Be prepared to compare B&B with DP and greedy approaches
4. **Implementation Details**: Know how to implement the priority queue and node representation
5. **Worst-case Complexity**: Remember that worst-case is still exponential, but practical performance is often much better
6. **Pruning Conditions**: Understand when and why branches get pruned

**Common Mistakes to Avoid:**

- Forgetting to sort items by value/weight ratio
- Incorrect bound calculation (especially fractional part)
- Not updating the best solution properly
- Using wrong priority queue ordering (should be max priority by bound)
