# Graph Representations: Adjacency Matrix and Adjacency List

## Introduction to Graph Representations

In graph theory, a graph is an abstract structure consisting of vertices (or nodes) connected by edges. While we can visualize graphs using diagrams, computers require concrete data structures to store and manipulate them. Two fundamental representations are the **Adjacency Matrix** and the **Adjacency List**. Choosing the right representation is crucial for efficient graph algorithm implementation, as each has distinct advantages and disadvantages depending on the graph's properties and the operations to be performed.

## Adjacency Matrix Representation

### Definition and Structure

An adjacency matrix is a 2D array (matrix) of size V×V, where V is the number of vertices in the graph. The matrix is typically denoted as `adjMatrix[][]`. The entry `adjMatrix[i][j]` indicates the presence (and potentially the weight) of an edge from vertex i to vertex j.

- For an **unweighted graph**: `adjMatrix[i][j] = 1` if there is an edge from vertex i to vertex j; otherwise, it is `0`.
- For a **weighted graph**: `adjMatrix[i][j]` stores the weight of the edge. A special value (like `0`, `Infinity`, or `-1`) denotes the absence of an edge.
- For an **undirected graph**: The matrix is symmetric along the main diagonal (`adjMatrix[i][j] = adjMatrix[j][i]`).

### Example: Undirected, Unweighted Graph

Consider the following simple undirected graph with 4 vertices (V0, V1, V2, V3):

```
    V0
   /  \
 V1 -- V2
   \  /
    V3
```

Edges: (V0,V1), (V0,V2), (V1,V2), (V1,V3), (V2,V3)

The corresponding 4x4 adjacency matrix would be:

|        | V0  | V1  | V2  | V3  |
| :----- | :-: | :-: | :-: | :-: |
| **V0** |  0  |  1  |  1  |  0  |
| **V1** |  1  |  0  |  1  |  1  |
| **V2** |  1  |  1  |  0  |  1  |
| **V3** |  0  |  1  |  1  |  0  |

Notice the symmetry. The matrix can be seen as a grid where a `1` marks a connection.

### Example: Directed, Weighted Graph

Consider a small directed, weighted graph representing flight routes and their costs:

```
      NYC
  100/   \200
    /     \
  SFO -> LAX
     150
```

Vertices: SFO (0), NYC (1), LAX (2)
Edges: SFO→NYC (100), SFO→LAX (150), NYC→LAX (200)

The 3x3 adjacency matrix (using `0` for no direct connection) would be:

|             | SFO (0) | NYC (1) | LAX (2) |
| :---------- | :-----: | :-----: | :-----: |
| **SFO (0)** |    0    |   100   |   150   |
| **NYC (1)** |    0    |    0    |   200   |
| **LAX (2)** |    0    |    0    |    0    |

This matrix is not symmetric, reflecting the directed nature of the graph.

### Space and Time Complexity Analysis

- **Space Complexity**: O(V²). The matrix always requires V² units of space, regardless of the number of edges. This makes it **space-inefficient for sparse graphs** (graphs with significantly fewer edges than the maximum possible, V²).
- **Time Complexity for Common Operations**:
  - **Check if an edge exists between vertex u and v**: O(1). This is a simple array lookup `adjMatrix[u][v]`.
  - **Find all adjacent vertices of a vertex u**: O(V). You must iterate through the entire row for `u` to find all non-zero entries.
  - **Add/Remove an edge**: O(1). Simply update the value at `adjMatrix[u][v]`.

## Adjacency List Representation

### Definition and Structure

An adjacency list represents a graph as an array of lists (or other dynamic data structures like arrays, linked lists, or hash maps). The size of the array is V (the number of vertices). Each entry `adjList[i]` stores a list of all vertices adjacent to vertex `i`.

- For an **unweighted graph**, `adjList[i]` is simply a list of neighboring vertex indices.
- For a **weighted graph**, each element in the list is a pair (or a struct) containing the neighbor's index and the edge weight.
- This representation **only stores existing edges**, making it very efficient for sparse graphs.

