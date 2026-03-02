# Basic Definitions and Terminology in Graph Theory

## Introduction to Graph Theory

Graph Theory is a fundamental area of mathematics and computer science that studies the properties and applications of graphs. A graph is a simple yet powerful structure used to model pairwise relationships between objects. It finds applications in diverse fields such as computer networks, social networks, transportation systems, biology, and more.

At its core, graph theory provides a language to describe connectivity and relationships, making it essential for solving complex problems in various domains.

## Basic Definitions

### What is a Graph?

A **graph** G is an ordered pair G = (V, E) consisting of:

- V: A non-empty set of **vertices** (also called nodes or points)
- E: A set of **edges** (also called links or lines) connecting pairs of vertices

**Example:**

```
Vertices: V = {A, B, C, D}
Edges: E = {(A,B), (A,C), (B,C), (C,D)}
```

ASCII Diagram:

```
    A
   / \
  B---C
       \
        D
```

### Vertices and Edges

**Vertices** represent the fundamental units or entities in a graph. They are typically drawn as circles or points.

**Edges** represent relationships or connections between vertices. They can be:

- **Undirected**: No direction implied (A-B is same as B-A)
- **Directed**: Have a specific direction (A→B is different from B→A)

### Order and Size

- **Order**: The number of vertices in a graph, denoted as |V| or n
- **Size**: The number of edges in a graph, denoted as |E| or m

**Example:** For a graph with 4 vertices and 5 edges:

- Order = 4
- Size = 5

### Incidence and Adjacency

- **Incidence**: An edge e is incident to a vertex v if v is one of the endpoints of e
- **Adjacency**: Two vertices are adjacent if they are connected by an edge
- Two edges are adjacent if they share a common vertex

**Example:**

```
Vertices: A, B, C
Edges: (A,B), (A,C)
```

- Edge (A,B) is incident to vertices A and B
- Vertices A and B are adjacent
- Edges (A,B) and (A,C) are adjacent (they share vertex A)

## Types of Edges

### Simple Graphs vs. Multigraphs

- **Simple Graph**: Contains no loops and no multiple edges between the same pair of vertices
- **Multigraph**: May contain multiple edges between the same pair of vertices

**Example of multigraph:**

```
Vertices: A, B
Edges: (A,B), (A,B)  // Multiple edges between A and B
```

### Loops

A **loop** is an edge that connects a vertex to itself.

**Example:**

```
Vertex: A
Edge: (A,A)  // This is a loop
```

### Directed Edges

A **directed edge** (or arc) has a specific direction from one vertex to another. Represented as an ordered pair (u,v) where u is the tail and v is the head.

**Example:**

```
Directed edge: A→B
Tail: A, Head: B
```

## Special Graph Types

### Complete Graphs

A **complete graph** Kₙ is a simple graph where every pair of distinct vertices is connected by a unique edge.

**Properties:**

- Number of edges: n(n-1)/2
- Each vertex has degree n-1

**Example: K₄**

```
ASCII Diagram:
  A---B
  |\ /|
  | X |
  |/ \|
  C---D
```

### Regular Graphs

A **regular graph** is one where all vertices have the same degree. If the degree is k, it's called k-regular.

**Example:**

- 3-regular graph (cubic graph): Each vertex has degree 3

### Bipartite Graphs

A **bipartite graph** is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V.

**Example:**

```
Set U: {A, C}
Set V: {B, D}
Edges: (A,B), (A,D), (C,B), (C,D)
```

ASCII Diagram:

```
A   C
 \ /
  X
 / \
B   D
```

### Weighted Graphs

A **weighted graph** has numerical values (weights) assigned to its edges. These weights might represent distance, cost, capacity, etc.

**Example:**

```
Vertices: A, B, C
Edges: (A,B) with weight 5, (B,C) with weight 3
```

## Graph Representations

### Adjacency Matrix

An **adjacency matrix** is a square matrix used to represent a finite graph. The elements indicate whether pairs of vertices are adjacent.

For a graph G with n vertices:

- Matrix is n×n
- Entry aᵢⱼ = 1 if there is an edge from vertex i to vertex j, 0 otherwise
- For weighted graphs: aᵢⱼ = weight of edge (i,j)

**Example:**

```
Vertices: A, B, C
Edges: (A,B), (A,C), (B,C)

Adjacency Matrix:
   A B C
A: 0 1 1
B: 1 0 1
C: 1 1 0
```

### Adjacency List

An **adjacency list** represents a graph as an array of lists. Each list describes the set of neighbors of a vertex.

**Example:**

```
Vertices: A, B, C
Edges: (A,B), (A,C), (B,C)

Adjacency List:
A: [B, C]
B: [A, C]
C: [A, B]
```

