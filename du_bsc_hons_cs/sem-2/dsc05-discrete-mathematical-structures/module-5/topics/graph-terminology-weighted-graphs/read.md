# Graph Terminology and Weighted Graphs

## Introduction

Graph theory is one of the most versatile and practical branches of mathematics, forming the foundation for numerous computer science applications. From social network analysis and Google Maps navigation to airline scheduling and circuit design, graphs provide a powerful framework for modeling relationships between objects. In this module, we will explore the fundamental terminology of graph theory and delve into the specialized area of weighted graphs, which assign numerical values to edges to represent costs, distances, or capacities.

Understanding graph terminology is essential for any computer science student, as algorithms like Dijkstra's shortest path, Kruskal's minimum spanning tree, and network flow algorithms rely heavily on a clear understanding of graph structure. The University of Delhi's curriculum emphasizes both theoretical foundations and practical applications, preparing students to tackle complex real-world problems using graph-based approaches.

This topic builds upon the basic concepts of graphs (vertices and edges) and introduces the mathematical formalism needed to work with more sophisticated graph structures. By the end of this module, you will be able to identify different types of graphs, understand their properties, and apply weighted graph concepts to solve optimization problems.

## Key Concepts

### Basic Graph Terminology

A **graph** G = (V, E) consists of a finite non-empty set of vertices (also called nodes or points) V = {v₁, v₂, ..., vₙ} and a set of edges (also called arcs or lines) E = {e₁, e₂, ..., eₘ}. Each edge connects two vertices, which may be the same vertex (forming a loop) or may connect the same pair of vertices more than once (forming parallel edges).

**Simple graphs** are graphs that have no loops and no parallel edges. Most of our discussion will focus on simple graphs, as they form the foundation for more complex structures.

A graph is called **undirected** if the edges have no direction, meaning the relationship between vertices is symmetric. In an undirected graph, an edge {u, v} is identical to edge {v, u}. Conversely, a **directed graph** (or digraph) has edges with direction, where an edge (u, v) is distinct from edge (v, u). In directed graphs, we use ordered pairs to represent edges, and we say edge (u, v) goes from u (the tail) to v (the head).

The **degree** of a vertex in an undirected graph is the number of edges incident to it. A vertex with degree 0 is called an **isolated vertex**, while a vertex with degree 1 is called a **pendant vertex**. In directed graphs, we distinguish between **in-degree** (number of edges entering the vertex) and **out-degree** (number of edges leaving the vertex).

### Special Graph Structures

**Complete graphs** are graphs where every pair of distinct vertices is connected by an edge. The complete graph with n vertices is denoted as Kₙ. Kₙ has n(n-1)/2 edges. For example, K₃ (a triangle) has 3 vertices and 3 edges, while K₄ (a tetrahedron) has 4 vertices and 6 edges.

**Bipartite graphs** are graphs whose vertex set can be divided into two disjoint sets U and V such that every edge connects a vertex in U to a vertex in V. No edge connects vertices within the same set. A complete bipartite graph Kₘ,ₙ has m vertices in one set and n vertices in the other, with all possible m×n edges connecting the two sets.

**Planar graphs** are graphs that can be drawn in a plane without any edges crossing. This concept is crucial in circuit design and map coloring problems. Euler's formula for planar graphs states that for a connected planar graph with V vertices, E edges, and F faces: V - E + F = 2.

**Subgraphs** are graphs formed from a subset of vertices and edges of a larger graph. A **spanning subgraph** uses all vertices of the original graph but only a subset of edges, while an **induced subgraph** uses a subset of vertices and all edges connecting those vertices in the original graph.

### Paths, Cycles, and Connectivity

A **path** is a sequence of vertices where each consecutive pair is connected by an edge. The **length** of a path is the number of edges it contains. A path is **simple** if it doesn't repeat any vertices (except possibly the starting and ending vertex in a cycle).

A **cycle** is a path that starts and ends at the same vertex. A cycle is simple if it doesn't repeat vertices (except the starting/ending vertex). An undirected graph with no cycles is called a **tree**, and a tree with n vertices has exactly n-1 edges.

Two vertices are **connected** if there exists a path between them. A graph is **connected** if every pair of vertices is connected. In directed graphs, we distinguish between **strongly connected** (there exists a directed path from any vertex to any other vertex) and **weakly connected** (the underlying undirected graph is connected).

### Weighted Graphs

A **weighted graph** is a graph where each edge is assigned a numerical value called its **weight** or **cost**. These weights can represent various quantities depending on the application: distances between cities, time required to complete a task, cost of a transportation route, or capacity of a network link.

Formally, a weighted graph G = (V, E, w) consists of vertices V, edges E, and a weight function w: E → ℝ that assigns a real number to each edge. The weight of a path is the sum of the weights of all edges comprising that path.

Weighted graphs can be either undirected or directed. In undirected weighted graphs, the weight function is symmetric: w(u, v) = w(v, u). In directed weighted graphs (also called **weighted digraphs**), weights may differ based on direction.

### Important Theorems and Properties

**Handshaking Lemma**: In any undirected graph, the sum of all vertex degrees equals twice the number of edges. Mathematically: Σ deg(v) = 2|E|. This fundamental result has many applications in graph theory and provides a quick way to verify graph properties.

