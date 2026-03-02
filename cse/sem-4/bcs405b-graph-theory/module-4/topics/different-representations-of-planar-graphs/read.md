# Different Representations of Planar Graphs

## Table of Contents

- [Different Representations of Planar Graphs](#different-representations-of-planar-graphs)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Planar Graphs](#definition-of-planar-graphs)
  - [Geometric Representations](#geometric-representations)
  - [Combinatorial Representations](#combinatorial-representations)
  - [Planar Graph Isomorphism](#planar-graph-isomorphism)
  - [Dual Graphs](#dual-graphs)
  - [Face Adjacency List](#face-adjacency-list)
- [Examples](#examples)
  - [Example 1: Representing K₄ (Complete Graph on 4 vertices)](#example-1-representing-k-complete-graph-on-4-vertices)
  - [Example 2: Building a Half-Edge Structure](#example-2-building-a-half-edge-structure)
  - [Example 3: Computing the Dual Graph](#example-3-computing-the-dual-graph)
- [Exam Tips](#exam-tips)

## Introduction

Planar graphs are fundamental structures in graph theory with extensive applications in computer science, circuit design, road networks, and geographical mapping. A graph is said to be planar if it can be drawn on a plane without any of its edges crossing each other. The study of planar graphs is essential because many real-world problems can be modeled as planar graphs, and their special properties allow for more efficient algorithms.

Understanding different representations of planar graphs is crucial for both theoretical analysis and practical implementation. While a graph can be represented in various ways, the representation chosen significantly impacts the efficiency of graph algorithms. For planar graphs specifically, certain representations take advantage of the special properties that arise from planarity, leading to more compact storage and faster processing. This module explores the geometric, combinatorial, and algebraic methods used to represent planar graphs, along with their advantages and applications.

## Key Concepts

### Definition of Planar Graphs

A graph G = (V, E) is called planar if it can be embedded in the plane such that no two edges intersect except at their common vertices. This embedding is called a planar embedding or plane graph. The regions bounded by the edges are called faces, and the unbounded outer region is called the outer face. A planar graph with a specific embedding is referred to as a plane graph.

**Important Properties:**

- A planar graph with n vertices (n ≥ 3) satisfies Euler's formula: n - m + f = 2, where n is the number of vertices, m is the number of edges, and f is the number of faces.
- For a connected planar simple graph with n ≥ 3 and m edges, we have m ≤ 3n - 6.
- Every planar graph has a vertex of degree at most 5.

### Geometric Representations

Geometric representations involve visual or coordinate-based descriptions of planar graphs. The most common geometric representation is the planar embedding that shows the actual layout of vertices and edges on a plane.

**Types of Geometric Representations:**

1. **Straight-Line Embedding**: Every edge is drawn as a straight line segment. By Fáry's theorem, every planar graph can be represented with straight-line edges.

2. **Radial Embedding**: Vertices are placed on concentric circles (or rays from a center), with edges drawn as curves connecting them.

3. **Circular Embedding**: All vertices are placed on a circle, and edges are drawn as chords inside the circle. This is particularly useful for outerplanar graphs.

4. **Grid Embedding**: Vertices are placed on integer grid points. This representation is valuable for VLSI design and computational geometry applications.

### Combinatorial Representations

Combinatorial representations capture the structure of planar graphs through data structures that can be processed by computers.

#### 1. Adjacency Matrix

For a graph with n vertices, the adjacency matrix A is an n × n matrix where A[i][j] = 1 if there is an edge between vertices i and j, and 0 otherwise.

**Advantages:**

- O(1) edge lookup
- Simple to implement
- Suitable for dense graphs

**Disadvantages:**

- Requires O(n²) space regardless of edges
- Inefficient for sparse planar graphs

#### 2. Incidence Matrix

For a graph with n vertices and m edges, the incidence matrix B is an n × m matrix where B[i][j] = 1 if vertex i is incident to edge j, and 0 otherwise.

**For Planar Graphs:**
The incidence matrix is particularly useful when combined with face information. The boundary of each face can be represented using the incidence relationships.

#### 3. Adjacency List

Each vertex maintains a list of its neighboring vertices. This is the most common representation for planar graphs in practice.

**Structure:**

```
Vertex 0: → 1 → 2 → 3
Vertex 1: → 0 → 2
Vertex 2: → 0 → 1 → 3
Vertex 3: → 0 → 2
```

**Advantages:**

- Space-efficient: O(n + m) where m is edges
- Efficient for graph traversal
- Suitable for sparse planar graphs

**Disadvantages:**

- Edge lookup is O(degree)

#### 4. Half-Edge Data Structure (DCEL)

The Half-Edge data structure (also called Doubly-Connected Edge List or DCEL) is specifically designed for planar subdivisions and is extensively used in computational geometry.

**Components:**

- **Vertex**: Stores coordinates and a reference to one outgoing half-edge
- **Half-Edge**: Represents half of an edge, stores reference to origin vertex, next half-edge, and twin half-edge
- **Face**: Stores reference to one half-edge on its boundary

This representation allows efficient traversal of faces, which is essential for many planar graph algorithms.

### Planar Graph Isomorphism

Two planar graphs are isomorphic if there exists a one-to-one correspondence between their vertices that preserves adjacency. For planar graphs, we can consider planar isomorphism, which requires not only vertex correspondence but also face preservation.

**Key Points:**

- Testing planar graph isomorphism is not known to be NP-complete
- The planar isomorphism problem can be solved in O(n²) time
- Canonical labeling is often used to test isomorphism

### Dual Graphs

For a plane graph G, the dual graph G\* is constructed by:

1. Creating a vertex in G\* for each face of G
2. Creating an edge in G\* between two vertices if the corresponding faces in G share a common edge
3. Adding a loop for each bridge in the original graph

**Properties of Dual Graphs:**

- If G is a connected planar graph, then (G*)* ≅ G
- The dual of a planar graph is also planar
- Duality is fundamental in many applications including network flow and electrical networks

**Example:**
For a square with diagonals:

- Original graph: 4 vertices, 6 edges, 4 faces
- Dual graph: 4 vertices (one for each face), edges correspond to shared boundaries

### Face Adjacency List

In planar graphs, it is often useful to store information about faces. The face adjacency list stores, for each face, the cyclic order of edges (or vertices) that bound it.

**Representation:**

- Each face stores a circular list of half-edges in counterclockwise order
- Allows O(1) access to neighboring faces
- Essential for algorithms like face traversal and planar embedding

## Examples

### Example 1: Representing K₄ (Complete Graph on 4 vertices)

K₄ is planar. Let's examine different representations:

**Adjacency Matrix (4×4):**

```
 0 1 2 3
0 0 1 1 1
1 1 0 1 1
2 1 1 0 1
3 1 1 1 0
```

**Adjacency List:**

```
0: 1, 2, 3
1: 0, 2, 3
2: 0, 1, 3
3: 0, 1, 2
```

**Verification of Planarity using Euler's Formula:**

- n = 4, m = 6
- For planar: m ≤ 3n - 6 = 3(4) - 6 = 6
- m = 6 satisfies the condition
- Number of faces: f = 2 - n + m = 2 - 4 + 6 = 4
- This is correct: 4 triangular faces (including outer face)

### Example 2: Building a Half-Edge Structure

Consider a triangle (3-cycle) with vertices A, B, C:

**Half-Edge Structure:**

- Half-edges: AB, BA, BC, CB, CA, AC
- Each vertex points to one outgoing half-edge
- Each face contains 3 half-edges in cyclic order

**Operations:**

- Starting from any half-edge, we can traverse the entire boundary of a face using the "next" pointer
- The "twin" pointer allows us to move between adjacent faces

This representation enables efficient algorithms like:

- Finding all faces: O(n)
- Traversing face boundaries: O(length of boundary)
- Finding neighboring faces: O(1)

### Example 3: Computing the Dual Graph

Given a planar graph representing a square with diagonals:

**Original Graph G:**

- Vertices: v1, v2, v3, v4 (corners)
- Edges: v1-v2, v2-v3, v3-v4, v4-v1 (boundary), v1-v3, v2-v4 (diagonals)
- Faces: f1 (inner square), f2 (outer region)

**Dual Graph G\*:**

- Vertices: f1*, f2* (one for each face)
- Edge: Between f1* and f2* (since faces share edges)

**Extended Example with More Detail:**
For a cube projection (planar graph with 8 vertices, 12 edges, 6 faces):

- Dual has 6 vertices (one per face)
- Each vertex in dual has degree 4
- The dual of a cube projection is the octahedron graph

## Exam Tips

1. **Euler's Formula Application**: Remember n - m + f = 2 for connected planar graphs. This is frequently tested in university exams.

2. **Planarity Condition**: For simple planar graphs with n ≥ 3, always verify m ≤ 3n - 6. This inequality is crucial for proving non-planarity.

3. **Representation Choice**: Know when to use each representation - adjacency matrix for dense graphs, adjacency lists for sparse planar graphs, half-edge for face-related operations.

4. **Dual Graph Properties**: Remember that (G*)* ≅ G for connected planar graphs. This is a fundamental property often tested.

5. **Fáry's Theorem**: Every planar graph can be drawn with straight lines - this is important for geometric representations.

6. **Space Complexity**: Adjacency matrix requires O(n²) space, while adjacency list requires O(n + m). For planar graphs, m ≤ 3n - 6, so space is O(n).

7. **Face Traversal**: The half-edge (DCEL) structure is optimal for operations involving faces, as it provides O(1) access to adjacent faces.

8. **Minimum Degree**: In a planar graph with n ≥ 3, there always exists a vertex with degree at most 5. This is useful for recursive planarity testing algorithms.
