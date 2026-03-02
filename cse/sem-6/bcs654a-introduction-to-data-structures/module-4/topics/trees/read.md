# Trees and Spanning Trees

## Introduction

In Graph Theory, a **tree** represents one of the most fundamental and elegant structures, serving as the backbone for numerous applications in computer science, telecommunications, and operations research. The tree data structure underlies critical systems such as file systems, hierarchical organizational charts, XML/HTML document object models, and network routing protocols. The elegance of trees stems from their simplicity—they are connected graphs devoid of cycles—yet they possess remarkable mathematical properties that make them indispensable in both theoretical and applied contexts.

## Formal Definition of a Tree

A **tree** is defined as an undirected graph T = (V, E) that satisfies any of the following equivalent conditions:

1. **Connected and Acyclic:** T is connected and contains no cycles.
2. **Unique Path Property:** There exists exactly one simple path between any two distinct vertices in T.
3. **Minimal Connected:** T is connected, but removing any single edge from E disconnects the graph.
4. **Maximal Acyclic:** T is acyclic, but adding any edge between two non-adjacent vertices creates exactly one cycle.
5. **Edge-Vertex Relation:** If T has n vertices, then it has exactly n − 1 edges.

### Theorem: Equivalence of Tree Definitions

**Theorem:** For an undirected graph G = (V, E) with |V| = n, the following statements are equivalent:

- (a) G is a tree (connected and acyclic)
- (b) G is connected and has exactly n − 1 edges
- (c) G is acyclic and has exactly n − 1 edges
- (d) There is exactly one simple path between any pair of distinct vertices
- (e) G is connected, and every edge is a bridge

**Proof:** We prove the equivalence through a chain of implications:

**(a) ⇒ (b):** A tree with n vertices must have n − 1 edges. We prove this by induction on n. For n = 1, the tree has 0 edges. Assume true for all trees with fewer than n vertices. Removing any edge from a tree with n vertices disconnects it into two components, each of which is a tree. By induction, these components have (n₁ − 1) and (n₂ − 1) edges respectively, where n₁ + n₂ = n. Total edges = (n₁ − 1) + (n₂ − 1) + 1 = n − 1.

**(b) ⇒ (c):** If a connected graph has n − 1 edges but contains a cycle, removing one edge from a cycle leaves a connected graph with n − 2 edges. By repeatedly removing edges from cycles while maintaining connectivity, we obtain a spanning tree with n − 1 edges, contradicting that we started with n − 1 edges. Therefore, the graph must be acyclic.

**(c) ⇒ (d):** An acyclic graph with n − 1 edges must be connected. Suppose it were disconnected with k components. Each component (being a tree) has edges equal to vertices minus 1. Summing: total edges = (n₁ − 1) + (n₂ − 1) + ... + (n_k − 1) = n − k. Since we have n − 1 edges, we get n − k = n − 1, implying k = 1. Thus connected. The unique path follows from acyclicity—if two distinct paths existed between vertices, they would form a cycle.

**(d) ⇒ (e):** If removing edge (u, v) disconnects the graph, there would be no path between u and v after removal. However, the original graph had a unique path between u and v, which must contain (u, v). This contradiction shows every edge is a bridge.

**(e) ⇒ (a):** A connected graph where every edge is a bridge cannot contain a cycle (cycles have non-bridge edges). Hence acyclic and thus a tree.

∎

## Essential Properties of Trees

For a tree T = (V, E) with n vertices:

1. **Edge Count:** |E| = n − 1
2. **Bridge Property:** Every edge is a bridge (its removal disconnects the graph)
3. **Leaf Count:** A tree with n ≥ 2 vertices has at least two leaves (pendant vertices)
4. **Degree Sum:** Σ\_{v∈V} deg(v) = 2(n − 1)
5. **Center:** The center of a tree is either one vertex or two adjacent vertices (obtained by repeatedly removing leaves)

## Tree Terminology

- **Leaf (Pendant Vertex):** A vertex with degree 1
- **Internal Vertex:** A vertex with degree ≥ 2
- **Rooted Tree:** A tree with a designated root vertex, establishing parent-child relationships
- **Level:** Distance (in edges) from the root to a vertex
- **Height:** Maximum level of any vertex in the rooted tree
- **Forest:** A graph consisting of one or more trees (acyclic, possibly disconnected)
- **Subtree:** A connected subgraph of a tree
- **Branch:** A path from a root to a leaf

## Example: Tree with 6 Vertices

```
 A
 / \
 B C
 / \ \
 D E F
```

- **Vertices:** {A, B, C, D, E, F}
- **Edges:** {(A,B), (A,C), (B,D), (B,E), (C,F)}
- **Edge Count:** 5 = 6 − 1 ✓
- **Leaves:** D, E, F (degree 1)
- **Internal Vertices:** A (degree 2), B (degree 3), C (degree 2)
- **Degree Sum:** 2 + 3 + 2 + 1 + 1 + 1 = 10 = 2(6 − 1) ✓

**Rooted at A:** Level 0: {A}, Level 1: {B, C}, Level 2: {D, E, F}, Height: 2

## Spanning Trees

### Definition

Given a connected, undirected graph G = (V, E), a **spanning tree** T = (V, E') is a subgraph of G that:

1. Contains all vertices of G (spanning property)
2. Forms a tree (connected and acyclic)
3. Has exactly |V| − 1 edges

### Key Properties

1. **Existence:** Every connected graph possesses at least one spanning tree
2. **Characterization:** A graph is connected if and only if it has a spanning tree
3. **Minimality:** A spanning tree is minimally connected—removing any edge disconnects it
4. **Maximality:** A spanning tree is maximally acyclic—adding any edge from G creates exactly one cycle
5. **Counting:** A complete graph K_n has n^(n−2) distinct spanning trees (Cayley's Formula)

### Constructing Spanning Trees

Two fundamental graph traversal algorithms produce spanning trees:

**Depth-First Search (DFS):** Explores as deep as possible before backtracking. Produces a tree with depth equal to the longest simple path. Time Complexity: O(|V| + |E|)

**Breadth-First Search (BFS):** Explores all neighbors at current distance before moving to the next level. Produces a spanning tree with minimum depth from root to all vertices. Time Complexity: O(|V| + |E|)

### Minimum Spanning Tree (MST)

For weighted graphs, a **Minimum Spanning Tree** is a spanning tree with minimum total edge weight. Classic algorithms include:

1. **Kruskal's Algorithm:** Greedy approach that sorts edges by weight and adds edges that don't form cycles. Time Complexity: O(|E| log|V|)

2. **Prim's Algorithm:** Grows the tree from a starting vertex by repeatedly adding the minimum weight edge connecting the tree to a new vertex. Time Complexity: O(|E| log|V|) with binary heap, O(|E| + |V| log|V|) with Fibonacci heap

**Theorem (Cut Property):** For any cut in a graph, the minimum weight edge crossing that cut belongs to some minimum spanning tree.

**Proof:** Let e be the minimum weight edge crossing cut (S, V−S). Suppose no MST contains e. Take any MST T. Adding e to T creates a cycle. This cycle must contain another edge f crossing the cut. Since e has minimum weight, w(e) ≤ w(f). Replacing f with e gives a spanning tree T' with weight w(T') = w(T) + w(e) − w(f) ≤ w(T). Since T is minimum, T' must also be minimum and contains e. ∎
