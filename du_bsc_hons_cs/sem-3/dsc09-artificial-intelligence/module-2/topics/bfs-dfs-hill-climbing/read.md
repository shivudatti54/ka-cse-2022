# BFS, DFS, and Hill Climbing Search Algorithms

## Introduction

Search algorithms form the backbone of problem-solving in Artificial Intelligence. When an AI system needs to find a solution from a large space of possible states, it employs search strategies to navigate through this space efficiently. Among the most fundamental search techniques are Breadth-First Search (BFS), Depth-First Search (DFS), and Hill Climbing—each with distinct characteristics, advantages, and applications.

BFS and DFS are uninformed (blind) search algorithms that explore the search space without any knowledge about the goal beyond what is provided in the problem definition. They differ fundamentally in their approach: BFS explores equally in all directions (like ripples in water), while DFS dives deep into one direction before backtracking (like exploring a maze). Hill Climbing, on the other hand, is an informed (heuristic) local search algorithm that uses domain-specific knowledge to guide its search toward better solutions.

For University of Delhi's Computer Science students, understanding these algorithms is essential—not only for theoretical knowledge but also for practical applications in game playing, path finding, puzzle solving, and optimization problems. These algorithms frequently appear in internal assessments and end-semester examinations, making thorough preparation crucial for academic success.

## Key Concepts

### Breadth-First Search (BFS)

Breadth-First Search is a complete search algorithm that systematically explores all nodes at the present depth before moving to nodes at the next depth level. It uses a **FIFO (First-In-First-Out)** queue data structure to manage the frontier of unexplored nodes.

**Algorithm Steps:**
1. Enqueue the initial state into the queue
2. Dequeue a node from the front of the queue
3. If this node is the goal, return the solution
4. Otherwise, expand all its children and enqueue them at the back of the queue
5. If the queue is empty, return failure (no solution exists)
6. Repeat from step 2

**Properties of BFS:**
- **Completeness:** BFS is complete—it will find a solution if one exists
- **Optimality:** BFS finds the shortest path (fewest edges) to the goal
- **Time Complexity:** O(b^d) where b is the branching factor and d is the depth of the shallowest goal
- **Space Complexity:** O(b^d) — BFS must store all frontier nodes in memory

**Advantages:** Guaranteed to find the optimal solution; complete and systematic
**Disadvantages:** High memory requirements; slow for deep solutions with large branching factors

### Depth-First Search (DFS)

Depth-First Search explores as far as possible along each branch before backtracking. It uses a **LIFO (Last-In-First-Out)** stack data structure (either explicitly or through recursion).

**Algorithm Steps:**
1. Push the initial state onto the stack
2. Pop a node from the top of the stack
3. If this node is the goal, return the solution
4. Otherwise, push all its children onto the stack (in some order)
5. If the stack is empty, return failure
6. Repeat from step 2

**Properties of DFS:**
- **Completeness:** DFS is incomplete in infinite state spaces; may get lost in deep paths
- **Optimality:** Not optimal—may find a solution that is not the shortest
- **Time Complexity:** O(b^m) where m is the maximum depth of the search tree
- **Space Complexity:** O(bm) — only stores nodes along the current path

**Advantages:** Low memory requirements; can find solutions in deep search spaces quickly
**Disadvantages:** Not guaranteed to find solution; not optimal; may get stuck in infinite loops without cycle detection

### Hill Climbing

Hill Climbing is a **local search algorithm** that attempts to find a better solution by iteratively moving in the direction of increasing value (or decreasing cost). It maintains a single current state and generates successors, moving to the best successor if it is better than the current state.

**Algorithm Steps:**
1. Initialize current state with a random or given starting point
2. Loop until a goal is reached or no further improvement is possible:
   - Generate all successors of the current state
   - Evaluate the heuristic (objective function) for each successor
   - If the best successor has better value than current state, move to that successor
   - Otherwise, terminate and return the current state

**Variants of Hill Climbing:**
- **Simple Hill Climbing:** Evaluates neighbors one by one and moves to the first better one
- **Steepest-Ascent Hill Climbing:** Evaluates all neighbors and moves to the best one
- **Stochastic Hill Climbing:** Randomly selects among better successors
- **Random-Restart Hill Climbing:** Repeats hill climbing from random starting points

