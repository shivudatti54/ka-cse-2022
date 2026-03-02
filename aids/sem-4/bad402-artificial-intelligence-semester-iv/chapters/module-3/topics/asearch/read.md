# A* Search

## Introduction

A* Search represents one of the most significant advances in artificial intelligence and automated problem-solving. Developed by Peter Hart, Nils Nilsson, and Bertram Raphael in 1968, this algorithm revolutionized the field of pathfinding and graph traversal by combining the strengths of two fundamental search approaches: Dijkstra's algorithm and Greedy Best-First Search. The elegance of A* lies in its theoretical guarantees—when properly implemented with a suitable heuristic function, it finds the optimal solution while exploring the minimum possible portion of the search space.

In the context of informed search strategies, A* occupies a central position because it provides a principled way to balance between exploring nodes that are close to the start (like Dijkstra's algorithm) and nodes that appear promising based on a heuristic estimate (like Greedy Best-First Search). This balance is achieved through the use of an evaluation function that considers both the actual cost incurred so far and the estimated cost to the goal. For students studying artificial intelligence at the University of Delhi, understanding A* Search is essential because it forms the foundation for many real-world applications including robotics navigation, video game character movement, network routing, and puzzle solving. The algorithm's mathematical properties, particularly its optimality conditions, make it a cornerstone topic in AI education and a frequent subject in competitive examinations.

## Key Concepts

### The Evaluation Function

The core of A* Search is its evaluation function, denoted as f(n), which estimates the total cost of path through any node n. The function is defined as:

f(n) = g(n) + h(n)

where g(n) represents the actual cost from the start node to node n—this is the path cost that the algorithm accumulates as it explores, making it a true measurement of what has been spent. The component h(n) is the heuristic function that estimates the minimum cost from node n to a goal state—this is a guess, based on problem-specific knowledge, about what remains to be done. The sum f(n) therefore represents the estimated total cost of the solution path that goes through node n. The algorithm always expands the node with the lowest f(n) value, prioritizing nodes that appear to lead to optimal solutions.

### Heuristic Functions

The heuristic function h(n) is the knowledge component that distinguishes A* from blind search algorithms. It must be designed based on understanding of the specific problem domain. Common heuristic functions include:

- Manhattan Distance: Used in grid-based problems, it sums the absolute differences in x and y coordinates between the current state and goal. For a robot moving on a grid with four-directional movement, this provides an admissible heuristic because the robot cannot move diagonally.

- Euclidean Distance: The straight-line distance between two points, computed as the square root of sum of squared coordinate differences. This is admissible because the straight line is always the shortest path.

- Number of Misplaced Tiles: Used in the 8-puzzle problem, this counts how many tiles are not in their goal positions. It is admissible because each misplaced tile must move at least once.

- Sum of Distances: Also used in sliding tile puzzles, this sums the Manhattan distance for each tile from its goal position, providing a tighter estimate than simply counting misplaced tiles.

### Admissibility

A heuristic function h(n) is called ADMISSIBLE if it never overestimates the true cost from node n to any goal state. Formally, h(n) ≤ h*(n) for all nodes n, where h*(n) is the true minimum cost from n to a goal. An admissible heuristic is optimistic—it may underestimate but never overestimate, ensuring that the estimated cost is never too high. This property is crucial for A* because it guarantees that f(n) = g(n) + h(n) never exceeds the true cost of any solution path passing through n. When h is admissible, A* is guaranteed to find an optimal solution.

### Consistency (Monotonicity)

A heuristic function is CONSISTENT or MONOTONE if for every node n and every successor n' generated from n by an action, the estimated cost from n to goal never exceeds the cost from n to n' plus the estimated cost from n' to goal. Mathematically: h(n) ≤ c(n, a, n') + h(n'). This property ensures that when A* expands a node, it has found the optimal path to that node—there is no need to reconsider previously expanded nodes. Consistency implies admissibility, and when the heuristic is consistent, A* can implement an efficient graph-search version that never re-expands nodes.

### Optimality Proof

The optimality of A* with an admissible heuristic rests on a key lemma: A* never expands a node with f(n) greater than the optimal solution cost C*. Assume the optimal solution has cost C*. When A* selects a node n from the priority queue for expansion, we have f(n) ≤ f(any node in queue). If h is admissible, then for the goal node on an optimal solution path, f(goal) = g(goal) + h(goal) = g(goal) + 0 = C*. Therefore, any node with f(n) > C* cannot be on an optimal solution path, and A* will always expand nodes in non-decreasing order of f(n), finding an optimal goal before considering suboptimal paths.

### Complete and Space Complexity

A* is COMPLETE—it will find a solution if one exists, assuming branching factor is finite and all costs are positive. The TIME COMPLEXITY of A* depends on the heuristic quality: in the worst case with a poor heuristic, it is exponential, O(b^d), where b is branching factor and d is solution depth. With a perfect heuristic, complexity becomes linear O(d). The SPACE COMPLEXITY is the most significant drawback of A*: it stores all generated nodes in memory, making it O(b^d) in the worst case. This limits A*'s applicability in large state spaces where memory becomes a bottleneck.

### Graph Search vs Tree Search

In the tree-search version of A*, each node may be generated multiple times along different paths. The graph-search version maintains a closed set (also called explored set) of expanded nodes to avoid re-expansion. When a node is generated that already exists in the closed set with a lower g(n) value, it is discarded. When using a consistent heuristic, the graph-search version never needs to re-add nodes to the priority queue because the first path found to any node is always optimal.

## Examples

### Example 1: 8-Puzzle Problem

Consider the 8-puzzle with the following configuration:

Initial State:
[2, 8, 3]
[1, 6, 4]
[7, 5, 0]

Goal State:
[1, 2, 3]
[8, 0, 4]
[7, 6, 5]

Using the Manhattan Distance heuristic (sum of distances of each tile from its goal position):

Step 1: Calculate f for initial state
- g(initial) = 0 (starting point)
- h(initial) = Manhattan distance: tile 1 is at position (1,0) goal (2,0) = 1, tile 2 at (0,0) goal (0,0) = 0, tile 3 at (0,1) goal (0,1) = 0, tile 4 at (0,2) goal (1,2) = 1, tile 5 at (1,2) goal (2,2) = 1, tile 6 at (1,1) goal (1,1) = 0, tile 7 at (2,0) goal (2,0) = 0, tile 8 at (0,0) goal (0,1) = 1
- Total h = 4
- f = 0 + 4 = 4

Step 2: Generate successors and calculate their f-values. For each move (sliding the blank), compute new g (incremented by 1) and new h.

Step 3: Continue expanding nodes in order of lowest f-value until the goal state is reached with f = g (since h = 0 at goal).

### Example 2: Route Finding on a Grid

Consider a 4x4 grid with start at (0,0) and goal at (3,3). Movement is allowed in four directions with cost 1 per move. Using Manhattan distance heuristic:

Initial node (0,0): g=0, h=|3-0|+|3-0|=6, f=6
First expansion chooses between (1,0) and (0,1), both with f=1+5=6.

As A* expands nodes, it prioritizes those that minimize f(n). The algorithm will explore in a diamond pattern, expanding nodes in order: f=6, f=7, f=8, until reaching goal with f=10 (the optimal path length).

### Example 3: Demonstrating Admissibility

Suppose we have a problem where the true cost to goal from node A is 10. An admissible heuristic must satisfy h(A) ≤ 10. Consider three heuristics:

h1(A) = 8: ADMISSIBLE (8 ≤ 10)
h2(A) = 10: ADMISSIBLE (10 ≤ 10)  
h3(A) = 12: NOT ADMISSIBLE (12 > 10)

If we use h3, A* might miss the optimal solution because it overestimates remaining cost, causing it to prefer apparently cheaper paths that actually lead to suboptimal solutions.

## Exam Tips

1. MEMORIZE THE A* FORMULA: f(n) = g(n) + h(n). This is the most fundamental concept—g(n) is actual cost from start, h(n) is heuristic estimate to goal.

2. DISTINGUISH ADMISSIBILITY FROM CONSISTENCY: Admissible means h(n) never overestimates (h(n) ≤ h*(n)). Consistent means h(n) ≤ cost(n to n') + h(n'). All consistent heuristics are admissible, but not vice versa.

3. KNOW WHY A* IS OPTIMAL: When h is admissible, f(n) never overestimates true solution cost through n, so expanding nodes in order of f ensures optimal solution is found first.

4. REMEMBER SPACE COMPLEXITY: A* has exponential space complexity O(b^d), making memory its primary limitation. This is why IDA* (Iterative Deepening A*) was developed.

5. UNDERSTAND THE DOMINANCE RELATION: If heuristic h1(n) ≥ h2(n) for all n, then h1 dominates h2 and will lead to fewer node expansions. Better heuristics explore less of the search space.

6. KNOW THE GRAPH-SEARCH VERSION: Use a CLOSED SET to avoid re-expanding nodes. With consistent heuristics, each node is expanded exactly once.

7. RECOGNIZE WHEN A* FAILS: When the heuristic is not admissible (overestimates), A* may find suboptimal solutions. When heuristic is not consistent, re-expansion may be needed.

8. PRACTICE CALCULATING MANHATTAN DISTANCE: This is the most common heuristic in exam questions. Sum horizontal plus vertical distances for each tile or position.