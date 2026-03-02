# Searching for Solutions in Artificial Intelligence

## Introduction

Search is a fundamental problem-solving technique in Artificial Intelligence that involves exploring a space of possible states to find a path from an initial state to a goal state. When an AI agent encounters a problem where the solution is not immediately apparent, it must systematically explore possible alternatives through search. This approach is essential because many real-world problems do not have direct algorithmic solutions and require the agent to "search" through possibilities.

The importance of search in AI cannot be overstated. From route finding in navigation systems to game playing, from puzzle solving to automated planning, search algorithms form the backbone of many intelligent systems. Understanding search techniques allows AI systems to make decisions in complex, uncertain environments where exhaustive enumeration of all possibilities is computationally infeasible. The study of search algorithms provides the foundation for understanding more advanced AI topics like machine learning, natural language processing, and computer vision.

This module introduces the fundamental concepts of problem-solving through search, covering both uninformed (blind) search strategies and informed (heuristic) search strategies. We will examine how AI systems represent problems, how they explore the solution space, and how they determine when a solution has been found. The techniques learned here are applicable across a wide range of AI applications and provide the conceptual foundation for more sophisticated intelligent systems.

## Key Concepts

### Problem Formulation

Before any search can begin, an AI system must first formulate the problem precisely. Problem formulation involves defining four essential components:

1. **Initial State**: The starting state from which the search begins. This represents where the agent currently is in the problem space.

2. **Goal State**: The target state or states that the agent is trying to reach. This defines what constitutes a solution to the problem.

3. **Successor Function**: A description of what actions are available from each state and what new states those actions lead to. This is often represented as a function that returns a set of (action, result) pairs.

4. **Path Cost**: A function that assigns a numerical cost to each path in the search tree. The cost is used to evaluate different solutions and find the optimal one.

For example, in the 8-puzzle problem, the initial state is any scrambled configuration of the 8 numbered tiles, the goal state is the ordered arrangement [1,2,3,4,5,6,7,8,blank], the successor function involves sliding tiles into the blank space, and the path cost might simply be the number of moves made.

### Search Space and Search Tree

The **search space** is the set of all states reachable from the initial state through any sequence of actions. It can be visualized as a graph where nodes represent states and edges represent actions that lead from one state to another.

The **search tree** is a tree structure that represents the exploration process. The root of the tree is the initial state, and each node represents a state that has been reached. The children of a node are the successors of that state. A path from the root to any node represents a sequence of actions taken to reach that state.

The branching factor is a critical characteristic of search problems. It represents the average number of successors from any given state. Problems with high branching factors are more challenging because the search tree grows exponentially.

### Uninformed Search Strategies

Uninformed search strategies (also called blind search) explore the search space without any additional information about which states are more promising than others. These strategies only know how to generate successors and test for goal states.

**Breadth-First Search (BFS)** expands the shallowest unexpanded node first. This guarantees finding the shortest-path solution when all edges have equal cost. BFS uses a FIFO queue to manage the frontier. The time and space complexity is O(b^d) where b is the branching factor and d is the depth of the solution. BFS is complete (finds a solution if one exists) and optimal when all step costs are equal.

**Depth-First Search (DFS)** expands the deepest unexpanded node first. DFS uses a LIFO stack for the frontier. The time complexity is O(b^m) where m is the maximum depth of the search tree. DFS is not complete in infinite state spaces (it can get lost in deep paths) and is not optimal. However, DFS requires less memory than BFS since it only stores a single path.

**Uniform Cost Search (UCS)** expands the node with the lowest path cost. It is a generalization of BFS that works with different path costs. UCS is complete and optimal. It uses a priority queue ordered by path cost.

### Informed Search Strategies

Informed search strategies use problem-specific knowledge (heuristics) to guide the search toward the goal more efficiently. A **heuristic function** h(n) estimates the cost from node n to the nearest goal state.

**Greedy Best-First Search** expands the node that appears to be closest to the goal. It uses h(n) to select the next node. Greedy search is not guaranteed to be complete or optimal but can be very fast when a good heuristic is available.

