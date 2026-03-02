# Spanning Trees

## Table of Contents

- [Spanning Trees](#spanning-trees)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Basic Properties](#definition-and-basic-properties)
  - [Minimum Spanning Tree (MST)](#minimum-spanning-tree-mst)
  - [Kruskal's Algorithm](#kruskals-algorithm)
  - [Prim's Algorithm](#prims-algorithm)
  - [Cut-Set Properties](#cut-set-properties)
  - [Number of Spanning Trees](#number-of-spanning-trees)
- [Examples](#examples)
  - [Example 1: Finding MST using Kruskal's Algorithm](#example-1-finding-mst-using-kruskals-algorithm)
  - [Example 2: Finding MST using Prim's Algorithm](#example-2-finding-mst-using-prims-algorithm)
  - [Example 3: Application of Cut Property](#example-3-application-of-cut-property)
- [Exam Tips](#exam-tips)

## Introduction

A spanning tree is a fundamental concept in graph theory that plays a crucial role in network design, circuit analysis, and optimization problems. A spanning tree of a connected graph is a subgraph that includes all vertices of the original graph while containing exactly (n-1) edges, where n is the number of vertices. This ensures that the subgraph remains connected and acyclic—meaning it contains no cycles.

The importance of spanning trees in computer science and engineering cannot be overstated. In computer networks, spanning trees are used to prevent loops in Ethernet networks through protocols like STP (Spanning Tree Protocol). In electrical circuits, they help analyze circuit behavior using fundamental cut-set and loop analysis. In transportation and communication networks, spanning trees provide the most efficient way to connect all nodes with minimal infrastructure. Furthermore, minimum spanning trees (MST) are essential for clustering analysis, image segmentation, and various approximation algorithms.

This module covers the properties of spanning trees, algorithms to find minimum spanning trees (Kruskal's and Prim's algorithms), cut-set properties, and the enumeration of spanning trees. These concepts form the backbone of many practical applications in computer networks, transportation systems, and optimization problems.

## Key Concepts

### Definition and Basic Properties

A **spanning tree** T of a connected graph G = (V, E) is a subgraph that satisfies:

- T includes all vertices of G (hence "spanning")
- T is a tree (connected and acyclic)
- T has exactly |V| - 1 edges

**Properties of Spanning Trees:**

1. A connected graph with n vertices always has at least one spanning tree
2. Every spanning tree of a graph with n vertices has exactly n-1 edges
3. Adding any edge to a spanning tree creates exactly one cycle
4. Removing any edge from a spanning tree disconnects the graph
5. A spanning tree is a maximal acyclic subgraph (cannot add more edges without creating cycles)

### Minimum Spanning Tree (MST)

Given a weighted connected graph, a **minimum spanning tree** is a spanning tree with minimum total weight. The total weight is the sum of weights of all edges in the tree.

**Key Properties of MST:**

- **Cut Property**: For any cut of the graph, the minimum weight edge crossing the cut belongs to some MST
- **Cycle Property**: For any cycle in the graph, the maximum weight edge in that cycle cannot belong to any MST

### Kruskal's Algorithm

Kruskal's algorithm is a greedy algorithm that builds the MST by adding edges in increasing order of weight, ensuring no cycles are created.

**Algorithm Steps:**

1. Sort all edges in non-decreasing order of their weights
2. Initialize a disjoint-set data structure for all vertices
3. For each edge (u, v) in sorted order:

- If u and v are in different components, add edge to MST and union the components

4. Repeat until MST has (n-1) edges

**Time Complexity**: O(E log E) or O(E log V) using appropriate data structures

### Prim's Algorithm

Prim's algorithm grows the MST by starting from an arbitrary vertex and repeatedly adding the minimum weight edge that connects a vertex in the tree to a vertex outside the tree.

**Algorithm Steps:**

1. Start with an arbitrary vertex as the initial tree
2. Maintain a priority queue of edges connecting tree vertices to non-tree vertices
3. Extract the minimum weight edge that connects to an unvisited vertex
4. Add the vertex and edge to MST
5. Repeat until all vertices are included

**Time Complexity**: O(V²) for naive implementation, O(E log V) with binary heap

### Cut-Set Properties

A **cut-set** of a connected graph with respect to a spanning tree T is the set of all edges in T whose removal disconnects the graph. Each cut-set contains exactly one edge from every fundamental cycle with respect to T.

**Properties:**

- Every edge of a spanning tree defines a cut-set (the fundamental cut-set)
- The edge weights in a cut-set satisfy the cut property for MST

### Number of Spanning Trees

For a complete graph Kₙ with n vertices, the number of spanning trees is n^(n-2) (Cayley's Formula). This significant result shows that even a simple complete graph has an enormous number of spanning trees.

## Examples

### Example 1: Finding MST using Kruskal's Algorithm

Consider a graph with vertices {A, B, C, D, E} and weighted edges:

- AB: 2, AC: 3, AD: 4, AE: 5, BC: 1, BD: 6, CD: 2, DE: 3

**Solution:**

Step 1: Sort edges by weight:
BC(1), AB(2), CD(2), AC(3), DE(3), AD(4), AE(5), BD(6)

Step 2-3: Process edges:

- BC(1): A and C in different components → Add BC, components: {B,C}, {A}, {D}, {E}
- AB(2): A and B in different components → Add AB, components: {A,B,C}, {D}, {E}
- CD(2): C and D in different components → Add CD, components: {A,B,C,D}, {E}
- AC(3): A and C already in same component → Skip (would create cycle)
- DE(3): D and E in different components → Add DE, components: {A,B,C,D,E}

MST edges: BC, AB, CD, DE
Total weight: 1 + 2 + 2 + 3 = 8

### Example 2: Finding MST using Prim's Algorithm

Using the same graph, starting from vertex A:

**Solution:**

Step 1: Start from A, tree = {A}
Edges from A: AB(2), AC(3), AD(4), AE(5)

Step 2: Pick minimum AB(2), add B to tree
Tree: {A, B}, Edges: AC(3), AD(4), AE(5), BC(1)

Step 3: Pick minimum BC(1), add C to tree
Tree: {A, B, C}, Edges: AD(4), AE(5), CD(2)

Step 4: Pick minimum CD(2), add D to tree
Tree: {A, B, C, D}, Edges: AE(5), DE(3)

Step 5: Pick minimum DE(3), add E to tree
Tree: {A, B, C, D, E}

MST edges: AB, BC, CD, DE
Total weight: 2 + 1 + 2 + 3 = 8

### Example 3: Application of Cut Property

Consider finding MST edge for a cut {A, B} | {C, D, E}:

Edges crossing the cut: AC(3), AD(4), BC(1)
Minimum is BC(1), which must be in the MST—verifying our previous results.

## Exam Tips

1. **Remember the edge count**: Any spanning tree of a graph with n vertices must have exactly n-1 edges—this is frequently tested.

2. **Kruskal vs Prim selection**: Use Kruskal's for sparse graphs (E ≈ V) and Prim's for dense graphs (E ≈ V²).

3. **Cycle and Cut properties**: These are fundamental to proving correctness of MST algorithms and are often asked in proofs.

4. **Cayley's Formula**: Remember Kₙ has n^(n-2) spanning trees—this appears in various forms.

5. **Spanning tree vs Minimum spanning tree**: A spanning tree exists in every connected graph; an MST requires weighted edges and optimization.

6. **Time complexities**: Know that Prim's is O(V²) naive and O(E log V) with heap; Kruskal's is O(E log V).

7. **Disjoint-set in Kruskal's**: Understanding union-find with path compression and union by rank is essential for implementing Kruskal's efficiently.
