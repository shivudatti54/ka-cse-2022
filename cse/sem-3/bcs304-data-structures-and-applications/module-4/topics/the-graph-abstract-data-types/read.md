# The Graph Abstract Data Type

## 1. Introduction and Formal Definitions

A **graph** is a fundamental non-linear data structure comprising a finite set of vertices (or nodes) connected by a set of edges (or arcs). Unlike hierarchical data structures such as trees, graphs impose no root node or parent-child relationship—any vertex may connect to any other vertex through zero or more edges.

### 1.1 Mathematical Foundation

**Definition 1.1 (Graph)**: A graph G is formally defined as an ordered pair G = (V, E), where:

- V = {v₁, v₂, ..., vₙ} is a finite, non-empty set of vertices (|V| = n denotes the order of the graph)
- E = {e₁, e₂, ..., eₘ} is a set of edges (|E| = m denotes the size of the graph)
- Each edge e ∈ E is associated with an unordered pair {u, v} of vertices for undirected graphs, or an ordered pair (u, v) for directed graphs

**Definition 1.2 (Simple Graph)**: A graph is simple if it contains no self-loops (edges connecting a vertex to itself) and no multiple edges between the same pair of vertices.

**Definition 1.3 (Complete Graph)**: A complete graph Kₙ on n vertices is a simple graph where every pair of distinct vertices is connected by exactly one edge. The number of edges in Kₙ is:

- Undirected: |E(Kₙ)| = n(n-1)/2
- Directed: |E(Kₙ)| = n(n-1)

## 2. Fundamental Graph Terminology

### 2.1 Basic Elements

**Vertex (Node)**: The fundamental unit of a graph. Each vertex v ∈ V may store a value or label. The vertex set V(G) denotes all vertices in graph G.

**Edge (Arc)**: A connection between two vertices. In an undirected graph, an edge is a 2-element subset {u, v} ⊆ V. In a directed graph (digraph), an edge is an ordered pair (u, v) ∈ V × V, where u is the source and v is the destination.

**Adjacency**: Two vertices u and v are adjacent (or neighbors) if there exists an edge {u, v} ∈ E (undirected) or (u, v) ∈ E (directed). The set of all neighbors of vertex v is denoted N(v) = {u ∈ V | {u, v} ∈ E}.

**Incidence**: An edge e = {u, v} is incident on vertices u and v. Vertex u is said to be incident to edge e.

### 2.2 Degree Properties

**Definition 2.1 (Degree)**: In an undirected graph, the degree of vertex v, denoted deg(v), is the number of edges incident on v. A self-loop contributes 2 to the degree.

**Theorem 2.1 (Handshaking Lemma)**: For any undirected graph G = (V, E), the sum of degrees of all vertices equals twice the number of edges:

$$\sum_{v \in V} \deg(v) = 2|E|$$

**Proof**: Each edge e = {u, v} contributes exactly 1 to deg(u) and 1 to deg(v). Therefore, summing deg(v) over all vertices counts each edge twice. ∎

**Corollary 2.1**: In any undirected graph, the number of vertices with odd degree is even.

**Definition 2.2 (In-Degree and Out-Degree)**: In a directed graph G = (V, E):

- In-degree of v: deg⁻(v) = |{(u, v) ∈ E}|
- Out-degree of v: deg⁺(v) = |{(v, u) ∈ E}|

**Theorem 2.2**: For any directed graph, the sum of in-degrees equals the sum of out-degrees, both equaling |E|.

$$\sum_{v \in V} \deg^-(v) = \sum_{v \in V} \deg^+(v) = |E|$$

### 2.3 Paths and Cycles

**Definition 2.3 (Path)**: A path of length k from vertex u to vertex v is a sequence of vertices P = (v₀, v₁, ..., vₖ) where v₀ = u, vₖ = v, and (vᵢ, vᵢ₊₁) ∈ E for 0 ≤ i < k.

- **Simple path**: No vertex is repeated (except possibly endpoints in a cycle)
- **Path length**: Number of edges in the path, or sum of weights for weighted graphs

**Definition 2.4 (Cycle)**: A cycle is a path where v₀ = vₖ and no other vertex is repeated. A graph containing no cycles is called **acyclic**.

