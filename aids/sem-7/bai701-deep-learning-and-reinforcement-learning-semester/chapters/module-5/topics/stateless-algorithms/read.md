# Minimum Spanning Tree: Prim's and Kruskal's Algorithms

## Introduction to Minimum Spanning Tree (MST)

A **Minimum Spanning Tree (MST)** is a fundamental concept in graph theory and network design. Given a connected, undirected graph `G = (V, E)` with `V` vertices and `E` edges, each having a weight (or cost), an MST is a subset of the edges that connects all the vertices together, without any cycles, and with the minimum possible total edge weight.

**Formal Definition:** For a connected, undirected graph `G = (V, E)` with edge weights `w(e)`, a Minimum Spanning Tree `T` is a tree (a connected, acyclic subgraph) that spans all vertices and minimizes the sum: `Σ w(e)` for all `e` in `T`.

### Key Properties of MSTs
1.  **Spanning:** Includes all vertices of the original graph.
2.  **Tree:** Contains no cycles.
3.  **Minimum:** Has the smallest total weight among all possible spanning trees.
4.  **Uniqueness:** An MST is unique only if each edge has a distinct weight. If edges have the same weight, multiple MSTs may exist.
5.  **Edge Count:** Any spanning tree of a graph with `V` vertices has exactly `V - 1` edges.

**Applications:** MSTs are crucial in designing efficient networks, such as:
*   Computer networks (reducing wiring cost)
*   Transportation networks
*   Telecommunications networks
*   Cluster analysis
*   Approximation algorithms for NP-hard problems (e.g., Traveling Salesman Problem)

---

## Prim's Algorithm

Prim's algorithm is a **greedy algorithm** that constructs an MST by starting from an arbitrary vertex and grows the spanning tree one edge at a time. At each step, it adds the cheapest possible edge that connects a vertex in the current tree to a vertex outside the tree.

### Algorithm Steps
1.  **Initialize:** Select an arbitrary vertex `s` to start the tree. Let `T = {s}`. Maintain a set of edges `MST = {}`.
2.  **Priority Queue:** Maintain a min-heap (priority queue) that stores edges incident to the current tree `T`, prioritized by their weight. Initialize the queue with all edges incident to `s`.
3.  **Grow the Tree:** While `T` does not contain all vertices:
    a. Extract the edge `e = (u, v)` with the minimum weight from the queue, where `u` is in `T` and `v` is not in `T`.
    b. Add vertex `v` to `T`.
    c. Add edge `e` to `MST`.
    d. Add all edges incident to `v` that connect to vertices not in `T` to the priority queue.
4.  **Terminate:** When `T` contains all `V` vertices, `MST` will contain the `V-1` edges forming the minimum spanning tree.

### Example Execution
Consider the following weighted graph:
```
        (A)
       / | \
     6/  |1 \5
     /   |   \
   (B)---(C)---(D)
     2    |3   4
          (E)
```
Let's build the MST starting from vertex `A`.

**Step 0:** `T = {A}`, `MST = {}`. Add edges from A: `(A,B,6)`, `(A,C,1)`, `(A,D,5)` to queue.
**Step 1:** Min edge is `(A,C,1)`. Add C to `T`, add edge to `MST`.
`T = {A, C}`, `MST = {(A,C)}`
Add edges from C to nodes not in T: `(C,B,2)`, `(C,D,3)`, `(C,E,3)`.
Queue now: `(A,B,6)`, `(A,D,5)`, `(C,B,2)`, `(C,D,3)`, `(C,E,3)`.
**Step 2:** Min edge is `(C,B,2)`. Add B to `T`, add edge to `MST`.
`T = {A, C, B}`, `MST = {(A,C), (C,B)}`
Add edges from B: `(B,D,4)` (B,A and B,C already in T). Queue: `(A,B,6)`, `(A,D,5)`, `(C,D,3)`, `(C,E,3)`, `(B,D,4)`.
**Step 3:** Min edge is `(C,D,3)`. Add D to `T`, add edge to `MST`.
`T = {A, C, B, D}`, `MST = {(A,C), (C,B), (C,D)}`
Add edges from D: `(D,E,4)` (D,A and D,C already in T). Queue: `(A,B,6)`, `(A,D,5)`, `(C,E,3)`, `(B,D,4)`, `(D,E,4)`.
**Step 4:** Min edge is `(C,E,3)`. Add E to `T`, add edge to `MST`.
`T = {A, C, B, D, E}`, `MST = {(A,C), (C,B), (C,D), (C,E)}`. STOP.

The final MST has a total weight of `1 + 2 + 3 + 3 = 9`.

### Implementation and Complexity
*   **Data Structures:** Priority Queue (Min-Heap) and a boolean array `inMST[]` to track included vertices.
*   **Time Complexity:** `O(E log V)`. Each edge is processed once (`O(E)`), and heap operations take `O(log V)` time each.
*   **Space Complexity:** `O(V + E)` to store the graph and the priority queue.

---

## Kruskal's Algorithm

Kruskal's algorithm is another **greedy algorithm** for finding an MST. Instead of growing a single tree, it considers all edges sorted by weight and adds them to the forest if they don't form a cycle, eventually connecting all components into one tree.

