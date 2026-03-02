# Heuristic Functions in Artificial Intelligence

## Introduction

Heuristic functions are fundamental components of informed search algorithms in Artificial Intelligence. A heuristic function, denoted as h(n), estimates the cost from a given state n to the goal state. Unlike (blind search) algorithms that explore all possible states uniformly, heuristic-guided searches use domain-specific knowledge to prioritize states that appear more promising, significantly reducing the search space and computational complexity.

In the context of 's Artificial Intelligence syllabus, understanding heuristic functions is crucial because they form the backbone of popular algorithms like A\* Search and Greedy Best-First Search. These algorithms are extensively used in pathfinding, puzzle solving, game playing, and robotics. The quality of a heuristic function directly determines the efficiency of the search algorithm - a good heuristic can find solutions quickly, while a poor one may lead to exponential time complexity.

Heuristic functions bridge the gap between pure algorithmic approaches and intelligent problem-solving by incorporating human-like reasoning about problem structure. This module explores various types of heuristics, their properties, and how to design effective heuristic functions for different problem domains.

## Key Concepts

### Definition of Heuristic Function

A heuristic function h(n) takes a node n (representing a state in the search space) and returns an estimated cost of the cheapest path from n to a goal state. The heuristic provides "educated guesses" about which states are closer to the goal, guiding the search in the most promising direction.

**Properties of Heuristic Functions:**

1. **Admissible Heuristic:** A heuristic h(n) is admissible if it never overestimates the actual cost to reach the goal. Formally, for all nodes n: h(n) ≤ h*(n), where h*(n) is the true optimal cost. Admissible heuristics guarantee that A\* search finds an optimal solution.

2. **Consistent (Monotonic) Heuristic:** A heuristic is consistent if for every node n and every successor n' generated from n: h(n) ≤ c(n, a, n') + h(n'), where c(n, a, n') is the cost of moving from n to n'. Consistency ensures that the f-value along any path is non-decreasing.

### Heuristic Evaluation Function

The heuristic evaluation function f(n) combines the cost so far g(n) with the heuristic estimate h(n):

**f(n) = g(n) + h(n)**

Where:

- **g(n):** The cost from the start node to node n (actual cost incurred)
- **h(n):** The estimated cost from node n to the goal (heuristic estimate)
- **f(n):** The estimated total cost of the solution through node n

This evaluation function is used by A\* search to prioritize node expansion.

### Types of Heuristic Functions

1. **Trivial Heuristic (h₁ = 0):** Returns zero for all nodes. Converts A\* into uniform-cost search, guaranteeing optimality but losing informed guidance.

2. **Manhattan Distance:** Used for grid-based problems. Calculates the sum of absolute differences in x and y coordinates. Admissible for 4-directional movement.

3. **Euclidean Distance:** Straight-line distance between two points. Calculated as √((x₁-x₂)² + (y₁-y₂)²). Always admissible.

4. **Tile Count (for sliding puzzles):** Counts the number of misplaced tiles. Admissible as each tile must move at least once.

5. **Gaschnig's Heuristic:** Counts the number of tiles not in their goal position that need to be moved. More accurate than simple tile count.

### Heuristic Dominance

If heuristic h₁ dominates h₂ (i.e., h₁(n) ≥ h₂(n) for all n and h₁ is admissible), then h₁ will expand no more nodes than h₂ in A\* search. This property allows us to compare heuristics and choose the strongest one available.

### Design of Heuristic Functions

**Methods for deriving heuristics:**

1. **Relaxed Problems:** Create a simplified version of the problem where some constraints are removed. The optimal solution cost in the relaxed problem serves as an admissible heuristic for the original problem.

2. **Pattern Database:** Precompute exact costs for subproblems and use these as heuristics.

3. **Learning from Experience:** Use machine learning to estimate costs based on previous problem instances.

## Examples

### Example 1: 8-Puzzle Problem

**Problem:** Given a 3×3 grid with 8 numbered tiles and one empty space, reach the goal state.

**State representation:** Array of 9 elements representing tile positions.

**Goal state:** [1, 2, 3, 4, 5, 6, 7, 8, 0] where 0 represents empty.

**Heuristic h₁ (Misplaced Tiles):** Count tiles not in goal position.

For state [1, 2, 3, 4, 5, 6, 0, 7, 8]:

