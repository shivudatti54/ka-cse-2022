# Isolated Vertex, Pendant Vertex, and Null Graph

## Table of Contents

- [Isolated Vertex, Pendant Vertex, and Null Graph](#isolated-vertex-pendant-vertex-and-null-graph)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Isolated Vertex](#isolated-vertex)
  - [Pendant Vertex (Leaf Vertex)](#pendant-vertex-leaf-vertex)
  - [Null Graph](#null-graph)
  - [Complete Graph](#complete-graph)
  - [Degree Sequence](#degree-sequence)
- [Examples](#examples)
  - [Example 1: Identifying Special Vertices](#example-1-identifying-special-vertices)
  - [Example 2: Null Graph Verification](#example-2-null-graph-verification)
  - [Example 3: Graph with Multiple Special Vertices](#example-3-graph-with-multiple-special-vertices)
  - [Example 4: Degree Sequence Analysis](#example-4-degree-sequence-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Graph theory is a fundamental branch of discrete mathematics that deals with objects called graphs, which consist of vertices (or nodes) connected by edges. In the study of graphs, understanding the properties of individual vertices and their relationships to the rest of the graph is essential. This topic covers three important types of vertices and graphs: isolated vertices, pendant vertices (also called leaf vertices), and null graphs.

These concepts form the building blocks for more advanced topics in graph theory and have practical applications in computer science, network analysis, social sciences, and various engineering disciplines. Whether analyzing computer networks, transportation systems, or social relationships, identifying special vertices helps in understanding the overall structure and behavior of the graph.

## Key Concepts

### Isolated Vertex

An **isolated vertex** is a vertex in a graph that has no edges connected to it. In other words, the degree of an isolated vertex is zero. Mathematically, a vertex v is isolated if deg(v) = 0.

**Properties of Isolated Vertices:**

- No adjacency with any other vertex
- Cannot be reached from any other vertex in the graph
- In adjacency matrix representation, the corresponding row and column contain all zeros
- Does not participate in any path or cycle within the graph

### Pendant Vertex (Leaf Vertex)

A **pendant vertex** (also called a leaf vertex or end vertex) is a vertex with degree exactly equal to 1. This means the vertex is connected to exactly one other vertex in the graph.

**Properties of Pendant Vertices:**

- Degree = 1
- Connected to exactly one other vertex
- Often represents endpoints or terminals in networks
- Important in tree structures where they represent leaf nodes
- In trees, pendant vertices are the leaves of the tree

**Difference between Isolated and Pendant:**

- Isolated vertex: degree = 0 (no connections)
- Pendant vertex: degree = 1 (exactly one connection)

### Null Graph

A **null graph** (also called empty graph or edgeless graph) is a graph that contains no edges. It may consist of one or more isolated vertices. The null graph with n vertices is denoted as Nₙ or Øₙ.

**Types of Null Graphs:**

1. **Trivial Null Graph**: A null graph with a single vertex (also considered as a trivial graph)
2. **Empty Graph**: A null graph with multiple vertices, all isolated

**Properties of Null Graphs:**

- All vertices have degree 0
- No edges exist in the graph
- Not connected (unless it has only one vertex)
- Adjacency matrix is a zero matrix
- Complement of a complete graph

### Complete Graph

Understanding null graphs requires knowing about complete graphs. A **complete graph** Kₙ is a graph where every pair of distinct vertices is connected by a unique edge. The complement of Kₙ (adding all missing edges to Kₙ to make it complete) results in a null graph.

### Degree Sequence

The degree sequence of a graph is a list of vertex degrees, usually written in non-increasing order. For graphs with isolated or pendant vertices:

- Isolated vertices contribute 0 to the degree sequence
- Pendant vertices contribute 1 to the degree sequence

## Examples

### Example 1: Identifying Special Vertices

Consider a graph G with vertices {A, B, C, D, E} and edges {(A,B), (B,C), (C,D)}.

**Solution:**

- Vertex A: degree 1 (connected to B only) → **Pendant vertex**
- Vertex B: degree 2 (connected to A and C)
- Vertex C: degree 2 (connected to B and D)
- Vertex D: degree 1 (connected to C only) → **Pendant vertex**
- Vertex E: degree 0 (no connections) → **Isolated vertex**

### Example 2: Null Graph Verification

Determine if the following graph is a null graph:

- Vertices: {P, Q, R, S}
- Edges: ∅ (empty set)

**Solution:**
Since there are no edges in the graph, this is a null graph N₄. All vertices P, Q, R, and S are isolated vertices with degree 0. The adjacency matrix would be a 4×4 zero matrix.

### Example 3: Graph with Multiple Special Vertices

Consider a graph with 6 vertices where vertex V₁ connects only to V₂, V₂ connects to V₁ and V₃, V₃ connects to V₂ and V₄, V₄ connects to V₃, and V₅ and V₆ are not connected to anyone.

**Solution:**

- V₁: degree 1 → Pendant vertex
- V₂: degree 2
- V₃: degree 2
- V₄: degree 1 → Pendant vertex
- V₅: degree 0 → Isolated vertex
- V₆: degree 0 → Isolated vertex

This graph contains: 2 pendant vertices, 2 isolated vertices, and 2 vertices of degree 2.

### Example 4: Degree Sequence Analysis

A graph has 5 vertices with degrees: 3, 2, 1, 0, 0. Identify the special vertices.

**Solution:**

- Degree 0 vertices: 2 vertices → These are isolated vertices
- Degree 1 vertex: 1 vertex → This is a pendant vertex
- Degree 2 vertex: 1 vertex
- Degree 3 vertex: 1 vertex

## Exam Tips

1. **Remember Definitions Clearly**: For exams, memorize that isolated vertex has degree 0, while pendant vertex has degree 1.

2. **Check Adjacency Matrix**: In graph representation questions, an isolated vertex will have a row/column of all zeros in the adjacency matrix.

3. **Tree Properties**: In trees (acyclic connected graphs), pendant vertices are called leaves, and every tree with at least 2 vertices has at least two pendant vertices.

4. **Null Graph Notation**: Remember that null graph with n vertices is denoted as Nₙ or Øₙ.

5. **Complement Relationship**: The complement of a complete graph Kₙ is the null graph Nₙ, and vice versa.

6. **Degree Sum Formula**: Using Handshaking Lemma, sum of all degrees = 2 × (number of edges). This helps verify your answers.

7. **Graph Classification**: A graph with all vertices isolated is a null graph; a single vertex with no edges is both a null graph and a trivial graph.

8. **Practical Applications**: Pendant vertices often represent endpoints in networks, while isolated vertices represent disconnected components.
