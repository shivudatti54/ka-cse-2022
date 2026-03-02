# Paths and Connectivity in Graph Theory

## Introduction to Paths and Connectivity

Paths and connectivity are fundamental concepts in graph theory that describe how vertices are connected to each other through sequences of edges. These concepts have numerous applications in computer science, including network routing, social network analysis, web crawling, and transportation systems.

In this section, we'll explore various types of paths, connectivity measures, and algorithms for determining connectivity in graphs.

## Basic Terminology

Before diving into paths and connectivity, let's review some essential graph theory terminology:

- **Graph**: A collection of vertices (nodes) and edges (connections between nodes)
- **Vertex (v)**: A fundamental unit in a graph (also called a node)
- **Edge (e)**: A connection between two vertices
- **Adjacent vertices**: Two vertices connected by an edge
- **Degree**: The number of edges incident to a vertex
- **Simple graph**: A graph without loops or multiple edges
- **Directed graph**: A graph where edges have direction
- **Weighted graph**: A graph where edges have numerical values

## Paths in Graphs

### What is a Path?

A **path** in a graph is a sequence of vertices where each consecutive pair is connected by an edge. Formally, a path from vertex u to vertex v is a sequence of vertices v₀, v₁, v₂, ..., vₖ such that:

- v₀ = u
- vₖ = v
- (vᵢ, vᵢ₊₁) is an edge for all i = 0, 1, 2, ..., k-1

The **length** of a path is the number of edges it contains.

### Types of Paths

1. **Simple Path**: A path where no vertices are repeated (except possibly the first and last)
2. **Cycle**: A path that starts and ends at the same vertex with no other repeated vertices
3. **Closed Path**: A path that starts and ends at the same vertex
4. **Trail**: A path where no edges are repeated (vertices may be repeated)
5. **Walk**: A general sequence of vertices and edges (no restrictions)

```
Example of different paths in a graph:

Vertices: A, B, C, D
Edges: A-B, B-C, C-D, D-A, A-C

Simple path: A → B → C → D
Cycle: A → B → C → D → A
Trail: A → B → C → A → C → D
Walk: A → B → C → A → B → C → D
```

### Path Representation

Paths can be represented in several ways:

- Vertex sequence: A, B, C, D
- Edge sequence: AB, BC, CD
- As a subgraph containing only the vertices and edges in the path

## Connectivity in Graphs

### Connected Graphs

A graph is **connected** if there is a path between every pair of distinct vertices. If a graph is not connected, it is **disconnected**.

```
Connected Graph:    Disconnected Graph:
A -- B             A -- B    C -- D
|    |
C -- D
```

### Components of a Graph

A **connected component** of a graph is a maximal connected subgraph. In other words, it's a subgraph where:

1. Every pair of vertices is connected by a path
2. No additional vertices can be added while maintaining connectivity

```
Graph with 3 components:
Component 1: A-B-C
Component 2: D-E
Component 3: F
```

### Types of Connectivity

1. **Vertex Connectivity**: The minimum number of vertices that need to be removed to disconnect the graph
2. **Edge Connectivity**: The minimum number of edges that need to be removed to disconnect the graph
3. **k-Connected**: A graph is k-connected if its vertex connectivity is at least k
4. **k-Edge-Connected**: A graph is k-edge-connected if its edge connectivity is at least k

## Special Types of Paths

### Eulerian Paths and Circuits

An **Eulerian path** is a path that traverses every edge exactly once. An **Eulerian circuit** is an Eulerian path that starts and ends at the same vertex.

**Theorem**: A connected graph has an Eulerian circuit if and only if every vertex has even degree.

**Theorem**: A connected graph has an Eulerian path (but not a circuit) if and only if exactly two vertices have odd degree.

```
Eulerian circuit example (all vertices have even degree):
A -- B
|    |
C -- D

Eulerian path example (vertices A and D have odd degree):
A -- B -- C
     |
     D
```

### Hamiltonian Paths and Cycles

A **Hamiltonian path** is a path that visits every vertex exactly once. A **Hamiltonian cycle** is a Hamiltonian path that forms a cycle by connecting the last vertex to the first.

Unlike Eulerian paths, there's no simple necessary and sufficient condition for Hamiltonian paths, making them computationally difficult to find (NP-complete problem).

