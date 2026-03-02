# Uninformed Search Strategies

## Introduction

Uninformed search strategies, also known as blind search strategies, are fundamental search algorithms used in Artificial Intelligence to solve problems without any prior knowledge about the problem domain. These strategies operate solely based on the information available in the problem definition - the initial state, goal state, and the set of operators/actions. Unlike informed search strategies that use heuristics to guide the search, uninformed search explores the search space systematically without any domain-specific knowledge to prioritize promising states.

In the context of 's Artificial Intelligence syllabus, uninformed search strategies form the foundation for understanding more complex search algorithms. These strategies are particularly important because they guarantee solution finding (if one exists) under certain conditions and provide a baseline for comparing the performance of more sophisticated algorithms. The major uninformed search techniques include Breadth-First Search (BFS), Depth-First Search (DFS), Uniform-Cost Search, Depth-Limited Search, Iterative Deepening Search, and Bidirectional Search. Each of these strategies differs in how they explore the search tree and consequently in their time complexity, space complexity, and solution quality.

## Key Concepts

### 1. Breadth-First Search (BFS)

Breadth-First Search is a complete search strategy that explores the search tree level by level. It starts from the root node (initial state) and expands all nodes at the current depth before moving to nodes at the next depth level. BFS uses a FIFO (First-In-First-Out) queue data structure to manage the frontier (the set of nodes waiting to be expanded).

**Properties of BFS:**

- **Completeness**: BFS is complete, meaning if a solution exists, BFS will find it.
- **Optimality**: BFS finds the shortest path in terms of the number of steps (unweighted graphs).
- **Time Complexity**: O(b^d) where b is the branching factor and d is the depth of the solution.
- **Space Complexity**: O(b^d) - this is the major drawback of BFS as it must store all expanded nodes in memory.

### 2. Depth-First Search (DFS)

Depth-First Search explores the search tree by going as deep as possible along each branch before backtracking. It uses a LIFO (Last-In-First-Out) stack data structure to manage the frontier. DFS expands the most recently generated node first.

**Properties of DFS:**

- **Completeness**: DFS is incomplete in infinite search spaces unless proper cycle checking is implemented.
- **Optimality**: DFS is not optimal; it may find a solution that is not the shortest.
- **Time Complexity**: O(b^m) where m is the maximum depth of the search tree.
- **Space Complexity**: O(bm) - much better than BFS as it only stores the path from root to current node.

### 3. Uniform-Cost Search (UCS)

Uniform-Cost Search is a variant of BFS that considers path costs instead of the number of steps. It expands the node with the lowest cumulative path cost g(n) from the root. UCS uses a priority queue ordered by path cost.

**Properties of UCS:**

- **Completeness**: UCS is complete if all step costs are positive.
- **Optimality**: UCS finds the optimal solution (minimum cost path) if all edge costs are non-negative.
- **Time Complexity**: O(b^(C*/ε)) where C* is the optimal cost and ε is the minimum step cost.
- **Space Complexity**: Similar to BFS, O(b^(C\*/ε)).

### 4. Depth-Limited Search (DLS)

Depth-Limited Search is a modification of DFS that imposes a limit on the depth of the search. Nodes at depth equal to the limit are treated as goal nodes (but not expanded further). This solves the infinite depth problem of DFS.

**Properties of DLS:**

- **Completeness**: DLS is complete only if the solution depth is within the limit.
- **Optimality**: DLS is not optimal.
- **Time Complexity**: O(b^l) where l is the depth limit.
- **Space Complexity**: O(bl)

### 5. Iterative Deepening Search (IDS)

Iterative Deepening Search combines the benefits of BFS and DFS. It performs repeated depth-limited searches with increasing depth limits (0, 1, 2, ..., n) until a solution is found. Each iteration explores the search tree completely up to the current depth limit before moving to the next limit.

**Properties of IDS:**

- **Completeness**: IDS is complete like BFS.
- **Optimality**: IDS finds the shortest path like BFS (when all step costs are equal).
- **Time Complexity**: O(b^d) - similar to BFS.
- **Space Complexity**: O(bd) - like DFS.

### 6. Bidirectional Search

Bidirectional search simultaneously searches forward from the initial state and backward from the goal state, meeting in the middle. This approach can significantly reduce the search time by exploring roughly half the search space from each direction.

**Properties of Bidirectional Search:**

- **Completeness**: Complete if both searches are complete.
- **Optimality**: Can be made optimal with proper implementation.
- **Time Complexity**: O(b^(d/2)) - much better than BFS.
- **Space Complexity**: O(b^(d/2)).

