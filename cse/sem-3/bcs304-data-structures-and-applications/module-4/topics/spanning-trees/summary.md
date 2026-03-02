# Spanning Trees

## Overview

A spanning tree of a connected undirected graph is a subgraph that is a tree and includes all the vertices of the graph. It provides the minimum structure needed to keep all vertices connected without any redundant edges. Spanning trees are fundamental to network design.

## Key Points

- A spanning tree of a graph with V vertices has exactly V - 1 edges.
- A spanning tree exists if and only if the graph is connected.
- DFS and BFS can be used to construct spanning trees, resulting in different tree structures.
- Adding any non-tree edge to a spanning tree creates exactly one cycle.
- Removing any edge from a spanning tree disconnects it into exactly two components.
- A disconnected graph can have a spanning forest, with V - k edges, where k is the number of components.

## Important Definitions

- **Spanning Tree**: A subgraph that is a tree and includes all the vertices of the graph.
- **DFS Spanning Tree**: A spanning tree constructed using Depth-First Search.
- **BFS Spanning Tree**: A spanning tree constructed using Breadth-First Search.
- **Spanning Forest**: A collection of spanning trees for a disconnected graph.

## Key Formulas / Syntax

- Cayley's formula: Number of spanning trees of K_n = n^(n-2)

## Comparisons

| Feature        | DFS Spanning Tree  | BFS Spanning Tree           |
| -------------- | ------------------ | --------------------------- |
| Shape          | Deep and narrow    | Short and wide              |
| Non-tree edges | Back edges         | Cross edges                 |
| Height         | Can be up to V - 1 | Equal to graph eccentricity |

## Exam Tips

- Remember that a spanning tree has exactly V - 1 edges.
- Understand the existence condition for a spanning tree (connected graph).
- Know how to construct DFS and BFS spanning trees.
- Recall Cayley's formula for the number of spanning trees of K_n.
- Understand the effect of adding or removing an edge from a spanning tree.
- Be familiar with the concept of a spanning forest for disconnected graphs.
