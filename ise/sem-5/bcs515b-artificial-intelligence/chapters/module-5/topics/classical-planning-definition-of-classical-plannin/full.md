# **Classical Planning**

## **Definition and Historical Context**

Classical planning is a subfield of artificial intelligence (AI) that deals with the planning problem: given a set of tasks and a set of available resources, determine a sequence of actions to achieve the desired state. The planning problem has been studied for decades, with the earliest work dating back to the 1960s.

The planning problem can be formally defined as follows:

- Let `Z` be a set of world states
- Let `A` be a set of actions
- Let `P` be a set of predicates (also known as fluents)
- Let `init` be the initial state
- Let `goal` be the desired state
- Let `Z` be a set of actions
- Let `pred` be the set of predicates

The planning problem can be stated as follows:

"Given the initial state `init`, the goal state `goal`, and a set of actions `A`, determine a sequence of actions `z = (z1, z2, ..., zn)` such that:

- For each state `zi` in the sequence:

* `zi` is reachable from `init` by applying the actions `z1, z2, ..., z(i-1)`
* `zi` satisfies the goal condition, i.e., `goal(zi)`
* `zi` is not in the sequence `z1, z2, ..., z(i-1)`

## **Planning Graphs**

A planning graph is a directed graph that represents the planning problem. The nodes of the graph represent the states of the world, and the edges represent the transitions between states.

The planning graph is constructed as follows:

- The root node represents the initial state `init`
- For each action `a` in `A`, a new node is created to represent the state obtained by applying `a` to the current state
- For each predicate `p` in `P`, a new node is created to represent the state that satisfies `p`
- For each pair of states `s1` and `s2`, an edge is created from `s1` to `s2` if there exists an action `a` such that `s2` is reachable from `s1` by applying `a`

## **Algorithms for Planning as State-Space Search**

There are several algorithms for planning as state-space search, including:

### 1. Breadth-First Search (BFS)

BFS is a traversal algorithm that explores the planning graph level by level, starting from the root node. The algorithm is guaranteed to find the shortest path to the goal state, but it can be slow for large planning problems.

**Example:**

Suppose we want to plan to go from the initial state `init` to the goal state `goal` using the actions `A = {move, turn, stop}`. The planning graph would be constructed as follows:

- Root node: `init`
- Node 1: `init -> move -> goal` (edge)
- Node 2: `init -> turn -> goal` (edge)
- Node 3: `init -> stop -> init` (edge)

The BFS algorithm would explore the graph as follows:

- Visit node 1: `init -> move -> goal`
- Visit node 2: `init -> turn -> goal`
- Visit node 3: `init -> stop -> init`
- Visit node 1 again: `init -> move -> goal`
- Visit node 2 again: `init -> turn -> goal`
- Visit node 3 again: `init -> stop -> init`

The algorithm would stop when it reaches the goal state `goal`.

### 2. Depth-First Search (DFS)

DFS is a traversal algorithm that explores the planning graph by visiting a node and then visiting its neighbors. The algorithm is not guaranteed to find the shortest path to the goal state, but it can be faster than BFS for large planning problems.

**Example:**

Suppose we want to plan to go from the initial state `init` to the goal state `goal` using the actions `A = {move, turn, stop}`. The planning graph would be constructed as follows:

- Root node: `init`
- Node 1: `init -> move -> goal` (edge)
- Node 2: `init -> turn -> goal` (edge)
- Node 3: `init -> stop -> init` (edge)

The DFS algorithm would explore the graph as follows:

- Visit node 1: `init -> move -> goal`
- Visit node 2: `init -> turn -> goal`
- Visit node 1 again: `init -> move -> goal`
- Visit node 3: `init -> stop -> init`
- Visit node 1 again: `init -> move -> goal`
- Visit node 2 again: `init -> turn -> goal`

The algorithm would stop when it reaches the goal state `goal`.

### 3. Best-First Search (BFS with Heuristics)

BFS with heuristics is a variant of BFS that uses a heuristic function to guide the search towards the goal state. The heuristic function estimates the distance from the current state to the goal state.

**Example:**

Suppose we want to plan to go from the initial state `init` to the goal state `goal` using the actions `A = {move, turn, stop}`. The planning graph would be constructed as follows:

- Root node: `init`
- Node 1: `init -> move -> goal` (edge)
- Node 2: `init -> turn -> goal` (edge)
- Node 3: `init -> stop -> init` (edge)

The BFS algorithm with heuristics would explore the graph as follows:

- Visit node 1: `init -> move -> goal` (edge)
- Visit node 2: `init -> turn -> goal` (edge)
- Visit node 1 again: `init -> move -> goal`
- Visit node 3: `init -> stop -> init`
- Visit node 1 again: `init -> move -> goal`
- Visit node 2 again: `init -> turn -> goal`

The algorithm would stop when it reaches the goal state `goal`.

## **Applications**

Classical planning has a wide range of applications in artificial intelligence, including:

- Robotics: planning to move a robot from one location to another
- Scheduling: planning to schedule a sequence of tasks to achieve a desired outcome
- Supply chain management: planning to manage the flow of goods and services

## **Case Studies**

- **Planning to move a robot from one location to another:** Suppose we want to plan to move a robot from the initial state `init` to the goal state `goal` using the actions `A = {move, turn, stop}`. The planning graph would be constructed as follows:

- Root node: `init`
- Node 1: `init -> move -> goal` (edge)
- Node 2: `init -> turn -> goal` (edge)
- Node 3: `init -> stop -> init` (edge)

The planning algorithm would explore the graph and find the shortest path to the goal state `goal`.

- **Scheduling:** Suppose we want to schedule a sequence of tasks to achieve a desired outcome. The planning graph would be constructed as follows:

- Root node: `init`
- Node 1: `init -> task1 -> goal` (edge)
- Node 2: `init -> task2 -> goal` (edge)
- Node 3: `init -> task3 -> goal` (edge)

The planning algorithm would explore the graph and find the shortest path to the goal state `goal`.

## **Modern Developments**

Classical planning has undergone significant developments in recent years, including:

- **Planning under uncertainty:** planning to achieve a desired outcome in the presence of uncertainty and incomplete information
- **Planning with multiple goals:** planning to achieve multiple goals simultaneously
- **Planning with constraints:** planning to achieve a desired outcome while satisfying constraints

## **Further Reading**

- **Planning:** Pieter Abader, Jürgen Dix, and Uta Prühm, "Planning," Springer, 2017
- **Artificial Intelligence:** Stuart Russell and Peter Norvig, "Artificial Intelligence: A Modern Approach," Pearson, 2010
- **Planning under uncertainty:** Stuart Russell and Peter Norvig, "Artificial Intelligence: A Modern Approach," Pearson, 2010
- **Planning with multiple goals:** Stuart Russell and Peter Norvig, "Artificial Intelligence: A Modern Approach," Pearson, 2010
- **Planning with constraints:** Stuart Russell and Peter Norvig, "Artificial Intelligence: A Modern Approach," Pearson, 2010

Note: This is a comprehensive outline of classical planning, and it is not intended to be a complete or definitive text on the subject.
