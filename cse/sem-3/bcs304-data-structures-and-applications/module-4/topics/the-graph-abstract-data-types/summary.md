# The Graph Abstract Data Type

## Overview

A graph is a non-linear data structure consisting of vertices connected by edges. Unlike trees, graphs have no root node and no parent-child hierarchy. The Graph Abstract Data Type defines the operations that can be performed on a graph without specifying the underlying implementation.

## Key Points

- A graph G is defined as an ordered pair G = (V, E), where V is a finite non-empty set of vertices and E is a set of edges.
- Vertices can be connected by directed or undirected edges.
- Graphs can be weighted, where each edge carries a numerical value.
- A path is a sequence of vertices connected by edges.
- A cycle is a path where the first and last vertices are the same.
- The degree of a vertex is the number of edges incident on it.

## Important Definitions

- **Graph**: A non-linear data structure consisting of vertices connected by edges.
- **Vertex** (Node): A fundamental unit of a graph.
- **Edge**: A connection between two vertices.
- **Path**: A sequence of vertices connected by edges.
- **Cycle**: A path where the first and last vertices are the same.
- **Degree**: The number of edges incident on a vertex.

## Key Formulas / Syntax

- **Handshaking Theorem**: Sum of all degrees = 2 \* |E|.
- **Complete graph edges**: K_n has n(n-1)/2 edges for undirected graphs.

## Comparisons

| Feature   | Tree                    | Graph                 |
| --------- | ----------------------- | --------------------- |
| Structure | Hierarchical            | Network               |
| Root      | Has a single root       | No root concept       |
| Cycles    | No cycles               | May have cycles       |
| Edges     | n - 1 edges for n nodes | No fixed relationship |

## Exam Tips

- Know the formal definition of a graph: G = (V, E).
- Memorize the Handshaking Theorem and the formula for complete graph edges.
- Practice computing in-degree and out-degree for directed graphs.
- Be ready to identify whether a given graph is connected, bipartite, complete, or acyclic.
- Distinguish between graph types and remember that a tree is a special case of a graph.
