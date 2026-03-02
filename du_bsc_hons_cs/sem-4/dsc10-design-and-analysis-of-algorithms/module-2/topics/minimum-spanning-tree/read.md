# Minimum Spanning Tree

## Introduction

A **Minimum Spanning Tree (MST)** is a fundamental concept in graph theory with profound applications in network design, transportation systems, and resource allocation. Given a connected, undirected, weighted graph, a spanning tree is a subgraph that includes all vertices of the original graph without forming any cycles. Among all possible spanning trees, the one with the minimum total edge weight is called the Minimum Spanning Tree.

The importance of MST extends far beyond theoretical computer science. In real-world scenarios, MST helps design efficient telecommunication networks, electrical grids, water distribution systems, and road networks while minimizing the total cost of construction. When laying cables between cities, connecting computers in a network, or planning airline routes, the MST provides the most cost-effective solution that ensures connectivity.

This topic is crucial for the DU syllabus as it tests your understanding of greedy algorithms—a powerful algorithmic paradigm. Both Kruskal's and Prim's algorithms demonstrate the greedy approach's effectiveness in solving optimization problems. Understanding when greedy algorithms work (like in MST) versus when they fail is essential for developing strong algorithmic thinking.

## Key Concepts

### Basic Definitions

A **graph** G = (V, E) consists of a set of vertices V and a set of edges E connecting pairs of vertices. A **weighted graph** assigns a numerical weight to each edge, often representing cost, distance, or capacity.

A **spanning tree** of a graph with n vertices is a connected, acyclic subgraph containing all n vertices. Every spanning tree has exactly n-1 edges.

A **minimum spanning tree** (MST) is a spanning tree with minimum possible total edge weight. For a graph with distinct edge weights, the MST is unique.

### Properties of MST

**Cut Property**: For any cut (partition of vertices into two non-empty sets), the minimum weight edge crossing the cut belongs to some MST. This property is the foundation for both Kruskal's and Prim's algorithms.

**Cycle Property**: For any cycle in the graph, the maximum weight edge in that cycle cannot belong to any MST. This property helps prove the correctness of MST algorithms.

**MST Counting**: A graph can have multiple MSTs if edge weights are not all distinct. If all weights are distinct, the MST is unique.

### Kruskal's Algorithm

Kruskal's algorithm is a greedy algorithm that builds the MST by adding edges in increasing order of weight, ensuring no cycles are formed.

**Algorithm Steps**:
1. Sort all edges in non-decreasing order of their weights
2. Initialize a disjoint set (Union-Find) data structure
3. For each edge in sorted order:
   - If the edge's endpoints are in different components, add the edge to MST
   - Union the two components
4. Continue until MST has (n-1) edges

**Time Complexity**: O(E log E) or equivalently O(E log V), using efficient sorting and Union-Find with path compression and union by rank.

### Prim's Algorithm

Prim's algorithm grows the MST from a starting vertex, always adding the minimum weight edge that connects a vertex in the tree to a vertex outside the tree.

**Algorithm Steps**:
1. Start with an arbitrary vertex, mark it as part of MST
2. Maintain a min-priority queue of edges connecting MST vertices to non-MST vertices
3. Repeat until all vertices are included:
   - Extract the minimum weight edge from the queue
   - Add the connected vertex to MST
   - Add all edges from this new vertex to non-MST vertices to the queue

**Time Complexity**: O(V²) with array implementation, O(E log V) with binary heap, O(E + V log V) with Fibonacci heap.

### Comparison: Kruskal's vs Prim's

| Aspect | Kruskal's | Prim's |
|--------|-----------|--------|
| Approach | Edge-centric | Vertex-centric |
| Data Structure | Union-Find | Priority Queue |
| Best For | Sparse graphs | Dense graphs |
| Time (Basic) | O(E log V) | O(V²) |
| Always Builds From | Multiple components | Single component |

## Examples

### Example 1: Applying Kruskal's Algorithm

Consider the following graph with vertices {A, B, C, D, E} and edges with weights:

