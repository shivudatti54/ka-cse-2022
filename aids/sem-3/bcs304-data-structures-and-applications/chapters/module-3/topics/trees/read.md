# Trees and Spanning Trees

## Introduction to Trees

In Graph Theory, a **tree** is one of the most fundamental and widely used structures. Trees are connected graphs without cycles, and they possess unique properties that make them essential in various computer science applications, including data structures (binary search trees, heaps), networking (spanning tree protocol), and algorithms (decision trees).

### Formal Definition of a Tree

A **tree** is an undirected graph that is both **connected** and **acyclic** (contains no cycles). Equivalently, a tree can be defined as a graph in which there is exactly one unique path between any two vertices.

### Key Properties of Trees

The following statements are all equivalent for an undirected graph *G = (V, E)* with *n* vertices and *m* edges. If *G* satisfies any one of these conditions, it is a tree, and therefore satisfies all of them:

1.  *G* is connected and acyclic (no cycles).
2.  *G* is connected and *m = n - 1*.
3.  *G* is acyclic and *m = n - 1*.
4.  There is exactly one simple path between any two distinct vertices in *G*.
5.  *G* is connected, but the removal of any single edge disconnects it (every edge is a **bridge**).
6.  *G* is acyclic, but the addition of any single edge between two non-adjacent vertices creates exactly one cycle.

### Terminology for Trees

*   **Leaf (or Pendant Vertex):** A vertex with a degree of 1.
*   **Internal Vertex:** A vertex that is not a leaf (i.e., with a degree greater than 1).
*   **Forest:** A graph that is acyclic but not necessarily connected. Its connected components are trees.
*   **Rooted Tree:** A tree in which one vertex has been designated as the **root**, imposing a parent-child hierarchy on the vertices.
*   **Level:** The number of edges on the path from the root to a vertex.
*   **Height:** The maximum level of any vertex in the tree.

### Example of a Tree

Consider the following tree with 6 vertices (A, B, C, D, E, F) and 5 edges. Notice that `m = n - 1` (5 = 6 - 1).

```
    A
   / \
  B   C
 / \   \
D   E   F
```

**ASCII Representation:**
```
Vertices: A, B, C, D, E, F
Edges: (A,B), (A,C), (B,D), (B,E), (C,F)
```
*   **Leaves:** D, E, F (degree 1)
*   **Internal Vertices:** A, B, C (degree 2, 3, and 2 respectively)
*   If we designate `A` as the root:
    *   **Level 0:** A
    *   **Level 1:** B, C
    *   **Level 2:** D, E, F
    *   **Height:** 2

---

## Introduction to Spanning Trees

A **spanning subgraph** of a graph *G* is a subgraph that contains all the vertices of *G*. A **spanning tree** of a connected, undirected graph *G* is a spanning subgraph of *G* that is itself a tree.

In simpler terms, a spanning tree is a subset of the edges of *G* that connects all the vertices together without any cycles. It must have exactly *n - 1* edges.

### Key Properties of Spanning Trees

1.  Every connected, undirected graph *G* has at least one spanning tree.
2.  A graph is connected **if and only if** it has a spanning tree.
3.  A spanning tree is a **minimal connected spanning subgraph**—removing any edge will disconnect it.
4.  It is also a **maximal acyclic spanning subgraph**—adding any edge from *G* not in the tree will create a cycle.

### Finding a Spanning Tree

Two fundamental algorithms are used to find spanning trees: Breadth-First Search (BFS) and Depth-First Search (DFS). The edges traversed during these searches form spanning trees called the **BFS Tree** and **DFS Tree**, respectively.

**Example Graph *G*:**
```
    A
   / \
  B — C
 / \   \
D   E   F
```
Edges: (A,B), (A,C), (B,C), (B,D), (B,E), (C,F). This graph has a cycle [A-B-C-A].

**A Spanning Tree for *G* (found by removing edges that form cycles):**
```
    A
   / \
  B   C
 / \   \
D   E   F
```
Edges in Spanning Tree: (A,B), (A,C), (B,D), (B,E), (C,F). The edge (B,C) was removed to break the cycle.

---

## Minimum Spanning Tree (MST)

For a **weighted, connected, undirected graph**, different spanning trees have different total costs (the sum of the weights of their edges). A **Minimum Spanning Tree (MST)** is a spanning tree with the minimum possible total cost compared to all other spanning trees of the graph.

MSTs have crucial applications in network design (e.g., finding the cheapest way to connect a set of locations with roads, cables, etc.).

### Algorithms for Finding MST

Two famous greedy algorithms are used to find an MST. Both algorithms assume the graph is connected and undirected.

