# Adjacency Matrix Representation of Graphs

## Table of Contents

- [Adjacency Matrix Representation of Graphs](#adjacency-matrix-representation-of-graphs)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Adjacency Matrix](#definition-of-adjacency-matrix)
  - [Undirected Graph Representation](#undirected-graph-representation)
  - [Directed Graph Representation](#directed-graph-representation)
  - [Weighted Graph Representation](#weighted-graph-representation)
  - [Special Types of Graphs](#special-types-of-graphs)
  - [Properties of Adjacency Matrix](#properties-of-adjacency-matrix)
  - [Space and Time Complexity](#space-and-time-complexity)
- [Examples](#examples)
  - [Example 1: Constructing Adjacency Matrix](#example-1-constructing-adjacency-matrix)
  - [Example 2: Directed Graph Analysis](#example-2-directed-graph-analysis)
  - [Example 3: Weighted Graph Shortest Path Foundation](#example-3-weighted-graph-shortest-path-foundation)
- [Exam Tips](#exam-tips)

## Introduction

The adjacency matrix is one of the fundamental and most widely used representations for graphs in computer science and discrete mathematics. It provides a systematic way to represent the connection between vertices using a two-dimensional array or matrix. Given its importance in graph algorithms and its frequent appearance in university examinations, understanding the adjacency matrix representation thoroughly is essential for every computer science students.

The adjacency matrix serves as the mathematical foundation for numerous graph algorithms including Floyd-Warshall algorithm for shortest paths, transitive closure, graph connectivity analysis, and various matrix-based graph operations. This representation offers constant-time edge lookup, making it particularly useful in scenarios where frequent edge existence checks are required.

In this module, we will explore the complete understanding of adjacency matrices, starting from basic definitions and progressing to advanced properties and applications. This knowledge forms the backbone for many algorithms studied in graph theory and will be frequently used in subsequent courses like analysis of algorithms, computer networks, and database management systems.

## Key Concepts

### Definition of Adjacency Matrix

For a simple graph G = (V, E) with n vertices, the adjacency matrix A is an n × n matrix defined as:

A[i][j] = 1 if there exists an edge between vertex i and vertex j
A[i][j] = 0 otherwise

The vertices are typically indexed from 0 to n-1 or 1 to n, and the matrix entry at row i and column j indicates whether an edge exists between vertex i and vertex j.

### Undirected Graph Representation

In an undirected graph, the adjacency matrix is always symmetric, meaning A[i][j] = A[j][i] for all i and j. This symmetry arises because edges are bidirectional - if vertex i is connected to vertex j, then vertex j is also connected to vertex i. For a simple undirected graph (no self-loops and no multiple edges), the diagonal entries are always zero: A[i][i] = 0 for all i.

**Example:** Consider an undirected graph with 4 vertices and edges: (1,2), (1,3), (2,4), (3,4)

The adjacency matrix would be:

```
 1 2 3 4
1 [ 0 1 1 0 ]
2 [ 1 0 0 1 ]
3 [ 1 0 0 1 ]
4 [ 0 1 1 0 ]
```

Notice how row 1, column 2 equals row 2, column 1 (both are 1), confirming the symmetric property.

### Directed Graph Representation

In a directed graph or digraph, edges have a specific direction, represented as ordered pairs (u, v). The adjacency matrix of a directed graph is generally not symmetric. Entry A[i][j] = 1 indicates a directed edge from vertex i to vertex j, but not necessarily from j to i. Self-loops (edges from a vertex to itself) can exist in directed graphs, and if present, the diagonal entry A[i][i] would be 1.

**Example:** Consider a directed graph with vertices {1, 2, 3, 4} and edges: (1→2), (1→3), (2→4), (3→2), (4→3)

The adjacency matrix would be:

```
 1 2 3 4
1 [ 0 1 1 0 ]
2 [ 0 0 0 1 ]
3 [ 0 1 0 0 ]
4 [ 0 0 1 0 ]
```

### Weighted Graph Representation

For weighted graphs, the adjacency matrix stores the weight of each edge instead of just 1 or 0. Typically, A[i][j] = w if there is an edge from i to j with weight w, and A[i][j] = ∞ (or 0 or -1 depending on convention) if no edge exists. The most common convention uses 0 or ∞ for non-existent edges.

For a weighted undirected graph, the matrix remains symmetric: A[i][j] = A[j][i] = weight of edge (i,j).

**Example:** Consider a weighted undirected graph with edge weights: (1,2)=4, (1,3)=2, (2,3)=1, (2,4)=5, (3,4)=3

The adjacency matrix:

```
 1 2 3 4
1 [ 0 4 2 0 ]
2 [ 4 0 1 5 ]
3 [ 2 1 0 3 ]
4 [ 0 5 3 0 ]
```

### Special Types of Graphs

**Complete Graph (Kn):** In a complete graph with n vertices, every pair of distinct vertices is connected by a unique edge. The adjacency matrix has 0s on the diagonal and 1s (or values for weighted complete graphs) everywhere else.

**Bipartite Graph:** While not directly identifiable from the adjacency matrix alone, certain patterns can indicate bipartite structure. A bipartite graph can be represented such that the adjacency matrix has a specific block structure.

**Null Graph:** A graph with no edges has an adjacency matrix with all zero entries.

### Properties of Adjacency Matrix

1. **Row Sum and Column Sum:** The sum of entries in row i (or column i) gives the degree of vertex i in an undirected graph. For directed graphs, row sum represents out-degree, and column sum represents in-degree.

2. **Matrix Powers:** For an unweighted graph, (A^k)[i][j] gives the number of distinct walks of length k from vertex i to vertex j. This property is crucial in understanding path counting and connectivity.

3. **Spectrum:** The eigenvalues of the adjacency matrix are called the spectrum of the graph. These eigenvalues have significant applications in chemistry (Hückel molecular orbital theory) and physics.

4. **Graph Isomorphism:** Two graphs are isomorphic if and only if their adjacency matrices are similar, meaning there exists a permutation matrix P such that A1 = P^T × A2 × P.

### Space and Time Complexity

**Space Complexity:** The adjacency matrix requires O(V²) space regardless of the number of edges. For sparse graphs (few edges relative to vertices), this is often inefficient compared to adjacency list representation.

**Time Complexity:**

- Edge existence check: O(1)
- Finding all neighbors of a vertex: O(V)
- Adding/removing an edge: O(1)
- Traversing all edges: O(V²)

## Examples

### Example 1: Constructing Adjacency Matrix

**Problem:** Draw the graph represented by the following adjacency matrix and find the degree of each vertex:

```
 A B C D E
A [ 0 1 0 1 0 ]
B [ 1 0 1 1 0 ]
C [ 0 1 0 0 1 ]
D [ 1 1 0 0 1 ]
E [ 0 0 1 1 0 ]
```

**Solution:**

**Step 1:** Identify edges from the matrix

- A-B (A[0][1] = 1)
- A-D (A[0][3] = 1)
- B-C (A[1][2] = 1)
- B-D (A[1][3] = 1)
- C-E (A[2][4] = 1)
- D-E (A[3][4] = 1)

**Step 2:** Draw the graph with 5 vertices A, B, C, D, E and connect them accordingly.

**Step 3:** Calculate degrees (row sums for undirected graph):

- Degree(A) = 1 + 1 = 2
- Degree(B) = 1 + 1 + 1 = 3
- Degree(C) = 1 + 1 = 2
- Degree(D) = 1 + 1 + 1 = 3
- Degree(E) = 1 + 1 = 2

**Verification:** Sum of all degrees = 2 + 3 + 2 + 3 + 2 = 12 = 2|E|, so |E| = 6 edges ✓

### Example 2: Directed Graph Analysis

**Problem:** Given the adjacency matrix of a directed graph, find:
(a) Out-degree and in-degree of each vertex
(b) Number of paths of length 2 from vertex 1 to vertex 3

Matrix:

```
 1 2 3 4
1 [ 0 1 1 0 ]
2 [ 0 0 1 1 ]
3 [ 1 0 0 1 ]
4 [ 0 0 0 0 ]
```

**Solution:**

**(a) Out-degree (row sum) and In-degree (column sum):**

- Vertex 1: Out-degree = 1+1+0 = 2, In-degree = 0+0+1+0 = 1
- Vertex 2: Out-degree = 0+1+1 = 2, In-degree = 1+0+0+0 = 1
- Vertex 3: Out-degree = 1+0+1 = 2, In-degree = 1+1+0+0 = 2
- Vertex 4: Out-degree = 0, In-degree = 0+1+1+0 = 2

**(b) Number of paths of length 2 from 1 to 3:**
We need to compute A² and look at entry (1,3).

A² = A × A:

```
 1 2 3 4
1 [ 1 0 1 2 ]
2 [ 1 0 1 1 ]
3 [ 0 1 1 1 ]
4 [ 0 0 0 0 ]
```

A²[1][3] = 1, so there is exactly 1 path of length 2 from vertex 1 to vertex 3.

Verification: Paths of length 2 from 1 to 3:
1 → 2 → 3 (1→2 exists, 2→3 exists)

### Example 3: Weighted Graph Shortest Path Foundation

**Problem:** Using the adjacency matrix approach, find the shortest path from vertex A to vertex D in the following weighted graph:

Adjacency Matrix (∞ denotes no edge):

```
 A B C D
A [ 0 4 ∞ 7 ]
B [ 4 0 3 2 ]
C [ ∞ 3 0 5 ]
D [ 7 2 5 0 ]
```

**Solution:**

Using a simple approach, let's trace possible paths:

- Direct: A → D = 7
- Via B: A → B → D = 4 + 2 = 6
- Via C: A → B → C → D = 4 + 3 + 5 = 12
- Via B then C: A → B → C → B → D (would be longer)

The shortest path is A → B → D with total weight 6.

This example demonstrates why algorithms like Dijkstra's or Floyd-Warshall are needed for larger graphs - they systematically compute these shortest paths.

## Exam Tips

1. **Remember the symmetric property:** For undirected graphs, always verify that A[i][j] = A[j][i]. If not, the matrix is incorrect.

2. **Degree calculation:** For undirected graphs, degree of vertex i = sum of row i (or column i). For directed graphs, out-degree = row sum, in-degree = column sum.

3. **Matrix power interpretation:** Remember that (A²)[i][j] gives the number of paths of length 2 between vertices i and j. This is crucial for connectivity questions.

4. **Space complexity awareness:** If a question asks about representation efficiency, remember that adjacency matrix uses O(V²) space, making it suitable for dense graphs but inefficient for sparse graphs.

5. **Weighted graph conventions:** Be clear about whether 0 or ∞ represents "no edge" in weighted graphs - this varies by textbook and must be inferred from context.

6. **Self-loop representation:** Self-loops are represented on the diagonal. A[i][i] = 1 indicates a self-loop at vertex i.

7. **Handshaking Lemma verification:** When calculating degrees, verify that sum of all degrees = 2 × |E| for undirected graphs. This is a good sanity check.

8. **Complete graph matrix:** For Kn (complete graph with n vertices), the adjacency matrix has 0s on diagonal and 1s everywhere else (for simple graphs without self-loops).

9. **Trace and degree sequence:** The trace (sum of diagonal elements) equals the number of self-loops. This is 0 for simple graphs.

10. **Adjacency matrix vs adjacency list:** In exams, if asked to compare, emphasize O(1) edge lookup vs O(V) for matrix, but O(V²) space vs O(V+E) for list.