- AB: 2, AC: 3, AD: 4, BC: 1, BD: 5, CD: 6, DE: 7, CE: 8

**Solution**:

**Step 1: Sort edges by weight**
BC(1), AB(2), AC(3), AD(4), BD(5), CD(6), DE(7), CE(8)

**Step 2: Apply Kruskal's**

- BC(1): B and C are different components → Add to MST. Components: {B,C}, {A}, {D}, {E}
- AB(2): A and B are different → Add to MST. Components: {A,B,C}, {D}, {E}
- AC(3): A and C already in same component → Skip
- AD(4): A and D are different → Add to MST. Components: {A,B,C,D}, {E}
- BD(5): B and D already in same component → Skip
- CD(6): C and D already in same component → Skip
- DE(7): D and E are different → Add to MST. Components: {A,B,C,D,E}

**MST Edges**: BC, AB, AD, DE
**Total Weight**: 1 + 2 + 4 + 7 = 14

### Example 2: Applying Prim's Algorithm

Using the same graph, start from vertex A.

**Solution**:

**Step 1**: Start with A, add all edges from A to priority queue: AB(2), AC(3), AD(4)

**Step 2**: Extract minimum - AB(2), add B to MST
Queue: AC(3), AD(4), BC(1) [from B]

**Step 3**: Extract minimum - BC(1), add C to MST
Queue: AC(3), AD(4), BD(5)

**Step 4**: Extract minimum - AC(3), but C already in MST → Skip
Queue: AD(4), BD(5), CD(6)

**Step 5**: Extract minimum - AD(4), add D to MST
Queue: BD(5), CD(6), DE(7)

**Step 6**: Extract minimum - BD(5), but D already in MST → Skip
Queue: CD(6), DE(7)

**Step 7**: Extract minimum - CD(6), but D already in MST → Skip
Queue: DE(7)

**Step 8**: Extract minimum - DE(7), add E to MST

**MST Edges**: AB, BC, AD, DE
**Total Weight**: 2 + 1 + 4 + 7 = 14

### Example 3: Real-World Application

A telecom company needs to connect 5 villages (A, B, C, D, E) with fiber optic cables. The cost (in lakhs) of laying cable between villages is:

- A-B: 10, A-C: 15, A-D: 20, B-C: 12, B-D: 25, C-D: 14, C-E: 18, D-E: 22

Find minimum cost to connect all villages.

**Solution using Kruskal's**:

Sorted edges: B-C(12), A-B(10), C-D(14), A-C(15), C-E(18), A-D(20), D-E(22), B-D(25)

Processing:
- A-B(10): Add → {A,B}, {C}, {D}, {E}
- B-C(12): Add → {A,B,C}, {D}, {E}
- C-D(14): Add → {A,B,C,D}, {E}
- C-E(18): Add → {A,B,C,D,E}

**Minimum Cost**: 10 + 12 + 14 + 18 = 54 lakhs

## Exam Tips

1. **Know the difference**: Remember Kruskal's adds edges (selecting from multiple components), Prim's adds vertices (growing from one component).

2. **Time complexities**: Be prepared to quote and derive time complexities. Kruskal's is O(E log V) with Union-Find, Prim's is O(V²) with arrays or O(E log V) with heaps.

3. **Cut property proof**: Understand and be able to explain the cut property as it forms the basis of correctness for both algorithms.

4. **When to use which**: Kruskal's is better for sparse graphs (few edges), Prim's is better for dense graphs (many edges).

5. **Unique MST condition**: If all edge weights are distinct, the MST is unique. This is a common exam question.

6. **Data structures**: Know that Kruskal's uses Union-Find (Disjoint Set) with path compression and union by rank. Prim's uses priority queue/min-heap.

7. **Stop condition**: Both algorithms stop when MST has exactly (n-1) edges. Don't keep adding edges beyond this.

8. **Application areas**: Be ready to explain real-world applications like network design, cluster analysis, and transportation planning.