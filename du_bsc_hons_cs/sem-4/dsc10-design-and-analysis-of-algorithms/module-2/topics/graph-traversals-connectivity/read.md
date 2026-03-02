# Graph Traversals and Connectivity

## Introduction

Graph traversal algorithms form the backbone of graph theory and serve as essential building blocks for solving complex computational problems. In the context of the University of Delhi's Computer Science curriculum, understanding graph traversals—particularly Breadth-First Search (BFS) and Depth-First Search (DFS)—is fundamental to mastering algorithmic design. These traversal techniques enable us to systematically explore vertices and edges in a graph, making them indispensable for solving problems ranging from finding shortest paths to detecting cycles and determining graph connectivity.

Graph connectivity represents a critical property that determines whether a graph can be "reached" from one vertex to another. In real-world applications, connectivity analysis helps in network design (ensuring robust communication networks), social network analysis (identifying connected communities), and transportation systems (verifying route availability). This topic builds upon the foundational concepts of graph theory introduced earlier and prepares students for advanced algorithmic challenges in competitive programming and technical interviews.

## Key Concepts

### Graph Representations

Before diving into traversals, understanding how graphs are represented in memory is essential:

**Adjacency Matrix**: A 2D array of size V×V where matrix[i][j] = 1 if there's an edge from vertex i to vertex j, else 0. Space complexity: O(V²). Best for dense graphs.

**Adjacency List**: An array of lists where each vertex has a list of its adjacent vertices. Space complexity: O(V + E). Best for sparse graphs—most practical scenarios.

### Breadth-First Search (BFS)

BFS explores vertices level by level, using a Queue data structure. Starting from a source vertex, it visits all immediate neighbors first before moving to vertices at the next level.

**Algorithm:**
```
BFS(graph, source):
    create queue Q
    mark source as visited
    enqueue source into Q
    
    while Q is not empty:
        vertex = dequeue from Q
        process vertex
        
        for each adjacent vertex v of vertex:
            if v is not visited:
                mark v as visited
                enqueue v into Q
```

**Time Complexity**: O(V + E) — each vertex and edge is visited once.
**Space Complexity**: O(V) — for the queue and visited array.

**Applications of BFS**:
- Finding shortest path in unweighted graphs
- Level-order traversal in trees
- Finding connected components
- Solving puzzles (minimum moves)

### Depth-First Search (DFS)

DFS explores as deep as possible along each branch before backtracking, using a Stack (either explicitly or through recursion).

**Algorithm (Iterative):**
```
DFS(graph, source):
    create stack S
    push source onto S
    
    while S is not empty:
        vertex = pop from S
        if vertex is not visited:
            mark vertex as visited
            process vertex
            
            for each adjacent vertex v of vertex (in reverse order):
                if v is not visited:
                    push v onto S
```

**Recursive Version:**
```
DFSrecursive(graph, vertex):
    mark vertex as visited
    process vertex
    
    for each adjacent vertex v of vertex:
        if v is not visited:
            DFSrecursive(graph, v)
```

**Time Complexity**: O(V + E)
**Space Complexity**: O(V) — for recursion stack or explicit stack

**Applications of DFS**:
- Detecting cycles
- Topological sorting
- Finding strongly connected components
- Solving maze problems
- Path finding

### Connectivity in Undirected Graphs

An undirected graph is **connected** if there exists a path between every pair of vertices. A **connected component** is a maximal connected subgraph.

To find connected components:
1. Run BFS or DFS from an unvisited vertex
2. Repeat until all vertices are visited
3. Each BFS/DFS tree represents one component

**Theorem**: A graph with n vertices and more than (n-1)(n-2)/2 edges must be connected (for simple graphs).

### Strong Connectivity in Directed Graphs

A directed graph is **strongly connected** if there exists a directed path from every vertex to every other vertex.

**Strongly Connected Components (SCCs)**: Maximal subsets of vertices where each vertex can reach every other vertex in that subset. Kosaraju's Algorithm and Tarjan's Algorithm are common methods to find SCCs.

