# Euler's Theorem in Graph Theory

## Introduction

Welcome,  Engineering students! In this module, we delve into one of the foundational results in Graph Theory: **Euler's Theorem**. This theorem, formulated by the prolific mathematician Leonhard Euler in 1736, solved the famous "Königsberg Bridge Problem" and laid the groundwork for the entire field. Understanding this theorem is crucial as it introduces fundamental concepts about traversing graphs, which have applications in computer networks, circuit design, logistics, and much more.

## Core Concepts

Before we state the theorem, let's define the key concepts involved.

### 1. Euler Path

An **Euler Path** is a path in a graph that traverses every **edge** of the graph exactly once. The vertices may be repeated.

### 2. Euler Circuit

An **Euler Circuit** is a special type of Euler Path that starts and ends at the **same vertex**. It is a closed trail that uses every edge exactly once.

### 3. Degree of a Vertex

The **degree** of a vertex is the number of edges incident to it. A vertex with an odd degree is called an **odd vertex**, and a vertex with an even degree is called an **even vertex**.

---

## Euler's Theorem (for Undirected Graphs)

Euler's theorem provides a simple yet powerful necessary and sufficient condition for a graph to possess an Euler Circuit or an Euler Path. The theorem is stated for connected graphs (graphs where there is a path between every pair of vertices).

### Theorem Statement:

1.  **Eulerian Circuit Exists:** A connected graph `G` has an **Euler circuit** if and only if every vertex in `G` has an **even degree**.

2.  **Eulerian Path Exists:** A connected graph `G` has an **Euler path** (but not an Euler circuit) if and only if it has **exactly two vertices of odd degree**. Furthermore, any Euler path must start at one of these odd-degree vertices and end at the other.

### Why does this work?

- For an Euler circuit, every time you enter a vertex via one edge, you must leave it via a different edge. This pairing of incoming and outgoing edges means the degree of each vertex must be even.
- For an Euler path, the start and end vertices are exceptions to this pairing rule. You leave the start vertex without entering it first, and you enter the end vertex without leaving it. This explains why these two vertices (and only these two) must have an odd degree.

---

## Examples

Let's apply the theorem to some common graphs.

**Example 1: Euler Circuit**
Consider a cycle graph `C₄` (a square).

- Degree of each vertex: 2 (even).
- According to the theorem, an Euler circuit exists.
- The circuit is simple: `A -> B -> C -> D -> A`.

**Example 2: Euler Path**
Consider a graph with vertices `A, B, C` and edges `A-B, B-C, C-A, A-D`.

- Degrees: `deg(A)=3`, `deg(B)=2`, `deg(C)=2`, `deg(D)=1`.
- There are exactly two vertices with odd degree: `A` and `D`.
- According to the theorem, an Euler path exists from `D` to `A` (or `A` to `D`).
- One such path is `D -> A -> B -> C -> A`.

**Example 3: Neither**
Consider the graph `K₄` (complete graph on 4 vertices).

- Degree of each vertex: 3 (odd).
- There are four (more than two) vertices of odd degree.
- Therefore, the graph has **neither** an Euler path nor an Euler circuit.

---

## Key Points & Summary

| Feature           | Necessary and Sufficient Condition (for a connected graph) |
| :---------------- | :--------------------------------------------------------- |
| **Euler Circuit** | **All vertices have even degree.**                         |
| **Euler Path**    | **Exactly two vertices have odd degree.**                  |
| **Neither**       | More than two vertices have odd degree.                    |

- **Foundation:** Euler's Theorem is the cornerstone for understanding graph traversability.
- **Application:** The algorithm to _find_ an Euler circuit (e.g., Fleury's algorithm or Hierholzer's algorithm) relies on this theorem to know one exists before starting.
- **Directed Graphs:** A similar theorem exists for directed graphs (digraphs), considering in-degree and out-degree. A digraph has an Euler circuit if and only if it is strongly connected and every vertex has equal in-degree and out-degree.
- **Remember:** The theorem only applies to **finite** graphs with **no isolated vertices** (though isolated vertices with degree 0, which is even, are technically allowed as long as the graph is connected).

In summary, Euler's Theorem provides an elegantly simple way to determine if a graph can be traversed in a single continuous path using every edge exactly once, a concept with profound theoretical and practical implications in engineering and computer science.
