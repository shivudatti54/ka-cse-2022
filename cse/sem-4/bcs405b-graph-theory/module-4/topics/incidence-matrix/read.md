# Incidence Matrix

## Table of Contents

- [Incidence Matrix](#incidence-matrix)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Incidence Matrix](#definition-of-incidence-matrix)
  - [Properties of Incidence Matrix](#properties-of-incidence-matrix)
  - [Types of Incidence Matrices](#types-of-incidence-matrices)
  - [Incidence Matrix for Special Graphs](#incidence-matrix-for-special-graphs)
- [Examples](#examples)
  - [Example 1: Undirected Graph Incidence Matrix](#example-1-undirected-graph-incidence-matrix)
  - [Example 2: Directed Graph Incidence Matrix](#example-2-directed-graph-incidence-matrix)
  - [Example 3: Finding Graph Properties from Incidence Matrix](#example-3-finding-graph-properties-from-incidence-matrix)
- [Exam Tips](#exam-tips)

## Introduction

The incidence matrix is a fundamental concept in graph theory that provides a powerful algebraic representation of graphs. It is a matrix-based representation that captures the relationship between vertices and edges in a graph. For students studying Graph Theory as part of the CSE curriculum (BCS405B), understanding incidence matrices is essential as it forms the foundation for various graph algorithms and applications in network analysis, electrical circuits, and transportation systems.

The incidence matrix is particularly useful because it allows us to represent complex graph structures in a compact mathematical form that can be easily manipulated using linear algebra techniques. This representation proves invaluable when solving problems related to network flows, circuit analysis, and graph connectivity. The matrix provides a systematic way to analyze the structural properties of graphs and has significant applications in computer science, operations research, and engineering disciplines.

In this module, we will explore the definition, properties, and applications of incidence matrices for both directed and undirected graphs. Understanding this topic is crucial for university exams as it frequently appears in question papers, and mastering it will help you solve complex graph theory problems efficiently.

## Key Concepts

### Definition of Incidence Matrix

For a graph G = (V, E) with n vertices and m edges, the incidence matrix is an n × m matrix denoted by M(G) or sometimes as [M_ij]. Each entry M_ij corresponds to the relationship between vertex i and edge j.

**For Undirected Graphs:**

The incidence matrix M = [m_ij] is defined as:

- m_ij = 1 if vertex i is incident to edge j
- m_ij = 0 otherwise

Each column of the incidence matrix corresponds to exactly two 1's (for edges that are not loops), representing the two endpoints of that edge. For a loop at vertex i, the column will have a single 1 at row i.

**For Directed Graphs:**

For a directed graph (digraph), the incidence matrix M = [m_ij] is defined as:

- m_ij = +1 if edge j leaves vertex i (outgoing edge)
- m_ij = -1 if edge j enters vertex i (incoming edge)
- m_ij = 0 otherwise

Each column in a directed graph incidence matrix will have exactly one +1 and one -1 (except for loops which have either +2 or -2 at the corresponding vertex).

### Properties of Incidence Matrix

**Property 1: Column Sum**

- For undirected graphs: Each column has exactly two 1's (for simple graphs without loops)
- For directed graphs: Each column has one +1 and one -1, so the sum is zero

**Property 2: Row Sum**

- For undirected graphs: The row sum gives the degree of the vertex
- For directed graphs: The row sum equals the outdegree minus indegree

**Property 3: Rank of Incidence Matrix**

- For a connected undirected graph, the rank of the incidence matrix is (n-1)
- For a disconnected graph with k components, the rank is (n-k)

**Property 4: Null Space**

- The all-ones vector is in the null space of the transpose of the incidence matrix for undirected graphs

**Property 5: Incidence Matrix and Adjacency Matrix Relationship**

- The product of the incidence matrix with its transpose gives information about the graph structure

### Types of Incidence Matrices

**1. Vertex-Edge Incidence Matrix:** The standard incidence matrix as defined above.

**2. Signed Incidence Matrix:** For directed graphs, explicitly uses +1 and -1 values.

**3. Modified Incidence Matrix:** Sometimes used in network flow problems with additional modifications.

### Incidence Matrix for Special Graphs

**Complete Graph K_n:**

- n vertices, n(n-1)/2 edges
- Each column has exactly two 1's

**Path Graph P_n:**

- n vertices, n-1 edges
- Matrix has a banded structure

**Cycle Graph C_n:**

- n vertices, n edges
- Each column has two 1's, forming a circulant pattern

**Tree:**

- A connected graph with n-1 edges
- Incidence matrix has rank n-1

## Examples

### Example 1: Undirected Graph Incidence Matrix

Consider an undirected graph G with 4 vertices and 5 edges:

- V = {v1, v2, v3, v4}
- E = {e1, e2, e3, e4, e5}
- Edges: e1 = {v1, v2}, e2 = {v2, v3}, e3 = {v3, v4}, e4 = {v1, v4}, e5 = {v2, v4}

**Solution:**

The incidence matrix M(G) is a 4×5 matrix:

```
 e1 e2 e3 e4 e5
v1 1 0 0 1 0
v2 1 1 0 0 1
v3 0 1 1 0 1
v4 0 0 1 1 1
```

**Verification:**

- Column e1 has 1's at v1 and v2 (correct, edge connects v1-v2)
- Column e2 has 1's at v2 and v3 (correct, edge connects v2-v3)
- Column e5 has 1's at v2 and v4 (correct, edge connects v2-v4)

Row sums (degrees):

- Degree(v1) = 1 + 0 + 0 + 1 + 0 = 2
- Degree(v2) = 1 + 1 + 0 + 0 + 1 = 3
- Degree(v3) = 0 + 1 + 1 + 0 + 1 = 3
- Degree(v4) = 0 + 0 + 1 + 1 + 1 = 3

### Example 2: Directed Graph Incidence Matrix

Consider a directed graph D with 3 vertices and 4 edges:

- V = {v1, v2, v3}
- E = {e1, e2, e3, e4}
- Directions: e1: v1→v2, e2: v2→v3, e3: v1→v3, e4: v3→v2

**Solution:**

The incidence matrix M(D) is a 3×4 matrix:

```
 e1 e2 e3 e4
v1 +1 0 +1 0
v2 -1 -1 0 -1
v3 0 +1 +1 +1
```

**Verification:**

- Column e1: +1 at v1 (tail), -1 at v2 (head) → v1→v2 ✓
- Column e2: -1 at v2 (head), +1 at v3 (tail) → v2→v3 ✓
- Column e4: +1 at v3 (tail), -1 at v2 (head) → v3→v2 ✓

Row sums:

- Row v1: 1 + 0 + 1 + 0 = 1 = outdegree(1) - indegree(1) = 2 - 1 = 1
- Row v2: -1 - 1 + 0 - 1 = -3 = outdegree(2) - indegree(2) = 1 - 4 = -3
- Row v3: 0 + 1 + 1 + 1 = 3 = outdegree(3) - indegree(3) = 3 - 0 = 3

### Example 3: Finding Graph Properties from Incidence Matrix

Given the incidence matrix of an undirected graph:

```
 e1 e2 e3 e4 e5
v1 1 1 0 0 0
v2 1 0 1 1 0
v3 0 1 1 0 1
v4 0 0 0 1 1
```

**Find:**
(a) The edges of the graph
(b) Degree of each vertex
(c) Whether the graph is connected

**Solution:**

(a) From the matrix:

- e1: v1-v2
- e2: v1-v3
- e3: v2-v3
- e4: v2-v4
- e5: v3-v4

(b) Degrees from row sums:

- deg(v1) = 1+1+0+0+0 = 2
- deg(v2) = 1+0+1+1+0 = 3
- deg(v3) = 0+1+1+0+1 = 3
- deg(v4) = 0+0+0+1+1 = 2

(c) Starting from v1: v1 connects to v2 and v3. From v2, we reach v4. All vertices are reachable, so the graph is connected.

## Exam Tips

1. **Remember the basic definition**: For undirected graphs, the incidence matrix entry is 1 if vertex is incident to edge, 0 otherwise. For directed graphs, use +1 for outgoing edges and -1 for incoming edges.

2. **Column verification**: In a simple undirected graph, each column (except loops) must have exactly two 1's. In directed graphs, each column must have one +1 and one -1.

3. **Degree calculation**: The row sum of the incidence matrix gives the degree of the vertex in undirected graphs. For directed graphs, it gives (outdegree - indegree).

4. **Rank is (n-1) for connected graphs**: This is a frequently tested property. For a connected graph with n vertices, the rank of the incidence matrix is n-1.

5. **Loop handling**: A loop at vertex i is represented by a column with a single 1 (in undirected case) or ±2 (in directed case) at row i.

6. **Matrix dimensions**: The incidence matrix is always n × m where n is the number of vertices and m is the number of edges.

7. **Relation with adjacency matrix**: While the adjacency matrix is n × n for n vertices, the incidence matrix is n × m. For dense graphs, incidence matrix may be more efficient.

8. **Application-based questions**: Be prepared to construct the incidence matrix from a given graph description or vice versa. This is a common university exam question.

9. **Properties of transpose**: Remember that M × M^T gives a matrix where diagonal elements are degrees and off-diagonal elements count common edges between vertices.

10. **Work systematically**: When constructing incidence matrices, list all vertices as rows and all edges as columns, then fill in 1's/-1's based on incidence.