**A\* Search** combines the advantages of UCS and Greedy search by using both the path cost g(n) and the heuristic h(n). The evaluation function is f(n) = g(n) + h(n), where g(n) is the cost from the start to node n, and h(n) is the estimated cost from n to the goal. A\* is complete and optimal if the heuristic is admissible (never overestimates the true cost). A heuristic is consistent if for every node n and successor n', h(n) ≤ c(n,n') + h(n').

### Heuristic Functions

The quality of an informed search largely depends on the heuristic function. A good heuristic provides accurate estimates of the remaining cost while being computationally efficient to calculate.

For the 8-puzzle problem, two common heuristics are:

- **h1**: Count the number of tiles out of place (misplaced tiles heuristic)
- **h2**: Sum of Manhattan distances (total distance each tile is from its goal position)

The Manhattan distance heuristic is generally better because it provides more accurate estimates while still being admissible.

### Properties of Search Algorithms

Understanding the properties of search algorithms is crucial for selecting the appropriate algorithm for a given problem:

- **Completeness**: An algorithm is complete if it guarantees finding a solution if one exists.
- **Optimality**: An algorithm is optimal if it finds the best solution (lowest cost) when a solution exists.
- **Time Complexity**: The amount of time the algorithm takes, typically expressed in terms of the branching factor b and solution depth d.
- **Space Complexity**: The amount of memory the algorithm requires.

## Examples

### Example 1: BFS on a Simple Graph

Consider the following graph where S is the start state and G is the goal state:

```
S --- A --- G
| |
B --- C
```

All edges have cost 1. Using BFS:

1. Start: Queue = [S], Visited = {}
2. Expand S: Queue = [A, B], Visited = {S}
3. Expand A: Queue = [B, G], Visited = {S, A}
4. Expand B: Queue = [G, C], Visited = {S, A, B}
5. Expand G: Goal found! Path: S → A → G

The solution path is S-A-G with a cost of 2.

### Example 2: A\* Search on the 8-Puzzle

Initial state:

```
1 2 3
4 5 6
7 8 _
```

Goal state:

```
1 2 3
4 5 6
7 8 _
```

Using Manhattan distance heuristic (h2):

From the initial state (which is already solved), h(n) = 0 since all tiles are in their correct positions. The algorithm would immediately identify this as the goal state with f(n) = 0 + 0 = 0.

Consider a slightly scrambled state:

```
1 2 3
4 5 6
7 _ 8
```

The misplaced tile (8) is 1 position away from its goal. The heuristic h(8) = 1 (Manhattan distance). Since all other tiles are in place, h(n) = 1. With g(n) = 1 (one move made), f(n) = 2.

The successor states would be evaluated, and the one with lowest f(n) value would be expanded first.

### Example 3: Comparing Search Strategies

For a problem with branching factor b = 10 and solution depth d = 5:

- **BFS**: Time = 10^5 + 10^4 + ... + 10 + 1 ≈ 111,111 nodes
- **DFS**: May explore up to 10^5 nodes in worst case
- **A\* with good heuristic**: May explore significantly fewer nodes by focusing on promising paths

This example demonstrates why informed search is preferred when a good heuristic is available - it can find solutions with far less exploration than uninformed methods.

## Exam Tips

1. **Remember the four components of problem formulation**: Initial state, goal state, successor function, and path cost. These are frequently tested in exams.

2. **Know the difference between BFS and DFS**: BFS is complete, optimal for unit costs, and uses a queue (FIFO). DFS is not complete in infinite spaces, not optimal, uses a stack (LIFO), and has lower memory requirements.

3. **A\* Search optimality condition**: Remember that A\* is optimal only when the heuristic is admissible. An admissible heuristic never overestimates the true cost to the goal.

4. **Greedy vs A\***: Greedy focuses on reaching the goal quickly (using h(n) only), while A\* balances path cost and estimated remaining cost (using g(n) + h(n)).

5. **Heuristic properties**: Know the difference between admissible and consistent heuristics. Consistent heuristics are always admissible, but the reverse is not necessarily true.

6. **Time and space complexity**: Be prepared to write the Big-O notation for different search algorithms. BFS has O(b^d) time and space, while DFS has O(b^m) time but O(bm) space.

7. **When to use which algorithm**: BFS for shortest path with unit costs, UCS for weighted graphs with optimal solution, Greedy for fast (but possibly suboptimal) solutions, and A\* when you need optimal solutions with heuristic guidance.
