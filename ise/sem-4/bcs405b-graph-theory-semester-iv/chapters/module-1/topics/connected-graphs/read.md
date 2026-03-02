Of course. Here is a comprehensive educational content module on "Connected Graphs" for  Engineering students, formatted as requested.

# Module 1: Graph Theory - Connected Graphs

**Subject:** Graph Theory | **Semester:** IV

## Introduction

In Graph Theory, the concept of **connectivity** is fundamental. It helps us understand the robustness and efficiency of a network, whether it's a computer network, a transportation system, or a social web. Simply put, a graph is connected if you can travel from any vertex to any other vertex by following the edges. If you cannot, the graph is disconnected. This module delves into the formal definitions, types, and key theorems related to connected graphs.

## Core Concepts

### 1. Definition of a Connected Graph

A graph `G` is said to be **connected** if there is a path between every pair of vertices. If there exists at least one pair of vertices for which no path exists, the graph is **disconnected**.

**Example:**
Consider two simple graphs:

- **Graph A:** A triangle (3 vertices all connected to each other). This is connected.
- **Graph B:** Two separate triangles with no connection between them. This is disconnected. There is no path from a vertex in the first triangle to a vertex in the second.

### 2. Components of a Graph

A **component** of a graph is a maximal connected subgraph. "Maximal" means that you cannot add any other vertex from the graph to this subgraph without breaking its connected property.

- In a **connected graph**, there is exactly **one component** (the entire graph itself).
- In a **disconnected graph**, there are **two or more components**.

**Example:**
Imagine a graph with three isolated vertices and a separate pair of connected vertices. This graph has four components: three single-vertex components and one component consisting of the connected pair.

### 3. Paths and Connectivity

The existence of a **path** is the criterion for connectivity. A path is a sequence of vertices where each consecutive pair is connected by an edge.

- The **distance** between two vertices `u` and `v`, denoted `d(u, v)`, is the length (number of edges) of the shortest path between them. If no path exists, the distance is defined as infinity (`∞`).

### 4. Cut-Vertices and Cut-Edges (Bridges)

These are special elements whose removal increases the number of components in a graph.

- **Cut-Vertex (Articulation Point):** A vertex `v` is a cut-vertex if its removal (along with its incident edges) disconnects the graph or increases the number of components.
- **Cut-Edge (Bridge):** An edge `e` is a cut-edge if its removal disconnects the graph or increases the number of components.

**Example:**
In a path graph `A-B-C-D`, the vertices `B` and `C` are cut-vertices. Removing `B` would disconnect `A` from `C` and `D`. Every edge in this path is a bridge. Removing any edge breaks the path into two components.

### 5. Vertex and Edge Connectivity

This quantifies _how_ connected a graph is, i.e., its resilience to failure.

- **Vertex Connectivity (κ(G)):** The minimum number of vertices whose removal results in a disconnected or trivial (single-vertex) graph.
- **Edge Connectivity (λ(G)):** The minimum number of edges whose removal results in a disconnected graph.

For any connected graph `G`, a fundamental theorem (Whitney's Theorem) states:
**κ(G) ≤ λ(G) ≤ δ(G)**
where `δ(G)` is the minimum degree of the graph.

**Example:**

- In a complete graph `K_n`, you must remove `n-1` vertices to disconnect it. So, `κ(K_n) = n-1`.
- A cycle graph `C_n` has `κ(C_n) = 2` and `λ(C_n) = 2`. You need to remove at least two vertices or two edges to disconnect it.
- A tree has vertex and edge connectivity of `1` (κ(T) = λ(T) = 1), as it has many cut-vertices and every edge is a bridge.

### 6. Theorems on Connectivity

Two important theorems help us understand the relationship between paths and connectivity:

- **Theorem:** A graph is disconnected if and only if its vertex set `V` can be partitioned into two non-empty subsets `V1` and `V2` such that there exists no edge in `G` with one end vertex in `V1` and the other in `V2`.

- **Theorem:** If a graph `G` has exactly two vertices of odd degree, then there exists a path connecting these two vertices. (This is a key lemma often used in the study of Eulerian paths).

## Key Points & Summary

- A graph is **connected** if a path exists between every pair of vertices; otherwise, it is **disconnected**.
- The connected parts of a graph are its **components**.
- **Cut-vertices** and **Cut-edges (Bridges)** are specific elements whose removal disconnects a graph.
- **Vertex Connectivity (κ)** and **Edge Connectivity (λ)** are numerical measures of a graph's robustness. They represent the minimum number of vertices or edges, respectively, that need to be removed to disconnect the graph.
- **Whitney's Theorem** provides a relationship: κ(G) ≤ λ(G) ≤ δ(G) for any connected graph `G`.
- Understanding connectivity is crucial for analyzing network reliability, routing protocols, and social network analysis.
