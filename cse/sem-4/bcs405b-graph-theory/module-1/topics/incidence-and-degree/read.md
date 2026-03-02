# Incidence and Degree in Graph Theory

## Table of Contents

- [Incidence and Degree in Graph Theory](#incidence-and-degree-in-graph-theory)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Definitions](#basic-definitions)
  - [Degree of a Vertex](#degree-of-a-vertex)
  - [Special Vertex Types](#special-vertex-types)
  - [The Handshaking Lemma](#the-handshaking-lemma)
  - [Degree Sequence](#degree-sequence)
  - [Regular Graphs](#regular-graphs)
  - [Complete Graphs](#complete-graphs)
  - [Bipartite Graphs](#bipartite-graphs)
  - [Subgraphs](#subgraphs)
- [Examples](#examples)
  - [Example 1: Identifying Vertex Types and Computing Degrees](#example-1-identifying-vertex-types-and-computing-degrees)
  - [Example 2: Checking if a Sequence is Graphical](#example-2-checking-if-a-sequence-is-graphical)
  - [Example 3: Properties of Complete Bipartite Graph](#example-3-properties-of-complete-bipartite-graph)
- [Exam Tips](#exam-tips)

## Introduction

Graph theory is a fundamental branch of discrete mathematics that deals with objects called graphs, which consist of vertices (or nodes) connected by edges. This module introduces the foundational concepts of incidence and degree, which are essential for understanding the structure and properties of graphs. These concepts form the building blocks for more advanced topics in graph theory, including connectivity, Eulerian and Hamiltonian paths, and graph coloring.

The study of incidence and degree is crucial in computer science and engineering applications. Network routing, social network analysis, transportation systems, and data structures all rely on understanding how vertices are connected and the extent of their connections. In the context of the university's BCS405B Graph Theory course, mastering these concepts is essential for solving problems related to graph characterization and analysis.

## Key Concepts

### Basic Definitions

A **graph** G = (V, E) consists of a finite non-empty set V of vertices (or nodes) and a set E of edges (or arcs). Each edge is associated with an unordered pair of vertices, called its endpoints. When an edge connects two vertices u and v, we say it is **incident** to both u and v, and similarly, u and v are incident to that edge.

**Simple graphs** are those that do not contain multiple edges between the same pair of vertices (no parallel edges) and no loops (edges connecting a vertex to itself). This course primarily focuses on simple graphs unless otherwise specified.

### Degree of a Vertex

The **degree** of a vertex v in a graph G, denoted as deg(v) or d(v), is the number of edges incident to v. When counting degree, each loop is counted twice (since it is incident to the same vertex at both ends). In a simple graph, the degree is simply the count of edges connected to that vertex.

**Maximum degree** (Δ(G)) represents the largest degree among all vertices in G, while **minimum degree** (δ(G)) represents the smallest degree. The relationship between these quantities provides important information about graph structure.

### Special Vertex Types

- **Isolated vertex**: A vertex with degree zero, meaning it has no edges connecting it to any other vertex. In practical terms, an isolated vertex stands alone in the graph with no connections.

- **Pendant vertex** (or leaf): A vertex with degree one, connected to exactly one other vertex. These vertices appear frequently in tree structures and represent endpoints or leaves in various applications.

- **Vertex of even degree**: A vertex where the degree is divisible by 2 (0, 2, 4, 6, ...).

- **Vertex of odd degree**: A vertex where the degree is not divisible by 2 (1, 3, 5, 7, ...).

### The Handshaking Lemma

One of the most fundamental theorems in graph theory, the **Handshaking Lemma**, states: In any graph, the sum of the degrees of all vertices equals twice the number of edges.

Mathematically: Σ\_{v∈V} deg(v) = 2|E|

This theorem is called the Handshaking Lemma because it can be interpreted as: in any gathering of people, if everyone shakes hands with everyone else, the total number of handshakes equals half the sum of all handshakes made by each person.

**Corollary**: The number of vertices of odd degree in any graph is always even.

This corollary is particularly useful in university exams, as it provides a quick check for graph validity and appears in various proof problems.

### Degree Sequence

The **degree sequence** of a graph is the sequence of degrees of all vertices, typically written in non-increasing order. For example, if a graph has vertices with degrees 4, 3, 3, 2, 1, 1, the degree sequence is (4, 3, 3, 2, 1, 1).

An important question in graph theory is whether a given sequence of integers is **graphical**, meaning it can be realized as the degree sequence of some graph. The Erdős–Gallai theorem provides necessary and sufficient conditions for a sequence to be graphical, though for simple graphs, the **Havel-Hakimi algorithm** offers a constructive method to check graphicality.

### Regular Graphs

A graph is called **regular** (or k-regular) if all its vertices have the same degree k. Regular graphs have significant theoretical importance and practical applications:

- **0-regular graph**: Contains no edges (empty graph)
- **1-regular graph**: A perfect matching, where every vertex has degree 1
- **2-regular graph**: A disjoint union of cycles
- **3-regular graph**: Also called a cubic graph
- **Complete graph K_n**: (n-1)-regular, since each vertex connects to all other (n-1) vertices

The number of edges in a k-regular graph with n vertices is nk/2, which must be an integer, implying nk must be even.

### Complete Graphs

A **complete graph** K_n is a simple graph where every pair of distinct vertices is connected by a unique edge. Key properties include:

- Number of vertices: n
- Number of edges: n(n-1)/2
- Degree of each vertex: n-1
- Maximum degree: n-1
- Minimum degree: n-1

K_1 is a single vertex with no edges, K_2 is a single edge, K_3 is a triangle, and so on.

### Bipartite Graphs

A **bipartite graph** is a graph whose vertex set can be partitioned into two disjoint sets U and V such that every edge connects a vertex in U to a vertex in V. No edge connects vertices within the same partition. The sets U and V are called the ** bipartition sets**.

A **complete bipartite graph** K\_{m,n} has all possible edges between the two partitions: every vertex in the first set (of size m) connects to every vertex in the second set (of size n). Properties include:

- Total vertices: m + n
- Total edges: mn
- Degree of vertices in first set: n
- Degree of vertices in second set: m

### Subgraphs

A **subgraph** of a graph G is a graph H = (V', E') where V' ⊆ V and E' ⊆ E, with each edge in E' having both endpoints in V'. An **induced subgraph** is formed by taking a subset of vertices and all edges between them that exist in the original graph.

A **spanning subgraph** uses all vertices of the original graph but may have fewer edges. A **spanning tree** is a spanning subgraph that is a tree (connected and acyclic).

## Examples

### Example 1: Identifying Vertex Types and Computing Degrees

Consider a graph G with vertices V = {a, b, c, d, e} and edges E = {ab, ad, ae, bc, bd, cd, de}.

**Solution:**

- Edges list with endpoints:
- ab connects a-b
- ad connects a-d
- ae connects a-e
- bc connects b-c
- bd connects b-d
- cd connects c-d
- de connects d-e

- Degree calculations:
- deg(a) = 3 (edges: ab, ad, ae)
- deg(b) = 3 (edges: ab, bc, bd)
- deg(c) = 2 (edges: bc, cd)
- deg(d) = 4 (edges: ad, bd, cd, de)
- deg(e) = 2 (edges: ae, de)

- Special vertices:
- No isolated vertices (all degrees > 0)
- No pendant vertices (no degree 1)
- Maximum degree: Δ(G) = 4 (vertex d)
- Minimum degree: δ(G) = 2 (vertices c and e)

- Verify Handshaking Lemma:
- Sum of degrees = 3 + 3 + 2 + 4 + 2 = 14
- Number of edges = 7
- 2|E| = 2 × 7 = 14 ✓

### Example 2: Checking if a Sequence is Graphical

Determine if the sequence (5, 4, 3, 2, 2, 1) is graphical.

**Solution using Havel-Hakimi Algorithm:**

1. Sort in descending order: (5, 4, 3, 2, 2, 1) — already sorted

2. Remove first element (5) and subtract 1 from next 5 elements:

- Remove 5: (4, 3, 2, 2, 1)
- Subtract 1 from first 5 elements: (3, 2, 1, 1, 0)

3. Sort descending: (3, 2, 1, 1, 0)

4. Remove first element (3) and subtract 1 from next 3 elements:

- Remove 3: (2, 1, 1, 0)
- Subtract 1: (1, 0, 0, 0)

5. Sort descending: (1, 0, 0, 0)

6. Remove first element (1) and subtract 1 from next 1 element:

- Remove 1: (0, 0, 0)
- Subtract 1: (-1, 0, 0)

Since we get a negative number (-1), the sequence is **not graphical**.

### Example 3: Properties of Complete Bipartite Graph

Find the number of vertices, edges, and degrees in K\_{3,4}.

**Solution:**

For complete bipartite graph K\_{m,n}:

- First partition has m vertices, second partition has n vertices
- Total vertices = m + n = 3 + 4 = 7
- Total edges = m × n = 3 × 4 = 12
- Each vertex in first set (size 3) has degree = n = 4
- Each vertex in second set (size 4) has degree = m = 3
- Maximum degree = 4, Minimum degree = 3

Verification by Handshaking Lemma:

- Sum of degrees = (3 × 4) + (4 × 3) = 12 + 12 = 24
- 2|E| = 2 × 12 = 24 ✓

## Exam Tips

1. **Remember the Handshaking Lemma**: Σdeg(v) = 2|E| is the most frequently tested concept. Always use it to verify your answers or find missing information.

2. **Odd degree corollary**: The number of odd-degree vertices must be even. This is a quick check that appears in many exam problems.

3. **Maximum edges in simple graph**: For n vertices, maximum edges = n(n-1)/2. Know this for complete graph calculations.

4. **Degree sequence properties**: The sum of degrees (which equals 2|E|) must be even. If asked to find the number of edges from degrees, divide sum by 2.

5. **Regular graph edge count**: For k-regular graph with n vertices, edges = nk/2. This must be integer, so nk must be even.

6. **Bipartite recognition**: If asked to determine if a graph is bipartite, check if it contains odd cycles. A graph is bipartite iff it contains no odd cycles.

7. **Complete bipartite properties**: K\_{m,n} has mn edges, and vertices have degrees m or n depending on their partition.

8. **Isomorphism invariance**: Degree sequence is a graph invariant. Isomorphic graphs must have the same degree sequence, but same degree sequence doesn't guarantee isomorphism.

9. **Watch for loops**: Remember that loops contribute 2 to degree. If the problem doesn't specify "simple graph," consider whether loops might be present.

10. **Work systematically**: When solving degree-related problems, list all vertices, identify their incident edges, count carefully, and verify with Handshaking Lemma.
