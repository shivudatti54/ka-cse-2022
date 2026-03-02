# GRAPHS

## Introduction

Graphs are fundamental non-linear data structures that model pairwise relationships between objects. Unlike linear data structures such as arrays, linked lists, stacks, and queues where elements are arranged sequentially, graphs represent connections that can form complex networks. The study of graphs is central to computer science and discrete mathematics, with applications spanning social networks, transportation systems, computer networks, dependency resolution, and algorithmic problem-solving.

In the context of the University of Delhi Data Structures curriculum, graphs represent a crucial transition from linear to non-linear data structures. Understanding graphs requires building upon the abstract data type concepts introduced earlier and prepares students for advanced algorithmic approaches. Graphs enable the representation of real-world scenarios where relationships are bidirectional or multidirectional, making them indispensable in modern computing applications.

The importance of graphs in computer science cannot be overstated. From finding the shortest path in navigation systems to detecting cycles in dependency graphs, from social network analysis to web page ranking, graphs provide the theoretical foundation for solving complex connectivity problems. This chapter explores the fundamental concepts, representations, operations, and applications of graphs as essential knowledge for any computer science undergraduate.

## Key Concepts

### Definition and Basic Terminology

A graph G is defined as an ordered pair G = (V, E) where V is a finite non-empty set of vertices (also called nodes) and E is a set of edges (also called arcs) that connect pairs of vertices. The vertices represent entities, and edges represent relationships between those entities. For example, in a social network graph, vertices could represent users and edges could represent friendships between users.

The order of a graph refers to the number of vertices |V|, while the size of a graph refers to the number of edges |E|. A graph is said to be trivial if it contains only one vertex and no edges. The neighborhood of a vertex v consists of all vertices that are adjacent to v, meaning there exists an edge connecting v to that vertex.

### Types of Graphs

**Undirected Graph**: In an undirected graph, edges have no direction. The edge {u, v} is identical to the edge {v, u}. If there is an edge between vertex u and vertex v, the relationship is symmetric. Social networks typically use undirected graphs where friendship is a mutual relationship.

**Directed Graph (Digraph)**: In a directed graph, edges have a specific direction. An edge is represented as an ordered pair (u, v), indicating a connection from u to v but not necessarily from v to u. The edge (u, v) is different from (v, u). Twitter followers, web page links, and task dependencies are naturally represented using directed graphs.

**Simple Graph**: A simple graph contains no self-loops (edges connecting a vertex to itself) and no multiple edges (parallel edges) between the same pair of vertices.

**Multigraph**: A multigraph allows multiple edges between the same pair of vertices. This is useful in scenarios like flight connections between cities where multiple airlines operate the same route.

**Pseudograph**: A pseudograph allows both self-loops and multiple edges.

**Weighted Graph**: In a weighted graph, each edge has an associated weight or cost. The weight can represent distance, time, cost, or any metric relevant to the problem. Navigation systems use weighted graphs where edge weights represent travel distances or times.

**Unweighted Graph**: In an unweighted graph, all edges are considered to have equal weight, typically treated as weight 1.

### Degree and In-Degree/Out-Degree

In an undirected graph, the degree of a vertex v, denoted deg(v), is the number of edges incident to v. Each loop contributes 2 to the degree. The sum of degrees of all vertices equals twice the number of edges, which is known as the Handshaking Lemma: Σ deg(v) = 2|E|.

In a directed graph, each vertex has two separate degree measures. The in-degree of v, denoted indeg(v), is the number of edges entering v. The out-degree of v, denoted outdeg(v), is the number of edges leaving v. The total degree is the sum of in-degree and out-degree.

### Paths and Cycles

A path in a graph is a sequence of vertices where each consecutive pair is connected by an edge. The length of a path is the number of edges traversed. A simple path does not repeat any vertices (except possibly the starting and ending vertex). A cycle is a path that starts and ends at the same vertex with at least one edge. A graph containing no cycles is called an acyclic graph.

In directed graphs, paths and cycles must follow the direction of edges. A directed cycle traverses edges in their specified directions. A directed acyclic graph (DAG) is a directed graph with no directed cycles.

### Connectivity

An undirected graph is connected if there is a path between every pair of vertices. If a graph is not connected, it consists of multiple connected components, where each component is a maximal connected subgraph. A vertex whose removal disconnects the graph is called an articulation point or cut vertex.

In directed graphs, strong connectivity requires a directed path from every vertex to every other vertex. A directed graph is weakly connected if the underlying undirected graph (ignoring edge directions) is connected.

### Graph Representations

**Adjacency Matrix**: A graph with n vertices is represented using an n × n matrix A where A[i][j] = 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For weighted graphs, the matrix entry contains the weight, with a special value (like infinity or 0) indicating no edge. The adjacency matrix requires O(V²) space regardless of the number of edges, making it suitable for dense graphs.

