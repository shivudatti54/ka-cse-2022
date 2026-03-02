# Fundamental Circuits

## Table of Contents

- [Fundamental Circuits](#fundamental-circuits)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Spanning Tree](#spanning-tree)
  - [Fundamental Circuit Definition](#fundamental-circuit-definition)
  - [Properties of Fundamental Circuits](#properties-of-fundamental-circuits)
  - [Finding Fundamental Circuits](#finding-fundamental-circuits)
  - [Fundamental Circuit Matrix](#fundamental-circuit-matrix)
- [Examples](#examples)
  - [Example 1: Simple Graph Fundamental Circuit](#example-1-simple-graph-fundamental-circuit)
  - [Example 2: Complete Graph K4](#example-2-complete-graph-k4)
  - [Example 3: Applying in Circuit Analysis](#example-3-applying-in-circuit-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Fundamental circuits are a fundamental concept in graph theory that plays a crucial role in understanding the cycle structure of graphs. In electrical network analysis and graph theory, circuits represent closed paths that allow us to analyze various properties of networks, including connectivity, independence, and topological relationships. The concept of fundamental circuits was developed to provide a systematic way of describing all possible cycles in a graph using a spanning tree as a foundation.

In the context of the university's Graph Theory syllabus, fundamental circuits hold significant importance as they form the basis for understanding the cycle space of a graph. This concept is extensively used in network flow analysis, electrical circuit theory, and combinatorial optimization. A fundamental circuit (also known as a fundamental cycle) is generated when we add exactly one edge (called a chord) to a spanning tree of the graph. This unique relationship between trees, chords, and cycles provides powerful analytical tools for solving complex graph-related problems.

The study of fundamental circuits connects deeply with several other graph theory concepts including cut sets, rank-nullity theorem, and matrix representations of graphs. Understanding this topic is essential for students pursuing computer science and engineering, as these concepts find applications in circuit design, network routing, and algorithm development.

## Key Concepts

### Spanning Tree

A spanning tree of a connected graph G is a subgraph that is a tree and includes all vertices of G. If a graph has n vertices, any spanning tree will have exactly n-1 edges. A spanning tree is maximal in the sense that adding any edge (that is not already in the tree) creates a cycle. This property is fundamental to understanding why fundamental circuits exist and how they are constructed.

There can be multiple spanning trees for a given graph. The choice of spanning tree affects the set of fundamental circuits obtained. For a complete graph with n vertices, the number of spanning trees is given by Cayley's formula: n^(n-2).

### Fundamental Circuit Definition

Let T be a spanning tree of a connected graph G. Let e be an edge of G that is not in T (called a chord or cotree edge). When we add this edge e to the tree T, we create a unique simple cycle C in G. This cycle C is called the **fundamental circuit** with respect to the edge e and the spanning tree T.

Formally, if T is a spanning tree of G and e ∈ E(G) - E(T), then the fundamental circuit C(T, e) is the unique cycle in T + e. The fundamental circuit consists of the edge e plus the unique path in T connecting the two endpoints of e.

### Properties of Fundamental Circuits

1. **Uniqueness**: For a given spanning tree T and a chord e, there is exactly one fundamental circuit. This uniqueness arises from the acyclic nature of trees - there is only one path between any two vertices in a tree.

2. **Number of Fundamental Circuits**: If a connected graph G has n vertices and m edges, then the number of fundamental circuits (with respect to any spanning tree) is exactly m - n + 1, which is equal to the cycle rank (or cyclomatic number) of the graph.

3. **Independence**: The set of all fundamental circuits (with respect to a fixed spanning tree) forms a basis for the cycle space of the graph. This means any cycle in the graph can be expressed as a symmetric difference of fundamental circuits.

4. **Cycle Rank**: The number m - n + 1 is called the cycle rank or cyclomatic number of the graph. It represents the minimum number of cycles needed to generate all cycles in the graph.

### Finding Fundamental Circuits

To find fundamental circuits:

1. First, construct any spanning tree T of the graph G using algorithms like Prim's, Kruskal's, or DFS/BFS
2. Identify all edges not in T (the chords)
3. For each chord e, find the unique path in T connecting the endpoints of e
4. The fundamental circuit for e is the path in T plus the edge e itself

### Fundamental Circuit Matrix

The fundamental circuit matrix (or fundamental cycle matrix) is an (m - n + 1) × m matrix used in graph theory and network analysis. Each row corresponds to a fundamental circuit, and each column corresponds to an edge. The entry is 1 if the edge is in the circuit, 0 otherwise.

## Examples

### Example 1: Simple Graph Fundamental Circuit

Consider a graph G with vertices {v1, v2, v3, v4} and edges: {v1v2, v2v3, v3v4, v4v1, v1v3}.

This graph has n = 4 vertices and m = 5 edges.

**Step 1: Find a spanning tree T**
Using any method, let's select edges {v1v2, v2v3, v3v4} as our spanning tree T.
These are n-1 = 3 edges and connect all vertices without creating cycles.

**Step 2: Identify chords**
The edges not in T are: {v4v1, v1v3}
These are the chords (cotree edges).

**Step 3: Find fundamental circuits**

For chord v4v1:

- Endpoints are v4 and v1
- Path in T from v4 to v1: v4 → v3 → v2 → v1
- Fundamental circuit: {v4v1, v3v4, v2v3, v1v2}

For chord v1v3:

- Endpoints are v1 and v3
- Path in T from v1 to v3: v1 → v2 → v3
- Fundamental circuit: {v1v3, v1v2, v2v3}

**Verification**: Number of fundamental circuits = m - n + 1 = 5 - 4 + 1 = 2 ✓

### Example 2: Complete Graph K4

Consider the complete graph K4 with vertices {v1, v2, v3, v4} containing all 6 possible edges.

n = 4, m = 6
Number of fundamental circuits = 6 - 4 + 1 = 3

**Spanning Tree T**: Choose edges {v1v2, v2v3, v3v4}

**Chords**: {v1v3, v1v4, v2v4}

**Fundamental Circuits:**

1. For chord v1v3:

- Path in T: v1 → v2 → v3
- Circuit: v1v3 + v1v2 + v2v3

2. For chord v1v4:

- Path in T: v1 → v2 → v3 → v4
- Circuit: v1v4 + v1v2 + v2v3 + v3v4

3. For chord v2v4:

- Path in T: v2 → v3 → v4
- Circuit: v2v4 + v2v3 + v3v4

These three fundamental circuits form a basis for the cycle space of K4.

### Example 3: Applying in Circuit Analysis

Consider an electrical network represented as a graph with 5 nodes and 7 edges. To analyze independent loops:

n = 5, m = 7
Number of fundamental circuits = 7 - 5 + 1 = 3

This tells us there are exactly 3 independent loops in the network. Any other loop in the network can be expressed as a combination (symmetric difference) of these 3 fundamental circuits.

If we apply Kirchhoff's Voltage Law, we would write equations for these 3 fundamental circuits to solve for unknown currents or voltages in the network.

## Exam Tips

1. **Remember the formula**: Number of fundamental circuits = m - n + 1 (cyclomatic number). This is frequently asked in university exams.

2. **Key definition**: A fundamental circuit is the unique cycle formed when adding one chord to a spanning tree.

3. **Properties to remember**: Fundamental circuits are unique for each chord-tree pair and form a basis for the cycle space.

4. **Procedure for finding fundamental circuits**: Always first construct a spanning tree, then identify chords, then find the unique path in the tree.

5. **Distinguish between tree edges and chords**: Tree edges (n-1 edges) form the spanning tree; chords (m-n+1 edges) are the remaining edges.

6. **Application in rank-nullity**: The cycle rank m - n + 1 equals the dimension of the cycle space, which is nullity of the graph's incidence matrix.

7. **Understand basis concept**: Any cycle in the graph can be expressed as XOR/symmetric difference of fundamental circuits.

8. **Remember: More than one spanning tree is possible**: Different spanning trees yield different sets of fundamental circuits, but all sets have the same size (m - n + 1).