### Algorithm Steps
1.  **Sort:** Sort all edges in the graph in non-decreasing order of their weight.
2.  **Initialize:** Create an empty set `MST` to store the resulting edges. Initialize a Union-Find (Disjoint Set Union - DSU) data structure where each vertex is its own set.
3.  **Process Edges:** For each edge `(u, v)` in the sorted list:
    a. Check if `u` and `v` belong to the same set (using Find operation). If they do, adding this edge would create a cycle, so skip it.
    b. If they belong to different sets, add the edge `(u, v)` to `MST` and union the sets containing `u` and `v`.
4.  **Terminate:** Stop when `MST` contains `V-1` edges.

### Example Execution
Using the same graph as before:
Edges sorted by weight: `(A,C,1)`, `(C,B,2)`, `(C,D,3)`, `(C,E,3)`, `(B,D,4)`, `(D,E,4)`, `(A,B,6)`, `(A,D,5)`.

**Step 0:** `MST = {}`. Sets: `{A}, {B}, {C}, {D}, {E}`.
**Step 1:** Process `(A,C,1)`. Find(A) != Find(C). Add to MST. Union sets A and C.
`MST = {(A,C)}`. Sets: `{A,C}, {B}, {D}, {E}`.
**Step 2:** Process `(C,B,2)`. Find(C) != Find(B). Add to MST. Union sets {A,C} and {B}.
`MST = {(A,C), (C,B)}`. Sets: `{A,B,C}, {D}, {E}`.
**Step 3:** Process `(C,D,3)`. Find(C) != Find(D). Add to MST. Union sets {A,B,C} and {D}.
`MST = {(A,C), (C,B), (C,D)}`. Sets: `{A,B,C,D}, {E}`.
**Step 4:** Process `(C,E,3)`. Find(C) != Find(E). Add to MST. Union sets {A,B,C,D} and {E}.
`MST = {(A,C), (C,B), (C,D), (C,E)}`. Sets: `{A,B,C,D,E}`. We have `V-1=4` edges. STOP.

The final MST is the same as Prim's, with a total weight of 9.

### Implementation and Complexity
*   **Data Structures:** Union-Find (Disjoint Set Union - DSU) data structure and a sorted list of edges.
*   **Time Complexity:** `O(E log E)` which is equivalent to `O(E log V)` since `E = O(V²)`. Dominated by the sorting step.
*   **Space Complexity:** `O(V + E)` for storing the graph and the DSU structure.

---

## Comparison: Prim's vs. Kruskal's Algorithm

| Feature | Prim's Algorithm | Kruskal's Algorithm |
| :--- | :--- | :--- |
| **Approach** | Grows a single tree vertex by vertex. | Builds the MST by merging forests, edge by edge. |
| **Data Structures** | Priority Queue (Min-Heap), Adjacency List | Union-Find (DSU), Sorted List of Edges |
| **Best Suited For** | Dense graphs (where `E` is close to `V²`) | Sparse graphs (where `E` is much less than `V²`) |
| **Time Complexity** | `O(E log V)` using a binary heap. `O(E + V log V)` with Fibonacci Heap. | `O(E log V)` (due to sorting and Union-Find) |
| **Selection Criteria** | Chooses the minimum weight edge connected to the current tree. | Chooses the minimum weight edge from the entire graph that doesn't form a cycle. |

**Choosing an Algorithm:**
*   Use **Prim's** for dense graphs where the number of edges is high.
*   Use **Kruskal's** for sparse graphs where the number of edges is low. Its simplicity and ease of implementation (especially with a good DSU) often make it the preferred choice.

---

## Proof of Correctness (Greedy Choice)

Both algorithms are greedy, and their correctness relies on the following fundamental theorem about MSTs.

**Theorem:** Let `G = (V, E)` be a connected, undirected graph with a weight function `w : E -> R`. Let `U` be a proper subset of `V`. If `(u, v)` is an edge of minimum weight such that `u ∈ U` and `v ∈ V \ U`, then there exists a minimum spanning tree that includes `(u, v)`.

This theorem guarantees that the greedy choice—taking the minimum weight edge connecting the current set to the rest of the graph (Prim) or the globally minimum weight edge that doesn't create a cycle (Kruskal)—is safe and will lead to an optimal solution.

---

## Exam Tips

1.  **Understand the Core Idea:** Prim builds a tree; Kruskal builds a forest that becomes a tree. This is the most fundamental difference.
2.  **Trace Examples:** Be prepared to manually execute both algorithms step-by-step on a small graph (5-6 vertices). Drawing the graph and tracking the data structures (heap for Prim, sets for Kruskal) is crucial.
3.  **Know the Complexities:** Remember the time complexities (`O(E log V)` for both) and the data structures used. Be able to explain why those complexities arise (heap operations, sorting).
4.  **Application Questions:** Be ready to suggest which algorithm is more suitable for a given scenario (e.g., a phone cable network with many connections vs. a road network linking major cities).
5.  **Cycle Detection:** For Kruskal's, emphasize the role of the Union-Find data structure in efficient cycle checking. Understand the `Find` and `Union` operations.
6.  **Implementation:** While you likely won't write full code, understand the pseudocode and the role of each component (e.g., the `key[]` array in Prim's algorithm).
7.  **Distinguish from Shortest Path:** MST minimizes the total cost to connect all nodes. Shortest Path (Dijkstra) minimizes the cost from a source to a destination. The results are often different. Don't confuse them.