**Adjacency List**: Each vertex maintains a list of its adjacent vertices. Typically implemented using arrays of lists or linked lists, adjacency lists require O(V + E) space, making them memory-efficient for sparse graphs. This representation is widely used in practice and is the standard for most graph algorithms.

### Graph Traversals

Breadth-First Search (BFS) explores vertices level by level, starting from a source vertex and visiting all neighbors before moving to the next level. BFS uses a queue data structure and is essential for finding shortest paths in unweighted graphs.

Depth-First Search (DFS) explores as far as possible along each branch before backtracking. DFS can be implemented using recursion or an explicit stack. DFS is fundamental to many graph algorithms including topological sorting, finding strongly connected components, and detecting cycles.

## Examples

### Example 1: Converting Edge List to Adjacency Matrix

Given an undirected graph with vertices {0, 1, 2, 3} and edges {(0,1), (0,2), (1,2), (2,3)}, construct the adjacency matrix.

Solution:
The adjacency matrix is a 4×4 matrix where rows and columns represent vertices 0, 1, 2, 3.

Initialize a 4×4 matrix with all zeros:
```
   0 1 2 3
0 [0 0 0 0]
1 [0 0 0 0]
2 [0 0 0 0]
3 [0 0 0 0]
```

For each edge (u, v), set both matrix[u][v] and matrix[v][u] to 1 since the graph is undirected:

- Edge (0,1): matrix[0][1] = 1, matrix[1][0] = 1
- Edge (0,2): matrix[0][2] = 1, matrix[2][0] = 1
- Edge (1,2): matrix[1][2] = 1, matrix[2][1] = 1
- Edge (2,3): matrix[2][3] = 1, matrix[3][2] = 1

Final adjacency matrix:
```
   0 1 2 3
0 [0 1 1 0]
1 [1 0 1 0]
2 [1 1 0 1]
3 [0 0 1 0]
```

### Example 2: BFS Traversal

Perform BFS starting from vertex 0 on the graph from Example 1.

Solution:
BFS uses a queue and a visited array. Initialize visited[0] = true and enqueue 0.

Step 1: Dequeue 0, visit it. Add unvisited neighbors 1 and 2 to queue.
Queue: [1, 2], Visited: {0}

Step 2: Dequeue 1, visit it. Add unvisited neighbor 3 to queue (neighbor 0 and 2 are already visited).
Queue: [2, 3], Visited: {0, 1}

Step 3: Dequeue 2, visit it. No new neighbors to add (all already visited).
Queue: [3], Visited: {0, 1, 2}

Step 4: Dequeue 3, visit it. No new neighbors.
Queue: [], Visited: {0, 1, 2, 3}

BFS Order: 0 → 1 → 2 → 3

### Example 3: Detecting Cycle Using DFS

Determine if the graph with vertices {A, B, C, D} and edges {(A,B), (B,C), (C,A), (C,D)} contains a cycle.

Solution:
Perform DFS starting from vertex A:

DFS from A: Visit A, then B, then C.
At C, we find that A (the parent of C in the DFS tree) is a back-edge target. Since C has an edge to A, and A is an ancestor of C in the DFS tree, this forms a cycle: A → B → C → A.

The graph contains a cycle. The back-edge from C to A confirms this.

## Exam Tips

1. MEMORIZE THE HANDSHAKING LEMMA: The sum of all vertex degrees equals twice the number of edges. This is frequently tested in exams.

2. UNDERSTAND THE DIFFERENCE BETWEEN ADJACENCY MATRIX AND ADJACENCY LIST: Know when to use each representation. Adjacency matrix is O(V²) space but O(1) edge lookup; adjacency list is O(V+E) space but O(deg(v)) edge lookup.

3. BFS VS DFS APPLICATIONS: Remember that BFS finds shortest paths in unweighted graphs and level-order traversal. DFS is used for topological sorting, cycle detection, and path finding.

4. DEGREE RELATIONSHIPS IN DIRECTED GRAPHS: Total indegree equals total outdegree equals the number of edges. This is a common exam question.

5. CONNECTIVITY CONCEPTS: Know the difference between connected, strongly connected, and weakly connected graphs. An undirected graph is connected if a path exists between every pair of vertices.

6. SPACE COMPLEXITY: For adjacency matrix: O(V²), for adjacency list: O(V + E). This comparison appears frequently in exam questions.

7. PRACTICE DRAWING REPRESENTATIONS: Be able to quickly draw adjacency matrix and adjacency list representations from a given graph. This is a scoring topic in practical exams.

8. WEIGHTED VS UNWEIGHTED: Remember that in weighted graphs, adjacency matrix stores weights instead of 1/0, while adjacency list stores (neighbor, weight) pairs.