### Example: Undirected, Unweighted Graph

Using the same 4-vertex graph from the previous example:

```
    V0
   /  \
 V1 -- V2
   \  /
    V3
```

The adjacency list representation would be:

- `adjList[0]`: [1, 2] (V0 is connected to V1 and V2)
- `adjList[1]`: [0, 2, 3] (V1 is connected to V0, V2, and V3)
- `adjList[2]`: [0, 1, 3] (V2 is connected to V0, V1, and V3)
- `adjList[3]`: [1, 2] (V3 is connected to V1 and V2)

### Example: Directed, Weighted Graph

Using the flight route graph:

```
      NYC
  100/   \200
    /     \
  SFO -> LAX
     150
```

The adjacency list representation would be:

- `adjList[SFO]`: [(NYC, 100), (LAX, 150)]
- `adjList[NYC]`: [(LAX, 200)]
- `adjList[LAX]`: [ ] (LAX has no outgoing edges)

### Space and Time Complexity Analysis

- **Space Complexity**: O(V + E). It requires space for the array of V head pointers/references and for storing E edges. This is optimal and much more efficient than a matrix for sparse graphs.
- **Time Complexity for Common Operations**:
  - **Check if an edge exists between vertex u and v**: O(degree(u)) or O(log(degree(u))) depending on the data structure used for the list (e.g., array vs. hash map). In the worst case (a complete graph), this becomes O(V).
  - **Find all adjacent vertices of a vertex u**: O(degree(u)). This is very efficient as you directly access the list of neighbors.
  - **Add an edge**: O(1) if adding to the front of a linked list or using an amortized dynamic array.
  - **Remove an edge**: O(degree(u)) as you may need to search the list for the edge to remove.

## Comparison Table

| Feature                     | Adjacency Matrix                    | Adjacency List                            |
| :-------------------------- | :---------------------------------- | :---------------------------------------- |
| **Space**                   | O(V²)                               | O(V + E)                                  |
| **Check edge (u, v)**       | **O(1)**                            | O(degree(u)) or O(log(degree(u)))         |
| **Find all neighbors of u** | O(V)                                | **O(degree(u))**                          |
| **Add an edge**             | **O(1)**                            | O(1)\*                                    |
| **Remove an edge**          | **O(1)**                            | O(degree(u))                              |
| **Best for**                | Dense graphs, frequent edge lookups | Sparse graphs, graph traversal algorithms |
| **Worst for**               | Sparse graphs (wastes space)        | Dense graphs (lots of lists to manage)    |

\*Assuming constant-time insertion (e.g., at the head of a linked list).

## Choosing the Right Representation

The choice hinges on the graph's density and the primary operations your algorithm will perform.

1.  **Use an Adjacency Matrix when:**
    - The graph is **dense** (E is close to V²).
    - You need to **frequently check for the existence of a specific edge**.
    - The graph is small enough that O(V²) space is acceptable.

2.  **Use an Adjacency List when:**
    - The graph is **sparse**.
    - You need to **traverse the graph** (e.g., using BFS or DFS), as it efficiently allows you to iterate through all neighbors of a node.
    - Memory usage is a primary concern.

## Exam Tips

1.  **Identify Graph Type:** Always check if the graph is directed/undirected and weighted/unweighted before drawing a representation. This drastically changes the matrix/list.
2.  **Matrix Symmetry:** Remember, the adjacency matrix for an **undirected graph is always symmetric** across the main diagonal. This is a quick way to check your work.
3.  **Efficiency Trade-offs:** Be prepared to justify your choice of representation for a given scenario. Use the keywords "dense graph" or "frequent edge existence checks" to argue for a matrix, and "sparse graph" or "traversal algorithms" to argue for a list.
4.  **Space Calculation:** For exam questions asking about space, an adjacency matrix will always use V² units. For a list, it's roughly V + E (for unweighted) or V + 2E (for weighted, if storing pairs).
5.  **Practice Drawing:** Practice converting between a graph diagram and its matrix/list representations quickly and accurately. This is a common exam task.
