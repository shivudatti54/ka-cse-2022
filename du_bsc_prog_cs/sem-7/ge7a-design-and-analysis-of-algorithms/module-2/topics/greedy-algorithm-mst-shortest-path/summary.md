# Greedy Algorithm: MST & Shortest Path

## Introduction
Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum. In the Design and Analysis of Algorithms (Ge7A) syllabus, two critical applications are finding **Minimum Spanning Trees (MST)** and **Shortest Paths** in weighted graphs. These form essential topics for Delhi University NEP 2024 examination.

---

## Key Concepts

### Greedy Algorithm Approach
- **Local Optimum**: Choose the best available option at each step
- **No Backtracking**: Decisions are final once made
- **Optimal Substructure**: Solution can be built incrementally
- **Time Complexity**: Generally more efficient than dynamic programming

---

### Minimum Spanning Tree (MST)

**Definition**: A spanning tree with minimum total edge weight connecting all vertices.

**Prim's Algorithm**
- Starts from an arbitrary vertex
- Grows MST by adding the minimum weight edge connecting the tree to a new vertex
- Uses priority queue (min-heap) for efficiency
- **Time Complexity**: O(E log V) with heap
- **Suitable for**: Dense graphs

**Kruskal's Algorithm**
- Sorts all edges by weight
- Adds edges in increasing order, skipping those that create cycles
- Uses Union-Find (Disjoint Set) data structure
- **Time Complexity**: O(E log E) or O(E log V)
- **Suitable for**: Sparse graphs

---

### Shortest Path Algorithms

**Dijkstra's Algorithm**
- Finds shortest path from source to all vertices
- Greedy approach: Always select the vertex with minimum distance
- Works only with **non-negative weights**
- **Time Complexity**: O(V²) basic, O(E log V) with heap
- **Cannot handle negative edge weights**

**Bellman-Ford Algorithm**
- Dynamic programming approach
- Relaxes all edges (V-1) times
- **Handles negative weights** (detects negative weight cycles)
- **Time Complexity**: O(VE)
- More general but slower than Dijkstra

---

## Delhi University Syllabus Alignment

| Topic | Coverage |
|-------|----------|
| Greedy Method | Fundamental approach, optimality conditions |
| MST | Prim's & Kruskal's algorithms |
| Single-Source Shortest Path | Dijkstra's algorithm |

---

## Conclusion

For exam preparation, remember:
- **MST**: Prim's (vertex-based) vs Kruskal's (edge-based)
- **Shortest Path**: Dijkstra for non-negative weights, Bellman-Fold for negative weights
- Focus on **algorithm steps**, **time complexity**, and **when to apply each**
- Practice tracing algorithms with examples

These greedy algorithms are efficient and widely used in network design, routing, and optimization problems.