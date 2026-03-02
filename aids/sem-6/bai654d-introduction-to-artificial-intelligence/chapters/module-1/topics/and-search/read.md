# Informed Search and Heuristics

## Introduction to Informed Search

Informed search algorithms, also known as heuristic search algorithms, are problem-solving methods that use domain-specific knowledge to guide the search process more efficiently than uninformed search strategies. Unlike blind search algorithms (like Breadth-First Search or Depth-First Search) that explore all possibilities without any additional information, informed search algorithms utilize heuristic functions to estimate which paths are most promising.

The key advantage of informed search is that it can significantly reduce the search space and find solutions more quickly, especially for complex problems where the state space is large.

## Heuristic Functions

A heuristic function, denoted as h(n), is a function that estimates the cost from the current state n to the goal state. It provides an educated guess about how close a state is to the solution.

**Properties of good heuristics:**
- **Admissible**: Never overestimates the true cost to reach the goal
- **Consistent/Monotonic**: For every node n and every successor n' of n, the estimated cost of reaching the goal from n is no greater than the step cost of getting to n' plus the estimated cost from n' to the goal: h(n) ≤ c(n, a, n') + h(n')

## Best-First Search

Best-First Search is a general approach that expands the node that appears most promising based on an evaluation function f(n). The algorithm uses a priority queue to select nodes for expansion.

```
OPEN = priority queue containing initial state
CLOSED = empty set

while OPEN is not empty:
    n = remove node with lowest f(n) from OPEN
    if n is goal state: return solution
    add n to CLOSED
    for each successor n' of n:
        if n' not in OPEN or CLOSED:
            add n' to OPEN with f(n') value
        else if better path to n' found:
            update f(n') value in OPEN
```

## Greedy Best-First Search

Greedy Best-First Search uses the heuristic function alone as its evaluation function: f(n) = h(n). It always expands the node that appears closest to the goal.

**Example: Route Finding**
```
Cities: A, B, C, D (Goal: D)
Heuristic: Straight-line distance to D

A --100km-- B --50km-- D
  \         |
   \        |
    \120km  |80km
     \      |
      C --60km-- D

From A: h(B) = 150km, h(C) = 180km
Expands B first, then D (goal found)
```

**Limitations:** Can get stuck in local minima and may not find the optimal solution.

## A* Search Algorithm

A* Search is the most popular informed search algorithm that combines the actual cost from the start (g(n)) with the heuristic estimate to the goal (h(n)): f(n) = g(n) + h(n)

```
Algorithm A* Search:
OPEN = priority queue with initial state (f(n) = g(n) + h(n))
CLOSED = empty set

while OPEN is not empty:
    n = remove node with smallest f(n) from OPEN
    if n is goal: return solution
    add n to CLOSED
    for each successor n' of n:
        g(n') = g(n) + cost(n, n')
        f(n') = g(n') + h(n')
        if n' not in OPEN or CLOSED:
            add n' to OPEN
        else if n' in OPEN with higher g(n'):
            update f(n') in OPEN
```

**Example: Pathfinding with A***
```
Grid: S (Start), obstacles, G (Goal)
Heuristic: Manhattan distance

S . . . .
. X X . .
. . . . G

Path: S → right → right → down → down → right → right → G
```

## Admissibility and Optimality of A*

**Theorem:** If h(n) is admissible, then A* is guaranteed to find an optimal solution.

**Proof sketch:** Since h(n) never overestimates the true cost, the algorithm will never overlook a potentially better path while exploring other options.

## Memory-Bounded Search Algorithms

For large problems, A* might require too much memory. Several variants address this:

**1. Iterative Deepening A* (IDA*)**
- Uses depth-first search with increasing f-limit
- Memory efficient but may re-explore nodes

**2. Recursive Best-First Search (RBFS)**
- Keeps track of the f-value of the best alternative path
- More efficient than IDA* but still recursive

**3. Memory-Bounded A* (MA*) and Simplified MA* (SMA*)**
- Use all available memory
- When memory is full, discard worst nodes

## Heuristic Quality and Dominance

The effectiveness of A* search depends heavily on the quality of the heuristic function.

**Definition:** Heuristic h₂ dominates h₁ if h₂(n) ≥ h₁(n) for all n, and both are admissible.

**Example: 8-Puzzle Heuristics**
- h₁: Number of misplaced tiles
- h₂: Manhattan distance (sum of distances of tiles from goal positions)

h₂ dominates h₁ since Manhattan distance is always ≥ number of misplaced tiles.

## Creating Effective Heuristics

**1. Relaxed Problems:** Remove constraints to create easier problems
- 8-Puzzle: Allow tiles to move anywhere (h₁) or allow tiles to move through others (h₂)

**2. Subproblem Abstraction:** Solve smaller subproblems
- Pattern databases for sliding puzzles

**3. Learning Heuristics:** Use machine learning to develop effective heuristics

## Comparison of Search Algorithms

| Algorithm | Complete? | Optimal? | Time Complexity | Space Complexity | Uses Heuristic? |
|-----------|-----------|----------|-----------------|------------------|-----------------|
| Breadth-First | Yes | Yes | O(b^d) | O(b^d) | No |
| Depth-First | No | No | O(b^m) | O(bm) | No |
| Uniform-Cost | Yes | Yes | O(b^(C*/ε)) | O(b^(C*/ε)) | No |
| Greedy BF | No | No | O(b^m) | O(b^m) | Yes |
| A* | Yes | Yes | Exponential | Exponential | Yes |
| IDA* | Yes | Yes | Exponential | O(bd) | Yes |

Where:
- b: branching factor
- d: depth of solution
- m: maximum depth
- C*: cost of optimal solution
- ε: minimum step cost

## Real-World Applications

**1. Pathfinding and Navigation**
- GPS systems use A* for route planning
- Video game AI for character movement

**2. Robotics**
- Motion planning around obstacles
- Manipulator arm trajectory planning

**3. Natural Language Processing**
- Parsing with heuristic estimates of grammatical correctness

**4. Puzzle Solving**
- 15-puzzle, Rubik's cube solutions
- Theorem proving with heuristic guidance

## Exam Tips

1. **Remember the key formulas:** f(n) = g(n) + h(n) for A*, and understand what each component represents
2. **Identify admissible heuristics:** Always check if h(n) ≤ h*(n) for all n
3. **Compare algorithms:** Be prepared to explain differences between informed and uninformed search
4. **Draw search trees:** Practice drawing and explaining search trees for A* and other algorithms
5. **Understand optimality conditions:** A* is optimal only with admissible heuristics
6. **Recognize memory issues:** Know the tradeoffs between memory usage and completeness/optimality
7. **Apply to problems:** Be ready to suggest appropriate heuristics for given problem domains