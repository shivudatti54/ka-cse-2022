# Digraphs and Binary Relations

### Introduction

In graph theory, a digraph is a type of graph that consists of vertices connected by directed edges. A binary relation on a set of vertices is a relation where each pair of vertices is related by a single edge. In this topic, we will explore digraphs and binary relations, including their definitions, properties, and applications.

### Digraphs

A **digraph** is a graph that has directed edges, where each edge has a direction and a label. Digraphs are also known as directed graphs or multigraphs.

**Definition:** A digraph G is a pair (V, E), where V is the set of vertices and E is the set of edges, each of which is a directed edge from one vertex to another.

**Properties:**

- A digraph has a **degree sequence**, which is a list of the degrees of all the vertices.
- A digraph is **connected** if there is a path from every vertex to every other vertex.
- A digraph is **strongly connected** if there is a path from every vertex to every other vertex in both directions.

### Binary Relations

A **binary relation** on a set of vertices is a relation where each pair of vertices is related by a single edge. Binary relations are denoted by a binary relation R, where R is a subset of the Cartesian product of the vertices.

**Definition:** A binary relation R on a set of vertices V is a subset of the Cartesian product V \* V, where V \* V = {(u, v) | u, v ∈ V}.

**Properties:**

- A binary relation is **reflexive** if (u, u) ∈ R for every vertex u.
- A binary relation is **antisymmetric** if (u, v) ∈ R and (v, u) ∈ R imply u = v.
- A binary relation is **transitive** if (u, v) ∈ R and (v, w) ∈ R imply (u, w) ∈ R.

### Examples

**Example 1:** Consider a digraph with vertices A, B, and C, where the edges are as follows:

|     | A   | B   | C   |
| --- | --- | --- | --- |
| A   | -   | →   | →   |
| B   | ←   | -   | ←   |
| C   | ←   | ←   | -   |

This digraph is strongly connected, since there is a path from every vertex to every other vertex in both directions.

**Example 2:** Consider a binary relation R on the set of vertices {1, 2, 3}, where R = {(1, 2), (2, 3), (3, 1)}.

This binary relation is transitive, since (1, 2) ∈ R and (2, 3) ∈ R imply (1, 3) ∈ R.

### Operations on Digraphs

Digraphs can be operated on in various ways, including:

- **Edge addition**: Adding a new edge to a digraph.
- **Edge removal**: Removing an edge from a digraph.
- **Vertex addition**: Adding a new vertex to a digraph.
- **Vertex removal**: Removing a vertex from a digraph.

These operations can be used to create new digraphs from existing ones.

### Hamiltonian Paths and Cycles

A **Hamiltonian path** is a path that visits every vertex in a digraph exactly once. A **Hamiltonian cycle** is a Hamiltonian path that starts and ends at the same vertex.

### Conclusion

In this topic, we have explored digraphs and binary relations, including their definitions, properties, and applications. We have also discussed operations on digraphs and Hamiltonian paths and cycles.
