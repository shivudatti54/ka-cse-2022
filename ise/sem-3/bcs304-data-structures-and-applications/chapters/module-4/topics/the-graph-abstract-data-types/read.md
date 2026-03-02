# The Graph Abstract Data Type

## Introduction

In the realm of data structures, a **Graph** is one of the most powerful and versatile abstractions used to model real-world relationships and networks. Unlike linear structures (arrays, linked lists) or hierarchical ones (trees), graphs are non-linear and can represent complex, interconnected relationships with no inherent parent-child hierarchy. This module delves into the Graph Abstract Data Type (ADT), its core concepts, representations, and fundamental operations, providing a foundation for solving complex problems in networking, social media analysis, routing, and more.

## Core Concepts & Terminology

A graph `G` is formally defined as a pair `(V, E)`, where:

- `V` is a finite set of **vertices** (also called **nodes**).
- `E` is a set of **edges** (also called **arcs**), which are pairs of vertices representing a connection between them.

For an edge `e = (u, v)`, the vertices `u` and `v` are said to be **adjacent**. The edge `e` is **incident** to both `u` and `v`.

### Types of Graphs

1.  **Undirected Graph:** Edges have no direction. The pair `(u, v)` is unordered, meaning `(u, v)` is the same as `(v, u)`. It represents a two-way relationship.
    - _Example:_ A Facebook friendship network. If Alice is friends with Bob, then Bob is also friends with Alice.

2.  **Directed Graph (Digraph):** Edges have a direction. The pair `<u, v>` is ordered, indicating a one-way relationship from `u` (the source) to `v` (the destination). `<u, v>` is different from `<v, u>`.
    - _Example:_ A web page link graph. A link from Page A to Page B does not imply a link back from Page B to Page A.

3.  **Weighted Graph:** A graph (directed or undirected) where each edge is assigned a numerical value, called a **weight** (or cost).
    - _Example:_ A map where cities are vertices, roads are edges, and the weight of an edge is the distance between the two cities.

### Common Terminology

- **Path:** A sequence of vertices where each adjacent pair is connected by an edge.
- **Cycle:** A path that starts and ends at the same vertex.
- **Connected Graph:** An undirected graph where there is a path between every pair of vertices.
- **Degree of a Vertex:** The number of edges incident to the vertex. In a digraph, we have **in-degree** (edges coming in) and **out-degree** (edges going out).

## The Graph ADT

The Graph ADT defines a set of operations that can be performed on a graph, independent of its underlying implementation.

### Common Operations

The primary operations of the Graph ADT include:

- `Graph()`: Constructor to create an empty graph.
- `add_vertex(v)`: Adds a vertex `v` to the graph.
- `add_edge(u, v)`: Adds an edge between vertices `u` and `v` (for a digraph, from `u` to `v`).
- `add_edge(u, v, w)`: Adds a weighted edge with weight `w`.
- `remove_vertex(v)`: Removes vertex `v` and all its incident edges.
- `remove_edge(u, v)`: Removes the edge between `u` and `v`.
- `get_vertices()`: Returns a list of all vertices in the graph.
- `get_edges()`: Returns a list of all edges in the graph.
- `is_adjacent(u, v)`: Returns `True` if there is an edge from `u` to `v`.
- `neighbors(v)`: Returns a list of all vertices adjacent to `v`.
- `get_weight(u, v)`: Returns the weight of the edge between `u` and `v`.

## Implementation Representations

The two most common ways to implement the Graph ADT are:

1.  **Adjacency Matrix:** A 2D array `matrix` of size `V x V`.
    - `matrix[i][j] = 1` (or weight `w`) indicates an edge from vertex `i` to vertex `j`.
    - `matrix[i][j] = 0` (or `∞`) indicates no edge.
    - _Pros:_ `O(1)` time to check if an edge exists.
    - _Cons:_ `O(V²)` space, which is inefficient for **sparse graphs** (graphs with relatively few edges).

2.  **Adjacency List:** An array (or dictionary) of lists. The index (or key) represents a vertex, and the corresponding list contains all vertices adjacent to it (often stored as tuples including the weight).
    - _Pros:_ `O(V + E)` space, making it efficient for sparse graphs.
    - _Cons:_ `O(Degree(V))` time to check for an edge, as it requires scanning the list.

The choice of representation depends on the specific application and whether the graph is dense or sparse. The adjacency list is generally preferred for most algorithm implementations.

## Key Points & Summary

- A **Graph** is an ADT defined by a set of **vertices** and **edges** connecting them.
- Graphs can be **undirected**, **directed**, or **weighted**, each serving different modeling purposes.
- The core Graph ADT operations involve adding/removing vertices/edges and querying relationships (`neighbors`, `is_adjacent`).
- The two primary implementation strategies are the **Adjacency Matrix** (fast edge lookup, high memory cost) and the **Adjacency List** (memory efficient, slower lookup).
- Understanding this ADT is the first step toward mastering fundamental graph algorithms like **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and shortest path algorithms (**Dijkstra's**), which will be covered in subsequent modules. Graphs are essential for solving complex, real-world engineering problems involving networks and relationships.
