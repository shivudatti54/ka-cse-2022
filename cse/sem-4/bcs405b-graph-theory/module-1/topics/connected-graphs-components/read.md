# Connected Graphs, Disconnected Graphs and Components

## Table of Contents

- [Connected Graphs, Disconnected Graphs and Components](#connected-graphs-disconnected-graphs-and-components)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Graph Definitions](#basic-graph-definitions)
  - [Walk, Path, and Cycle](#walk-path-and-cycle)
  - [Connected Graphs](#connected-graphs)
  - [Components](#components)
  - [Connectivity in Directed Graphs](#connectivity-in-directed-graphs)
  - [Cut Vertices and Cut Edges](#cut-vertices-and-cut-edges)
- [Examples](#examples)
  - [Example 1: Identifying Connected and Disconnected Graphs](#example-1-identifying-connected-and-disconnected-graphs)
  - [Example 2: Finding Components Using BFS](#example-2-finding-components-using-bfs)
  - [Example 3: Strongly Connected Components](#example-3-strongly-connected-components)
- [Exam Tips](#exam-tips)

## Introduction

Graph theory is a fundamental branch of discrete mathematics that provides powerful tools for modeling relationships between objects. A graph consists of vertices (or nodes) and edges that connect pairs of vertices. The concept of connectivity is central to graph theory as it determines whether we can travel from one vertex to another through a sequence of edges. This topic explores the fundamental notions of connected graphs, disconnected graphs, and components, which are essential for understanding more advanced graph properties and algorithms.

Connectivity in graphs has practical applications in various fields including computer networks, transportation systems, social networks, and circuit design. Understanding whether a graph is connected or disconnected helps determine the robustness of networks, the reachability of nodes, and the existence of paths between entities. This module provides the foundation for studying traversal algorithms, network flow problems, and graph connectivity measures.

## Key Concepts

### Basic Graph Definitions

A **graph** G = (V, E) consists of a finite non-empty set V of vertices (or nodes) and a set E of edges, where each edge is an unordered pair of distinct vertices. A graph is called **simple** if it has no loops (edges connecting a vertex to itself) and no multiple edges (more than one edge between the same pair of vertices).

A graph can be **undirected** (edges have no direction) or **directed** (edges, called arcs, have a specific direction from one vertex to another). In this module, we primarily focus on undirected graphs for connectivity concepts, though we will also discuss directed graph connectivity.

### Walk, Path, and Cycle

A **walk** in a graph is a sequence of vertices where consecutive vertices are adjacent (connected by an edge). The length of a walk is the number of edges traversed. A **trail** is a walk with no repeated edges, while a **path** is a walk with no repeated vertices.

A **cycle** is a closed path where the starting and ending vertices are the same, and no other vertex is repeated. For example, in a triangle graph, traveling from vertex A to B to C and back to A forms a cycle of length 3.

### Connected Graphs

An undirected graph is said to be **connected** if there exists a path between every pair of vertices. In other words, for any two distinct vertices u and v in the graph, there exists a sequence of edges that allows us to reach v starting from u. The smallest connected graph is a single vertex with no edges, which is trivially connected.

A graph that is not connected is called **disconnected**. In a disconnected graph, there exists at least one pair of vertices between which no path exists. The disconnected graph can be decomposed into maximal connected subgraphs.

### Components

A **component** (or connected component) of an undirected graph is a maximal connected subgraph. That is, a component is a connected subgraph that is not properly contained in any other connected subgraph of the graph. Each vertex belongs to exactly one component, and two vertices are in the same component if and only if there exists a path between them.

The number of connected components in a graph G is denoted as ω(G). A graph is connected if and only if ω(G) = 1. The components of a graph can be found using algorithms like Breadth-First Search (BFS) or Depth-First Search (DFS).

### Connectivity in Directed Graphs

For directed graphs, we define two types of connectivity:

**Strongly Connected**: A directed graph is strongly connected if there exists a directed path from every vertex to every other vertex. That is, for any pair of distinct vertices u and v, there is a directed path from u to v and also from v to u.

**Weakly Connected**: A directed graph is weakly connected if the underlying undirected graph (obtained by ignoring edge directions) is connected. The underlying undirected graph replaces each directed edge with an undirected edge.

A **strongly connected component** (SCC) of a directed graph is a maximal strongly connected subgraph. Every directed graph can be decomposed into its strongly connected components, which form a DAG (Directed Acyclic Graph) when contracted.

### Cut Vertices and Cut Edges

A **cut vertex** (or articulation point) is a vertex whose removal (along with all incident edges) increases the number of connected components in the graph. Similarly, a **cut edge** (or bridge) is an edge whose removal disconnects the graph. These concepts are important for analyzing graph robustness and network reliability.

## Examples

### Example 1: Identifying Connected and Disconnected Graphs

Consider the following graphs:

Graph G₁: V = {1, 2, 3, 4}, E = {{1,2}, {2,3}, {3,4}}
Graph G₂: V = {1, 2, 3, 4, 5}, E = {{1,2}, {2,3}, {4,5}}

**Solution:**

For G₁: Starting from vertex 1, we can reach vertex 2 via edge {1,2}. From vertex 2, we can reach vertex 3 via {2,3}, and from 3 we can reach 4 via {3,4}. Therefore, there is a path between every pair of vertices. G₁ is connected with ω(G₁) = 1.

For G₂: Vertices 1, 2, and 3 form one connected component. Vertices 4 and 5 form another component. However, there is no path between vertex 3 and vertex 4 (or 5). Therefore, G₂ is disconnected with ω(G₂) = 2.

### Example 2: Finding Components Using BFS

Given graph G: V = {a, b, c, d, e, f, g}, E = {{a,b}, {a,c}, {b,d}, {c,d}, {e,f}, {f,g}}

**Solution:**

Starting from vertex 'a':

- Visit 'a', mark as visited
- From 'a', visit 'b' and 'c'
- From 'b', visit 'd'
- From 'c', we find 'd' already visited
- Vertices visited: {a, b, c, d} - This is Component 1

Starting from unvisited vertex 'e':

- Visit 'e', then 'f', then 'g'
- Vertices visited: {e, f, g} - This is Component 2

Therefore, the graph has 2 components: {a, b, c, d} and {e, f, g}.

### Example 3: Strongly Connected Components

Consider the directed graph D: V = {1, 2, 3, 4}, E = {(1,2), (2,1), (2,3), (3,4), (4,3)}

**Solution:**

Let's analyze reachability:

- From vertex 1: can reach 1, 2 (via 1→2), and 3 (via 1→2→3)
- From vertex 2: can reach 2, 1, 3, 4
- From vertex 3: can reach 3, 4
- From vertex 4: can reach 4, 3

Vertices 1 and 2 can reach each other (1↔2), so {1, 2} is a strongly connected component.

Vertices 3 and 4 can reach each other (3↔4), so {3, 4} is a strongly connected component.

The strongly connected components are: {1, 2} and {3, 4}.

## Exam Tips

1. **Remember the definition**: A graph is connected if there is a path between every pair of vertices; otherwise, it is disconnected.

2. **Number of components**: The notation ω(G) represents the number of connected components. For a connected graph, ω(G) = 1.

3. **Component identification**: Use BFS or DFS to find all components. Start from any vertex, traverse all reachable vertices—that's one component.

4. **Directed vs undirected connectivity**: In directed graphs, check for strongly connected (both directions) or weakly connected (ignore directions).

5. **Trivial case**: A graph with a single vertex is always connected, regardless of whether edges exist.

6. **Cut vertices and edges**: Remember that removing a cut vertex or bridge increases the number of components.

7. **SCC in directed graphs**: Every directed graph can be decomposed into strongly connected components that form a DAG when contracted.

8. **Prove disconnected**: To prove a graph is disconnected, find two vertices with no path between them or identify isolated vertices.
