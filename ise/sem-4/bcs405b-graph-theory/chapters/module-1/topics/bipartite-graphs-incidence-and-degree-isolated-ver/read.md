# Bipartite Graphs - Incidence and Degree - Isolated Vertex

=====================================================

## Introduction

---

A bipartite graph is a type of graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to a vertex in the other set. In other words, bipartite graphs are graphs that can be divided into two separate groups of vertices, and edges only exist between vertices from different groups.

## Definition

---

A bipartite graph is defined as follows:

- Let `G = (V, E)` be a graph.
- Let `U` and `V` be two disjoint sets of vertices in `V`.
- A bipartite graph is a graph `G` such that every edge in `E` connects a vertex in `U` to a vertex in `V`.

## Examples

---

- A phone call network with two types of users: landline users and mobile users. Each landline user is connected to every mobile user, forming a bipartite graph.
- A library with two types of books: fiction and non-fiction. Each fiction book is connected to every non-fiction book, forming a bipartite graph.

## Incidence of a Bipartite Graph

---

The incidence of a bipartite graph refers to the relationship between the edges and the vertices. In a bipartite graph, each edge connects a vertex from one set to a vertex in the other set.

### Definition

The incidence of a bipartite graph `G = (V, E)` is defined as:

- For each vertex `v ∈ V`, let `d(v)` be the degree of `v`, which is the number of edges incident on `v`.
- The incidence of `G` is a collection of ordered pairs `(u, v)`, where `u ∈ U` and `v ∈ V`, such that `(u, v) ∈ E`.

### Example

Suppose we have a bipartite graph `G` with vertices `U = {a, b, c}` and `V = {1, 2, 3}`, where:

- `(a, 1) ∈ E`
- `(a, 2) ∈ E`
- `(b, 1) ∈ E`
- `(c, 2) ∈ E`
- `(c, 3) ∈ E`

The incidence of `G` is:

- `(a, 1)`
- `(a, 2)`
- `(b, 1)`
- `(c, 2)`
- `(c, 3)`

## Degree of a Vertex in a Bipartite Graph

---

The degree of a vertex in a bipartite graph is the number of edges incident on that vertex.

### Definition

Let `v ∈ V` be a vertex in a bipartite graph `G = (V, E)`. The degree of `v`, denoted by `d(v)`, is the number of edges incident on `v`.

### Example

Using the same bipartite graph as above, we can calculate the degree of each vertex:

- `d(a) = 2` because `(a, 1)` and `(a, 2)` are both incident on `a`.
- `d(b) = 1` because `(b, 1)` is the only edge incident on `b`.
- `d(c) = 2` because `(c, 2)` and `(c, 3)` are both incident on `c`.

## Isolated Vertex in a Bipartite Graph

---

An isolated vertex in a bipartite graph is a vertex that has no edges incident on it.

### Definition

A vertex `v ∈ V` is said to be isolated in a bipartite graph `G = (V, E)` if there are no edges incident on `v`.

### Example

Using the same bipartite graph as above, we can identify the isolated vertices:

- There are no isolated vertices in this graph because every vertex has at least one edge incident on it.

However, if we have a bipartite graph with isolated vertices, we can identify them as follows:

Suppose we have a bipartite graph `G` with vertices `U = {a}` and `V = {1, 2, 3}`, where:

- There are no edges incident on `a`.

In this case, `a` is an isolated vertex because it has no edges incident on it.

## Key Concepts

---

- Bipartite graph: a graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to a vertex in the other set.
- Incidence of a bipartite graph: the relationship between the edges and the vertices.
- Degree of a vertex in a bipartite graph: the number of edges incident on a vertex.
- Isolated vertex: a vertex that has no edges incident on it.
