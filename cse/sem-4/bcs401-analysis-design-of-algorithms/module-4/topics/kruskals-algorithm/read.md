# Kruskal's Algorithm

## Table of Contents

- [Kruskal's Algorithm](#kruskals-algorithm)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Minimum Spanning Tree Definition](#minimum-spanning-tree-definition)
  - [Greedy Approach in Kruskal's Algorithm](#greedy-approach-in-kruskals-algorithm)
  - [Disjoint Set Union (Union-Find) Data Structure](#disjoint-set-union-union-find-data-structure)
  - [Algorithm Steps](#algorithm-steps)
  - [Time Complexity Analysis](#time-complexity-analysis)
- [Examples](#examples)
  - [Example 1: Step-by-Step Execution](#example-1-step-by-step-execution)
  - [Example 2: Numerical Problem](#example-2-numerical-problem)
- [Exam Tips](#exam-tips)

## Introduction

Kruskal's Algorithm is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, and weighted graph. A spanning tree is a subgraph that includes all vertices of the original graph without forming any cycles, and the minimum spanning tree is the spanning tree with the smallest possible total edge weight. The algorithm was developed by Joseph Kruskal in 1956 and operates by sorting all edges in non-decreasing order of their weights and progressively adding edges that do not form cycles with the already selected edges.

The fundamental principle underlying Kruskal's Algorithm is the **cut property**, which states that for any cut in the graph (a partition of vertices into two non-empty sets), the minimum weight edge crossing that cut belongs to some minimum spanning tree. This greedy choice—always selecting the lightest edge that doesn't create a cycle—proves to be globally optimal due to the matroid structure of the spanning tree problem. The algorithm exemplifies the greedy method paradigm, where locally optimal choices lead to a globally optimal solution under specific conditions.

In the broader context of algorithm design, Kruskal's Algorithm stands alongside Prim's Algorithm and Dijkstra's Algorithm as essential graph optimization techniques. While Prim's Algorithm grows a single tree from a starting vertex, Kruskal's Algorithm builds the MST as a forest that eventually coalesces into a single tree. The practical implementation relies heavily on the **Disjoint Set Union (DSU)** data structure, also known as Union-Find, which efficiently manages the connectivity information required to detect cycles.

## Key Concepts

### Minimum Spanning Tree Definition

A spanning tree of a connected graph with n vertices contains exactly n-1 edges. The minimum spanning tree is the spanning tree with the minimum sum of edge weights. The MST satisfies several important properties: it is unique if all edge weights are distinct, and it contains no cycles (by definition). The total weight of the MST provides a lower bound on any possible connected subgraph spanning all vertices.

### Greedy Approach in Kruskal's Algorithm

The greedy strategy in Kruskal's Algorithm involves making a series of decisions, each choosing the locally optimal solution without considering future consequences. Specifically, the algorithm examines edges in order of increasing weight and adds an edge to the MST if and only if it does not create a cycle with the edges already selected. This approach is justified by the cut property: at each step, the lightest edge crossing some cut is guaranteed to be part of some MST, so adding such an edge never leads to a suboptimal solution.

The greedy choice property ensures that local optimality translates to global optimality for the MST problem. This is a special case where the greedy method succeeds, unlike in other optimization problems where greedy approaches may fail to find global optima.

### Disjoint Set Union (Union-Find) Data Structure

The DSU data structure maintains a collection of disjoint sets and supports two primary operations: **Find** determines which set a particular element belongs to, and **Union** merges two sets into one. In Kruskal's Algorithm, DSU tracks connected components as edges are added. Before adding an edge (u, v), we check whether u and v belong to the same component using Find. If they do, adding the edge would create a cycle, so the edge is skipped. If they belong to different components, we Union them and include the edge in the MST.

Two critical optimizations enhance DSU efficiency: **Union-by-Rank** attaches the smaller tree under the root of the larger tree to minimize tree height, and **Path Compression** flattens the tree structure during Find operations by making each node point directly to the root. With both optimizations, the amortized time complexity of each operation becomes α(n), where α is the inverse Ackermann function—a constant for all practical values of n.

### Algorithm Steps

```
KRUSKAL(G):
 Input: Connected undirected weighted graph G = (V, E)
 Output: Minimum Spanning Tree T

 T ← ∅ // Initialize empty MST
 Sort edges E by weight in non-decreasing order
 Initialize DSU with each vertex as separate set

 for each edge (u, v) in sorted order:
 if Find(u) ≠ Find(v): // u and v in different components
 T ← T ∪ {(u, v)} // Add edge to MST
 Union(u, v) // Merge components

 return T
```

The algorithm terminates when |T| = n-1 edges have been added, forming a spanning tree. Since the graph is connected, this condition is always reached.

### Time Complexity Analysis

The time complexity of Kruskal's Algorithm is **O(E log E)** or equivalently **O(E log V)**. This derives from: sorting edges takes O(E log E) time, and the DSU operations perform approximately E Find operations and (V-1) Union operations. With path compression and union-by-rank, each DSU operation takes O(α(V)) amortized time, which is effectively constant. Since O(E log E) = O(E log V) for connected graphs where E ≥ V-1, the dominant factor is the sorting step.

## Examples

### Example 1: Step-by-Step Execution

Consider a graph with vertices {A, B, C, D, E} and the following edges with weights:

| Edge  | Weight |
| ----- | ------ |
| (A,B) | 2      |
| (A,C) | 3      |
| (B,C) | 1      |
| (B,D) | 4      |
| (C,D) | 5      |
| (C,E) | 6      |
| (D,E) | 7      |

**Step 1:** Sort edges by weight: (B,C)=1, (A,B)=2, (A,C)=3, (B,D)=4, (C,D)=5, (C,E)=6, (D,E)=7

**Step 2:** Process (B,C) weight 1: Find(B) ≠ Find(C), add to MST. Components: {B,C}, {A}, {D}, {E}

**Step 3:** Process (A,B) weight 2: Find(A) ≠ Find(B), add to MST. Components: {A,B,C}, {D}, {E}

**Step 4:** Process (A,C) weight 3: Find(A) = Find(C), skip (would form cycle)

**Step 5:** Process (B,D) weight 4: Find(B) ≠ Find(D), add to MST. Components: {A,B,C,D}, {E}

**Step 6:** Process (C,D) weight 5: Find(C) = Find(D), skip (would form cycle)

**Step 7:** Process (C,E) weight 6: Find(C) ≠ Find(E), add to MST. Components: {A,B,C,D,E}

**Step 8:** MST complete with n-1 = 4 edges. Total weight = 1 + 2 + 4 + 6 = 13

The resulting MST edges are: (B,C), (A,B), (B,D), (C,E)

### Example 2: Numerical Problem

Given a graph with 6 vertices and the following edge weights, determine the MST weight after applying Kruskal's Algorithm:

Edges: w(1,2)=3, w(1,3)=4, w(2,3)=2, w(2,4)=5, w(3,4)=1, w(3,5)=6, w(4,5)=3, w(4,6)=2, w(5,6)=4

**Sorted edges:** (3,4)=1, (2,3)=2, (1,2)=3, (4,6)=2, (4,5)=3, (1,3)=4, (5,6)=4, (2,4)=5, (3,5)=6

Adding edges: (3,4), (2,3), (1,2), (4,6), (4,5) — five edges for 6 vertices

MST Weight = 1 + 2 + 3 + 2 + 3 = 11

## Exam Tips

1. **Remember the two key conditions**: An edge is added to MST if and only if it connects two different components (Find(u) ≠ Find(v)).

2. **Time complexity mastery**: Know that O(E log E) simplifies to O(E log V) for connected graphs, and understand why the inverse Ackermann function α(n) appears in DSU analysis.

3. **Cut property proof understanding**: Be prepared to explain that if e is the minimum weight edge crossing a cut, then there exists an MST containing e—this justifies the greedy choice.

4. **Distinguish from Prim's Algorithm**: Kruskal's builds a forest that merges, while Prim's grows a single tree; Kruskal's uses DSU, Prim's typically uses priority queues.

5. **Handle disconnected graphs**: If the input graph is disconnected, Kruskal's produces a Minimum Spanning Forest (a minimum spanning tree for each connected component).

6. **Edge cases**: Remember that if multiple edges have the same weight, any order works, though this may affect which MST is produced if weights are not distinct.

7. **Space complexity**: The algorithm requires O(V) space for the DSU structure plus O(E) for storing sorted edges.
