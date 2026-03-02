# GRAPHS

## Introduction

Graphs are one of the most versatile and powerful data structures in computer science, representing pairwise relationships between objects. Unlike linear data structures such as arrays and linked lists, or even hierarchical structures like trees, graphs can model complex, non-hierarchical relationships that appear abundantly in real-world scenarios. From social networks connecting millions of users to road networks navigating cities, from airline flight schedules to dependency resolution in software packages, graphs provide the mathematical abstraction needed to solve countless computational problems.

The study of graphs, known as graph theory, began in 1736 when Leonhard Euler solved the famous Königsberg bridge problem. Since then, graph theory has evolved into a fundamental area of mathematics and computer science. In the context of the Computer Science curriculum at the University of Delhi, understanding graphs is essential because they form the backbone of many algorithms and applications studied in advanced courses. The graph abstract data type (ADT), along with elementary graph operations, provides a framework for representing and manipulating graph-based information efficiently.

This chapter explores graphs in depth, covering their definitions, types, representations, and fundamental operations. We will examine both theoretical concepts and practical implementations, preparing you to tackle graph-based problems that frequently appear in university examinations and technical interviews.

## Key Concepts

### Definition and Basic Terminology

A graph G is defined as an ordered pair G = (V, E), where V is a finite non-empty set of vertices (also called nodes) and E is a set of edges (also called arcs or links). Each edge connects two vertices, which may be the same vertex (forming a loop) or different vertices. The cardinality of V, denoted |V|, represents the number of vertices in the graph, while |E| represents the number of edges.

Consider a social network example where vertices represent users and edges represent friendships between users. The graph captures who is connected to whom, enabling analysis of friend recommendations, influence propagation, and community detection.

**Key Terminology:**

- **Adjacent Vertices**: Two vertices u and v are adjacent if there exists an edge (u, v) connecting them.
- **Degree of a Vertex**: The degree of a vertex v, denoted deg(v), is the number of edges incident to v. In directed graphs, we distinguish between in-degree (edges pointing to v) and out-degree (edges emerging from v).
- **Path**: A path is a sequence of vertices where consecutive vertices are connected by edges. The length of a path equals the number of edges traversed.
- **Cycle**: A cycle is a path that starts and ends at the same vertex, with all intermediate vertices distinct.
- **Connected Graph**: An undirected graph is connected if there exists a path between every pair of vertices.
- **Complete Graph**: A complete graph on n vertices, denoted Kn, is an undirected graph where every pair of distinct vertices is connected by a unique edge.

### Types of Graphs

**Undirected Graphs**: In an undirected graph, edges have no direction. The edge (u, v) is identical to (v, u). Social networks, where friendship is mutual, are naturally modeled as undirected graphs.

**Directed Graphs (Digraphs)**: In a directed graph, edges have a specific direction, represented as ordered pairs (u, v), where u is the source and v is the destination. The web, where web pages link to other pages, is modeled as a directed graph. Twitter follow relationships are another example where direction matters.

**Weighted Graphs**: In weighted graphs, each edge carries a numerical weight representing cost, distance, time, or capacity. Road networks where weights represent distances between cities exemplify weighted graphs. Airline networks where weights represent ticket prices between airports are another example.

**Unweighted Graphs**: All edges are treated equally, with no numerical value associated with them.

**Simple Graphs**: Simple graphs have no self-loops (edges from a vertex to itself) and no multiple edges between the same pair of vertices.

**Multigraphs**: Multigraphs allow multiple edges between the same pair of vertices. Telephone networks between cities may have multiple phone lines connecting the same two cities.

### Graph Representations

The choice of graph representation significantly impacts the efficiency of graph algorithms. Two primary representations exist, each with distinct advantages and disadvantages.

**Adjacency Matrix**: A graph with n vertices is represented using an n × n matrix A, where A[i][j] = 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For weighted graphs, A[i][j] stores the weight, or infinity if no edge exists.

For a graph with vertices {0, 1, 2, 3} and edges {(0,1), (0,2), (1,2), (2,3)}, the adjacency matrix is:

```
    0 1 2 3
  0 0 1 1 0
  1 1 0 1 0
  2 1 1 0 1
  3 0 0 1 0
```

**Advantages of Adjacency Matrix:**
- Edge existence query: O(1) time complexity
- Simple to implement
- Efficient for dense graphs where |E| ≈ |V|²

