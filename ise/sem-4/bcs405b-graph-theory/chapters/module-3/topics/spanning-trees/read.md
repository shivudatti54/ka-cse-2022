# Spanning Trees

## 1. Introduction and Definition

A **Spanning Tree** of a connected, undirected graph `G` is a subgraph that is a **tree** and includes **all the vertices** of `G`. It connects all the vertices together with the **minimum number of edges** required. Since a tree with `n` vertices has exactly `n-1` edges, a spanning tree must also have exactly `n-1` edges.

**Key Properties:**

- It is acyclic (contains no cycles).
- It is connected (there is a path between every pair of vertices).
- It is a maximal acyclic subgraph and a minimal connected subgraph of `G`.

**Formal Definition:** For a graph `G = (V, E)` with `|V| = n` vertices, a spanning tree `T = (V, E')` is a connected, acyclic subgraph where `E' ⊆ E` and `|E'| = n-1`.

## 2. Why are Spanning Trees Important?

Spanning trees are a fundamental concept in graph theory with critical applications in:

- **Network Design:** Ensuring all nodes (e.g., computers, cities) in a network are connected without any redundant loops, which can cause broadcast storms or inefficient routing. Think of a road network connecting all cities without any unnecessary extra roads.
- **Cluster Analysis:** Finding a hierarchy or structure within data.
- **Approximation Algorithms:** For problems like the Traveling Salesperson Problem (TSP).
- **Protocols:** Network protocols like the **Spanning Tree Protocol (STP)** in Ethernet networks actively use this concept to prevent loops and ensure a loop-free logical topology.

## 3. Finding a Spanning Tree

Any connected graph has at least one spanning tree. Two common algorithms to find a spanning tree are **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. The traversal itself implicitly creates a spanning tree, often called a **BFS Tree** or **DFS Tree**.

**Example:**
Consider a simple graph `G` with 4 vertices (`A, B, C, D`) and 5 edges.

```
    A
   / \
  B   C
   \ /
    D
Edges: A-B, A-C, B-D, C-D, B-C
```

A possible spanning tree `T` (found using BFS starting at A) would be:

```
    A
   / \
  B   C
   \
    D
Edges in T: A-B, A-C, B-D
```

This tree has 4 vertices and 3 edges, is connected, and has no cycles.

## 4. Minimum Spanning Tree (MST)

For a **weighted, connected, undirected graph**, where each edge has an associated cost or weight, a **Minimum Spanning Tree (MST)** is a spanning tree with the **minimum possible total edge weight** among all possible spanning trees.

**Formal Definition:** For `G = (V, E)` with a weight function `w: E → R`, an MST `T` is a spanning tree that minimizes `w(T) = Σ_{(u,v) ∈ T} w(u,v)`.

### Applications of MST:

- Designing least-cost network infrastructure (e.g., fiber optic cable layouts, electrical grids, water pipe systems).
- Solving problems like clustering, image segmentation, and handwriting recognition.
- Approximating solutions to complex optimization problems.

## 5. Algorithms for Finding MST

Two classic **greedy algorithms** are used to find the MST of a graph. Both algorithms incrementally build the MST by always adding the next best possible edge.

### Prim's Algorithm

Prim's algorithm starts from a single vertex and grows the MST one edge at a time. At each step, it adds the cheapest edge that connects a vertex in the current MST to a vertex outside the MST.

**Steps:**

1.  Initialize a tree with a single, arbitrary vertex.
2.  From all edges that connect vertices in the tree to vertices not in the tree, find the minimum-weight edge.
3.  Add this edge and the new vertex to the tree.
4.  Repeat steps 2 and 3 until all vertices are included.

**Idea:** "Grow a tree from a seed vertex."

**Visualization (Using the example graph):**
Let's assume our graph has weights:

- A-B: 4
- A-C: 1
- B-C: 2
- B-D: 5
- C-D: 3