### Articulation Points and Bridges

**Articulation Point (Cut Vertex)**: A vertex whose removal increases the number of connected components.

**Bridge (Cut Edge)**: An edge whose removal increases the number of connected components.

These can be found using DFS with discovery times and low values—a crucial application of graph traversal.

## Examples

### Example 1: BFS Traversal

Consider the following graph with vertices {0, 1, 2, 3, 4} and edges: {(0,1), (0,2), (1,3), (2,3), (3,4)}

```
    0
   / \
  1   2
   \ /
    3
     \
      4
```

**Step-by-step BFS from vertex 0:**

1. Start: Queue = [0], Visited = {0}
2. Dequeue 0, process it. Add neighbors 1, 2 to queue.
   Queue = [1, 2], Visited = {0, 1, 2}
3. Dequeue 1, process it. Add neighbor 3 (not visited).
   Queue = [2, 3], Visited = {0, 1, 2, 3}
4. Dequeue 2, process it. Neighbor 3 already visited.
   Queue = [3], Visited unchanged
5. Dequeue 3, process it. Add neighbor 4.
   Queue = [4], Visited = {0, 1, 2, 3, 4}
6. Dequeue 4, process it. No unvisited neighbors.

**BFS Order**: 0 → 1 → 2 → 3 → 4

**Shortest Distance from 0**: dist[0]=0, dist[1]=1, dist[2]=1, dist[3]=2, dist[4]=3

### Example 2: DFS Traversal

Using the same graph, perform DFS starting from vertex 0:

**Step-by-step DFS:**

1. Visit 0, push to stack. Mark visited.
   Stack: [0], Visited: {0}
2. Pop 0, process. Push neighbors (2, then 1 for reverse).
   Stack: [1, 2], Visited: {0}
3. Pop 1, process. Push neighbor 3.
   Stack: [2, 3], Visited: {0, 1}
4. Pop 3, process. Push neighbor 4.
   Stack: [2, 4], Visited: {0, 1, 3}
5. Pop 4, process. No unvisited neighbors.
   Stack: [2], Visited: {0, 1, 3, 4}
6. Pop 2, process. Neighbor 3 already visited.
   Stack: [], Visited: {0, 1, 3, 4, 2}

**DFS Order**: 0 → 1 → 3 → 4 → 2

### Example 3: Counting Connected Components

Graph: 3 components
- Component 1: vertices {0, 1, 2} — edges {(0,1), (1,2)}
- Component 2: vertices {3, 4} — edge {(3,4)}
- Component 3: vertex {5} — isolated

**Algorithm**:
```
components = 0
for each vertex v in graph:
    if v is not visited:
        BFS(v)  // marks all vertices in this component
        components += 1

return components  // Output: 3
```

## Exam Tips

1. **Choose BFS vs. DFS appropriately**: Use BFS for shortest path in unweighted graphs; use DFS for cycle detection, topological sort, and problems requiring backtracking.

2. **Time complexity is always O(V + E)**: Remember this is the standard complexity for both BFS and DFS on graphs represented using adjacency lists.

3. **Space complexity matters**: BFS uses O(V) for queue; DFS uses O(V) for stack (or recursion stack). For very deep graphs, consider iterative vs. recursive trade-offs.

4. **Understand when graphs are connected**: An undirected graph with n vertices is connected if and only if it has at least n-1 edges and the graph remains a single component.

5. **BFS gives shortest path distances**: In unweighted graphs, the distance from source to any vertex in BFS is the minimum number of edges.

6. **DFS visit order has multiple interpretations**: Pre-order, post-order, and finishing times are all relevant for advanced applications like topological sort.

7. **Strong connectivity applies to directed graphs**: Remember that strongly connected components partition the vertices of a directed graph.

8. **Practice edge cases**: Handle disconnected graphs, graphs with isolated vertices, and single-node graphs explicitly in your algorithms.