- Tiles at positions 1,2,3,4,5,6 are correct
- Tiles 7 and 8 are in wrong positions
- h₁ = 2

**Heuristic h₂ (Manhattan Distance):** Sum of distances each tile is from its goal position.

For the same state:

- Tile 7 at position 7 (index 6): Goal position 7 → distance |6-7| + |1-2| = 1 + 1 = 2
- Tile 8 at position 8 (index 7): Goal position 8 → distance |7-8| + |1-2| = 1 + 1 = 2
- h₂ = 4

The Manhattan distance heuristic dominates the misplaced tiles heuristic because it provides a tighter estimate.

### Example 2: A\* Search on Grid Pathfinding

**Problem:** Find shortest path from start (0,0) to goal (3,3) in a 4×4 grid with obstacles.

**Grid:**

```
S . X .
. . X .
. . . .
X . . G
S=Start, G=Goal, X=Obstacle, .=Open
```

**Movement:** 4-directional (up, down, left, right) with cost 1 per move.

**Step-by-step A\* execution:**

1. Start node (0,0): g=0, h=Manhattan to (3,3) = 6, f=6
2. Expand (0,0): explore (1,0), (0,1)
3. Continue until goal (3,3) is reached with optimal path

**Heuristic computation for node (1,1):**

- g(n) = 2 (two moves from start: (0,0)→(0,1)→(1,1))
- h(n) = |3-1| + |3-1| = 4 (Manhattan distance)
- f(n) = 2 + 4 = 6

### Example 3: Comparing Heuristics for 8-Puzzle

**Given state:** [2, 1, 6, 4, 0, 5, 7, 3, 8]
**Goal state:** [1, 2, 3, 4, 5, 6, 7, 8, 0]

**h₁ (Misplaced tiles):**

- Position 0: 2≠1 → wrong
- Position 1: 1≠2 → wrong
- Position 2: 6≠3 → wrong
- Position 3: 4≠4 → correct
- Position 4: 0≠5 → wrong
- Position 5: 5≠6 → wrong
- Position 6: 7≠7 → correct
- Position 7: 3≠8 → wrong
- Position 8: 8≠0 → wrong
- h₁ = 7 misplaced tiles

**h₂ (Manhattan distance):**
Calculate position differences for each tile:

- Tile 1: position 1 → goal 0: |0-0| + |1-0| = 1
- Tile 2: position 0 → goal 1: |0-0| + |0-1| = 1
- Tile 3: position 7 → goal 8: |2-2| + |1-2| = 1
- Tile 5: position 5 → goal 5: |1-1| + |2-1| = 1
- Tile 6: position 2 → goal 4: |0-1| + |2-1| = 2
- Tile 7: position 6 → goal 6: |2-2| + |0-2| = 2
- Tile 8: position 8 → goal 7: |2-2| + |2-1| = 1
- h₂ = 1+1+1+1+2+2+1 = 9

Since h₂ = 9 > h₁ = 7, Manhattan distance is a stronger heuristic and will explore fewer nodes.

## Exam Tips

1. **Remember the f(n) formula:** f(n) = g(n) + h(n). This is the most frequently tested concept in exams.

2. **Admissible vs Consistent:** Know that all consistent heuristics are admissible, but not vice versa. Be able to prove consistency using the triangle inequality.

3. **Heuristic dominance:** If h₁(n) ≥ h₂(n) for all n, then h₁ dominates h₂ and will expand fewer or equal nodes.

4. **Zero heuristic effect:** When h(n) = 0 for all nodes, A\* becomes uniform-cost search (equivalent to Dijkstra's algorithm).

5. **Optimality condition:** A\* with an admissible heuristic is guaranteed to find an optimal solution. This is a critical theorem to remember.

6. **Relaxed problems:** Remember that admissible heuristics can be derived by solving relaxed versions of the problem where constraints are removed.

7. **Time complexity:** A\* with a good heuristic has O(b^d) complexity where b is branching factor and d is solution depth, much better than uniform-cost search's exponential complexity.

8. **Space complexity:** A\* maintains all generated nodes in memory, so space complexity is O(b^d). This can be a limitation for large problems.

9. **Monotonicity check:** To verify consistency, always check if h(n) ≤ cost(n,n') + h(n') for all transitions.

10. **Common heuristics:** Know that Manhattan distance is admissible for 4-directional movement, while diagonal distance is for 8-directional movement.