**Theorem 2.3**: In a simple undirected graph with n vertices, the longest possible simple path contains at most n-1 edges.

## 3. Classification of Graphs

### 3.1 By Directionality

**Undirected Graph**: Edges have no orientation. Edge {u, v} is identical to {v, u}.

**Directed Graph (Digraph)**: Every edge has a specific direction. Edge (u, v) goes from u to v, but (v, u) is a distinct edge unless both exist.

### 3.2 By Weighting

**Unweighted Graph**: Edges carry no numerical value.

**Weighted Graph**: Each edge e ∈ E has an associated weight w(e) ∈ ℝ⁺. Weights may represent distance, cost, time, capacity, or any quantifiable metric.

### 3.3 By Connectivity

**Connected Graph**: An undirected graph G is connected if ∀u, v ∈ V, there exists a path from u to v.

**Strongly Connected Graph**: A directed graph G is strongly connected if ∀u, v ∈ V, there exists a directed path from u to v.

**Weakly Connected Graph**: A directed graph is weakly connected if replacing all directed edges with undirected edges produces a connected graph.

### 3.4 Special Graph Structures

**Bipartite Graph**: A graph G = (V, E) is bipartite if V can be partitioned into two disjoint sets U and W (V = U ∪ W, U ∩ W = ∅) such that every edge connects a vertex in U to a vertex in W.

**Theorem 2.4 (Characterization of Bipartite Graphs)**: A graph is bipartite if and only if it contains no odd-length cycles.

**Directed Acyclic Graph (DAG)**: A directed graph with no directed cycles. DAGs are extensively used in task scheduling, build systems, topological ordering, and version control.

**Tree**: A connected acyclic undirected graph with n vertices and n-1 edges. A forest is an acyclic undirected graph (potentially disconnected).

## 4. Graph Representations

### 4.1 Adjacency Matrix

For a graph G = (V, E) with |V| = n, the adjacency matrix A is an n × n matrix where:

$$A[i][j] = \begin{cases} 1 & \text{if } (v_i, v_j) \in E \text{ (or } \{v_i, v_j\} \in E\text{)} \\ 0 & \text{otherwise} \end{cases}$$

For weighted graphs: A[i][j] = w(v_i, v_j) if edge exists, ∞ otherwise.

**Space Complexity**: O(n²)

**Time Complexity**:

- Check adjacency: O(1)
- Insert/Delete edge: O(1)
- Insert vertex: O(n²) (matrix must be resized)

### 4.2 Adjacency List

For each vertex v ∈ V, maintain a list of its neighbors.

**Space Complexity**: O(n + m)

**Time Complexity**:

- Check adjacency: O(deg(v)) in worst case
- Insert/Delete edge: O(1) at head of list
- Insert vertex: O(1)

## 5. The Graph Abstract Data Type

The Graph ADT provides an abstract interface for graph operations, independent of the underlying representation.

### 5.1 Formal Specification

**Data**:

- V: finite set of vertices
- E: set of edges (pairs of vertices)

**Fundamental Operations**:

| Operation           | Precondition           | Postcondition                         | Complexity  |
| ------------------- | ---------------------- | ------------------------------------- | ----------- |
| createGraph()       | None                   | Returns empty graph with V = ∅, E = ∅ | O(1)        |
| addVertex(g, v)     | v ∉ V(g)               | V' = V ∪ {v}, E' = E                  | O(1)/O(n)²  |
| removeVertex(g, v)  | v ∈ V(g)               | V' = V \ {v}, E' = E \ {e : v ∈ e}    | O(n + m)    |
| addEdge(g, u, v)    | u, v ∈ V(g), {u,v} ∉ E | E' = E ∪ {{u,v}} or {(u,v)}           | O(1)        |
| removeEdge(g, u, v) | {u,v} ∈ E              | E' = E \ {{u,v}}                      | O(1)        |
| adjacent(g, u, v)   | u, v ∈ V(g)            | Returns true if {u,v} ∈ E             | O(1)/O(deg) |
| getNeighbors(g, v)  | v ∈ V(g)               | Returns set N(v)                      | O(deg(v))   |
| getVertices(g)      | None                   | Returns set V                         | O(n)        |
| getEdges(g)         | None                   | Returns set E                         | O(m)        |
| inDegree(g, v)      | v ∈ V(g)               | Returns deg⁻(v)                       | O(m)        |
| outDegree(g, v)     | v ∈ V(g)               | Returns deg⁺(v)                       | O(m)        |

