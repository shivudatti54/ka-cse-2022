# Problem Solving Agents

## Introduction

Problem solving is one of the fundamental aspects of Artificial Intelligence, representing the core mechanism through which intelligent systems can achieve goals in complex environments. A problem solving agent is an AI system that employs search techniques to find a sequence of actions that transforms an initial state into a desired goal state. This approach forms the backbone of many AI applications, from game playing to route planning and automated reasoning.

The study of problem solving agents is crucial for CSE students as it provides the foundational knowledge required to understand how AI systems can autonomously navigate complex decision spaces. Unlike simple reactive agents, problem solving agents operate by explicitly representing the problem environment, formulating goals, and systematically exploring possible action sequences to find optimal or near-optimal solutions. This module covers the theoretical framework and practical algorithms that enable agents to solve well-defined problems efficiently.

Understanding problem solving agents becomes increasingly important in modern computing, where applications range from puzzle solving (like the 8-puzzle or Rubik's cube) to complex scheduling problems, robotics path planning, and navigation systems. The techniques learned in this module serve as building blocks for more advanced AI topics such as planning, machine learning, and expert systems.

## Key Concepts

### 1. Problem Definition and Components

A well-defined problem in AI consists of five essential components that together specify what the agent needs to achieve:

- **Initial State**: The starting situation or condition from which the agent begins its search. This represents the current state of the environment that the agent perceives or is given.
- **Goal State**: The desired end condition that the agent aims to achieve. Goals can be either a specific state or a set of states satisfying a goal test.
- **State Space**: The complete set of all possible states that can be reached from the initial state through any sequence of legal actions. The state space defines the boundaries of the search.
- **Operators/Actions**: The set of possible moves or transformations that the agent can apply to change from one state to another. Each operator has preconditions (when it can be applied) and effects (how it changes the state).
- **Path Cost**: A numerical cost associated with each path taken from the initial state to the goal state. This allows the agent to compare different solutions based on efficiency.

### 2. Problem Formulation

Problem formulation involves carefully defining these five components to accurately represent the real-world problem as an AI-searchable problem. The quality of problem formulation directly impacts the success of the search algorithm. A well-formulated problem should capture all essential details while abstracting away irrelevant information to keep the state space manageable.

For example, in the 8-puzzle problem, the initial state is a 3×3 grid with tiles numbered 1-8 in random positions with one blank space. The goal state has all tiles arranged in order from 1-8 with the blank in the bottom-right corner. The operators are the four possible moves (up, down, left, right) that slide a tile into the blank space. The path cost can be simply the number of moves or the sum of Manhattan distances traveled by tiles.

### 3. Types of Search Strategies

Search strategies are classified based on how they explore the state space:

**Uninformed Search (Blind Search)**: These algorithms have no additional information about states beyond what is provided in the problem definition. They can only generate successors and distinguish goal states from non-goal states.

- **Breadth-First Search (BFS)**: Explores all nodes at depth d before moving to depth d+1. Guarantees finding the shallowest goal state and is complete for finite state spaces. Time and space complexity is O(b^d) where b is the branching factor.
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking. Has space complexity O(bm) where m is maximum depth. Not complete for infinite spaces but memory efficient.
- **Uniform-Cost Search**: Expands the node with the lowest path cost rather than depth. Guarantees optimal solution when all edge costs are non-negative.

**Informed Search (Heuristic Search)**: These algorithms use problem-specific knowledge (heuristics) to guide the search toward the goal more efficiently.

- **Greedy Best-First Search**: Expands the node that appears closest to the goal based on a heuristic function h(n). Not guaranteed to be optimal or complete.
- **A\* Search**: Combines uniform-cost search and greedy best-first search by evaluating nodes using f(n) = g(n) + h(n), where g(n) is the path cost and h(n) is the heuristic estimate to goal. A\* is complete and optimal if the heuristic is admissible.

### 4. Heuristic Functions

A heuristic function h(n) estimates the cost from node n to the nearest goal state. The quality of the heuristic directly determines the efficiency of informed search algorithms.

- **Admissible Heuristic**: Never overestimates the true cost. If h(n) is admissible, A\* finds an optimal solution.
- **Consistent/Monotonic Heuristic**: For every node n and successor n', the estimated cost from n to goal is no greater than the cost from n to n' plus the estimated cost from n' to goal. Consistent heuristics guarantee optimality with A\*.

Common heuristics for the 8-puzzle include the number of misplaced tiles (simple but not very informative) and the Manhattan distance (sum of distances of each tile from its goal position, which is admissible and more accurate).

### 5. Performance Metrics for Search Algorithms

When evaluating search algorithms, we consider four key criteria:

- **Completeness**: Does the algorithm always find a solution if one exists?
- **Optimality**: Does the algorithm find the best (lowest cost) solution?
- **Time Complexity**: How long does the search take in terms of nodes expanded?
- **Space Complexity**: How much memory is required during the search?

## Examples

### Example 1: 8-Puzzle Problem

**Problem**: Given a 3×3 grid with 8 numbered tiles and one blank space, find the sequence of moves to reach the goal state:

Initial State:

```
1 3 5
4 2 6
7 8 _
```

Goal State:

```
1 2 3
4 5 6
7 8 _
```

**Solution using BFS**:

Step 1: Identify the initial state and goal state

- Initial: Position with tiles 1,3,5 in row 1; 4,2,6 in row 2; 7,8,\_ in row 3
- Goal: All tiles in numerical order

Step 2: Define operators (legal moves)

- Blank can move Up, Down, Left, or Right (if space permits)

Step 3: BFS expands level by level

- Level 0: Initial state (1 state)
- Level 1: All states reachable in 1 move (3-4 states typically)
- Level 2: All states reachable in 2 moves
- Continue until goal found

Using BFS guarantees finding the shortest solution (minimum number of moves), though it may require exploring thousands of states for complex puzzles.

**Solution using A\* with Manhattan Distance Heuristic**:

For the initial state above, calculate Manhattan distance for each tile:

- Tile 1: at (0,0), goal (0,0) → distance = 0
- Tile 2: at (1,1), goal (0,1) → distance = 1
- Tile 3: at (0,1), goal (0,2) → distance = 1
- Tile 4: at (1,0), goal (1,0) → distance = 0
- Tile 5: at (0,2), goal (1,2) → distance = 1
- Tile 6: at (1,2), goal (1,2) → distance = 0
- Tile 7: at (2,0), goal (2,0) → distance = 0
- Tile 8: at (2,1), goal (2,1) → distance = 0
- Total h(n) = 3

A\* expands nodes with lowest f(n) = g(n) + h(n), dramatically reducing nodes explored compared to BFS.

### Example 2: Route Finding Problem (Romania Map)

**Problem**: Find the shortest path from Arad to Bucharest in Romania.

```
Arad → Sibiu (140) → Fagaras (99) → Bucharest (211) = Total: 450
Arad → Sibiu (140) → Rimnicu Vilcea (80) → Pitesti (97) → Bucharest (101) = Total: 418
Arad → Timisoara (118) → Lugoj (111) → Mehadica (70) → Bucharest (75) = Total: 374
```

Using Uniform-Cost Search (Dijkstra's algorithm): Explores nodes in order of cumulative path cost, guaranteeing the optimal solution of 418 via Pitesti.

Using A\* with straight-line distance heuristic:

- h(Arad) = 366 (straight-line to Bucharest)
- A\* focuses on the most promising paths, finding the optimal solution while exploring far fewer nodes than uniform-cost search.

### Example 3: Vacuum Cleaner World

**Problem**: Agent starts in one location with dirt in both squares; goal is to clean all dirt.

**State Representation**:

- State = (Location, DirtLeft, DirtRight)
- Initial: (A, Dirty, Dirty)
- Goal: Either (A, Clean, Clean) or (B, Clean, Clean)

**Operators**:

- Suck: Clean current square
- Left: Move to other square (if not at edge)
- Right: Move to other square (if not at edge)

**Solution**:

1. Suck (A, Dirty, Dirty) → (A, Clean, Dirty)
2. Right (A, Clean, Dirty) → (B, Clean, Dirty)
3. Suck (B, Clean, Dirty) → (B, Clean, Clean)

This simple problem illustrates how to formulate real-world cleaning tasks as search problems.

## Exam Tips

1. **Know the Five Components**: Always remember that any well-defined problem must have initial state, goal state, state space, operators, and path cost. This is frequently asked in exams.

2. **Differentiate BFS and DFS**: BFS is complete, optimal for unit costs, but exponential space. DFS is not complete for infinite spaces but uses linear space. Understand when to use each.

3. **A\* Algorithm Properties**: Remember that A\* is complete and optimal only when the heuristic is admissible. The admissibility condition h(n) ≤ true cost is crucial for exam questions.

4. **Complexities Matter**: Be prepared to calculate or state time and space complexities for different search algorithms. BFS: O(b^d), DFS: O(bm), A\*: O(b^d) in worst case.

5. **Heuristic Selection**: Understand what makes a good heuristic—should be informative (narrowing search) while remaining admissible. The 8-puzzle Manhattan distance is a classic example.

6. **Greedy vs A\***: Greedy Best-First Search uses only h(n) and is not optimal, while A\* uses f(n) = g(n) + h(n) and is optimal with admissible heuristics.

7. **Problem Formulation is Key**: Many exam questions give a real-world scenario and ask you to formulate it as a search problem. Practice identifying states, operators, and goals.