#### 1. Kruskal's Algorithm

Kruskal's algorithm sorts all edges by increasing weight and then adds them to the growing spanning tree, but only if adding the edge does not create a cycle.

**Steps:**
1.  Sort all edges in non-decreasing order of their weight.
2.  Initialize an empty set *MST* for the edges of the minimum spanning tree.
3.  For each edge in the sorted list:
    *   If adding the edge to *MST* does not form a cycle, add it.
    *   Else, discard it.
4.  Repeat step 3 until *MST* has *n-1* edges.

**Example:**
```
Graph:
A---2---B
|      /|
|     / |
|    /  |
3   4   1
|  /    |
| /     |
C---5---D

Edges sorted by weight:
(B,D):1, (A,B):2, (A,C):3, (B,C):4, (C,D):5
```

**Execution:**
1.  Add (B,D) cost=1. MST = {(B,D)}
2.  Add (A,B) cost=2. MST = {(B,D), (A,B)}
3.  Add (A,C) cost=3. MST = {(B,D), (A,B), (A,C)}. **Stop.** We have 3 edges for 4 vertices.

The resulting MST has a total cost of 1+2+3 = 6.
```
A---2---B
|       |
|       |
3       1
|       |
C       D
```

#### 2. Prim's Algorithm

Prim's algorithm starts from an arbitrary root vertex and grows the spanning tree by adding the cheapest edge that connects a vertex in the tree to a vertex outside the tree.

**Steps:**
1.  Initialize a tree with a single arbitrary vertex (the root).
2.  Find the minimum-weight edge that connects a vertex in the tree to a vertex not in the tree.
3.  Add that edge and the new vertex to the tree.
4.  Repeat steps 2-3 until all vertices are included.

**Example (using the same graph, starting at vertex A):**
```
Initialization: Tree = {A}, Cost=0
Edges from A: (A,B)=2, (A,C)=3. Cheapest is (A,B)=2.
1. Add vertex B. Tree = {A,B}. Cost=2.
Edges from Tree: (A,C)=3, (B,C)=4, (B,D)=1. Cheapest is (B,D)=1.
2. Add vertex D. Tree = {A,B,D}. Cost=3.
Edges from Tree: (A,C)=3, (B,C)=4, (D,C)=5. Cheapest is (A,C)=3.
3. Add vertex C. Tree = {A,B,C,D}. Cost=6. **Stop.**
```

The resulting MST is the same as from Kruskal's algorithm.

### Comparison of Kruskal's and Prim's Algorithms

| Feature | Kruskal's Algorithm | Prim's Algorithm |
| :--- | :--- | :--- |
| **Basic Approach** | Edge-based. Builds MST by adding edges in increasing weight order. | Vertex-based. Grows the MST one vertex at a time from a root. |
| **Data Structures** | **Union-Find (Disjoint Set)** data structure to efficiently detect cycles. | **Priority Queue (Min-Heap)** to efficiently select the next cheapest edge. |
| **Time Complexity** | O(m log m) due to sorting edges. Becomes O(m log n) for a sparse graph. | O(m log n) using a binary heap and adjacency list. Can be improved with Fibonacci heap. |
| **Best For** | Sparse graphs (graphs with fewer edges). | Dense graphs (graphs with many edges). |
| **Result** | Can generate the MST in a non-linear, scattered fashion. | Generates the MST as a connected tree from the root. |

---

## Exam Tips

1.  **Know the Definitions Cold:** Be able to recite the multiple equivalent definitions of a tree. An exam question might ask "Prove that a connected graph with n-1 edges is acyclic," which is essentially proving it's a tree.
2.  **Count the Edges:** The formula `m = n - 1` is powerful. Use it to quickly verify if a graph could be a tree or to find the number of vertices/edges in a spanning tree. If a graph has *n* vertices and more than *n-1* edges, it **must** contain a cycle.
3.  **Understand the Algorithms:** Don't just memorize the steps of Kruskal's and Prim's. Understand *why* they are greedy algorithms and why that greedy choice leads to a global optimum. Be prepared to execute them step-by-step on a small graph.
4.  **Cycle Detection:** For Kruskal's, the key is efficient cycle detection. Understand how the Union-Find data structure works at a conceptual level.
5.  **Spot the MST:** In a multiple-choice question, you might be shown several spanning trees and asked to identify the MST. The fastest way is often to sum the weights and compare, but understanding the algorithms can help you eliminate wrong choices quickly.
6.  **Application Context:** Be ready to suggest that an MST is the solution to a word problem about minimizing connection cost (e.g., linking computers, laying cable, planning roads).