**Disadvantages of Adjacency Matrix:**
- Space complexity: O(V²), regardless of actual edges
- Inefficient for sparse graphs

**Adjacency List**: Each vertex maintains a list of its neighboring vertices. Typically implemented using arrays of linked lists or vectors.

For the same graph, the adjacency list representation is:
```
0 → [1, 2]
1 → [0, 2]
2 → [0, 1, 3]
3 → [2]
```

**Advantages of Adjacency List:**
- Space complexity: O(V + E), efficient for sparse graphs
- Iterating through neighbors is straightforward

**Disadvantages of Adjacency List:**
- Edge existence query: O(degree(v)) time, potentially O(V) in worst case
- More complex implementation than matrix

### Elementary Graph Operations

**Breadth-First Search (BFS)**: BFS explores a graph level by level, starting from a source vertex. It uses a queue data structure to track vertices to be explored. BFS discovers all vertices at distance k before discovering vertices at distance k+1.

Algorithm steps:
1. Mark source vertex as visited and enqueue it
2. While queue is not empty:
   - Dequeue a vertex
   - For each unvisited neighbor, mark as visited and enqueue

BFS produces the shortest path (in terms of edge count) from the source to all reachable vertices in an unweighted graph. The time complexity is O(V + E) using adjacency list representation.

**Depth-First Search (DFS)**: DFS explores as far as possible along each branch before backtracking. It uses a stack (either explicitly or through recursion) to track vertices.

Algorithm steps:
1. Mark current vertex as visited
2. For each unvisited neighbor of current vertex:
   - Recursively visit that neighbor

DFS is fundamental to many graph algorithms, including topological sorting, finding connected components, and detecting cycles. Its time complexity is O(V + E).

### Graph Connectivity

In undirected graphs, connectivity defines whether all vertices are reachable from any other vertex. A **connected component** is a maximal connected subgraph. The number of connected components indicates how many disconnected pieces exist in the graph.

For directed graphs, we distinguish between:
- **Strongly Connected**: A directed graph is strongly connected if there is a directed path from every vertex to every other vertex.
- **Weakly Connected**: Ignoring edge directions, if the underlying undirected graph is connected.

**Tarjan's Algorithm** and **Kosaraju's Algorithm** are efficient methods for finding strongly connected components in O(V + E) time.

### Trees as Graphs

A tree is a special case of an undirected, acyclic, connected graph. Formally, a tree with n vertices has exactly n-1 edges. Every tree is a connected acyclic graph, and conversely, every connected acyclic graph is a tree.

**Key Properties of Trees:**
- There is exactly one path between any two vertices
- Adding any edge to a tree creates exactly one cycle
- Removing any edge disconnects the tree
- A tree with n vertices has n-1 edges

A **forest** is a disjoint union of trees, meaning each connected component is a tree.

### Spanning Trees

A **spanning tree** of a connected graph is a subgraph that is a tree and includes all vertices of the original graph. Every connected graph has at least one spanning tree. A **minimum spanning tree (MST)** in a weighted graph is a spanning tree with minimum total edge weight.

**Famous MST Algorithms:**
- **Kruskal's Algorithm**: Sort all edges by weight, add edges to MST if they don't create a cycle (using Union-Find data structure). Time complexity: O(E log V).
- **Prim's Algorithm**: Grow the MST from a starting vertex, always adding the minimum weight edge that connects to an unvisited vertex. Time complexity: O(E log V) with binary heap, O(E + V log V) with Fibonacci heap.

### Shortest Path Algorithms

Finding the shortest path between vertices is a fundamental graph problem with numerous applications.

**Dijkstra's Algorithm**: Finds shortest paths from a single source to all other vertices in a weighted graph with non-negative edge weights. It uses a priority queue to always process the vertex with minimum distance. Time complexity: O((V + E) log V).

**Bellman-Ford Algorithm**: Handles graphs with negative edge weights (but no negative cycles). It relaxes all edges V-1 times. Time complexity: O(VE).

**Floyd-Warshall Algorithm**: Finds shortest paths between all pairs of vertices. Time complexity: O(V³), suitable for dense graphs.

### Topological Sort

Topological sorting orders vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v), u appears before v in the ordering. This is essential for task scheduling, build systems, and dependency resolution.

**Kahn's Algorithm** and **DFS-based topological sort** are the two common approaches, both with O(V + E) time complexity.

## Examples

### Example 1: Representing a City Map as a Graph

