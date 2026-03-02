# Representations of Graphs

## Overview

Graphs can be represented using adjacency matrices, adjacency lists, or adjacency multilists. The choice of representation depends on the graph's density, the need for edge lookups, and memory efficiency. Understanding the trade-offs between these representations is crucial for efficient graph algorithms.

## Key Points

- Adjacency matrix: a 2D array of size V x V, where A[i][j] = 1 if there is an edge from vertex i to vertex j.
- Adjacency list: an array of linked lists, where each list represents the neighbors of a vertex.
- Adjacency multilist: a representation that stores each edge as a single node that appears in two lists simultaneously.
- Dense graphs are best represented using adjacency matrices, while sparse graphs are best represented using adjacency lists.
- Adjacency matrices have a space complexity of O(V^2), while adjacency lists have a space complexity of O(V + E).

## Important Definitions

- **Adjacency matrix**: a 2D array representing the edges of a graph.
- **Adjacency list**: an array of linked lists representing the neighbors of each vertex.
- **Adjacency multilist**: a representation that stores each edge as a single node in two lists.
- **Dense graph**: a graph where the number of edges is close to V^2.
- **Sparse graph**: a graph where the number of edges is much less than V^2.

## Key Formulas / Syntax

- Adjacency matrix: A[i][j] = 1 if there is an edge from vertex i to vertex j.
- Adjacency list: `insertEdge(Graph* g, int u, int v)` inserts an edge between vertices u and v.

## Comparisons

| Criteria    | Adjacency Matrix | Adjacency List | Adjacency Multilist |
| ----------- | ---------------- | -------------- | ------------------- |
| Space       | O(V^2)           | O(V + E)       | O(V + E)            |
| Edge lookup | O(1)             | O(degree)      | O(degree)           |
| Add edge    | O(1)             | O(1)           | O(1)                |
| Remove edge | O(1)             | O(degree)      | O(degree)           |

## Exam Tips

- Be able to determine the space complexity of a graph representation.
- Understand the trade-offs between adjacency matrices and adjacency lists.
- Know how to calculate the degree of a vertex from both matrix and list representations.
- Be familiar with the structure of an adjacency multilist.
- Practice converting between graph diagrams, matrices, and lists.