**Properties of Hill Climbing:**
- **Completeness:** Not complete—can get stuck in local maxima
- **Optimality:** Not optimal—may find local maxima instead of global maximum
- **Time Complexity:** Depends on the number of neighbors and landscape of the search space

**Advantages:** Fast; minimal memory requirements; suitable for optimization problems
**Disadvantages:** Gets stuck in local maxima; sensitive to starting point; does not explore thoroughly

**Common Problems:**
- **Local Maximum:** Stuck at a peak that is not the highest
- **Plateau:** Flat region where all neighbors have same value
- **Ridge:** Narrow ridge that requires moving in two directions simultaneously

## Examples

### Example 1: BFS on a Graph

Consider the following graph where S is the start and G is the goal:

```
        S
       /|\
      A B C
     /| |\
    D E F G
```

**Step-by-step BFS traversal:**

1. Queue: [S], Visited: []
2. Dequeue S, expand: Queue: [A, B, C], Visited: [S]
3. Dequeue A, expand: Queue: [B, C, D, E], Visited: [S, A]
4. Dequeue B, expand: Queue: [C, D, E, F], Visited: [S, A, B]
5. Dequeue C, expand: Queue: [D, E, F, G], Visited: [S, A, B, C]
6. Dequeue D (no expansion): Queue: [E, F, G], Visited: [S, A, B, C, D]
7. Dequeue E (no expansion): Queue: [F, G], Visited: [S, A, B, C, D, E]
8. Dequeue F (no expansion): Queue: [G], Visited: [S, A, B, C, D, E, F]
9. Dequeue G — **Goal found!**

**Path:** S → C → G (depth 2, shortest path)

### Example 2: DFS on the Same Graph

Using the same graph and exploring children from left to right:

**Step-by-step DFS traversal:**

1. Stack: [S], Visited: []
2. Pop S, push children: Stack: [A, B, C], Visited: [S]
3. Pop A, push children: Stack: [B, C, D, E], Visited: [S, A]
4. Pop E, no children: Stack: [B, C, D], Visited: [S, A, E]
5. Pop D, no children: Stack: [B, C], Visited: [S, A, E, D]
6. Pop C, push G: Stack: [B, C, G], Visited: [S, A, E, D]
7. Pop G — **Goal found!**

**Path:** S → A → E (may vary based on order)

### Example 3: Hill Climbing for the 8-Queens Problem

The 8-Queens problem requires placing 8 queens on a chessboard so none attack each other. Using **number of attacking pairs** as the heuristic (objective function to minimize):

**Initial State:** Random placement with 17 attacking pairs
**Goal State:** 0 attacking pairs

**Steepest-Ascent Hill Climbing Steps:**

1. Current: [4, 2, 7, 1, 3, 8, 5, 6], Heuristic: 17
2. Generate all successors (move each queen to each column in its row)
3. Find best successor: Move queen in row 3 from column 7 to column 6
4. New State: [4, 2, 6, 1, 3, 8, 5, 6], Heuristic: 12
5. Continue until no improvement possible...

If stuck at local maximum (e.g., heuristic = 1), restart from a different random position. With random restart, the algorithm typically finds the global optimum (0 attacking pairs).

## Exam Tips

1. **Understand when to use each algorithm:** BFS for shortest path when all edges have equal cost; DFS for memory-constrained environments; Hill Climbing for optimization problems with heuristics.

2. **Remember the data structures:** BFS uses Queue (FIFO); DFS uses Stack (LIFO) or recursion; Hill Climbing maintains current state with no explicit storage.

3. **Know the complexities:** BFS is O(b^d) time and space; DFS is O(bm) space; Hill Climbing is problem-dependent.

4. **Completeness matters:** BFS is complete and optimal; DFS is neither complete nor optimal; Hill Climbing is not complete.

5. **Hill Climbing variants:** Be familiar with simple, steepest-ascent, stochastic, and random-restart variants.

6. **Local maxima solutions:** Know how to handle local maxima in Hill Climbing—random restarts, simulated annealing, or genetic algorithms.

7. **Practical applications:** BFS for web crawling and social networks; DFS for topological sorting and cycle detection; Hill Climbing for training neural networks and parameter optimization.

8. **Trace algorithms:** Practice tracing through small examples—you may be asked to show the order of node expansion or the path found.