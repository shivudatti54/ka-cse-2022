# Planar Graphs

## Table of Contents

- [Planar Graphs](#planar-graphs)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Basic Properties](#definition-and-basic-properties)
  - [Maximal Planar Graphs](#maximal-planar-graphs)
  - [Outer Planar Graphs](#outer-planar-graphs)
  - [Kuratowski's Theorem](#kuratowskis-theorem)
  - [Dual Graphs](#dual-graphs)
  - [Four Color Theorem and Five Color Theorem](#four-color-theorem-and-five-color-theorem)
- [Examples](#examples)
  - [Example 1: Verifying Euler's Formula](#example-1-verifying-eulers-formula)
  - [Example 2: Proving Non-Planarity Using Euler's Formula](#example-2-proving-non-planarity-using-eulers-formula)
  - [Example 3: Application of Kuratowski's Theorem](#example-3-application-of-kuratowskis-theorem)
- [Exam Tips](#exam-tips)

## Introduction

A planar graph is a fundamental concept in graph theory that deals with the geometric representation of graphs on a plane without edge crossings. A graph is said to be planar if it can be drawn in such a way that no two edges intersect except at their common vertices. This concept was first studied by Euler in the 18th century and has significant applications in various fields including circuit design, map coloring, urban planning, and network layout.

The study of planar graphs is crucial because it deals with problems that appear in real-world scenarios where minimizing crossings is essential. For instance, in printed circuit boards (PCBs), we need to connect components without allowing wires to cross each other. Similarly, in transportation networks and road systems, we want to avoid intersections that could cause congestion or accidents. Understanding planar graphs helps computer scientists optimize layout algorithms and solve complex routing problems efficiently.

This module covers the essential properties of planar graphs, Euler's formula and its applications, important theorems like Kuratowski's theorem and the Four Color Theorem, and various characterizations of planar graphs. These concepts are vital for the university examination as they form a significant portion of the Graph Theory syllabus.

## Key Concepts

### Definition and Basic Properties

A graph G = (V, E) is called planar if it can be embedded in the plane without any two edges crossing. Such an embedding is called a planar embedding. The regions bounded by the edges in a planar embedding are called faces. A planar graph divides the plane into several connected regions, with one region being the unbounded (outer) region.

**Theorem (Euler's Formula):** For any connected planar graph with v vertices, e edges, and r regions (faces), we have:
**v - e + r = 2**

This is one of the most important results in graph theory and serves as the foundation for many properties of planar graphs. The formula was discovered by Leonhard Euler in 1750.

**Generalized Euler's Formula:** For a planar graph with c connected components:
**v - e + r = c + 1**

### Maximal Planar Graphs

A planar graph is called maximal planar (or triangulated) if it is planar and adding any edge (without adding vertices) destroys planarity. In a maximal planar graph with v ≥ 3 vertices, every face (including the outer face) is bounded by exactly 3 edges, meaning it is a triangulation. For a maximal planar graph with v vertices (v ≥ 3) and e edges:
**e = 3v - 6**

This formula is derived from Euler's formula. Since each of the r faces is bounded by 3 edges and each edge bounds 2 faces, we have 3r = 2e, or r = 2e/3. Substituting in Euler's formula gives us e = 3v - 6.

### Outer Planar Graphs

A graph is outer planar if it can be embedded in the plane such that all vertices belong to the outer face. These graphs are subgraphs of maximal planar graphs and have the property that they do not contain K4 or K2,3 as homeomorphic subgraphs.

For a connected outer planar graph with v ≥ 2 vertices and e edges:
**e ≤ 2v - 3**

### Kuratowski's Theorem

This theorem provides a complete characterization of planar graphs. A graph is planar if and only if it does not contain a subdivision of K5 (the complete graph on 5 vertices) or K3,3 (the complete bipartite graph with 3 vertices in each part).

A subdivision of a graph is obtained by replacing edges with paths (adding vertices of degree 2 along edges). K5 requires 10 edges, and when drawn in the plane, at least 5 edges must cross. Similarly, K3,3 with its 9 edges cannot be embedded without crossings.

### Dual Graphs

Given a planar embedding of a connected planar graph G, we can construct its dual graph G\* as follows:

- Create a vertex in G\* for each face of G
- For each edge e of G, create an edge in G\* between the faces adjacent to e
- If an edge is incident to the same face on both sides, create a loop in G\*

The dual of a planar graph is also planar. The concept of dual graphs is particularly useful in solving problems related to map coloring and network flows.

### Four Color Theorem and Five Color Theorem

The Four Color Theorem states that any planar graph can be properly colored using at most four colors. This famous theorem was proven in 1976 by Appel and Haken using computer assistance. The Five Color Theorem, proven earlier by Kempe in 1879, states that any planar graph can be colored with at most five colors and provides a constructive proof.

A proper coloring is one where no two adjacent vertices share the same color.

## Examples

### Example 1: Verifying Euler's Formula

**Problem:** Consider a planar graph with v = 5 vertices arranged as a pentagon with all diagonals drawn. Count the vertices, edges, and faces, and verify Euler's formula.

**Solution:**

**Step 1: Count vertices (v)**
The pentagon has 5 vertices (the vertices of the pentagon). When we draw all diagonals, we create additional vertices where diagonals intersect inside the pentagon. However, for a simple planar graph, we consider the planar embedding where diagonals don't all intersect at a single point. Let us consider a simpler case where we draw a pentagon and two non-intersecting diagonals.

For the pentagon with two non-crossing diagonals:

- v = 5 (outer vertices)

**Step 2: Count edges (e)**

- 5 edges form the pentagon
- 2 diagonals
- Total: e = 7

**Step 3: Count faces (r)**
The graph divides the plane into:

- 3 triangular regions inside
- 1 outer region (unbounded)
- Total: r = 4

**Step 4: Verify Euler's Formula**
v - e + r = 5 - 7 + 4 = 2 ✓

### Example 2: Proving Non-Planarity Using Euler's Formula

**Problem:** Show that K5 (complete graph on 5 vertices) is non-planar.

**Solution:**

**Step 1: Assume K5 is planar**
For a planar graph with v vertices and e edges, we have the inequality e ≤ 3v - 6 (for v ≥ 3).

**Step 2: Calculate for K5**

- v = 5 vertices
- e = C(5,2) = 10 edges

**Step 3: Check the inequality**
3v - 6 = 3(5) - 6 = 15 - 6 = 9

Here, e = 10 > 9, which violates the inequality for planar graphs.

**Step 4: Conclusion**
Since 10 > 9, K5 cannot satisfy Euler's formula for planar graphs. Therefore, K5 is non-planar.

### Example 3: Application of Kuratowski's Theorem

**Problem:** Determine whether the graph shown below is planar or not:

```
 a --- b
 | X |
 | / \ |
 d c
```

**Solution:**

**Step 1: Identify the graph structure**
This graph is essentially K5 with one missing edge (between a and c, or b and d).

**Step 2: Apply Kuratowski's Theorem**
We need to check if this graph contains a subdivision of K5 or K3,3.

**Step 3: Analyze the subgraph**
The graph has 5 vertices. Looking at the structure, all 5 vertices are connected to each other except for one missing edge. The vertex in the center with degree 4 connects to all four outer vertices.

**Step 4: Determine planarity**
Since this graph is homeomorphic to K5 (it can be obtained from K5 by removing one edge, which is equivalent to edge subdivision), and K5 is non-planar, this graph is also non-planar.

According to Kuratowski's theorem, any graph containing a subdivision of K5 or K3,3 is non-planar. Therefore, this graph is non-planar.

## Exam Tips

1. **Memorize Euler's Formula:** v - e + r = 2 for connected planar graphs. This is the most frequently tested concept. Always start exam problems by identifying v, e, and r.

2. **Know the Key Inequality:** For any planar graph with v ≥ 3, e ≤ 3v - 6. This is derived from Euler's formula and is used to prove non-planarity.

3. **Kuratowski's Theorem:** Remember that K5 and K3,3 are the fundamental non-planar graphs. If a graph contains a subdivision of either, it is non-planar.

4. **Maximal Planar Graph Properties:** Remember that maximal planar graphs have exactly 3v - 6 edges and all faces are triangles (v ≥ 3).

5. **Outer Planar Graphs:** For outer planar graphs, e ≤ 2v - 3. These graphs are important and often confused with regular planar graphs.

6. **Four Color Theorem:** Know that any planar graph can be colored with at most 4 colors. This is a classic exam topic.

7. **Dual Graphs:** Understand how to construct a dual from a planar embedding. The dual of a plane graph is also a plane graph.

8. **Drawing Strategies:** When checking planarity, try to redraw the graph in different ways. Sometimes re-layout can reveal a planar embedding.

9. **Application of Euler's Formula:** When given a planar graph, use Euler's formula to find missing information. For example, if you know v and e, you can find r = e - v + 2.

10. **Prove Non-Planarity:** Use either the edge count inequality (e > 3v - 6) or Kuratowski's theorem. Both methods are commonly tested.
