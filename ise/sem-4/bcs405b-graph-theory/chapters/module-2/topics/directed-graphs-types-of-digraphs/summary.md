# Directed Graphs – Types of Digraphs

### Definitions and Key Concepts

- A **directed graph** (digraph) is a type of graph where edges have direction.
- A **digraph** is a pair (V, E) consisting of a set of vertices V and a set of edges E, where each edge has a direction.

### Types of Digraphs

- **Tournament Graph**: A digraph where every pair of distinct vertices is connected by a directed edge.
  - Definition: A tournament graph is a digraph G = (V, E) where every pair of distinct vertices u and v is connected by a directed edge from u to v.
- **Strongly Connected Digraph**: A digraph where there is a path from every vertex to every other vertex.
  - Definition: A strongly connected digraph is a digraph G = (V, E) where for every pair of distinct vertices u and v, there is a directed path from u to v and from v to u.
- **Directed Cycles**: A cycle in a digraph where every edge has a direction.
  - Definition: A directed cycle is a path in a digraph where every edge has a direction and the path starts and ends at the same vertex.
- **Digraph with no directed cycles**: A digraph where there is no directed cycle.
  - Definition: A digraph G = (V, E) is said to have no directed cycles if there is no path in G that starts and ends at the same vertex.

### Important Formulas and Theorems

- **Tournament Graph Theorem**: A tournament graph has a Hamiltonian cycle if and only if it is strongly connected.
- **Strongly Connected Component Theorem**: A strongly connected digraph is connected and has no sinks or sources.

### Important Theorems

- **Frobenius Theorem**: A tournament graph has a Hamiltonian cycle if and only if it is strongly connected and has an even number of vertices.
- **Alon-Boppana Theorem**: A tournament graph has a Hamiltonian cycle if and only if it is strongly connected and has at most 3 vertices.

### Important Results

- **Menger's Theorem**: The minimum number of edges that must be removed from a digraph to disconnect it is equal to the maximum number of vertices that can be disconnected by a single edge.
- **Havel-Hakimi Algorithm**: An algorithm for finding the Hamiltonian cycle of a tournament graph.
