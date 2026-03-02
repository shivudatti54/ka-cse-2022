# Spanning Trees


## Table of Contents

- [Spanning Trees](#spanning-trees)
- [1. Introduction and Fundamental Definitions](#1-introduction-and-fundamental-definitions)
- [2. Fundamental Properties and Theoretical Foundations](#2-fundamental-properties-and-theoretical-foundations)
  - [Theorem 2.1 (Edge Count in Spanning Trees):\*\* A spanning tree containing n vertices possesses exactly n - 1 edges.](#theorem-21-edge-count-in-spanning-trees-a-spanning-tree-containing-n-vertices-possesses-exactly-n---1-edges)
  - [Theorem 2.2 (Characterization of Spanning Trees):\*\* For a connected graph G = (V, E), a subgraph T = (V, E') is a spanning tree if and only if |E'| = |V| - 1.](#theorem-22-characterization-of-spanning-trees-for-a-connected-graph-g--v-e-a-subgraph-t--v-e-is-a-spanning-tree-if-and-only-if-e--v---1)
  - [Theorem 2.3 (Connectivity and Edge Count):\*\* For any graph G with n vertices and c connected components, a spanning forest (collection of trees, one per component) contains exactly n - c edges.](#theorem-23-connectivity-and-edge-count-for-any-graph-g-with-n-vertices-and-c-connected-components-a-spanning-forest-collection-of-trees-one-per-component-contains-exactly-n---c-edges)
  - [Theorem 2.4 (Fundamental Cycle Property):\*\* Let T be a spanning tree of G. For any edge e ∈ E(G) \ E(T), the graph T + e (obtained by adding e to T) contains exactly one cycle. Conversely, every cycle in G contains at least one edge not in T.](#theorem-24-fundamental-cycle-property-let-t-be-a-spanning-tree-of-g-for-any-edge-e--eg--et-the-graph-t--e-obtained-by-adding-e-to-t-contains-exactly-one-cycle-conversely-every-cycle-in-g-contains-at-least-one-edge-not-in-t)
  - [Theorem 2.5 (Fundamental Cutset Property):** Let T be a spanning tree of G. For any edge e ∈ E(T), the removal of e from T (denoted T - e) disconnects T into exactly two components. The set of edges in E(G) that cross this cut (one endpoint in each component) is called a **fundamental cutset\*\*, and it must contain edge e.](#theorem-25-fundamental-cutset-property-let-t-be-a-spanning-tree-of-g-for-any-edge-e--et-the-removal-of-e-from-t-denoted-t---e-disconnects-t-into-exactly-two-components-the-set-of-edges-in-eg-that-cross-this-cut-one-endpoint-in-each-component-is-called-a-fundamental-cutset-and-it-must-contain-edge-e)
- [3. Construction of Spanning Trees via Graph Traversal](#3-construction-of-spanning-trees-via-graph-traversal)
  - [3.1 Depth-First Search (DFS) Spanning Tree](#31-depth-first-search-dfs-spanning-tree)
  - [3.2 Breadth-First Search (BFS) Spanning Tree](#32-breadth-first-search-bfs-spanning-tree)
  - [3.3 Comparative Analysis](#33-comparative-analysis)
- [4. Enumeration of Spanning Trees](#4-enumeration-of-spanning-trees)
  - [4.1 Cayley's Formula](#41-cayleys-formula)
  - [4.2 Kirchhoff's Matrix-Tree Theorem](#42-kirchhoffs-matrix-tree-theorem)
- [5. Minimum Spanning Trees (MST)](#5-minimum-spanning-trees-mst)
  - [5.1 Problem Definition](#51-problem-definition)
  - [5.2 The Cut Property (Correctness Foundation)](#52-the-cut-property-correctness-foundation)
  - [5.3 The Exchange Lemma](#53-the-exchange-lemma)
  - [5.4 Kruskal's Algorithm](#54-kruskals-algorithm)
  - [5.5 Prim's Algorithm](#55-prims-algorithm)
  - [5.6 Comparison of MST Algorithms](#56-comparison-of-mst-algorithms)
- [6. Applications and Complexity Summary](#6-applications-and-complexity-summary)
  - [Complexity Summary](#complexity-summary)
- [7. Assessment Questions](#7-assessment-questions)
  - [Question 1 (Analysis - Hard)](#question-1-analysis---hard)
  - [Question 2 (Proof - Hard)](#question-2-proof---hard)
  - [Question 3 (Application - Hard)](#question-3-application---hard)
  - [Question 4 (Analysis - Hard)](#question-4-analysis---hard)

## 1. Introduction and Fundamental Definitions

A **spanning tree** constitutes one of the most significant structures in graph theory, serving as the foundation for numerous algorithmic applications in network design, connectivity problems, and optimization scenarios. The formal definition is as follows:

**Definition 1.1 (Spanning Tree):** Let G = (V, E) be a connected, undirected graph. A subgraph T = (V, E') is called a **spanning tree** of G if and only if:

1. V(T) = V(G) — the vertex sets are identical (the tree spans all vertices);
2. T is connected — there exists a path between every pair of vertices in T;
3. T is acyclic — T contains no cycles.

Equivalently, a spanning tree is a **maximal acyclic subgraph** or a **minimal connected subgraph** of G. These two characterizations are dual to each other and provide valuable insights into the structure of spanning trees.

## 2. Fundamental Properties and Theoretical Foundations

### Theorem 2.1 (Edge Count in Spanning Trees):\*\* A spanning tree containing n vertices possesses exactly n - 1 edges.

**Proof by Induction:**

_Base Case:_ For n = 1, the spanning tree consists of a single isolated vertex with zero edges. Since 1 - 1 = 0, the property holds.

_Inductive Hypothesis:_ Assume the theorem holds for all trees with k vertices (where k ≥ 1), i.e., every tree with k vertices contains exactly k - 1 edges.

_Inductive Step:_ Consider a tree T with k + 1 vertices. Since k + 1 ≥ 2, T must contain at least one leaf (a vertex of degree 1) — this follows directly from the handshaking lemma for trees. Remove this leaf vertex along with its incident edge. The resulting subgraph T' contains k vertices and remains acyclic and connected (since removing a leaf cannot disconnect a tree). By the inductive hypothesis, T' contains exactly k - 1 edges. Reconstructing T by adding the removed leaf and edge yields k edges. Since k = (k + 1) - 1, the theorem holds for k + 1 vertices.

By the principle of mathematical induction, the theorem is proven for all n ≥ 1. ∎

### Theorem 2.2 (Characterization of Spanning Trees):\*\* For a connected graph G = (V, E), a subgraph T = (V, E') is a spanning tree if and only if |E'| = |V| - 1.

**Proof:** The forward implication follows from Theorem 2.1. For the converse, suppose T is a subgraph of G with |V| vertices and |V| - 1 edges. If T were not connected, by Theorem 2.3 (discussed below), it would contain at least |V| - c edges, where c ≥ 2 is the number of components — contradiction. Similarly, if T contained a cycle, removing one edge from that cycle would still preserve connectivity, yielding a subgraph with |V| - 1 edges that remains connected — contradiction to the minimality implied by |E'| = |V| - 1. Hence, T must be a tree. ∎

### Theorem 2.3 (Connectivity and Edge Count):\*\* For any graph G with n vertices and c connected components, a spanning forest (collection of trees, one per component) contains exactly n - c edges.

**Proof:** Apply Theorem 2.1 to each of the c components. If component i contains n_i vertices, its spanning tree contains n_i - 1 edges. Summing over all components:
∑(n_i - 1) = (∑ n_i) - c = n - c. ∎

### Theorem 2.4 (Fundamental Cycle Property):\*\* Let T be a spanning tree of G. For any edge e ∈ E(G) \ E(T), the graph T + e (obtained by adding e to T) contains exactly one cycle. Conversely, every cycle in G contains at least one edge not in T.

**Proof:** Adding edge e = (u, v) to T creates an alternative path between u and v (since T is connected). This path combined with e forms a cycle. If two distinct cycles were created, T would contain two distinct u-v paths, implying the existence of a cycle in T — contradiction. For the converse, any cycle in G must contain an edge whose removal disconnects the cycle while preserving the overall connectivity to span all vertices; such an edge cannot belong to T. ∎

### Theorem 2.5 (Fundamental Cutset Property):** Let T be a spanning tree of G. For any edge e ∈ E(T), the removal of e from T (denoted T - e) disconnects T into exactly two components. The set of edges in E(G) that cross this cut (one endpoint in each component) is called a **fundamental cutset\*\*, and it must contain edge e.

**Proof:** Since T is a tree (acyclic), removing any edge must increase the number of components by exactly one — from 1 to 2. The cutset consists precisely of all edges in G with endpoints in different components of T - e. Edge e itself belongs to this cutset by construction. ∎

## 3. Construction of Spanning Trees via Graph Traversal

### 3.1 Depth-First Search (DFS) Spanning Tree

When performing DFS on a connected graph, the **tree edges** — those edges that lead to the discovery of previously unvisited vertices — form a DFS spanning tree. The remaining edges are classified as **back edges** (connecting a vertex to its ancestor in the DFS tree) or **cross edges**.

**Construction Algorithm:**

```
DFS(v):
    mark v as visited
    for each neighbor u of v:
        if u is not visited:
            add edge (v, u) to tree edges
            DFS(u)
```

**Example:** Consider graph G with vertices {0,1,2,3} and adjacency list:

- 0: [1, 2]
- 1: [0, 2, 3]
- 2: [0, 1, 3]
- 3: [1, 2]

Executing DFS from vertex 0 yields tree edges: {(0,1), (1,2), (2,3)}. The DFS tree exhibits a **deep, narrow** structure characteristic of depth-first exploration. The edges {(0,2), (1,3)} become back edges.

**Properties of DFS Spanning Tree:**

- Height can be O(V) in the worst case (e.g., a path graph).
- Root-to-any-vertex path is not necessarily the shortest path in the original graph.

### 3.2 Breadth-First Search (BFS) Spanning Tree

BFS traversal produces a **BFS spanning tree** where tree edges correspond to discoveries of new vertices. Non-tree edges are **cross edges** (connecting vertices at the same or adjacent levels) or back edges.

**Construction Algorithm:**

```
BFS(s):
    mark s as visited, enqueue s
    while queue is not empty:
        v = dequeue
        for each neighbor u of v:
            if u is not visited:
                mark u as visited
                add edge (v, u) to tree edges
                enqueue u
```

**Example:** Using the same graph, BFS from vertex 0 yields tree edges: {(0,1), (0,2), (1,3)}. The BFS tree exhibits a **short, wide** structure.

**Properties of BFS Spanning Tree:**

- Height equals the eccentricity of the root (maximum distance from root).
- The root-to-vertex path in the BFS tree is always a **shortest path** in the original unweighted graph.

### 3.3 Comparative Analysis

| Property            | DFS Spanning Tree              | BFS Spanning Tree                     |
| ------------------- | ------------------------------ | ------------------------------------- |
| **Structure**       | Deep and narrow                | Short and wide                        |
| **Height**          | O(V) worst case                | O(diameter)                           |
| **Path**            | Not necessarily shortest       | Short Propertyest in unweighted graph |
| **Non-tree Edges**  | Back edges                     | Cross edges                           |
| **Data Structure**  | Stack (implicit via recursion) | Queue                                 |
| **Time Complexity** | O(V + E)                       | O(V + E)                              |

## 4. Enumeration of Spanning Trees

### 4.1 Cayley's Formula

**Theorem 4.1 (Cayley's Formula):** The complete graph K_n on n vertices possesses exactly n^(n-2) distinct spanning trees.

**Proof Sketch (Kirchhoff/Cayley):** One elegant combinatorial proof employs the **Prüfer sequence** representation. Each spanning tree of K_n can be uniquely encoded by a sequence of length n-2 over the alphabet {1, 2, ..., n}. Conversely, every such sequence corresponds to exactly one spanning tree. Since there are n^(n-2) possible sequences, this establishes the count. ∎

**Applications:** For K_5, the number of spanning trees equals 5^3 = 125. For K_6, we obtain 6^4 = 1296 spanning trees.

### 4.2 Kirchhoff's Matrix-Tree Theorem

**Theorem 4.2 (Matrix-Tree Theorem):** Let G be a connected graph with n vertices. Let L be the Laplacian matrix defined as L = D - A, where D is the degree matrix (diagonal matrix containing vertex degrees) and A is the adjacency matrix. Then the number of spanning trees of G equals any cofactor of L (determinant of any (n-1) × (n-1) principal submatrix obtained by deleting one row and the corresponding column).

**Proof Sketch:** The theorem relies on the combinatorial properties of the Laplacian matrix. Every column of L sums to zero, and L is singular with rank n-1 for connected graphs. The matrix-tree theorem can be proven using the Kirchhoff's Effective Resistance interpretation or via the all-minors matrix-tree theorem. The determinant of the reduced Laplacian counts the number of spanning trees through the combinatorial enumeration of all possible tree structures. ∎

**Computational Application:** For a graph with n vertices, the determinant computation requires O(n^3) time using Gaussian elimination, making it suitable for small to medium-sized graphs.

## 5. Minimum Spanning Trees (MST)

### 5.1 Problem Definition

Given a connected, undirected, weighted graph G = (V, E, w) with weight function w: E → ℝ, a **minimum spanning tree** is a spanning tree of G with minimum total edge weight:
$$w(T^*) = \min_{T \text{ is spanning tree}} \sum_{e \in E(T)} w(e)$$

The MST problem possesses optimal-substructure property: any subtree of an MST is itself an MST for the subgraph induced by its vertices.

### 5.2 The Cut Property (Correctness Foundation)

**Lemma 5.1 (Cut Property):** Let S be any subset of vertices that is strictly neither empty nor equal to V. Consider the cut (S, V-S) that separates the graph into two parts. Let e be the edge of minimum weight crossing this cut (the "lightest edge"). Then there exists a minimum spanning tree that contains edge e.

**Proof:** Suppose, for contradiction, that no MST contains e. Let T be an MST that does not contain e. Since T is spanning, there exists some edge f that crosses the cut (S, V-S) and belongs to T (otherwise T would be disconnected). Since e is the lightest edge crossing the cut, we have w(e) ≤ w(f). If w(e) = w(f), we can replace f with e to obtain another MST containing e. If w(e) < w(f), replacing f with e yields a spanning tree T' with strictly smaller weight: w(T') = w(T) - w(f) + w(e) < w(T), contradicting the minimality of T. ∎

### 5.3 The Exchange Lemma

**Lemma 5.2 (Exchange Lemma):** Let T be a minimum spanning tree and let e be any edge not in T. Adding e to T creates a cycle. If f is any edge on this cycle that is not in T, then w(f) ≥ w(e) for some MST, or equivalently, there exists an MST T' = T - f + e.

### 5.4 Kruskal's Algorithm

**Algorithm:**

```
Kruskal(G):
    Sort all edges in non-decreasing order by weight
    Initialize a disjoint-set union-find structure
    For each edge (u, v) in sorted order:
        if find(u) ≠ find(v):
            add edge (u, v) to MST
            union(u, v)
    Return MST
```

**Proof of Correctness:** Kruskal's algorithm repeatedly applies the cut property. When processing edge e, all previously selected edges form a forest F. The connected components of F define a cut; if u and v are in different components, e is the lightest edge crossing this cut. Adding e to the MST is therefore justified by the cut property. By induction, the final forest is connected (otherwise, a lighter crossing edge would exist) and acyclic (otherwise, we'd have processed a heavier edge connecting the same component).

**Time Complexity:**

- Sorting edges: O(E log E)
- Union-Find operations: O(E α(V)) where α is the inverse Ackermann function (practically constant)
- Total: **O(E log E)** or equivalently **O(E log V)** since E ≤ V^2.

### 5.5 Prim's Algorithm

**Algorithm:**

```
Prim(G, r):
    key[v] = ∞ for all v
    parent[v] = NULL for all v
    key[r] = 0
    Insert all vertices into priority queue Q
    While Q is not empty:
        u = extract-min(Q)
        For each neighbor v of u:
            if v ∈ Q and w(u, v) < key[v]:
                key[v] = w(u, v)
                parent[v] = u
                decrease-key(Q, v)
    Return MST from parent array
```

**Proof of correctness:** Prim's algorithm also relies on the cut property. At each iteration, the set of vertices already included in the MST (call this set S) defines a cut (S, V-S). The algorithm selects the minimum-weight edge crossing this cut (the vertex v with minimum key value). By the cut property, this edge can belong to some MST. By induction, the constructed tree is always a subtree of some MST.

**Time Complexity:**

- With binary heap: O(E log V)
- With Fibonacci heap: O(E + V log V)

### 5.6 Comparison of MST Algorithms

| Algorithm | Data Structure      | Time Complexity             | Best For                      |
| --------- | ------------------- | --------------------------- | ----------------------------- |
| Kruskal   | Union-Find, Sorting | O(E log V)                  | Sparse graphs (E ≈ V)         |
| Prim      | Priority Queue      | O(E log V) / O(E + V log V) | Dense graphs (E ≈ V²)         |
| Boruvka   | Union-Find          | O(E log V)                  | Parallel/distributed settings |

## 6. Applications and Complexity Summary

Spanning trees and MSTs find applications in:

- Network design (telecommunications, transportation)
- Clustering algorithms
- Image segmentation
- Distributed computing (broadcast protocols)
- Approximation algorithms (traveling salesman problem)

### Complexity Summary

| Operation                           | Time Complexity |
| ----------------------------------- | --------------- |
| DFS/BFS spanning tree               | O(V + E)        |
| Kruskal's MST                       | O(E log V)      |
| Prim's MST (binary heap)            | O(E log V)      |
| Counting spanning trees (Kirchhoff) | O(V³)           |

## 7. Assessment Questions

### Question 1 (Analysis - Hard)

Consider a connected weighted graph G with 6 vertices and 10 edges. Using Kruskal's algorithm, determine which edge is added last to the MST and compute the total weight. Given edges with weights: (1,2)=3, (2,3)=4, (3,4)=5, (4,5)=6, (5,6)=7, (1,4)=10, (2,5)=11, (3,6)=12, (1,6)=14, (2,4)=15.

### Question 2 (Proof - Hard)

Prove that for a connected graph with distinct edge weights, the minimum spanning tree is unique.

### Question 3 (Application - Hard)

Given the following adjacency matrix representing a weighted graph, construct the Laplacian matrix and compute the number of spanning trees using Kirchhoff's theorem:

```
    0  1  2  3
--------------
0 | 0  5  0  0
1 | 5  0  3  0
2 | 0  3  0  6
3 | 0  0  6  0
```

### Question 4 (Analysis - Hard)

In a BFS spanning tree constructed from vertex 0, what is the maximum possible distance from the root to any vertex in the tree? Justify your answer with respect to the graph diameter.
