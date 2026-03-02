# Kruskal's Algorithm

## Introduction

Kruskal's Algorithm is a fundamental algorithm in graph theory used to find the **Minimum Spanning Tree (MST)** of a connected, weighted, and undirected graph. A spanning tree is a subgraph that includes all vertices of the original graph without forming any cycles, and a minimum spanning tree is the spanning tree with the minimum possible total edge weight.

The algorithm was developed by Joseph Kruskal in 1956 and belongs to the class of **greedy algorithms**. It works by sorting all the edges of the graph in non-decreasing order of their weights and then adding edges to the MST one by one, ensuring that no cycle is formed. This greedy approach ensures optimality because adding the smallest available edge that doesn't create a cycle always leads to an optimal solution.

In the context of University of Delhi's Computer Science curriculum, Kruskal's Algorithm holds significant importance as it demonstrates how greedy algorithms work and how the Union-Find (Disjoint Set Union) data structure efficiently supports cycle detection. Understanding this algorithm is essential for solving real-world problems like network design, cluster analysis, and approximate solutions to NP-hard problems like the Traveling Salesman Problem.

## Key Concepts

### Minimum Spanning Tree (MST)

A **Minimum Spanning Tree** of a weighted, connected, undirected graph G = (V, E) is a spanning tree with minimum total edge weight. The MST satisfies three important properties:

1. **Cut Property**: For any cut (partition of vertices into two non-empty sets), the minimum weight edge crossing the cut belongs to some MST.
2. **Cycle Property**: The maximum weight edge in any cycle does not belong to any MST.
3. **Unique Weight Property**: If all edge weights are distinct, the MST is unique.

### Greedy Approach in Kruskal's Algorithm

Kruskal's algorithm follows a greedy strategy where at each step, it chooses the locally optimal solution. The algorithm maintains a forest (collection of trees) and gradually merges trees by adding edges. The greedy choice of always picking the minimum weight edge that doesn't create a cycle leads to a globally optimal solution.

### Disjoint Set Union (DSU) / Union-Find

The **Union-Find** data structure, also known as Disjoint Set Union (DSU), is crucial for efficiently implementing Kruskal's algorithm. It supports two primary operations:

- **Find(x)**: Returns the representative (root) of the set containing element x. This is used to detect cycles—if the endpoints of an edge belong to the same set, adding the edge would create a cycle.

- **Union(x, y)**: Merges the sets containing elements x and y into a single set. This is performed when an edge is added to the MST.

To optimize these operations, we use **path compression** (during Find) and **union by rank/size**. With these optimizations, the amortized time complexity becomes nearly O(α(n)), where α(n) is the inverse Ackermann function, practically constant.

### Algorithm Steps

1. **Sort all edges** in non-decreasing order of their weights.
2. **Initialize** a disjoint set for each vertex (each vertex is in its own set).
3. **Iterate** through sorted edges:
   - For each edge (u, v), check if u and v are in different sets using Find.
   - If they are in different sets, add the edge to MST and perform Union(u, v).
   - If they are in the same set, skip the edge (it would create a cycle).
4. **Stop** when MST contains (V-1) edges, where V is the number of vertices.

### Time Complexity

The time complexity of Kruskal's algorithm is **O(E log E)**, which can also be expressed as **O(E log V)**:

- Sorting edges: O(E log E) = O(E log V)
- For each edge, two Find operations: O(E × α(V)) ≈ O(E)
- Union operations: O(E × α(V)) ≈ O(E)

Since α(V) is practically constant, the dominant factor is sorting the edges.

## Examples

### Example 1: Simple Graph with 5 Vertices

Consider the following graph with 5 vertices (A, B, C, D, E) and the following edges with weights:

| Edge | Weight |
|------|--------|
| A-B  | 2      |
| A-C  | 3      |
| B-C  | 1      |
| B-D  | 4      |
| C-D  | 5      |
| C-E  | 6      |
| D-E  | 7      |

**Step-by-step execution:**

**Step 1: Sort edges by weight**
B-C(1), A-B(2), A-C(3), B-D(4), C-D(5), C-E(6), D-E(7)

**Step 2: Initialize DSU**
Each vertex is its own set: {A}, {B}, {C}, {D}, {E}

**Step 3: Process edges**

- **Edge B-C (weight 1)**: Find(B) = B, Find(C) = C → Different sets
  - Add B-C to MST
  - Union(B, C) → Set becomes {B, C}
  - MST edges: 1, Count: 1

- **Edge A-B (weight 2)**: Find(A) = A, Find(B) = {B, C} → Different sets
  - Add A-B to MST
  - Union(A, B) → Set becomes {A, B, C}
  - MST edges: 2, Count: 2

- **Edge A-C (weight 3)**: Find(A) = {A, B, C}, Find(C) = {A, B, C} → Same set
  - Skip (would create cycle)
  - MST edges: 2, Count: 2