```
Step-by-step execution starting from vertex A:
1. Start with {A}. Cheapest edge is A-C (1). Add C. MST Edges: A-C
2. Set is {A, C}. Edges to outside: A-B(4), C-B(2), C-D(3). Cheapest is C-B (2). Add B. MST Edges: A-C, C-B
3. Set is {A, B, C}. Edges to outside: A-B(4), B-D(5), C-D(3). Cheapest is C-D (3). Add D. MST Edges: A-C, C-B, C-D
Total Weight: 1 + 2 + 3 = 6
```

### Kruskal's Algorithm

Kruskal's algorithm sorts all the edges by their weight and then adds them to the MST in increasing order, skipping any edge that would form a cycle.

**Steps:**

1.  Sort all edges in non-decreasing order of their weight.
2.  Initialize the MST as an empty set.
3.  For each edge in the sorted list:
    - If adding the edge to the MST does not create a cycle, add it.
    - Otherwise, discard it.
4.  Stop when the MST has `n-1` edges.

**Idea:** "Pick the globally cheapest edge that doesn't cause a cycle."

**Visualization (Using the same weighted graph):**

1.  Sorted edges: A-C(1), C-B(2), C-D(3), A-B(4), B-D(5)
2.  Add A-C (weight 1). No cycle.
3.  Add C-B (weight 2). No cycle.
4.  Add C-D (weight 3). No cycle. Now we have 3 edges (n-1=3 for 4 vertices). Stop.
    Total Weight: 1 + 2 + 3 = 6

**Data Structure:** Kruskal's algorithm efficiently checks for cycles using a **Union-Find (Disjoint Set Union - DSU)** data structure.

## 6. Comparison of Prim's and Kruskal's Algorithms

| Feature                               | Prim's Algorithm                                                        | Kruskal's Algorithm                                     |
| :------------------------------------ | :---------------------------------------------------------------------- | :------------------------------------------------------ |
| **Basic Approach**                    | Vertex-based: Grows the MST from a starting node.                       | Edge-based: Adds edges in sorted order of weight.       |
| **Suitable Data Structure**           | **Priority Queue (Min-Heap)** for efficient extraction of the min edge. | **Union-Find (DSU)** for efficient cycle checking.      |
| **Time Complexity** (with optimal DS) | `O(E log V)`                                                            | `O(E log E)` ≈ `O(E log V)`                             |
| **Best For**                          | Dense graphs (where `E` is large, close to `V²`).                       | Sparse graphs (where `E` is much smaller than `V²`).    |
| **Cycle Checking**                    | Inherently avoids cycles by connecting new vertices.                    | Must explicitly check for cycles before adding an edge. |

## 7. Proof of Correctness (The Greedy Choice)

Both Prim's and Kruskal's algorithms are greedy, but how do we know they always produce the true MST? The answer lies in a fundamental theorem.

**Theorem:** Let `G = (V, E)` be a connected, undirected, weighted graph. Let `T` be an MST of `G`. Let `(u, v)` be an edge of `G` that is a **minimum-weight edge** crossing some partition `(S, V-S)` of the graph. Then there exists an MST that includes `(u, v)`.

This theorem guarantees that the greedy choice—always taking the cheapest available edge under the algorithm's rules—is safe and will lead to a globally optimal solution.

## 8. Exam Tips and Common Pitfalls

- **Cycle Detection:** Remember that a spanning tree must be acyclic. When using Kruskal's, always check if an edge connects two vertices already in the same connected component of the growing forest.
- **Graph Must Be Connected:** You can only find a spanning tree for a **connected** graph. If the graph is disconnected, the result is a **spanning forest** (a collection of spanning trees, one for each connected component).
- **Multiple MSTs:** A graph can have more than one MST, especially if multiple edges have the same weight. Both algorithms will find _an_ MST, but it might not be unique.
- **Weight Assumption:** MST algorithms are designed for undirected graphs. The weights can be negative, zero, or positive. The algorithms still work correctly.
- **Prim's vs. Kruskal's:** In an exam, if asked which algorithm to use, justify your choice based on graph density. For a dense graph, Prim's (with adjacency matrix) can be more efficient. For a sparse graph, Kruskal's is often simpler and equally efficient.
