# Elementary Graph Operations

## Introduction

Graphs are fundamental non-linear data structures used to model pairwise relationships between objects. In computer science, graphs find extensive applications in social networks, transportation systems, computer networks, and dependency resolution. Having understood the theoretical foundations of graphs and their abstract data types, we now turn our attention to elementary graph operations—the basic manipulations that allow us to build, modify, and query graph structures.

Elementary graph operations form the backbone of any graph-based algorithm. These operations include initializing a graph, adding and removing vertices and edges, checking vertex existence, retrieving neighbors, and traversing the graph. Mastery of these operations is essential because complex graph algorithms like shortest path (Dijkstra's), minimum spanning tree (Prim's/Kruskal's), and network flow algorithms build upon these fundamental primitives. In this topic, we will explore both adjacency matrix and adjacency list representations along with their associated operations, analyzing the time and space complexities for each.

## Key Concepts

### Graph Representation Methods

The choice of graph representation significantly impacts the efficiency of elementary operations. There are two primary ways to represent graphs in memory:

**Adjacency Matrix:** A 2D array of size V × V where V is the number of vertices. If there is an edge from vertex i to vertex j, matrix[i][j] = 1 (or the weight for weighted graphs); otherwise, it is 0. For undirected graphs, the matrix is symmetric.

**Adjacency List:** An array of linked lists where the ith index contains a list of all neighbors of vertex i. This is more space-efficient for sparse graphs (graphs with fewer edges).

### Basic Operations on Graphs

**1. Graph Initialization**
Creating an empty graph with a specified number of vertices. For adjacency matrix, we initialize a V × V matrix with zeros. For adjacency list, we create an array of V empty lists.

**2. Adding a Vertex**
In adjacency matrix representation, adding a vertex requires creating a new (V+1) × (V+1) matrix and copying old values—a costly O(V²) operation. In adjacency list, we simply append an empty list to the array, taking O(1) time.

**3. Adding an Edge**
For undirected graphs using adjacency matrix, we set both matrix[u][v] and matrix[v][u] to 1. For directed graphs, only matrix[u][v] is modified. Using adjacency list, we add v to the list of u (and u to the list of v for undirected graphs). Both operations take O(1) for adjacency list and O(1) for matrix (direct index access).

**4. Removing an Edge**
The inverse of adding an edge—setting the matrix entry to 0 or removing the element from the linked list. Time complexity is O(1) for matrix and O(degree) for adjacency list.

**5. Removing a Vertex**
This is more complex than removing an edge. For adjacency matrix, we must remove the corresponding row and column, requiring O(V²) time. For adjacency list, we must remove the vertex from all adjacency lists and then remove the list itself, taking O(V + E) time.

**6. Checking Edge Existence**
Using adjacency matrix, we directly check matrix[u][v] in O(1) time. With adjacency list, we must search the list of u for v, taking O(degree of u) time.

**7. Getting All Neighbors**
In adjacency matrix, we must scan the entire row for vertex u, taking O(V) time. In adjacency list, we simply traverse the list at index u, taking O(degree of u) time.

### Graph Traversal Operations

**Breadth-First Search (BFS)** explores vertices level by level, using a queue data structure. Starting from a source vertex, we visit all adjacent vertices first before moving to vertices at the next level. BFS is essential for finding the shortest path in unweighted graphs.

**Depth-First Search (DFS)** explores as far as possible along each branch before backtracking, using a stack (or recursion). DFS is crucial for detecting cycles, topological sorting, and solving maze problems.

### Additional Elementary Operations

- **isEmpty():** Checks whether the graph contains any vertices
- **isFull():** Checks if memory allocation is possible (for fixed-size implementations)
- **vertexCount():** Returns the number of vertices
- **edgeCount():** Returns the number of edges
- **inDegree(vertex):** Returns the number of incoming edges
- **outDegree(vertex):** Returns the number of outgoing edges

## Examples

### Example 1: Adding and Removing Edges in Adjacency List

Consider an undirected graph with vertices {0, 1, 2, 3}. Initially, we have an empty adjacency list:

```
adj = [[], [], [], []]
```

**Operation: addEdge(0, 1)**
We add 1 to adj[0] and 0 to adj[1]:
```
adj = [[1], [0], [], []]
```

**Operation: addEdge(1, 2)**
```
adj = [[1], [0, 2], [1], []]
```

**Operation: addEdge(2, 3)**
```
adj = [[1], [0, 2], [1, 3], [2]]
```

**Operation: removeEdge(1, 2)**
We remove 2 from adj[1] and 1 from adj[2]:
```
adj = [[1], [0], [1], [2]]
```

### Example 2: BFS Traversal

Given the graph:
```
    0
   /|\
  1 | 2
  |/
  3
```
Adjacency list: adj = [[1,2,3], [0,3], [0], [0,1]]

**BFS starting from vertex 0:**
1. Queue: [0], Visited: {0}
2. Dequeue 0, visit neighbors 1,2,3 → Queue: [1,2,3], Visited: {0,1,2,3}
3. Dequeue 1 - already visited neighbors
4. Dequeue 2 - already visited neighbors
5. Dequeue 3 - already visited neighbors

**BFS Order: 0 → 1 → 2 → 3**

### Example 3: DFS Traversal

Same graph as above. **DFS starting from vertex 0 (recursive):**

1. Visit 0, mark visited
2. Go to neighbor 1 (unvisited), mark visited
3. Go to neighbor 3 (unvisited from 1), mark visited
4. Backtrack to 1, no more unvisited neighbors
5. Backtrack to 0, go to neighbor 2 (unvisited), mark visited

**DFS Order: 0 → 1 → 3 → 2**

## Exam Tips

1. **Representation Choice:** Remember that adjacency matrix provides O(1) edge lookup but uses O(V²) space. Adjacency list uses O(V + E) space but edge lookup is O(V) in worst case.

2. **Time Complexities:** For exams, memorize these: Adding edge is O(1) for both representations. Removing vertex is O(V²) for matrix and O(V + E) for list.

3. **BFS vs DFS Applications:** BFS is used for shortest path in unweighted graphs, level-order traversal. DFS is used for cycle detection, topological sort, and solving puzzles with backtracking.

4. **Symmetric Property:** In undirected graphs using adjacency matrix, the matrix is always symmetric: matrix[i][j] = matrix[j][i].

5. **Space Optimization:** For sparse graphs (E << V²), always prefer adjacency list. For dense graphs (E close to V²), adjacency matrix may be more efficient.

6. **Recursive DFS Memory:** Remember that recursive DFS uses system stack and may cause stack overflow for very large graphs. Iterative versions using explicit stacks are safer.

7. **In-degree and Out-degree:** In directed graphs, out-degree is the size of adjacency list. In-degree requires scanning all vertices or maintaining an additional in-degree array.

8. **Graph Types:** Know the difference between directed and undirected, weighted and unweighted, cyclic and acyclic graphs—these affect how operations behave.