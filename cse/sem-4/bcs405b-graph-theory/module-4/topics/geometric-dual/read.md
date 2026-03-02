# Geometric Dual

## Table of Contents

- [Geometric Dual](#geometric-dual)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Geometric Dual](#definition-of-geometric-dual)
  - [Properties of Geometric Dual](#properties-of-geometric-dual)
  - [Self-Dual Graphs](#self-dual-graphs)
  - [Relationship with Combinatorial Dual](#relationship-with-combinatorial-dual)
- [Examples](#examples)
  - [Example 1: Dual of a Triangle](#example-1-dual-of-a-triangle)
  - [Example 2: Dual of a Square with Diagonal](#example-2-dual-of-a-square-with-diagonal)
  - [Example 3: Self-Dual Graph Verification](#example-3-self-dual-graph-verification)
- [Exam Tips](#exam-tips)

## Introduction

The geometric dual is a fundamental concept in graph theory that establishes a relationship between two planar graphs. Given a planar embedding of a graph, we can construct its geometric dual by placing a vertex in each face of the original graph and connecting vertices whose corresponding faces share a common edge. This concept is crucial in understanding the topological properties of planar graphs and has significant applications in computer science, circuit design, and geographical information systems.

The study of geometric dual is particularly important for the university's BCS405B Graph Theory course as it appears in Module 4. This topic builds upon previous knowledge of planar graphs, Euler's formula, and graph embeddings. Understanding geometric dual helps students analyze the relationships between different planar representations and solve complex graph theoretical problems that frequently appear in university examinations.

The geometric dual possesses several remarkable properties that make it theoretically significant. For instance, the dual of a dual returns to the original graph (under certain conditions), and many graph properties such as connectivity and planarity have dual counterparts. These properties make geometric dual an essential tool for both theoretical analysis and practical applications in network design and optimization.

## Key Concepts

### Definition of Geometric Dual

Given a connected planar graph G with a planar embedding, the **geometric dual** G\* is constructed as follows:

1. Place a vertex in each face of G (including the outer face)
2. For each edge e of G that separates two faces f₁ and f₂, create an edge in G\* connecting the vertices corresponding to f₁ and f₂
3. If an edge belongs to only one face (i.e., it's a bridge or on the boundary of the outer face), create a loop in G\*

**Important Note**: The geometric dual depends on the specific embedding of the graph. Different embeddings of the same abstract graph can yield non-isomorphic geometric duals.

### Properties of Geometric Dual

1. **Vertex-Face Correspondence**: The number of vertices in G\* equals the number of faces in G.

2. **Edge Correspondence**: The number of edges in G\* equals the number of edges in G.

3. **Face-Vertex Correspondence**: The degree of each vertex in G\* equals the number of edges bounding the corresponding face in G.

4. **Duality Property**: (G*)* ≅ G for connected planar graphs without bridges.

5. **Planarity**: The geometric dual of any planar graph is always planar.

6. **Connectivity**: The dual of a connected planar graph is connected.

### Self-Dual Graphs

A graph G is called **self-dual** if G ≅ G\*. For a planar graph with n vertices, e edges, and f faces, self-duality requires:

- n\* = f (number of vertices in dual equals faces in original)
- e\* = e (number of edges in dual equals edges in original)
- f\* = n (number of faces in dual equals vertices in original)

Using Euler's formula n - e + f = 2, self-dual graphs satisfy n = f, which implies 2n - e = 2, or e = 2n - 2.

### Relationship with Combinatorial Dual

While geometric dual is defined for specific embeddings, the **combinatorial dual** (or abstract dual) is defined for abstract graphs without considering embeddings. A graph H is a combinatorial dual of G if there exists a one-to-one correspondence between edges such that a set of edges in G forms a cycle if and only if the corresponding set in H forms a cut-set. Every geometric dual is a combinatorial dual, but the converse is not always true.

## Examples

### Example 1: Dual of a Triangle

**Problem**: Find the geometric dual of a triangle (K₃) with the standard planar embedding.

**Solution**:

Step 1: Consider the triangle with vertices A, B, C. The embedding has:

- 3 vertices
- 3 edges
- 2 faces (one interior triangle, one exterior region)

Step 2: Place one vertex in each face:

- Let v₁ be the vertex in the interior face
- Let v₂ be the vertex in the exterior face

Step 3: For each edge of the triangle (which separates both faces), connect v₁ and v₂.

Result: The geometric dual of K₃ is a single edge connecting two vertices, which is K₂.

**Verification**:

- Original: n = 3, e = 3, f = 2
- Dual: n* = 2, e* = 3, f\* = 3
- Using Euler's formula for dual: 2 - 3 + 3 = 2 ✓

### Example 2: Dual of a Square with Diagonal

**Problem**: Construct the geometric dual of a square (cycle C₄) with one diagonal drawn inside.

**Solution**:

Step 1: The graph has vertices A, B, C, D with edges AB, BC, CD, DA (forming the square) and AC (diagonal).

Step 2: Count faces:

- Face f₁: Triangle ABC (bounded by AB, BC, AC)
- Face f₂: Triangle ACD (bounded by AC, CD, DA)
- Face f₃: Exterior face (bounded by AB, BC, CD, DA)

Step 3: Create vertices v₁, v₂, v₃ for these three faces.

Step 4: Add edges where faces share boundaries:

- Edge AB is shared by f₁ and f₃ → connect v₁ and v₃
- Edge BC is shared by f₁ and f₃ → connect v₁ and v₃ (parallel edge, creates multiple edges)
- Edge CD is shared by f₂ and f₃ → connect v₂ and v₃
- Edge DA is shared by f₂ and f₃ → connect v₂ and v₃
- Edge AC is shared by f₁ and f₂ → connect v₁ and v₂

Result: The dual has 3 vertices with multiple edges between v₁ and v₃, and between v₂ and v₃.

### Example 3: Self-Dual Graph Verification

**Problem**: Verify that the wheel graph W₄ (a cycle C₄ with a hub vertex connected to all cycle vertices) is self-dual.

**Solution**:

Step 1: W₄ has:

- n = 5 vertices (4 cycle vertices + 1 hub)
- e = 8 edges (4 cycle edges + 4 spokes)
- f = ? (using Euler: 5 - 8 + f = 2, so f = 5)

Step 2: The dual will have:

- n\* = f = 5 vertices
- e\* = e = 8 edges
- f\* = n = 5 faces

Step 3: The dual of W₄ is isomorphic to W₄ itself. This can be verified by noting that in W₄, each face (including the outer face) is bounded by 3 edges, and each vertex (including the hub) has degree 4 in the original, corresponding to faces of size 3 in the dual.

Therefore, W₄ is self-dual.

## Exam Tips

1. **Memorize the Construction Method**: The exam frequently asks students to draw the geometric dual. Remember: place a vertex in each face, connect vertices whose faces share an edge.

2. **Apply Euler's Formula**: Always verify your dual using Euler's formula. For the dual G* of a connected planar graph G: |V(G*)| - |E(G*)| + |F(G*)| = 2.

3. **Count Faces Carefully**: Many students lose marks by incorrectly counting faces. Remember to include the outer (exterior) face.

4. **Handle Bridges and Multiple Edges**: If an edge is a bridge or belongs to only one face, the corresponding edge in the dual becomes a loop.

5. **Understand the Relationship**: The number of vertices in G\* equals the number of faces in G, and the number of edges remains the same.

6. **Self-Dual Condition**: Remember that for self-dual graphs, e = 2n - 2 (derived from Euler's formula and n = f).

7. **Embedding Matters**: Be aware that different embeddings can produce different geometric duals of the same abstract graph.

8. **Dual of Dual**: For connected planar graphs without bridges, (G*)* ≅ G. This is an important property often tested in exams.
