Of course. Here is a comprehensive educational guide on Graph Theory, formatted for  Engineering students preparing for their Semester-End Examination.

---

### **Module 5: Graph Theory - Semester-End Examination Guide**

#### **1. Introduction**

Graph Theory is a fundamental branch of discrete mathematics that studies the properties and applications of graphs. A graph is a mathematical structure used to model pairwise relations between objects. It is incredibly powerful for solving real-world problems in computer networks, data structures, social networks, transportation systems, and project planning.

#### **2. Core Concepts & Definitions**

A graph **G** is defined as an ordered pair **G = (V, E)**, where:

- **V** is a non-empty set of **vertices** (or nodes).
- **E** is a set of **edges** (or lines), which are 2-element subsets of V.

**Basic Terminology:**

- **Order & Size:** The number of vertices `|V|` is the **order** of a graph. The number of edges `|E|` is its **size**.
- **Degree of a Vertex:** The number of edges incident with a vertex. In a directed graph, we have **in-degree** and **out-degree**.
- **Isolated Vertex:** A vertex with a degree of 0.
- **Pendant Vertex:** A vertex with a degree of 1.
- **Types of Graphs:**
  - **Simple Graph:** A graph without loops or multiple edges.
  - **Complete Graph (Kₙ):** A simple graph where every pair of distinct vertices is connected by a unique edge.
  - **Regular Graph:** A graph where each vertex has the same degree.
  - **Bipartite Graph:** A graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V.
  - **Planar Graph:** A graph that can be drawn on a plane without any edges crossing.
- **Walk, Path, and Circuit:**
  - **Walk:** A sequence of vertices where each consecutive pair is connected by an edge.
  - **Path:** A walk in which no vertex is repeated.
  - **Circuit:** A closed path (i.e., it starts and ends at the same vertex).

#### **3. Graph Representations**

Two common ways to represent a graph computationally are:

1.  **Adjacency Matrix:** A 2D array of size V x V. The entry `A[i][j]` is 1 if there is an edge from vertex i to vertex j, otherwise 0. For weighted graphs, the entry contains the weight of the edge.
2.  **Adjacency List:** An array of lists. The size of the array is equal to the number of vertices. Each entry `list[i]` contains all vertices adjacent to vertex i.

#### **4. Important Theorems and Results**

- **Handshaking Lemma:** In any undirected graph, the sum of the degrees of all vertices is equal to twice the number of edges.
  > **∑\_{v∈V} deg(v) = 2|E|**
  > This implies that the number of vertices with an odd degree is always even.
- **Euler's Formula (for connected planar graphs):** If a graph has V vertices, E edges, and F faces (regions), then:
  > **V - E + F = 2**
- **Eulerian Path & Circuit:** A graph contains an Eulerian circuit if and only if every vertex has an even degree. It contains an Eulerian path if and only if exactly zero or two vertices have an odd degree.
- **Hamiltonian Path & Circuit:** A Hamiltonian path visits each vertex exactly once. A Hamiltonian circuit is a cycle that visits each vertex exactly once and returns to the start. (No simple necessary and sufficient condition is known; it's an NP-complete problem).

#### **5. Graph Traversals**

Two fundamental algorithms for searching a graph:

- **Breadth-First Search (BFS):** Explores a graph level-by-level. It uses a queue data structure. It is useful for finding the shortest path in an unweighted graph.
- **Depth-First Search (DFS):** Explores a graph by going as deep as possible along a branch before backtracking. It uses a stack (or recursion). It is useful for topological sorting, detecting cycles, and solving puzzles.

#### **6. Key Points & Summary**

- Graph Theory provides powerful models for network analysis.
- Understand the definitions of **walk, trail, path, and circuit**.
- The **Handshaking Lemma** is a frequently tested concept.
- Know the difference between **Eulerian** (edge-based) and **Hamiltonian** (vertex-based) paths/circuits.
- Be able to **represent a graph** using an adjacency matrix and an adjacency list.
- Understand the basic concepts behind **BFS and DFS** traversal algorithms.
- For planar graphs, **Euler's formula** is crucial.

**Example:** The famous "Seven Bridges of Königsberg" problem, which led to the foundation of Graph Theory, was solved by Euler by showing that a Eulerian circuit did not exist, as more than two vertices had an odd degree.