- **Edge B-D (weight 4)**: Find(B) = {A, B, C}, Find(D) = D → Different sets
  - Add B-D to MST
  - Union(B, D) → Set becomes {A, B, C, D}
  - MST edges: 3, Count: 3

- **Edge C-D (weight 5)**: Find(C) = {A, B, C, D}, Find(D) = {A, B, C, D} → Same set
  - Skip (would create cycle)
  - MST edges: 3, Count: 3

- **Edge C-E (weight 6)**: Find(C) = {A, B, C, D}, Find(E) = E → Different sets
  - Add C-E to MST
  - Union(C, E) → Set becomes {A, B, C, D, E}
  - MST edges: 4, Count: 4

Now we have V-1 = 4 edges, so we stop.

**MST Edges**: B-C(1), A-B(2), B-D(4), C-E(6)
**Total Weight**: 1 + 2 + 4 + 6 = 13

### Example 2: Graph with Duplicate Edge Weights

Consider a graph with 4 vertices where multiple edges have the same weight:

Vertices: {1, 2, 3, 4}
Edges: (1,2)=5, (2,3)=5, (3,4)=5, (1,3)=5, (2,4)=5, (1,4)=5

**Sorted edges (all weight 5):**
(1,2), (2,3), (3,4), (1,3), (2,4), (1,4) - in any order since all equal

**Processing:**
- Add (1,2): MST = {(1,2)}, DSU: {1,2}, {3}, {4}
- Add (2,3): MST = {(1,2), (2,3)}, DSU: {1,2,3}, {4}
- Add (3,4): MST = {(1,2), (2,3), (3,4)}, DSU: {1,2,3,4}

**MST Weight**: 5 + 5 + 5 = 15

When edges have equal weights, the algorithm may produce different valid MSTs depending on the order of processing. All such MSTs have the same total weight.

### Example 3: Practical Application - Network Design

**Problem**: Design a minimum cost network connecting 4 cities with the following connection costs:

| Connection | Cost (in lakhs) |
|------------|-----------------|
| Delhi-Mumbai | 12 |
| Delhi-Chennai | 8 |
| Delhi-Kolkata | 10 |
| Mumbai-Chennai | 7 |
| Mumbai-Kolkata | 15 |
| Chennai-Kolkata | 9 |

**Solution using Kruskal's Algorithm:**

**Step 1: Sort edges by cost**
Mumbai-Chennai(7), Delhi-Chennai(8), Chennai-Kolkata(9), Delhi-Kolkata(10), Delhi-Mumbai(12), Mumbai-Kolkata(15)

**Step 2: Process edges**
- Add Mumbai-Chennai(7): MST cost = 7
- Add Delhi-Chennai(8): MST cost = 7 + 8 = 15
- Add Chennai-Kolkata(9): MST cost = 7 + 8 + 9 = 24
- Add Delhi-Kolkata(10): Skip (creates cycle)
- Add Delhi-Mumbai(12): Skip (creates cycle)
- Add Mumbai-Kolkata(15): Skip (creates cycle)

**Result**: Optimal network connections are:
- Delhi ↔ Chennai (8 lakhs)
- Mumbai ↔ Chennai (7 lakhs)
- Kolkata ↔ Chennai (9 lakhs)

**Total Minimum Cost**: 24 lakhs

## Exam Tips

1. **Understand the core concept**: Kruskal's algorithm builds MST by adding edges in increasing order of weight, skipping those that create cycles. Remember to explain both the algorithm and the Union-Find structure in exams.

2. **Know the time complexity**: O(E log V) or O(E log E) — be able to derive this from edge sorting and Union-Find operations.

3. **Comparison with Prim's algorithm**: Prim's algorithm is better for dense graphs (O(V²) or O(E log V) with Fibonacci heap), while Kruskal's is better for sparse graphs. Know when to use which.

4. **Cycle detection explanation**: In exams, explain how Find operation detects cycles—if Find(u) equals Find(v), adding edge (u,v) would create a cycle.

5. **Trace the algorithm**: Practice tracing Kruskal's algorithm on small graphs. You must be able to show step-by-step execution and identify which edges are included/excluded.

6. **Properties of MST**: Remember the Cut Property and Cycle Property — these are frequently asked in theoretical questions.

7. **Union-Find optimizations**: Know path compression and union by rank — these are key to achieving near-linear time complexity for Find and Union operations.

8. **Greedy justification**: Be prepared to explain why the greedy approach works — the cut property guarantees that the minimum weight edge crossing any cut belongs to some MST.

9. **Handling edge cases**: Consider disconnected graphs (result is Minimum Spanning Forest), graphs with equal weights (multiple valid MSTs), and single vertex graphs.

10. **Applications**: Know real-world applications like network design, cluster analysis in data science, and image segmentation.