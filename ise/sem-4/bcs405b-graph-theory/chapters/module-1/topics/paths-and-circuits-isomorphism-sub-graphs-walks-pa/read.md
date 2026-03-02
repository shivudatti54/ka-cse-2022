# **Paths and Circuits – Isomorphism, Sub-Graphs, Walks, Paths and Circuits, Connected Graphs, Disconnected Graphs and Components**

## **Introduction**

In graph theory, a path is a sequence of vertices connected by edges, and a circuit is a closed path that starts and ends at the same vertex. This study material covers the concepts of paths and circuits, including isomorphism, sub-graphs, walks, and their relationship with connected and disconnected graphs.

## **Paths**

A **path** is a sequence of vertices connected by edges, where each pair of adjacent vertices is connected by an edge. A path is denoted as P = (v1, v2, ..., vn), where v1, v2, ..., vn are the vertices of the path.

- **Weighted path**: A path with weights assigned to each edge.
- **Unweighted path**: A path without weights assigned to each edge.

## **Circuits**

A **circuit** is a closed path that starts and ends at the same vertex. A circuit is denoted as C = (v1, v2, ..., vn, v1), where v1, v2, ..., vn are the vertices of the circuit.

- **Weighted circuit**: A circuit with weights assigned to each edge.
- **Unweighted circuit**: A circuit without weights assigned to each edge.

## **Isomorphism**

Two graphs G1 = (V1, E1) and G2 = (V2, E2) are said to be **isomorphic** if there exists a bijection f: V1 → V2 such that for every edge e = (u, v) in E1, there exists an edge f(e) = (f(u), f(v)) in E2.

- **Example**: Two graphs are isomorphic if they have the same number of vertices and edges, and the adjacency matrix of one graph can be transformed into the adjacency matrix of the other graph using a permutation matrix.

## **Sub-Graphs**

A sub-graph of a graph G = (V, E) is a graph G' = (V', E') such that V' ⊆ V and E' ⊆ E.

- **Example**: A sub-graph is a graph that is formed by selecting some of the vertices and edges of the original graph.

## **Walks**

A **walk** is a sequence of vertices connected by edges, where each pair of adjacent vertices is connected by an edge, but not necessarily in the order of visitation.

- **Example**: A walk is a path that visits a vertex twice or more.

## **Paths and Circuits**

A path is a walk without repetition of vertices, while a circuit is a walk that starts and ends at the same vertex.

- **Example**: A path from vertex A to vertex B is a walk from A to B without revisiting any vertex. A circuit from A to B is a walk from A to B that starts and ends at A.

## **Connected Graphs**

A graph is said to be **connected** if there exists a path between every pair of vertices.

- **Example**: A graph with three vertices (A, B, C) and three edges (A-B, B-C, C-A) is connected.

## **Disconnected Graphs**

A graph is said to be **disconnected** if there does not exist a path between every pair of vertices.

- **Example**: A graph with three vertices (A, B, C) and three edges (A-B, B-C, C-A) is disconnected.

## **Components**

A **component** is a sub-graph that is connected and has no cut vertices.

- **Example**: A component is a sub-graph that is not part of a larger connected sub-graph.

### Key Concepts

- **Path**: A sequence of vertices connected by edges.
- **Circuit**: A closed path that starts and ends at the same vertex.
- **Isomorphism**: Two graphs are isomorphic if there exists a bijection between their vertices.
- **Sub-graph**: A graph formed by selecting some of the vertices and edges of the original graph.
- **Walk**: A sequence of vertices connected by edges.
- **Connected graph**: A graph with a path between every pair of vertices.
- **Disconnected graph**: A graph with no path between every pair of vertices.
- **Component**: A sub-graph that is connected and has no cut vertices.

### Example Problems

1.  Given two graphs G1 = (V1, E1) and G2 = (V2, E2), determine if they are isomorphic.
2.  Given a graph G = (V, E), find a sub-graph of G with three vertices.
3.  Given a graph G = (V, E), find a path from vertex A to vertex B.
4.  Given a graph G = (V, E), find a circuit in G.
5.  Given a graph G = (V, E), determine if G is connected or disconnected.

### Practice Questions

1.  What is the difference between a path and a walk?
2.  What is the definition of an isomorphism between two graphs?
3.  What is a sub-graph, and how is it formed?
4.  What is a connected graph, and what is an example of one?
5.  What is a disconnected graph, and what is an example of one?