**Eulerian Path and Circuit**: An Eulerian path traverses each edge exactly once. A graph has an Eulerian circuit if and only if it is connected and all vertices have even degree. An Eulerian path (but not circuit) exists if exactly two vertices have odd degree.

**Dijkstra's Algorithm**: For finding shortest paths in weighted graphs with non-negative weights, Dijkstra's algorithm efficiently computes the shortest path from a source vertex to all other vertices. Its time complexity is O(V²) with simple implementation or O(E log V) with priority queues.

**Minimum Spanning Tree (MST)**: For a connected weighted undirected graph, a spanning tree with minimum total edge weight. Two classic algorithms are Prim's algorithm and Kruskal's algorithm, both with time complexity O(E log V) with proper data structures.

## Examples

### Example 1: Analyzing Graph Properties

Consider a graph with vertices {A, B, C, D, E} and edges: AB, AC, AD, BC, BD, CD, DE.

(a) Determine if the graph is simple, complete, or bipartite.
(b) Find the degree of each vertex.
(c) Identify any isolated or pendant vertices.

**Solution:**

(a) The graph has no loops or parallel edges, so it is simple. It is not complete because vertices B and E are not directly connected, and C and E are not directly connected. To check if it's bipartite, we need to partition vertices into two sets with no edges within each set. Let's try: Set 1 = {A, D, E}, Set 2 = {B, C}. Checking edges: AB (A-B, different sets ✓), AC (A-C, ✓), AD (A-D, same set ✗). So it is NOT bipartite.

(b) Degrees: deg(A) = 3 (edges AB, AC, AD); deg(B) = 3 (AB, BC, BD); deg(C) = 3 (AC, BC, CD); deg(D) = 4 (AD, BD, CD, DE); deg(E) = 1 (DE).

(c) No isolated vertices (all have degree > 0). Vertex E has degree 1, so it is a pendant vertex.

### Example 2: Weighted Graph Shortest Path

Consider the following weighted undirected graph with vertices {P, Q, R, S, T} and edge weights:
P-Q: 4, P-R: 2, Q-R: 1, Q-S: 5, R-S: 3, R-T: 6, S-T: 2

Find the shortest path from P to T and its total weight.

**Solution:**

We can use Dijkstra's algorithm:

**Step 1**: Start at P with distance 0. Mark P as visited.
- Distance to Q: 4 (via P-Q)
- Distance to R: 2 (via P-R)
- Others: ∞

**Step 2**: Choose vertex R (distance 2, smallest unvisited). Mark R as visited.
- Distance to Q: min(4, 2+1=3) = 3 (via P-R-Q)
- Distance to S: 2+3=5 (via P-R-S)
- Distance to T: 2+6=8 (via P-R-T)

**Step 3**: Choose vertex Q (distance 3). Mark Q as visited.
- Distance to S: min(5, 3+5=8) = 5
- Distance to T: min(8, 3+5=8) = 8

**Step 4**: Choose vertex S (distance 5). Mark S as visited.
- Distance to T: min(8, 5+2=7) = 7

**Step 5**: Choose vertex T (distance 7). Mark T as visited.

Shortest path from P to T: P → R → S → T
Total weight: 2 + 3 + 2 = 7

### Example 3: Minimum Spanning Tree

For the same graph in Example 2, find the minimum spanning tree using Kruskal's algorithm.

**Solution:**

Sort edges by weight:
1. Q-R: 1
2. P-R: 2
3. R-S: 3
4. P-Q: 4
5. S-T: 2 → Wait, let me reorder: 1, 2, 2, 3, 4, 5, 6

Actually: Q-R(1), P-R(2), S-T(2), R-S(3), P-Q(4), Q-S(5), R-T(6)

Apply Kruskal's:
1. Add Q-R (1) - doesn't form cycle ✓
2. Add P-R (2) - doesn't form cycle ✓
3. Add S-T (2) - doesn't form cycle ✓
4. Add R-S (3) - doesn't form cycle ✓ (connects R to S, but S-T already connects them differently)
5. Add P-Q (4) - would form cycle with P-R-Q ✗ skip
6. Add Q-S (5) - would form cycle ✗ skip
7. Add R-T (6) - would form cycle ✗ skip

MST edges: Q-R, P-R, S-T, R-S
Total weight: 1 + 2 + 2 + 3 = 8

## Exam Tips

1. **Understand definitions precisely**: In DU exams, students often lose marks by confusing similar terms. Remember that "complete" means every pair of vertices is connected, while "connected" means there's a path between every pair.

2. **Apply the Handshaking Lemma strategically**: When given degree sequence information, use Σ deg(v) = 2|E| to find missing information quickly. This is a frequently tested concept.

3. **Dijkstra's Algorithm is crucial**: Be prepared to trace Dijkstra's algorithm step-by-step in exams. Remember it only works with non-negative edge weights.

4. **Know the MST algorithms**: Both Prim's and Kruskal's algorithms are important. Kruskal's is easier to implement and understand—sort edges by weight and add if no cycle forms.

5. **Bipartite graph testing**: To check if a graph is bipartite, try to 2-color it. If you find an edge connecting two same-colored vertices, it's not bipartite.

6. **Directed vs Undirected**: Always pay attention to whether the graph is directed or undirected. In-degree and out-degree only apply to directed graphs, and weight symmetry only applies to undirected weighted graphs.

7. **Real-world applications**: Connect your answers to real-world scenarios. For example, weighted graphs model road networks, and MST helps design efficient telecommunication networks.