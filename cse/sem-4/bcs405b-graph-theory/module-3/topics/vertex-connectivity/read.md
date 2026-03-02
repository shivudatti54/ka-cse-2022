# Vertex Connectivity

## Table of Contents

- [Vertex Connectivity](#vertex-connectivity)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Vertex Cut (Separating Set)](#vertex-cut-separating-set)
  - [Vertex Connectivity (κ(G))](#vertex-connectivity-g)
  - [Relationship Between Vertex Connectivity and Edge Connectivity](#relationship-between-vertex-connectivity-and-edge-connectivity)
  - [Order of Connectivity](#order-of-connectivity)
  - [Block-Cut Vertex Graph](#block-cut-vertex-graph)
- [Examples](#examples)
  - [Example 1: Finding Vertex Connectivity of a Cycle Graph](#example-1-finding-vertex-connectivity-of-a-cycle-graph)
  - [Example 2: Vertex Connectivity of a Complete Bipartite Graph](#example-2-vertex-connectivity-of-a-complete-bipartite-graph)
  - [Example 3: Application Problem](#example-3-application-problem)
- [Exam Tips](#exam-tips)

## Introduction

Vertex connectivity is a fundamental concept in graph theory that measures the resilience and robustness of a graph. It quantifies the minimum number of vertices that need to be removed to disconnect the graph or reduce it to a trivial graph. This concept is crucial in network design, communication systems, transportation networks, and reliability engineering. Understanding vertex connectivity helps engineers and computer scientists design systems that can withstand failures and ensure continued connectivity even when certain nodes become unavailable.

The study of vertex connectivity bridges the gap between theoretical graph concepts and practical applications. In computer networks, for instance, vertex connectivity helps determine the minimum number of servers or routers that must fail before the network becomes partitioned. Similarly, in transportation networks, it indicates the vulnerability of the system to targeted attacks on specific locations. This topic builds upon earlier concepts of paths, cycles, and connectivity, making it essential for students to have a solid foundation in basic graph theory before delving into this module.

## Key Concepts

### Vertex Cut (Separating Set)

A vertex cut, also known as a separating set, is a set of vertices whose removal from a graph increases the number of connected components or results in a trivial graph. More formally, for a connected graph G, a vertex cut is a set S ⊆ V(G) such that G - S (the graph obtained by removing vertices in S and all edges incident to them) is either disconnected or has only one vertex. The cardinality of a minimum vertex cut is denoted by κ(G).

For example, in a complete graph Kₙ, removing any (n-2) vertices leaves at least two remaining vertices that are still connected (since complete graphs have all possible edges). However, removing (n-1) vertices leaves at most one vertex, which is considered trivial. Therefore, the vertex connectivity of Kₙ is κ(Kₙ) = n-1.

### Vertex Connectivity (κ(G))

The vertex connectivity of a graph G, denoted κ(G) or sometimes κ₁(G), is defined as the minimum number of vertices whose removal disconnects the graph or reduces it to a trivial graph (a single vertex). If G is a complete graph Kₙ, then κ(Kₙ) = n-1. For non-complete graphs, vertex connectivity can range from 0 to n-1.

A graph with vertex connectivity 0 is disconnected. A graph with vertex connectivity 1 is called "articulated" or has a cut vertex—a vertex whose removal disconnects the graph. Graphs with higher vertex connectivity require the removal of more vertices to disconnect them, making them more robust.

### Relationship Between Vertex Connectivity and Edge Connectivity

Vertex connectivity and edge connectivity are closely related concepts. Edge connectivity, denoted λ(G), measures the minimum number of edges whose removal disconnects the graph. Whitney's theorem establishes the fundamental relationship between these two measures:

**Whitney's Theorem:** For any graph G with n vertices (n ≥ 2):
κ(G) ≤ λ(G) ≤ δ(G)

where δ(G) is the minimum degree of the graph. This inequality shows that vertex connectivity provides the most stringent measure of graph resilience, followed by edge connectivity, and finally minimum degree which provides an upper bound.

### Order of Connectivity

The inequality κ(G) ≤ λ(G) ≤ δ(G) defines what is known as the "order of connectivity." This relationship is particularly important because it allows us to establish bounds on vertex connectivity using more easily computable parameters like minimum degree. For regular graphs where all vertices have the same degree, this relationship becomes even more significant in analyzing network robustness.

It's important to note that while κ(G) ≤ λ(G) always holds, the gap between them can be arbitrarily large. For instance, consider a wheel graph or certain bipartite graphs where edge connectivity can be significantly higher than vertex connectivity.

### Block-Cut Vertex Graph

A cut vertex (or articulation point) is a vertex whose removal increases the number of connected components in the graph. The concept of blocks (maximal 2-connected subgraphs) and cut vertices leads to the construction of the block-cut vertex graph, which is a bipartite graph representing the relationship between blocks and cut vertices in the original graph. This construction is particularly useful in algorithm design and in understanding the structural properties of graphs.

## Examples

### Example 1: Finding Vertex Connectivity of a Cycle Graph

**Problem:** Find the vertex connectivity of the cycle graph Cₙ (where n ≥ 3).

**Solution:**

Step 1: Understand the structure of Cₙ
A cycle graph Cₙ has n vertices arranged in a circle, with each vertex connected to its two neighbors, giving exactly n edges.

Step 2: Determine minimum degree
In Cₙ, every vertex has degree 2, so δ(Cₙ) = 2.

Step 3: Find a vertex cut
Removing any single vertex from Cₙ leaves a path graph Pₙ₋₁, which is still connected. Therefore, no single vertex forms a vertex cut.

Step 4: Remove two vertices
Removing two adjacent vertices from Cₙ breaks the cycle into a single path (if adjacent) or two separate paths (if not adjacent). In either case, the graph becomes disconnected or has more than one component. Thus, κ(Cₙ) = 2.

**Verification:** By Whitney's theorem, κ(Cₙ) ≤ λ(Cₙ) ≤ δ(Cₙ) = 2. Since we found that 2 vertices are needed to disconnect Cₙ, we have κ(Cₙ) = 2.

### Example 2: Vertex Connectivity of a Complete Bipartite Graph

**Problem:** Find the vertex connectivity of Kₘ,ₙ where m, n ≥ 2.

**Solution:**

Step 1: Understand Kₘ,ₙ structure
Kₘ,ₙ is a complete bipartite graph with two partite sets containing m and n vertices respectively. Every vertex in one set is connected to all vertices in the other set.

Step 2: Determine minimum degree
The minimum degree δ(Kₘ,ₙ) = min(m, n), since vertices in the smaller partite set have connections only to vertices in the larger set.

Step 3: Find the minimum vertex cut
To disconnect Kₘ,ₙ, we need to separate the two partite sets. Removing all vertices from one partite set (say the smaller one with min(m,n) vertices) makes it impossible to travel between the remaining vertices. Thus, κ(Kₘ,ₙ) = min(m, n).

Step 4: Verify with Whitney's theorem
We have κ(Kₘ,ₙ) = min(m, n) ≤ λ(Kₘ,ₙ) = min(m, n) ≤ δ(Kₘ,ₙ) = min(m, n). All three values are equal in this case.

**Answer:** κ(Kₘ,ₙ) = min(m, n)

### Example 3: Application Problem

**Problem:** A communication network is represented by a graph with 8 vertices. The minimum degree is 4, and the edge connectivity is 4. What are the possible values of vertex connectivity?

**Solution:**

Step 1: Apply Whitney's theorem
For any graph G: κ(G) ≤ λ(G) ≤ δ(G)

Step 2: Substitute given values
We know: λ(G) = 4 and δ(G) = 4

Therefore: κ(G) ≤ 4 ≤ 4

Step 3: Determine possible values
This gives us κ(G) ≤ 4, and since λ(G) = 4, we have κ(G) ≤ 4. The minimum possible value is at least 1 (for connected graphs with cut vertices).

Step 4: Conclusion
The vertex connectivity κ(G) can be 1, 2, 3, or 4. Without additional information about the graph structure, we cannot determine the exact value, but we know it cannot exceed 4.

**Answer:** κ(G) ∈ {1, 2, 3, 4}

## Exam Tips

1. **Remember Whitney's Theorem**: The inequality κ(G) ≤ λ(G) ≤ δ(G) is fundamental and frequently tested in university exams. Always apply this theorem when comparing connectivity measures.

2. **Vertex vs. Edge Connectivity**: Remember that vertex connectivity considers vertex removal while edge connectivity considers edge removal. Vertex cuts are generally more impactful as removing a vertex eliminates all incident edges.

3. **Complete Graphs**: For complete graphs Kₙ, always remember κ(Kₙ) = λ(Kₙ) = δ(Kₙ) = n-1. This is a classic result that appears frequently in exams.

4. **Cycle Graphs**: For cycle graphs Cₙ (n ≥ 3), vertex connectivity equals 2, regardless of n. This is because removing two vertices disconnects the cycle.

5. **Cut Vertices**: A graph has vertex connectivity 1 if and only if it contains a cut vertex. Be able to identify cut vertices in various graph structures.

6. **Minimum Degree as Upper Bound**: Always remember that δ(G) provides an upper bound on vertex connectivity. If you know the minimum degree, you can immediately state that κ(G) ≤ δ(G).

7. **Disconnected Graphs**: For disconnected graphs, vertex connectivity is defined as 0. This is an important edge case that students sometimes overlook.

8. **Graph Families**: Memorize vertex connectivity for common graph families: paths (κ(Pₙ) = 1 for n ≥ 2), cycles (κ(Cₙ) = 2), complete graphs (κ(Kₙ) = n-1), and complete bipartite (κ(Kₘ,ₙ) = min(m,n)).
