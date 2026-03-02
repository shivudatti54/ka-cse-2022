# Properties of Trees

## Table of Contents

- [Properties of Trees](#properties-of-trees)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Basic Properties](#definition-and-basic-properties)
  - [Characterization Theorems](#characterization-theorems)
  - [Centers and Radii](#centers-and-radii)
  - [Spanning Trees](#spanning-trees)
  - [Rooted Trees and Binary Trees](#rooted-trees-and-binary-trees)
  - [Weighted Trees and Minimum Spanning Trees](#weighted-trees-and-minimum-spanning-trees)
- [Examples](#examples)
  - [Example 1: Verifying a Tree Structure](#example-1-verifying-a-tree-structure)
  - [Example 2: Finding the Center of a Tree](#example-2-finding-the-center-of-a-tree)
  - [Example 3: Counting Spanning Trees](#example-3-counting-spanning-trees)
- [Exam Tips](#exam-tips)

## Introduction

A tree is one of the most fundamental and visually intuitive structures in graph theory. In computer science and discrete mathematics, trees serve as the backbone for numerous applications including hierarchical data structures, network routing algorithms, decision-making processes, and organizational charts. Unlike the complex cyclic graphs we've studied previously, trees possess a unique simplicity—a connected graph with no cycles—making them both theoretically elegant and practically invaluable.

The study of tree properties forms Module 3 of the BCS405B Graph Theory course, building upon the foundational concepts of graphs, paths, and connectivity established in earlier modules. Understanding trees is essential for CSE students as they encounter applications in data structures (binary trees, BSTs), database systems (B-trees), networking (spanning tree protocols), and algorithm design (divide and conquer approaches). This module explores the unique characteristics that distinguish trees from other graph types, the relationships between vertices and edges, and the powerful theorems that characterize tree structures.

## Key Concepts

### Definition and Basic Properties

A **tree** is defined as a connected acyclic graph—meaning it is a graph where exactly one path exists between any two vertices, and no closed walks exist. If a graph is acyclic but not necessarily connected, it is called a **forest**. Each connected component of a forest is therefore a tree. The vertices of degree 1 in a tree are called **leaves** or **pendant vertices**, while vertices with degree greater than 1 are termed **internal vertices** or **branch vertices**.

A tree with n vertices always contains exactly n-1 edges. This fundamental property, proven through mathematical induction, distinguishes trees from general connected graphs. Any connected graph with n vertices and n-1 edges must be a tree, and conversely, any tree with n vertices has exactly n-1 edges.

### Characterization Theorems

The power of tree theory lies in its multiple characterizations. A graph T with n vertices is a tree if and only if it satisfies any one of these equivalent conditions:

1. **Connectivity criterion**: T is connected and has n-1 edges
2. **Acyclicity criterion**: T is acyclic and has n-1 edges
3. **Unique path property**: T is connected, and every edge is a bridge (removing any edge disconnects the graph)
4. **Fundamental cycle criterion**: T becomes cyclic upon adding any single edge

These characterizations provide versatile tools for proving whether a given graph is a tree and for understanding the structural properties of tree graphs.

### Centers and Radii

The **center** of a tree is defined as the set of vertices that minimize the maximum distance to all other vertices. A tree's center consists of either one vertex (if the tree's diameter is even) or two adjacent vertices (if the diameter is odd). This concept is crucial in facility location problems and network design.

The **eccentricity** of a vertex is the maximum distance from that vertex to any other vertex in the tree. The **radius** is the minimum eccentricity among all vertices. The diameter, as we know, is the maximum distance between any two vertices. For any tree, the relationship holds: radius ≤ diameter ≤ 2 × radius.

### Spanning Trees

A **spanning tree** of a connected graph G is a subgraph that is a tree and contains all vertices of G. Every connected graph possesses at least one spanning tree. If G has n vertices and m edges, any spanning tree will contain exactly n-1 edges, meaning we remove (m - n + 1) edges to obtain a spanning tree. These (m - n + 1) edges represent the **cyclomatic number** or the number of independent cycles in the graph.

The **Cayley Formula** states that the complete graph Kₙ has exactly n^(n-2) distinct spanning trees. This remarkable result, proven by Cayley in 1889, demonstrates the combinatorial richness of complete graphs.

### Rooted Trees and Binary Trees

A **rooted tree** assigns a distinguished vertex as the root, establishing parent-child relationships among vertices. The root is typically placed at the top, with edges directed away from it. This orientation enables the study of tree depth, height, and level structures.

A **binary tree** is a rooted tree where each vertex has at most two children, traditionally labeled as left and right child. Binary trees are extensively used in computer science for expression evaluation, search operations, and sorting algorithms. The number of distinct binary trees with n vertices follows the Catalan numbers: Cₙ = (2n)!/(n!(n+1)!).

### Weighted Trees and Minimum Spanning Trees

In practical applications, edges often carry weights representing costs, distances, or capacities. A **minimum spanning tree (MST)** of a weighted connected graph is a spanning tree with minimum total edge weight. Two classical algorithms for finding MSTs are:

- **Kruskal's Algorithm**: Sort edges by weight, add edges greedily without forming cycles
- **Prim's Algorithm**: Grow the tree from a starting vertex, always adding the minimum weight edge connecting the tree to a new vertex

## Examples

### Example 1: Verifying a Tree Structure

**Problem**: Determine whether the graph with vertices {A, B, C, D, E} and edges {AB, BC, CD, DE} forms a tree.

**Solution**:

Step 1: Count vertices and edges

- Number of vertices (n) = 5
- Number of edges = 4

Step 2: Apply tree characterization
For a graph with 5 vertices to be a tree, it must be connected and have exactly 4 edges (n-1 = 5-1 = 4).

Step 3: Check connectivity
Starting from vertex A, we can reach all vertices: A→B→C→D→E. The graph is connected.

Step 4: Verify acyclicity
The edge set forms a simple path: A—B—C—D—E. No cycles exist.

Conclusion: The graph IS a tree (specifically, a path graph P₅). Note that this is a tree even though it has only 2 leaves (A and E), with the other three vertices being internal.

### Example 2: Finding the Center of a Tree

**Problem**: Find the center and radius of the tree with edges: {AB, AC, AD, CE, CF, EG, EH}

```
 A
 /|\
 B C D
 |
 E
 /|\
 G H F
```

**Solution**:

Step 1: Identify leaf vertices
Leaves are vertices with degree 1: B, D, F, H (and C has degree 1 as well)
Actually: deg(B)=1, deg(C)=1, deg(D)=1, deg(F)=1, deg(H)=1
Leaves: B, C, D, F, H

Step 2: Remove leaves iteratively (pruning method)
Iteration 1: Remove B, C, D, F, H
Remaining vertices: A, E, G
Degrees: deg(A)=2 (connected to E), deg(E)=3 (to A, G, F removed), deg(G)=2 (to E, H removed)

New leaves after iteration 1: A and G (both have degree 2, but we consider them for next iteration)
Actually, with A and G having degree 2, they're not leaves yet. Let's reconsider.

Let's use proper leaf removal:

- Initial leaves: B, C, D, F, H (all degree 1)
- After removing these: A now has degree 1 (was connected to B, C, D), E has degree 2 (connected to A, G, F), G has degree 1 (connected to E, H)
- New leaves: A, G
- After removing A and G: E remains with degree 0

Center = {E}, Radius = 1 (maximum distance from E to any vertex is 1)

### Example 3: Counting Spanning Trees

**Problem**: How many distinct spanning trees does K₃ (complete graph on 3 vertices) have?

**Solution**:

Step 1: Apply Cayley's Formula
For complete graph Kₙ, number of spanning trees = n^(n-2)

Step 2: Substitute n = 3
Number of spanning trees = 3^(3-2) = 3^1 = 3

Step 3: Verify by enumeration
K₃ has vertices {1, 2, 3} and edges {12, 23, 13}
Possible spanning trees (pick any 2 edges that connect all 3 vertices):

- Edges {12, 23}
- Edges {12, 13}
- Edges {23, 13}

All three are valid spanning trees. This matches Cayley's formula.

## Exam Tips

1. **Memorize the key equivalence**: For a graph with n vertices, "connected + (n-1) edges" = "acyclic + (n-1) edges" = "tree". Use whichever is easier to prove or disprove in exam problems.

2. **Remember leaf properties**: A tree with more than 2 vertices must have at least 2 leaves. This is proven by the handshaking lemma and is frequently tested.

3. **Center-finding algorithm**: Use the "leaf pruning" method—repeatedly remove all leaves until 1 or 2 vertices remain. This is the center of the tree.

4. **Spanning tree edge count**: Always remember: if a connected graph has n vertices and m edges, any spanning tree has exactly (n-1) edges, meaning (m - n + 1) edges must be removed.

5. **Cayley's Formula applications**: Know that Kₙ has n^(n-2) spanning trees. This frequently appears in numerical problems.

6. **Binary tree relationships**: For a binary tree with n vertices, i internal vertices, and l leaves: n = i + l and i = l - 1 (for proper binary trees where each internal node has exactly 2 children).

7. **Tree vs. forest distinction**: Remember—a forest is a collection of trees (acyclic graph), while a tree is a connected acyclic graph. This distinction appears in many university exam questions.

8. **Minimum spanning tree algorithms**: While implementation details may not be required, understanding that both Kruskal's and Prim's algorithms produce optimal MSTs is essential.