Consider a simplified map of Delhi with key locations as vertices and major roads as edges with distances (in km) as weights:

Vertices: {CP (Connaught Place), Hauz Khas, Dwarka, Noida, Gurgaon}
Edges: {(CP-Hauz Khas, 8), (CP-Dwarka, 15), (CP-Noida, 12), (Hauz Khas-Gurgaon, 10), (Dwarka-Gurgaon, 25), (Noida-Gurgaon, 20)}

**Adjacency Matrix Representation:**

```
        HK  CP  DW  NO  GU
HK      0   8   ∞   ∞   10
CP      8   0   15  12  ∞
DW      ∞  15   0   ∞   25
NO      ∞  12   ∞   0   20
GU      10  ∞   25  20  0
```

**Adjacency List Representation:**
```
CP: [(Hauz Khas, 8), (Dwarka, 15), (Noida, 12)]
Hauz Khas: [(CP, 8), (Gurgaon, 10)]
Dwarka: [(CP, 15), (Gurgaon, 25)]
Noida: [(CP, 12), (Gurgaon, 20)]
Gurgaon: [(Hauz Khas, 10), (Dwarka, 25), (Noida, 20)]
```

To find the shortest distance from Connaught Place to Gurgaon, we can apply Dijkstra's algorithm:
- Initial distances: CP = 0, others = ∞
- Process CP: Update HK = 8, DW = 15, NO = 12
- Process HK (distance 8): Update GU = 18 (via HK)
- The shortest path is CP → Hauz Khas → Gurgaon with total distance 18 km.

### Example 2: BFS Traversal in an Undirected Graph

Given a graph with vertices {A, B, C, D, E, F} and edges: {A-B, A-C, B-D, C-D, D-E, E-F}

Starting BFS from vertex A:
1. Queue: [A], Visit A
2. Queue: [B, C], Visit B, mark visited
3. Queue: [C, D], Visit C, mark visited
4. Queue: [D, D], Visit first D (when dequeued), mark visited
5. Queue: [D, E], Visit E when D is processed
6. Queue: [E, F], Visit F when E is processed

BFS Visit Order: A → B → C → D → E → F
Levels from A: A(level 0), B and C(level 1), D(level 2), E and F(level 3)

### Example 3: Detecting Cycle Using DFS

Consider a directed graph with vertices {1, 2, 3, 4} and edges: {(1,2), (2,3), (3,1), (3,4)}

Using DFS with three-color marking (WHITE = unvisited, GRAY = in progress, BLACK = completed):
- Start DFS from vertex 1: Color 1 as GRAY
- Visit 2: Color 2 as GRAY
- Visit 3: Color 3 as GRAY
- From 3, we see an edge to 1, which is GRAY (still in recursion stack)
- This indicates a cycle: 1 → 2 → 3 → 1

Cycle detection is crucial in scenarios like deadlock detection in operating systems, detecting circular dependencies in build systems, and ensuring validity of prerequisite relationships in course planning.

## Exam Tips

1. **Understand the difference between adjacency matrix and adjacency list** - Know when to use each representation based on graph density. This is a frequently asked question in DU examinations.

2. **Master BFS and DFS algorithms** - Be able to trace through these algorithms step by step, including the state of data structures at each iteration. Know their time and space complexities.

3. **Know the conditions for graph types** - Understand when a graph is connected, strongly connected, or weakly connected. Be able to provide examples of each type.

4. **Remember graph properties** - In a tree with n vertices, there are exactly n-1 edges. In a complete graph Kn, there are n(n-1)/2 edges.

5. **Practice shortest path problems** - Be able to apply Dijkstra's algorithm manually. Remember that it doesn't work with negative edge weights.

6. **Topological sort only applies to DAGs** - Before applying topological sort, verify the graph is acyclic. Know both Kahn's algorithm and DFS-based approaches.

7. **Understand real-world applications** - Connecting theoretical concepts to applications like social networks, road maps, and web page linking demonstrates deeper understanding in answer writing.

8. **Know time complexities** - For BFS/DFS: O(V+E). For adjacency matrix operations: O(1) for edge queries, O(V²) space. For adjacency list: O(V+E) space.

9. **Memorize key definitions** - Be precise with definitions of path, cycle, connected components, spanning tree, and minimum spanning tree.

10. **Practice previous year questions** - Many DU examination questions repeat patterns. Solve questions on graph representations, traversals, and finding connected components.