# Prim's Algorithm for Minimum Spanning Tree

## Table of Contents

- [Prim's Algorithm for Minimum Spanning Tree](#prims-algorithm-for-minimum-spanning-tree)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Minimum Spanning Tree Definition](#minimum-spanning-tree-definition)
  - [The Cut Property (Proof of Correctness)](#the-cut-property-proof-of-correctness)
  - [Greedy Choice Property](#greedy-choice-property)
  - [Algorithm Steps](#algorithm-steps)
  - [Data Structures and Time Complexities](#data-structures-and-time-complexities)
- [Examples](#examples)
  - [Example 1: Small Graph Execution](#example-1-small-graph-execution)
  - [Example 2: Dense Graph with Array Implementation](#example-2-dense-graph-with-array-implementation)
  - [Example 3: Comparison with Kruskal's Algorithm](#example-3-comparison-with-kruskals-algorithm)
- [Exam Tips](#exam-tips)

## Introduction

Prim's Algorithm is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a connected, weighted undirected graph. A spanning tree is a subgraph that includes all vertices of the original graph without any cycles, while an MST is a spanning tree with minimum total edge weight. The algorithm was developed by Czech mathematician Vojtěch Jarník in 1930 and later independently by computer scientist Robert C. Prim in 1957.

The fundamental principle underlying Prim's Algorithm is the **cut property**: for any cut in the graph (a partition of vertices into two non-empty sets), the minimum weight edge crossing that cut belongs to some MST. This property provides the theoretical foundation for the greedy approach, where at each step, the algorithm selects the minimum weight edge that connects a vertex in the growing tree to a vertex outside it.

In the context of Analysis and Design of Algorithms, Prim's Algorithm serves as a canonical example of the greedy method, demonstrating how locally optimal choices lead to a globally optimal solution under specific conditions. The algorithm finds applications in network design (telecommunications, road networks), clustering analysis, and approximation algorithms for NP-hard problems.

## Key Concepts

### Minimum Spanning Tree Definition

A **spanning tree** of a connected graph G = (V, E) with n vertices is a subgraph that is a tree containing all n vertices. A **minimum spanning tree** (MST) is a spanning tree with the minimum possible total edge weight, where the sum of weights of all edges in the tree is minimized.

### The Cut Property (Proof of Correctness)

The cut property states: Let S be a non-empty proper subset of vertices V, and consider all edges with exactly one endpoint in S (the cut (S, V-S)). The minimum weight edge across this cut belongs to every minimum spanning tree.

_Proof_: Consider any MST T. If the minimum weight edge e across cut (S, V-S) is not in T, then adding e to T creates a cycle. This cycle must contain another edge f crossing the same cut. Since e has minimum weight, weight(e) ≤ weight(f). Removing f from the cycle gives a spanning tree T' with weight(T') = weight(T) + weight(e) - weight(f) ≤ weight(T). Since T is an MST, T' must also be minimum, and thus e belongs to some MST. ∎

### Greedy Choice Property

At each iteration, Prim's Algorithm selects the minimum weight edge connecting a vertex in the current tree to a vertex outside. By the cut property, this edge must belong to some MST. Adding this edge preserves the possibility of reaching an optimal solution, and by induction, the final tree is an MST.

### Algorithm Steps

1. Initialize: Start with an arbitrary vertex s. Add s to the tree T. Initialize a priority queue with all edges incident to s, keyed by weight.
2. Repeat until all vertices are included:
   a. Extract the minimum weight edge (u, v) from the priority queue, where exactly one endpoint is in T.
   b. Add the vertex v and edge (u, v) to T.
   c. For each edge (v, w) incident to v where w is not in T, insert (v, w) into the priority queue.
3. Return T as the minimum spanning tree.

### Data Structures and Time Complexities

| Data Structure         | Time Complexity | Space Complexity |
| ---------------------- | --------------- | ---------------- |
| Array/Adjacency Matrix | O(V²)           | O(V)             |
| Binary Min-Heap        | O(E log V)      | O(V + E)         |
| Fibonacci Heap         | O(E + V log V)  | O(V + E)         |

The O(V²) implementation using arrays is optimal for dense graphs (E ≈ V²). For sparse graphs, the binary heap implementation provides better performance.

## Examples

### Example 1: Small Graph Execution

Consider a graph with vertices {A, B, C, D, E} and the following edge weights:

- A-B: 2, A-C: 3, A-D: 4
- B-C: 1, B-E: 7
- C-D: 5, C-E: 6
- D-E: 8

**Step-by-step execution starting from vertex A:**

1. Start at A. T = {A}. Keys: B(2), C(3), D(4)
2. Select edge A-B (weight 2). T = {A, B}. Update: C(1 via B), D(4), E(7)
3. Select edge B-C (weight 1). T = {A, B, C}. Update: D(4), E(6 via C)
4. Select edge A-D (weight 4). T = {A, B, C, D}. Update: E(6)
5. Select edge C-E (weight 6). T = {A, B, C, D, E}. Complete.

**MST Weight: 2 + 1 + 4 + 6 = 13**

### Example 2: Dense Graph with Array Implementation

For a complete graph with n vertices and uniform edge weights of 1, the MST has weight n-1. Using the O(V²) array implementation, at each step we scan all vertices to find the minimum key value, giving O(V²) total time. The algorithm correctly produces any spanning tree since all edges have equal weight.

### Example 3: Comparison with Kruskal's Algorithm

For the same graph, Kruskal's algorithm would:

1. Sort all edges: B-C(1), A-B(2), A-C(3), A-D(4), C-D(5), C-E(6), B-E(7), D-E(8)
2. Process edges in order, adding if they don't form cycles

Both algorithms produce MSTs of equal total weight, demonstrating that the greedy approach, when correct, yields the same optimum regardless of implementation details.

## Exam Tips

1. **Understand the cut property proof**: The cut property is fundamental to proving Prim's correctness. Be able to state and prove it.
2. **Know all three complexities**: Understand when to use each implementation—array for dense graphs, binary heap for general use, Fibonacci heap for theoretical optimality.
3. **Distinguish from Kruskal's**: Prim's grows a single tree from a source vertex; Kruskal's builds a forest that merges into a tree.
4. **Trace algorithm manually**: Practice executing the algorithm step-by-step on small graphs, maintaining the priority queue or key array.
5. **Identify time complexity from graph characteristics**: Dense graphs (E = O(V²)) favor O(V²) implementation; sparse graphs favor O(E log V).
6. **Recognize greedy vs dynamic programming**: Prim's makes locally optimal choices; DP solves overlapping subproblems with optimal substructure.
7. **Apply to real-world problems**: Understand network design applications where MST minimization matters.
