# Cut-Sets and Cut-Vertices

## Table of Contents

- [Cut-Sets and Cut-Vertices](#cut-sets-and-cut-vertices)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Cut-Vertices (Articulation Points)](#cut-vertices-articulation-points)
  - [Bridges (Cut-Edges)](#bridges-cut-edges)
  - [Cut-Sets (Edge Cuts)](#cut-sets-edge-cuts)
  - [Edge Connectivity and Vertex Connectivity](#edge-connectivity-and-vertex-connectivity)
  - [Finding Cut-Vertices: DFS-Based Algorithm](#finding-cut-vertices-dfs-based-algorithm)
  - [Block-Cut Graph](#block-cut-graph)
- [Examples](#examples)
  - [Example 1: Identifying Cut-Vertices and Bridges](#example-1-identifying-cut-vertices-and-bridges)
  - [Example 2: Finding Cut-Set with Minimum Edges](#example-2-finding-cut-set-with-minimum-edges)
  - [Example 3: Algorithm for Cut-Vertices](#example-3-algorithm-for-cut-vertices)
- [Exam Tips](#exam-tips)

## Introduction

In graph theory, understanding the connectivity of a graph is fundamental to analyzing network reliability, communication systems, and structural dependencies. Cut-sets and cut-vertices are critical concepts that help us identify the "weak points" in a graph structure. A cut-vertex (also known as an articulation point) is a vertex whose removal disconnects the graph or increases the number of connected components. Similarly, a cut-set (or edge cut) is a set of edges whose removal disconnects the graph. These concepts are extensively used in network design, where identifying critical nodes and links helps in creating robust communication networks and transportation systems.

The study of cut-sets and cut-vertices is essential for the university's Graph Theory course (BCS405B) as it forms the foundation for understanding graph connectivity, planarity, and network flow. These concepts appear frequently in algorithm design, particularly in finding bridges in networks, designing fault-tolerant systems, and solving practical problems like telephone network planning and road traffic management.

## Key Concepts

### Cut-Vertices (Articulation Points)

A **cut-vertex** (or articulation point) of a graph G is a vertex v such that the removal of v (along with all edges incident to v) increases the number of connected components in G. In other words, there exists at least one pair of vertices u and w in G such that every path from u to w contains v.

**Formal Definition:** A vertex v in a connected graph G is a cut-vertex if G - v (the graph obtained by removing v and all edges incident to v) is disconnected.

**Properties of Cut-Vertices:**

1. A graph with no cut-vertices is called a **biconnected graph** or **2-vertex-connected graph**.
2. The removal of a cut-vertex may disconnect the graph into multiple components.
3. In a tree, every vertex with degree > 1 is a cut-vertex.
4. End vertices (leaf nodes) in a tree are not cut-vertices.

### Bridges (Cut-Edges)

A **bridge** (or cut-edge) is an edge whose removal disconnects a graph. If an edge e = (u, v) is a bridge, then there is no path from u to v in G - e.

**Formal Definition:** An edge e in a connected graph G is a bridge if G - e (the graph obtained by removing e) is disconnected.

**Properties of Bridges:**

1. An edge is a bridge if and only if it does not belong to any cycle.
2. A bridge is a special case of a cut-set with a single edge.
3. In a tree, every edge is a bridge.
4. The removal of a bridge always increases the number of connected components by exactly 1.

### Cut-Sets (Edge Cuts)

A **cut-set** (or edge cut) is a set of edges whose removal disconnects a graph. More specifically, an edge cut is a set of edges S such that G - S (the graph obtained by removing all edges in S) has more connected components than G, and S is minimal with respect to this property (no proper subset of S has the same property).

**Formal Definition:** A set S of edges in a connected graph G is a cut-set if G - S is disconnected, and for any proper subset S' ⊂ S, the graph G - S' is still connected.

**Properties of Cut-Sets:**

1. A cut-set always contains at least one edge from every spanning tree of G.
2. The edge connectivity λ(G) of a graph G is the minimum number of edges whose removal disconnects G.
3. For any graph G, λ(G) ≤ δ(G), where δ(G) is the minimum degree of G.

### Edge Connectivity and Vertex Connectivity

**Edge Connectivity (λ):** The edge connectivity of a connected graph G, denoted λ(G), is the minimum number of edges whose removal disconnects G. A graph is **k-edge-connected** if λ(G) ≥ k.

**Vertex Connectivity (κ):** The vertex connectivity of a connected graph G, denoted κ(G), is the minimum number of vertices whose removal disconnects G (or makes it trivial). A graph is **k-vertex-connected** if κ(G) ≥ k.

**Relationship:** For any graph G with n vertices:

- κ(G) ≤ λ(G) ≤ δ(G)
- κ(G) ≤ n - 1

### Finding Cut-Vertices: DFS-Based Algorithm

The algorithm to find all cut-vertices in a connected graph uses depth-first search (DFS). Key concepts include:

**Discovery Time (disc[v]):** The time when vertex v is first visited in DFS.

**Lowest Reachability (low[v]):** The minimum discovery time reachable from v through zero or more tree edges followed by at most one back edge.

**Rules for Cut-Vertices:**

1. For a root of DFS tree: It is a cut-vertex if and only if it has at least two children in the DFS tree.
2. For a non-root vertex v: It is a cut-vertex if and only if there exists a child c of v such that low[c] ≥ disc[v].

### Block-Cut Graph

A **block** (or biconnected component) is a maximal subgraph that has no cut-vertices. The **block-cut graph** (or BC-tree) is a bipartite graph where one partition represents the blocks, and the other represents the cut-vertices. Each cut-vertex connects to all blocks that contain it.

## Examples

### Example 1: Identifying Cut-Vertices and Bridges

Consider the graph G with vertices {a, b, c, d, e, f} and edges: (a,b), (b,c), (c,d), (d,e), (e,f), (f,a), (b,e), (c,f).

**Solution:**

Step 1: Draw and analyze the graph.

Step 2: Identify bridges by checking if any edge lies on a cycle:

- Edge (a,b): Part of cycle a-b-f-a → Not a bridge
- Edge (b,c): Part of cycle b-c-d-e-b → Not a bridge
- Edge (c,d): Part of cycle c-d-e-f-c → Not a bridge
- Edge (d,e): Part of cycle d-e-b-c-d → Not a bridge
- Edge (e,f): Part of cycle e-f-a-b-e → Not a bridge
- Edge (f,a): Part of cycle a-f-e-b-a → Not a bridge
- Edge (b,e): Part of cycle b-e-d-c-b → Not a bridge
- Edge (c,f): Part of cycle c-f-e-d-c → Not a bridge

Since all edges lie on cycles, **there are no bridges**.

Step 3: Identify cut-vertices by testing removal:

- Remove a: Remaining graph still connected through b-f-e path → a is NOT a cut-vertex
- Remove b: Graph splits into components {c,d,e,f} and {a} (no connection) → **b is a cut-vertex**
- Remove c: Graph splits into {a,b} and {d,e,f} → **c is a cut-vertex**
- Remove d: Graph splits into {a,b,c} and {e,f} → **d is a cut-vertex**
- Remove e: Graph splits into {a,b,c,d} and {f} → **e is a cut-vertex**
- Remove f: Graph splits into {a,b} and {c,d,e} → **f is a cut-vertex**

**Answer:** Cut-vertices: b, c, d, e, f; Bridges: None

### Example 2: Finding Cut-Set with Minimum Edges

Find the minimum edge cut (edge connectivity) of the graph:

Vertices: {1, 2, 3, 4}
Edges: (1,2), (1,3), (2,3), (2,4), (3,4)

**Solution:**

Step 1: The minimum degree δ(G) = 2 (vertices 1, 2, 3, 4 all have degree 2).

Step 2: Check if we can disconnect with 1 edge:

- Removing any single edge doesn't disconnect the graph because the remaining edges still provide alternative paths.

Step 3: Try removing 2 edges:

- Consider removing edges (1,2) and (1,3): Remaining edges are (2,3), (2,4), (3,4) → Graph remains connected (2-3-4 forms a path to all).
- Consider removing edges (2,4) and (3,4): Remaining edges are (1,2), (1,3), (2,3) → This forms a triangle, still connected.
- Consider removing edges (1,2) and (2,4): Remaining edges are (1,3), (2,3), (3,4) → Connected through path 1-3-4.

Step 4: Try removing specific edge pairs:

- Remove (1,2) and (2,3): Remaining edges (1,3), (2,4), (3,4). Now vertex 2 is only connected to 4, and 1 is connected to 3. Graph disconnects! Component 1: {1,3}; Component 2: {2,4}

**Answer:** The minimum edge cut is 2, so λ(G) = 2.

### Example 3: Algorithm for Cut-Vertices

For the graph: vertices {1,2,3,4,5}, edges {(1,2), (2,3), (3,4), (4,5), (5,2)} - a cycle with a tail.

Using DFS starting from vertex 1:

Step 1: DFS Tree traversal:

- Visit 1: disc[1] = 1, parent = None
- Visit 2: disc[2] = 2, parent = 1
- Visit 3: disc[3] = 3, parent = 2
- Visit 4: disc[4] = 4, parent = 3
- Visit 5: disc[5] = 5, parent = 4
- Back edge found: (5,2) - this creates a cycle

Step 2: Calculate low values (working backwards):

- low[5] = min(disc[5], disc[2]) = min(5,2) = 2 (due to back edge)
- low[4] = min(disc[4], low[5]) = min(4,2) = 2
- low[3] = min(disc[3], low[4]) = min(3,2) = 2
- low[2] = min(disc[2], low[3], disc[1]) = min(2,2,1) = 1
- low[1] = min(disc[1], low[2]) = min(1,1) = 1

Step 3: Identify cut-vertices:

- Root (vertex 1): Has only 1 child → NOT a cut-vertex
- Vertex 2: Check child 3: low[3] ≥ disc[2]? 2 ≥ 2 → YES → **Vertex 2 is a cut-vertex**
- Vertex 3: Check child 4: low[4] ≥ disc[3]? 2 ≥ 3 → NO
- Vertex 4: Check child 5: low[5] ≥ disc[4]? 2 ≥ 4 → NO
- Vertex 5: No children in DFS tree

**Answer:** The only cut-vertex is 2. Removing vertex 2 disconnects vertex 1 from the rest {3,4,5}.

## Exam Tips

1. **Remember the key difference**: A cut-vertex is a vertex whose removal disconnects the graph, while a bridge (cut-edge) is a single edge whose removal disconnects the graph.

2. **Bridge detection shortcut**: An edge is a bridge if and only if it does not belong to any cycle in the graph.

3. **Tree properties**: In a tree, every edge is a bridge, and every non-leaf vertex (degree > 1) is a cut-vertex.

4. **DFS algorithm for cut-vertices**: Focus on the conditions - root is cut-vertex only if it has ≥2 children; non-root is cut-vertex if low[child] ≥ disc[parent].

5. **Connectivity relationships**: Always remember κ(G) ≤ λ(G) ≤ δ(G) for any graph G.

6. **Complete graphs**: Kn has no cut-vertices and no bridges since every vertex is connected to every other vertex directly or through multiple paths.

7. **Block-cut tree**: Know that this bipartite graph connects blocks (biconnected components) to their articulation points.

8. **Minimum cuts**: For exam problems asking for minimum cut-sets, check edge-by-edge removal first, then pairs of edges, etc.
