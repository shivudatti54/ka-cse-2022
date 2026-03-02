# Kuratowski's Theorem

## Table of Contents

- [Kuratowski's Theorem](#kuratowskis-theorem)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Planar Graphs](#planar-graphs)
  - [Homeomorphic Graphs](#homeomorphic-graphs)
  - [The Complete Graph K5](#the-complete-graph-k5)
  - [The Complete Bipartite Graph K3,3](#the-complete-bipartite-graph-k33)
  - [Subdivisions and Graph Minors](#subdivisions-and-graph-minors)
  - [Euler's Formula](#eulers-formula)
- [Kuratowski's Theorem Statement](#kuratowskis-theorem-statement)
- [Examples](#examples)
  - [Example 1: Testing the Petersen Graph](#example-1-testing-the-petersen-graph)
  - [Example 2: Verifying Planarity of a Grid Graph](#example-2-verifying-planarity-of-a-grid-graph)
  - [Example 3: Application to Utility Problem](#example-3-application-to-utility-problem)
- [Exam Tips](#exam-tips)

## Introduction

Kuratowski's Theorem is one of the most fundamental results in graph theory, providing a complete characterization of planar graphs. Published by the Polish mathematician Kazimierz Kuratowski in 1930, this theorem addresses the fundamental question: "When is a graph planar?" In simpler terms, the theorem tells us exactly what makes a graph capable of being drawn on a plane without any of its edges crossing. This characterization is not just theoretically significant but also has practical applications in circuit design, road network planning, and geographical mapping systems.

Before diving into the theorem itself, it is essential to understand that planar graphs form the foundation of many real-world applications. For instance, when designing printed circuit boards (PCBs), engineers must ensure that the electrical connections can be made without crossing, which is essentially a planar graph problem. Similarly, subway or metro maps are designed to be visually planar even if the actual geographical layout is three-dimensional. Kuratowski's Theorem provides the mathematical toolkit to verify planarity and understand the structural barriers that prevent a graph from being planar.

## Key Concepts

### Planar Graphs

A graph is said to be **planar** if it can be drawn in a plane such that no two edges intersect except at their common endpoints. This drawing is called a **plane graph**. It is crucial to note that a graph may have a non-planar appearance in one particular drawing but still be planar if there exists some other drawing where edges do not cross. For example, a square with its two diagonals appears to have crossing edges when drawn in the standard manner, but by repositioning one diagonal to the outside, we can draw it without crossings—making it planar.

The concept of planarity extends to graphs embedded on other surfaces as well, but for this module, we focus exclusively on the plane. A **plane graph** is a planar graph together with a specific embedding (drawing) on the plane. Every planar graph can be represented as a plane graph.

### Homeomorphic Graphs

Two graphs are considered **homeomorphic** if they can both be obtained from the same graph by repeatedly subdividing edges. More formally, a graph G is homeomorphic to graph H if there exists a graph that is isomorphic to subdivisions of both G and H. This concept is particularly important in Kuratowski's Theorem because the theorem does not merely state that certain specific graphs are non-planar—it states that any non-planar graph must contain a subgraph that is homeomorphic to one of these fundamental non-planar graphs.

When we **subdivide** an edge, we replace it with a path of length two by inserting a new vertex in the middle. This operation preserves the essential topological structure of the graph while adding more vertices. Homeomorphism essentially means "same shape" in topological terms, capturing the idea that two graphs have the same fundamental structure regardless of how many times edges have been subdivided.

### The Complete Graph K5

The complete graph K5 is a graph with 5 vertices where every pair of vertices is connected by an edge. This graph has exactly 10 edges. K5 is a fundamental example of a non-planar graph. No matter how you attempt to draw K5 on a plane, you will always have at least one crossing. This is because K5 has too many edges relative to its vertices to fit in the plane without crossings.

The proof that K5 is non-planar can be understood intuitively: with 5 vertices, there are 10 possible edges. In a plane graph, if we apply Euler's formula (which we'll discuss shortly), we can derive bounds on the number of edges relative to vertices. For a connected planar graph with n ≥ 3 vertices and m edges, we have m ≤ 3n - 6. For n = 5, this gives m ≤ 9, but K5 has m = 10 edges, violating this inequality.

### The Complete Bipartite Graph K3,3

The complete bipartite graph K3,3 consists of two sets of 3 vertices each, with every vertex in one set connected to every vertex in the other set. This graph has 6 vertices and 9 edges. K3,3 is another fundamental non-planar graph, and interestingly, it is not homeomorphic to K5—they represent two distinct "families" of non-planarity.

K3,3 is particularly important because it models the classic utility problem: three houses (on one side) and three utilities (gas, water, electricity on the other side)—can each house be connected to each utility without any lines crossing? The answer is no, and K3,3 being non-planar mathematically proves this.

### Subdivisions and Graph Minors

A **subdivision** of an edge involves replacing an edge (u, v) with two edges (u, w) and (w, v), where w is a new vertex. A graph that can be obtained from another graph through a sequence of edge subdivisions is called a **subdivision** of the original graph. The terms "subdivision" and "homeomorphic" are closely related but not identical—a graph G is a subdivision of H if G can be obtained by subdividing edges of H.

A **minor** of a graph is a graph that can be obtained by deleting edges and vertices and by contracting edges. The concept of graph minors is more general than subdivisions and plays a significant role in more advanced graph theory, including Robertson and Seymour's famous Graph Minor Theorem.

### Euler's Formula

While not part of Kuratowski's Theorem directly, Euler's Formula is essential for understanding why certain graphs are non-planar. For any connected planar graph with n vertices, m edges, and f faces (including the outer face), we have:

**n - m + f = 2**

From this formula, we derive the important inequality m ≤ 3n - 6 for planar graphs without loops or multiple edges (simple planar graphs). This inequality provides a quick test: if a simple graph has more than 3n - 6 edges, it must be non-planar.

## Kuratowski's Theorem Statement

**Kuratowski's Theorem (1930):** A graph is planar if and only if it does not contain a subgraph that is homeomorphic to either K5 or K3,3.

This elegant statement provides a complete characterization: a graph is planar exactly when it avoids containing any graph that is a subdivision of K5 or K3,3. In other words, if you can find a part of your graph that looks like K5 or K3,3 (possibly with extra vertices along the edges), then your graph cannot be planar. Conversely, if no such subgraph exists, the graph must be planar.

The theorem is often stated equivalently in terms of graph minors: a graph is planar if and only if it does not contain K5 or K3,3 as a minor. This minor-based formulation is sometimes easier to apply in practice because edge contraction is easier to check than finding subdivisions.

## Examples

### Example 1: Testing the Petersen Graph

The Petersen graph is a well-known non-planar graph with 10 vertices and 15 edges. It is often used as a counterexample in graph theory. To prove it is non-planar using Kuratowski's Theorem, we need to find a subgraph homeomorphic to K5 or K3,3.

Consider the outer pentagon vertices and the inner 5-star of the standard drawing. By selecting appropriate vertices and understanding the connections, we can identify a subgraph homeomorphic to K3,3. Specifically, we can choose three vertices from the outer cycle and three from the inner star configuration, and show that the connections between them form a K3,3 subdivision. Since K3,3 is non-planar and the Petersen graph contains a K3,3-subdivision as a subgraph, by Kuratowski's Theorem, the Petersen graph is non-planar.

### Example 2: Verifying Planarity of a Grid Graph

Consider a 3×3 grid graph (9 vertices arranged in 3 rows and 3 columns, with edges between adjacent vertices horizontally and vertically). This is essentially the planar graph formed by the squares of a chessboard.

To verify planarity using Kuratowski's Theorem, we check whether it contains any subgraph homeomorphic to K5 or K3,3. The grid graph is sparse (it has exactly 12 edges for 9 vertices, satisfying m ≤ 3n - 6 = 21). More importantly, it is clearly drawable as a grid without crossings. We cannot find any subgraph that resembles K5 or K3,3—the maximum "complete" structure we can find is small and local. Therefore, by Kuratowski's Theorem, the 3×3 grid is planar, which we already know from its straightforward embedding.

### Example 3: Application to Utility Problem

Recall the classic problem: three houses need to be connected to three utilities (gas, water, electricity) without any connections crossing. This is equivalent to asking whether K3,3 is planar.

Using Kuratowski's Theorem, we know K3,3 is non-planar because it is one of the two fundamental non-planar graphs. The utility problem asks exactly whether K3,3 can be drawn without crossings—the answer is no. If we try to modify the problem by allowing one utility to remain unconnected, we get a graph with 5 edges (5 connections) from each house to two utilities, which is planar because it does not contain K3,3 as a subgraph. This demonstrates how Kuratowski's Theorem helps analyze practical resource allocation problems.

## Exam Tips

1. **Memorize the two fundamental non-planar graphs:** K5 (complete graph on 5 vertices) and K3,3 (complete bipartite graph with 3 vertices on each side) are the ONLY graphs you need to remember as the basis for non-planarity.

2. **Understand the difference between "subdivision" and "homeomorphic":** A subdivision inserts new vertices along edges, while homeomorphic means one graph can be obtained from another through subdivisions (possibly including vertex removal).

3. **Apply the inequality m ≤ 3n - 6 as a quick test:** For simple planar graphs, if m > 3n - 6, the graph must be non-planar. This is a quick elimination method in exams.

4. **Know the statement in both forms:** Kuratowski's Theorem can be stated as "no subgraph homeomorphic to K5 or K3,3" OR "no minor of K5 or K3,3." Both are valid characterizations.

5. **Euler's formula is your friend:** Remember n - m + f = 2 for connected planar graphs. This helps derive edge bounds and can help identify potential non-planarity quickly.

6. **Practice identifying K5 and K3,3 in larger graphs:** When given a complex graph, look for 5 vertices with all pairwise connections (K5 pattern) or two sets of 3 vertices with all cross-connections (K3,3 pattern).

7. **Note that K5 and K3,3 are not homeomorphic to each other:** They represent two distinct "types" of non-planarity. This is important when analyzing a graph—you may need to check for both patterns.