### Comparison of Representations

| Representation   | Space Complexity | Edge Lookup | Neighbor Iteration | Best For |
| ---------------- | ---------------- | ----------- | ------------------ | -------- | --- | --------- | --------- | ------------- |
| Adjacency Matrix | O(               | V           | ²)                 | O(1)     | O(  | V         | )         | Dense graphs  |
| Adjacency List   | O(               | V           | +                  | E        | )   | O(deg(v)) | O(deg(v)) | Sparse graphs |

## Degree of a Vertex

### Definition

The **degree** of a vertex v, denoted deg(v), is the number of edges incident to v.

- In a simple graph: deg(v) = number of neighbors
- For directed graphs: we have in-degree and out-degree
- A vertex with degree 0 is called an **isolated vertex**
- A vertex with degree 1 is called a **pendant vertex**

### Handshaking Lemma

The **Handshaking Lemma** states that the sum of degrees of all vertices in a graph is equal to twice the number of edges.

**Formula:** ∑ deg(v) = 2|E|

**Proof:** Each edge contributes exactly 2 to the total degree sum (1 for each endpoint).

**Example:**

```
Vertices: A(deg=2), B(deg=2), C(deg=2)
Edges: (A,B), (A,C), (B,C)
Sum of degrees = 2+2+2 = 6
Twice number of edges = 2×3 = 6
```

### Degree Sequence

The **degree sequence** of a graph is the list of vertex degrees, usually written in non-increasing order.

**Example:** For the graph above: (2,2,2)

### Regular Graphs Revisited

A graph is called **regular** if all vertices have the same degree. If the degree is k, it's called k-regular.

**Examples:**

- Complete graph Kₙ is (n-1)-regular
- Cycle graph Cₙ is 2-regular
- Petersen graph is 3-regular

## Special Vertex Types

### Isolated Vertex

A vertex with degree 0 is called an **isolated vertex**. It has no connections to other vertices.

### Pendant Vertex

A vertex with degree 1 is called a **pendant vertex** (or leaf vertex). It's connected to exactly one other vertex.

### Cut Vertex

A **cut vertex** (or articulation point) is a vertex whose removal increases the number of connected components.

### Universal Vertex

A **universal vertex** is adjacent to all other vertices in the graph. In a graph of order n, a universal vertex has degree n-1.

## Graph Isomorphism

Two graphs G and H are **isomorphic** if there exists a bijection between their vertex sets that preserves adjacency.

**Formally:** G ≅ H if ∃ f:V(G)→V(H) such that (u,v) ∈ E(G) ⇔ (f(u),f(v)) ∈ E(H)

**Example:**

```
Graph G:         Graph H:
  A---B           X---Y
  |   |           |   |
  C---D           Z---W

These graphs are isomorphic under mapping: A→X, B→Y, C→Z, D→W
```

## Basic Graph Families

### Path Graph

A **path graph** Pₙ is a graph whose vertices can be arranged in a sequence v₁, v₂, ..., vₙ with edges between consecutive vertices.

**Properties:**

- Order: n
- Size: n-1
- Degree sequence: Two vertices of degree 1, others of degree 2

### Cycle Graph

A **cycle graph** Cₙ is a graph that consists of a single cycle through all vertices.

**Properties:**

- Order: n
- Size: n
- Regular: 2-regular (all vertices have degree 2)

### Complete Graph

As mentioned earlier, a **complete graph** Kₙ has all possible edges between its vertices.

**Properties:**

- Order: n
- Size: n(n-1)/2
- Regular: (n-1)-regular

### Complete Bipartite Graph

A **complete bipartite graph** Kₘ,ₙ is a bipartite graph where every vertex in one set is connected to every vertex in the other set.

**Properties:**

- Order: m+n
- Size: m×n
- Regular only if m=n

## Exam Tips

1. **Understand the fundamental definitions** - Make sure you can clearly define vertex, edge, degree, order, and size without hesitation.

2. **Practice with examples** - Draw small graphs (3-5 vertices) and practice calculating their properties.

3. **Memorize the Handshaking Lemma** - This is frequently tested and useful for solving problems.

4. **Recognize special graph types** - Be able to identify complete graphs, bipartite graphs, regular graphs, etc.

5. **Compare representations** - Understand when to use adjacency matrix vs. adjacency list and their trade-offs.

6. **Practice isomorphism problems** - These can be tricky; practice with small graphs to develop intuition.

7. **Work through degree sequence problems** - Given a degree sequence, determine if a simple graph exists with that sequence.

8. **Time management** - Graph theory problems can be time-consuming; practice solving them efficiently.