## Examples

### Example 1: Breadth-First Search on a Small Graph

Consider the following graph with nodes A through G, where A is the start state and G is the goal state:

```
 A
 / \
 B C
 / \ \
D E F
 \
 G
```

**Step-by-step BFS traversal:**

1. **Initialize**: Queue = [A], Visited = {A}
2. **Expand A**: Add neighbors B, C to queue. Queue = [B, C], Visited = {A, B, C}
3. **Expand B**: Add neighbors D, E to queue. Queue = [C, D, E], Visited = {A, B, C, D, E}
4. **Expand C**: Add neighbor F to queue. Queue = [D, E, F], Visited = {A, B, C, D, E, F}
5. **Expand D**: No unvisited neighbors. Queue = [E, F]
6. **Expand E**: Add neighbor G to queue. Queue = [F, G], Visited = {A, B, C, D, E, F, G}
7. **Goal reached**: G is the goal, solution found!

**Solution Path**: A → B → E → G (depth = 3)

### Example 2: Comparing DFS and BFS for the 8-Puzzle Problem

For the 8-Puzzle problem with initial state:

```
2 8 3
1 6 4
7 5 _
```

Goal state:

```
1 2 3
4 5 6
7 8 _
```

**BFS Characteristics:**

- Explores all states at depth 0, then depth 1, then depth 2, etc.
- Typically requires millions of nodes in memory
- Guaranteed to find optimal solution (minimum moves)
- May take minutes to solve on standard hardware

**DFS Characteristics:**

- Goes deep along one path until hitting depth limit or dead end
- Uses much less memory (only stores current path)
- May find solution quickly but not necessarily optimal
- Can get stuck in infinite loops without cycle detection

**For this specific puzzle:**

- BFS: ~181,440 possible states, finds solution in ~20-31 moves
- DFS: May explore fewer nodes but risk of not finding solution

### Example 3: Uniform-Cost Search with Different Path Costs

Consider a graph where edge costs vary:

```
 4
 A -----> B
 | \ /|
 2| \ / |6
 | \ / |
 v X v
 C --> D --> G
 1 5
```

Edge costs: A→B=4, A→C=2, A→D=10, C→D=1, B→D=6, D→G=5

**UCS Execution:**

1. Start at A with cost 0. Frontier: {A(0)}
2. Expand A: Frontier = {C(2), B(4), D(10)}
3. Expand C (lowest cost): Add D(2+1=3). Frontier = {D(3), B(4), D(10)}
4. Expand D(3): Add G(3+5=8). Frontier = {B(4), D(10), G(8)}
5. Expand B(4): Frontier = {D(4+6=10), D(10), G(8)}
6. Expand G(8): Goal reached!

**Optimal Solution**: A → C → D → G with total cost 8

This demonstrates how UCS finds the minimum-cost path rather than the path with fewest edges.

## Exam Tips

1. **Remember the key difference**: BFS explores level by level (queue-based), while DFS explores depth-first (stack-based). This is the most frequently asked concept in exams.

2. **BFS is optimal for unweighted graphs**: If all edges have equal cost, BFS finds the shortest path. This property is crucial for solving shortest path problems.

3. **DFS is not complete in infinite spaces**: Without proper cycle detection and depth limits, DFS may never terminate. This is a common exam point.

4. **UCS vs BFS**: UCS generalizes BFS by considering path costs. When all costs are equal, UCS behaves exactly like BFS.

5. **IDS combines advantages**: Iterative Deepening Search achieves the space efficiency of DFS with the optimality of BFS. This makes it the preferred uninformed search strategy in practice.

6. **Time-Space Tradeoff**: Remember the tradeoff - BFS uses more memory but finds optimal solution; DFS uses less memory but may not find optimal solution.

7. **Bidirectional search complexity**: The time complexity is O(b^(d/2)), which is significantly better than BFS's O(b^d), making it efficient when both start and goal states are known.

8. **When to use each strategy**: Use BFS for shortest path in unweighted graphs. Use DFS when memory is limited and solution depth is known to be shallow. Use UCS when path costs matter. Use IDS when optimal solution with minimal memory is needed.

9. **Completeness definition**: A search strategy is complete if it guarantees finding a solution whenever one exists. BFS and UCS are complete; basic DFS is not.

10. **Know the complexity formulas**: Be able to write the time and space complexity for each algorithm in terms of branching factor (b) and depth (d).
