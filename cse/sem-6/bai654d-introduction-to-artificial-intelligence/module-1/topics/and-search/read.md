# AND Search and AND-OR Graphs

## Introduction to Problem Decomposition

Many real-world problems can be solved by breaking them down into smaller, independent subproblems. This divide-and-conquer approach is formalized in AI through AND-OR graphs and AND search. Unlike standard search (OR search), where finding any single path to the goal suffices, AND search requires solving all subproblems that arise from decomposing a problem.

### Example: Travel Planning

To "travel from city A to city D," we might decompose the problem: fly from A to B AND take a train from B to D. Both subproblems must be solved for the overall problem to be solved.

## AND Nodes vs OR Nodes

In an AND-OR graph:

- **OR nodes** represent choices. Only one successor needs to be solved. This is the same as standard search where we pick the best path among alternatives.
- **AND nodes** represent problem decompositions. All successors must be solved. The problem is decomposed into subproblems that must all be completed.

### Solution Graph

A solution in an AND-OR graph is not a single path but a **solution graph** (also called a solution tree) that:

1. Contains the start node
2. For every OR node included, contains exactly one of its successors
3. For every AND node included, contains all of its successors
4. Every leaf node in the solution graph is a solved (terminal) node

## AND-OR Search Trees

An AND-OR search tree is a hierarchical representation where:

```markdown
Problem P
├── [OR] Method 1: Solve P directly
├── [AND] Method 2: Decompose into subproblems
│ ├── Subproblem P1
│ └── Subproblem P2
└── [AND] Method 3: Alternative decomposition
├── Subproblem P3
├── Subproblem P4
└── Subproblem P5
```

### Example: Integration Problem

To integrate a complex function, we might:

- (OR) Apply integration by parts
- (AND) Decompose into partial fractions, then integrate each fraction separately

Each fraction becomes its own subproblem, and ALL must be solved.

## Problem Reduction

Problem reduction is the process of transforming a problem into a set of easier subproblems. The key idea is:

1. **Decompose** the original problem into subproblems using AND nodes
2. **Solve** each subproblem independently (these may themselves be decomposed further)
3. **Combine** the solutions of all subproblems to form the solution of the original problem

### Example: Tower of Hanoi (3 disks, pegs A, B, C)

Move 3 disks from A to C:

- AND node decomposes into:
- Move 2 disks from A to B (subproblem)
- Move disk 3 from A to C (primitive)
- Move 2 disks from B to C (subproblem)

Each "move 2 disks" subproblem is further decomposed recursively.

## The AO\* Algorithm

The AO* algorithm is the primary algorithm for searching AND-OR graphs. It extends the ideas of A* search to handle AND nodes. AO\* maintains a graph of explored nodes and iteratively refines cost estimates.

### Key Concepts:

- **h(n)**: Heuristic estimate of the cost to solve the subproblem rooted at node n
- **Cost of an AND node**: Sum of costs of all successors plus the arc costs
- **Cost of an OR node**: Minimum cost among all successors (choosing the best decomposition)

### AO\* Algorithm Steps:

```markdown
1. Initialize graph G with start node s
   Set h(s) = heuristic estimate

2. Repeat until s is SOLVED or h(s) = infinity:
   a. Select a non-terminal leaf node n from the best partial solution graph rooted at s
   b. Expand n, generating its successors
   c. For each new successor m:

- If m is a terminal (solved) node, mark SOLVED, h(m) = 0
- Else set h(m) = heuristic estimate
  d. Propagate cost revisions backward:
- Update h-values of ancestors based on new information
- For AND nodes: h = sum of successor costs + arc costs
- For OR nodes: h = min of successor costs + arc cost
- Mark nodes as SOLVED when appropriate
- An AND node is SOLVED when ALL successors are SOLVED
- An OR node is SOLVED when ANY successor is SOLVED

3. If s is SOLVED, extract and return the solution graph
   If h(s) = infinity, return failure
```

## Worked Example of AO\*

Consider the following AND-OR graph where we want to solve problem A:

```markdown
A (start, h=5)
├── [OR] → B (h=3) → solved (cost 0)
└── [AND] → {C, D}
├── C (h=2) → solved (cost 0)
└── D (h=4) → solved (cost 0)
Arc costs: A→B = 3, A→{C,D} = 1 (each arc to C and D costs 1)
```

### Step 1: Expand A

- OR successor B: estimated cost = 3 + 3 = 6
- AND successors {C, D}: estimated cost = (1 + 2) + (1 + 4) = 8
- Best current option: B (cost 6), mark B as part of best solution

### Step 2: Expand B

- B leads to a solved terminal node (cost 0)
- Update: h(B) = 0, cost through B = 3 + 0 = 3
- Also check AND path: cost through {C,D} = (1+2) + (1+4) = 8
- Best: B path with cost 3

### Step 3: Mark B as SOLVED, then A is SOLVED via B

- Solution graph: A → B → terminal

## Cost Computation Rules

For an OR node n with successors s1, s2, ..., sk:

- **h(n) = min over i of [cost(n, si) + h(si)]**

For an AND node n with successors s1, s2, ..., sk:

- **h(n) = sum over all i of [cost(n, si) + h(si)]**

A node is marked SOLVED when:

- It is a terminal node (primitive problem with known solution)
- It is an OR node with at least one SOLVED successor
- It is an AND node with ALL successors SOLVED

## Properties of AO\*

| Property       | Value                                                 |
| -------------- | ----------------------------------------------------- |
| Complete       | Yes, for finite graphs with consistent heuristics     |
| Optimal        | Yes, if heuristic is admissible (never overestimates) |
| Space          | O(number of nodes in the graph)                       |
| Handles cycles | Must be modified to detect and handle cycles          |

## Comparison: AND Search vs OR Search

| Aspect           | OR Search (A\*)                      | AND Search (AO\*)          |
| ---------------- | ------------------------------------ | -------------------------- |
| Solution         | Single path from start to goal       | Solution graph (tree)      |
| Node types       | Only OR nodes (choose one successor) | Both AND and OR nodes      |
| Goal             | Find one goal state                  | Solve all subproblems      |
| Cost of AND node | N/A                                  | Sum of all successor costs |
| Cost of OR node  | Min of successor costs               | Min of successor costs     |
| Application      | Pathfinding, puzzle solving          | Theorem proving, planning  |

## Applications of AND-OR Search

1. **Theorem Proving**: Break a theorem into lemmas (AND), choose proof strategies (OR)
2. **Game Playing**: Represent game trees where MAX nodes are OR nodes and MIN nodes are AND nodes (opponent must be handled for all responses)
3. **Planning**: Decompose a complex plan into subplans that must all succeed
4. **Software Testing**: A test suite (AND) must pass all test cases; each test case may have alternative implementations (OR)
5. **Mathematical Problem Solving**: Decompose integrals, equations into parts

## Exam Tips

1. **Draw AND-OR trees clearly**: Use arcs to connect AND-node successors (a curved line linking the edges indicates AND)
2. **Remember cost formulas**: AND node cost = SUM of all children costs; OR node cost = MIN of children costs
3. **Trace AO\* step by step**: Show the expansion, cost revision, and marking of SOLVED nodes at each step
4. **Distinguish from A\***: AO\* works on AND-OR graphs and finds solution graphs, not just paths
5. **Know when to apply**: AND search is used when problems can be decomposed into subproblems that must all be solved
6. **SOLVED propagation**: An AND node is SOLVED only when ALL children are SOLVED; an OR node is SOLVED when ANY child is SOLVED
