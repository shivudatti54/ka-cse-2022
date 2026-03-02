# Shortest Paths & Spanning Trees
## Discrete Mathematical Structures (DU Syllabus)

### Introduction
These are fundamental graph theory concepts used in network design, routing protocols, and optimization problems. This topic covers two main areas: finding the shortest route between nodes and connecting all nodes with minimum total weight.

---

### Shortest Path Algorithms

- **Shortest Path Problem**: Finding the minimum distance/cost path between two vertices in a weighted graph
- **Dijkstra's Algorithm**:
  - Greedy approach
  - Works only with non-negative edge weights
  - Time Complexity: O(V²) or O(E log V) with priority queue
  - Used in GPS and routing protocols
- **Bellman-Ford Algorithm**:
  - Dynamic programming approach
  - Handles negative edge weights (no negative cycles)
  - Time Complexity: O(VE)
- **Floyd-Warshall Algorithm**:
  - All-pairs shortest path
  - Dynamic programming
  - Time Complexity: O(V³)
  - Finds shortest paths between every pair of vertices

---

### Spanning Trees

- **Spanning Tree**: A subgraph that is a tree containing all vertices of the original graph
- **Properties**:
  - Contains exactly V-1 edges
  - No cycles
  - Connected (for connected graphs)
- **Cut Property**: For any cut in the graph, the minimum weight edge crossing the cut belongs to some MST

---

### Minimum Spanning Tree (MST)

- **Definition**: Spanning tree with minimum total edge weight
- **Prim's Algorithm**:
  - Grows one tree starting from a source vertex
  - Uses priority queue (greedy approach)
  - Time Complexity: O(E log V)
  - Suitable for dense graphs
- **Kruskal's Algorithm**:
  - Sorts edges by weight, adds minimum edges avoiding cycles
  - Uses Union-Find (Disjoint Set) data structure
  - Time Complexity: O(E log V)
  - Suitable for sparse graphs

---

### Conclusion
Shortest path algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall) optimize route finding, while spanning tree algorithms (Prim's, Kruskal's) ensure efficient network connectivity. Master these for network optimization problems in exams.

**Exam Focus**: Know algorithm steps, time complexities, and when to apply each (negative weights → Bellman-Ford, dense graph → Prim's, etc.)