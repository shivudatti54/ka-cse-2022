# Introduction to Graph Theory

## Table of Contents

- [Introduction to Graph Theory](#introduction-to-graph-theory)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of a Graph](#definition-of-a-graph)
  - [Types of Graphs](#types-of-graphs)
  - [Basic Terminology](#basic-terminology)
  - [Special Graphs](#special-graphs)
- [Examples](#examples)
  - [Example 1: Identifying Graph Properties](#example-1-identifying-graph-properties)
  - [Example 2: Determining if a Graph is Bipartite](#example-2-determining-if-a-graph-is-bipartite)
  - [Example 3: Drawing a Graph from Adjacency List](#example-3-drawing-a-graph-from-adjacency-list)
- [Exam Tips](#exam-tips)

## Introduction

Graph Theory is a fundamental branch of discrete mathematics that deals with objects called graphs, which consist of vertices (or nodes) connected by edges. Despite its abstract nature, graph theory has become one of the most practical and applicable areas of mathematics in computer science, particularly in areas such as network design, algorithm development, social network analysis, and data structures.

The origin of graph theory can be traced back to 1736 when Leonhard Euler solved the famous Königsberg bridge problem. Euler demonstrated that it was impossible to traverse all seven bridges of Königsberg without crossing any bridge twice. This problem led to the foundation of graph theory as a mathematical discipline. Since then, the field has grown exponentially, finding applications in computer networks, transportation systems, electrical circuits, and even in understanding molecular structures.

For CSE students, graph theory forms the backbone of many algorithms studied in data structures, analysis of algorithms, and compiler design. Understanding the basic definitions and properties of graphs is essential before delving into graph traversal algorithms, spanning trees, and network flow problems. This module introduces the fundamental concepts that will be built upon throughout the course.

## Key Concepts

### Definition of a Graph

A **graph** G is defined as an ordered pair G = (V, E), where V is a finite non-empty set of vertices (or nodes) and E is a set of edges (or arcs) connecting pairs of vertices. If an edge connects vertices u and v, we denote it as uv or (u, v).

**Example:** Consider a graph with V = {v1, v2, v3, v4} and E = {v1v2, v2v3, v3v4, v4v1}. This represents a simple cycle of four vertices.

### Types of Graphs

**1. Simple Graph:** A graph that does not contain loops (edges connecting a vertex to itself) or multiple edges (more than one edge connecting the same pair of vertices).

**2. Multi-Graph:** A graph that may contain multiple edges between the same pair of vertices but does not contain loops.

**3. Pseudograph:** A graph that may contain both loops and multiple edges.

**4. Directed Graph (Digraph):** A graph where each edge has a specific direction, from one vertex to another. Directed edges are called arcs or directed edges.

**5. Undirected Graph:** A graph where edges have no direction; the edge uv is identical to vu.

**6. Weighted Graph:** A graph where each edge has an associated weight or cost. These are extensively used in optimization problems.

### Basic Terminology

**Adjacency:** Two vertices are adjacent if they are connected by an edge. For an undirected graph G with edge e = {u, v}, vertices u and v are said to be adjacent, and the edge e is incident to both u and v.

**Degree of a Vertex:** The degree of a vertex v, denoted as deg(v), is the number of edges incident to v. In a directed graph, we define:

- In-degree: number of edges entering vertex v
- Out-degree: number of edges leaving vertex v

**Isolated Vertex:** A vertex with zero degree (no edges incident to it).

**Pendant Vertex:** A vertex with degree 1.

**Handshaking Lemma:** In any undirected graph, the sum of all vertex degrees equals twice the number of edges. Mathematically: Σ deg(v) = 2|E|

**Path:** A sequence of vertices where each consecutive pair is connected by an edge. A path is simple if no vertex is repeated.

**Cycle:** A path that starts and ends at the same vertex, with all other vertices distinct.

**Connected Graph:** An undirected graph is connected if there exists a path between every pair of vertices.

**Disconnected Graph:** A graph that is not connected; it consists of two or more connected components.

**Complete Graph:** A simple graph in which every pair of distinct vertices is connected by a unique edge. A complete graph with n vertices is denoted as Kn.

**Bipartite Graph:** A graph whose vertex set can be partitioned into two disjoint sets such that every edge connects a vertex from one set to a vertex from the other set.

**Subgraph:** A graph H = (V', E') is a subgraph of G = (V, E) if V' ⊆ V and E' ⊆ E.

### Special Graphs

**Null Graph:** A graph with vertices but no edges.

**Regular Graph:** A graph where all vertices have the same degree. A k-regular graph has all vertices of degree k.

**Cycle Graph (Cn):** A graph with n vertices arranged in a cycle.

**Wheel Graph (Wn):** A cycle graph Cn-1 with an additional vertex connected to all other vertices.

**Complete Bipartite Graph (Km,n):** A bipartite graph where each vertex in the first set is connected to every vertex in the second set.

## Examples

### Example 1: Identifying Graph Properties

Consider the graph G with vertices V = {A, B, C, D, E} and edges E = {AB, BC, CD, DE, EA, AC}.

**Solution:**

1. **Type of graph:** This is a simple undirected graph (no loops, no multiple edges).

2. **Degrees of each vertex:**

- deg(A) = 3 (connected to B, C, E)
- deg(B) = 2 (connected to A, C)
- deg(C) = 3 (connected to B, D, A)
- deg(D) = 2 (connected to C, E)
- deg(E) = 2 (connected to D, A)

3. **Verify Handshaking Lemma:** Sum of degrees = 3 + 2 + 3 + 2 + 2 = 12
   Number of edges = 6
   2|E| = 2 × 6 = 12 ✓ (Satisfied)

4. **Is the graph connected?** Yes, we can reach any vertex from any other vertex.

### Example 2: Determining if a Graph is Bipartite

Determine if the graph with vertices {1, 2, 3, 4, 5} and edges {12, 23, 34, 45, 15} is bipartite.

**Solution:**

Let's try to partition vertices into two sets U and V such that edges only connect vertices between sets.

Starting with vertex 1 in set U = {1}

- 1 connects to 2 → put 2 in set V = {2}
- 1 connects to 5 → put 5 in set V = {2, 5}
- 2 connects to 3 → put 3 in set U = {1, 3}
- 3 connects to 4 → put 4 in set V = {2, 5, 4}
- 4 connects to 5 → Now 4 is in V and 5 is in V (both same set!)

Since vertex 4 and vertex 5 are both in set V but connected by an edge (4-5), this graph is NOT bipartite. This graph contains an odd-length cycle (1-2-3-4-5-1 has length 5), which makes it non-bipartite.

### Example 3: Drawing a Graph from Adjacency List

Construct the graph from the following adjacency list representation:

- A: B, D
- B: A, C, E
- C: B, D
- D: A, C
- E: B

**Solution:**

From the adjacency list, we can draw the graph:

Vertices: V = {A, B, C, D, E}

Edges:

- A connects to B and D → edges: AB, AD
- B connects to A, C, and E → edges: BA (already AB), BC, BE
- C connects to B and D → edges: CB (already BC), CD
- D connects to A and C → edges: DA (already AD), DC (already CD)
- E connects to B → edge: EB (already BE)

Final edge set: E = {AB, AD, BC, BE, CD}

This is an undirected simple graph with 5 vertices and 5 edges. The degrees are: deg(A)=2, deg(B)=3, deg(C)=2, deg(D)=2, deg(E)=1. Sum = 10 = 2 × 5 ✓

## Exam Tips

1. **Memorize the Handshaking Lemma:** Σ deg(v) = 2|E| is one of the most frequently tested concepts. Always use it to verify your answers or find missing information.

2. **Know the relationship between vertices and edges:** In a simple graph with n vertices, the maximum number of edges is n(n-1)/2 (for complete graph Kn).

3. **Understand bipartite graphs:** Remember that a graph is bipartite if and only if it contains no odd-length cycles.

4. **Directed vs Undirected graphs:** In directed graphs, each edge is an ordered pair (u,v), and the in-degree plus out-degree gives the total connections.

5. **Complete graph properties:** In Kn, every vertex has degree (n-1), and total edges = n(n-1)/2.

6. **Regular graph definition:** In a k-regular graph with n vertices, total edges = (n × k)/2.

7. **Know all terminology:** Understand the difference between adjacent vertices, incident edges, isolated vertices, and pendant vertices.

8. **Practice drawing graphs:** Many exam questions give adjacency matrices or lists and ask you to draw the graph or find properties.