### 5.2 Invariants

For a valid graph instance:

1. V is finite
2. E ⊆ V × V (for directed) or E ⊆ {{u,v} : u, v ∈ V, u ≠ v} (for simple undirected)
3. No duplicate edges in simple graphs
4. Degree sums satisfy handshaking lemma

## 6. Practice Problems

### Problem 1 (Numerical - Application)

Given an undirected graph G with 8 vertices and 12 edges, calculate:
(a) The sum of all vertex degrees
(b) The average degree
(c) If three vertices have degree 5, 4, and 3 respectively, find the sum of degrees of the remaining five vertices

**Solution**:
(a) By Handshaking Theorem: Σdeg(v) = 2|E| = 2 × 12 = 24
(b) Average degree = 24/8 = 3
(c) Sum of remaining five = 24 - (5 + 4 + 3) = 12

### Problem 2 (Proof-Based)

Prove that in any simple undirected graph with minimum degree δ ≥ 2, there exists a cycle of length at least δ + 1.

### Problem 3 (Analysis)

Consider a directed graph represented using adjacency matrix with n = 1000 vertices and m = 5000 edges. Determine:
(a) Space required for adjacency matrix representation
(b) Time to check if two specific vertices are adjacent
(c) Time to find all outgoing edges from a vertex

---

## 7. Multiple Choice Questions

### Question 1 (Application)

A simple undirected graph has 6 vertices and 9 edges. What is the sum of degrees of all vertices?

(A) 9  
(B) 12  
(C) 18  
(D) 24

**Answer: (C) 18**  
By Handshaking Theorem: Σdeg(v) = 2|E| = 2 × 9 = 18

### Question 2 (Analysis)

In a directed graph with 10 vertices and 15 edges, if vertex A has out-degree 4 and in-degree 3, and vertex B has out-degree 2 and in-degree 5, what is the sum of in-degrees of the remaining 8 vertices?

(A) 6  
(B) 7  
(C) 8  
(D) 10

**Answer: (C) 8**  
Total in-degrees = |E| = 15. Sum of known in-degrees = 3 + 5 = 8. Remaining = 15 - 8 = 7... Wait, recalculating: Total in-degrees = 15. Known: A_in=3, B_in=5. Sum = 8. Remaining = 15 - 8 = 7. But this doesn't match options. Let me verify: Actually, the question asks for sum of remaining 8 vertices. If total = 15, and we sum in-degrees of 8 vertices, it should be 15 - (3+5) = 7. Wait, there are only 10 vertices total. A and B are 2 vertices. Remaining = 8 vertices. So remaining in-degrees = 15 - 8 = 7. The answer should be (B) 7.

Actually, let me reconsider: Total in-degrees = 15 (one per edge). A_in=3, B_in=5. Sum of remaining 8 = 15 - 8 = 7.

### Question 3 (Application)

Which of the following statements is TRUE for a bipartite graph?

(A) It must contain a cycle of odd length  
(B) It can have self-loops  
(C) Its vertex set can be partitioned into two independent sets  
(D) It cannot be connected

**Answer: (C)**  
By definition, a bipartite graph's vertices can be partitioned into two disjoint sets U and W such that every edge connects a vertex in U to a vertex in W. This means no two vertices within the same set are adjacent—each set is independent.

### Question 4 (Analysis)

What is the minimum number of edges in a connected graph with 7 vertices?

(A) 6  
(B) 7  
(C) 14  
(D) 21

**Answer: (A) 6**  
A connected graph with n vertices must have at least n-1 edges (a tree). For n=7, minimum edges = 6.

### Question 5 (Application)

In an adjacency matrix representation of a graph with n vertices, what is the space complexity to store a weighted graph?

(A) O(n)  
(B) O(n²)  
(C) O(n + m)  
(D) O(m)

**Answer: (B) O(n²)**  
An adjacency matrix requires an n × n matrix regardless of the number of edges.