```
Hamiltonian path: A → B → C → D
Hamiltonian cycle: A → B → C → D → A
```

## Connectivity Algorithms

### Breadth-First Search (BFS) for Connectivity

BFS can be used to determine connectivity and find shortest paths in unweighted graphs.

```
Algorithm: BFS-Connectivity(G, s)
1. Initialize visited array, mark all vertices as unvisited
2. Create a queue Q
3. Mark s as visited and enqueue s
4. While Q is not empty:
   a. Dequeue a vertex v
   b. For each neighbor u of v:
      If u is unvisited, mark as visited and enqueue u
5. If all vertices are visited, graph is connected
```

### Depth-First Search (DFS) for Connectivity

DFS is another algorithm that can determine connectivity by exploring as far as possible along each branch.

```
Algorithm: DFS-Connectivity(G, s)
1. Initialize visited array, mark all vertices as unvisited
2. Call DFS-Visit(s)
3. If all vertices are visited, graph is connected

DFS-Visit(v):
1. Mark v as visited
2. For each neighbor u of v:
   If u is unvisited, call DFS-Visit(u)
```

### Finding Connected Components

To find all connected components in a graph:

```
Algorithm: Find-Components(G)
1. Initialize component counter c = 0
2. Initialize visited array, mark all vertices as unvisited
3. For each vertex v in G:
   If v is unvisited:
      c = c + 1
      Perform BFS or DFS from v, marking all reachable vertices as belonging to component c
```

## Distance in Graphs

### Shortest Path

The **distance** between two vertices u and v is the length of the shortest path between them. If no path exists, the distance is infinity.

### Diameter and Radius

- **Diameter**: The maximum distance between any pair of vertices in a graph
- **Radius**: The minimum eccentricity of any vertex (where eccentricity is the maximum distance from a vertex to all other vertices)
- **Center**: A vertex with eccentricity equal to the radius

```
Example graph:
A -- B -- C -- D
     |
     E

Distance between A and D: 3
Diameter: 3 (A to D)
Radius: 2 (vertex B has eccentricity 2)
Center: B
```

## Connectivity in Directed Graphs

### Strong Connectivity

A directed graph is **strongly connected** if there is a directed path from every vertex to every other vertex.

### Weak Connectivity

A directed graph is **weakly connected** if the underlying undirected graph (ignoring edge directions) is connected.

### Strongly Connected Components

A **strongly connected component** (SCC) is a maximal subgraph where every vertex is reachable from every other vertex.

```
Directed graph:
A → B → C → A (strongly connected component)
D → E (another component)
```

Kosaraju's algorithm and Tarjan's algorithm are commonly used to find SCCs in directed graphs.

## Applications of Paths and Connectivity

1. **Network Routing**: Finding optimal paths in computer networks
2. **Social Networks**: Analyzing connectivity and influence in social media
3. **Web Crawling**: Determining reachable pages on the web
4. **Transportation Systems**: Planning routes in road networks
5. **Circuit Design**: Ensuring connectivity in electronic circuits
6. **Epidemiology**: Modeling disease spread through contact networks

## Comparison of Connectivity Concepts

| Concept             | Definition                                 | Condition                     | Algorithm               |
| ------------------- | ------------------------------------------ | ----------------------------- | ----------------------- |
| Connected Graph     | Path exists between all vertex pairs       | No isolated components        | BFS/DFS                 |
| Eulerian Circuit    | Visits every edge once, returns to start   | All vertices have even degree | Fleury's algorithm      |
| Hamiltonian Cycle   | Visits every vertex once, returns to start | No simple condition           | Backtracking, heuristic |
| Strong Connectivity | Directed paths between all vertex pairs    | SCC covers all vertices       | Kosaraju's algorithm    |

## Exam Tips

1. **Remember key definitions**: Be precise with terms like path, trail, walk, cycle.
2. **Connectivity conditions**: Know the necessary and sufficient conditions for Eulerian paths/circuits.
3. **Algorithm steps**: Understand BFS/DFS for connectivity testing.
4. **Practice with examples**: Work through examples of finding paths, components, and connectivity measures.
5. **Directed vs undirected**: Be careful to distinguish between strong and weak connectivity in directed graphs.
6. **Shortest path**: Remember that BFS finds shortest paths in unweighted graphs.
7. **Component counting**: Practice finding connected components in various graphs.
