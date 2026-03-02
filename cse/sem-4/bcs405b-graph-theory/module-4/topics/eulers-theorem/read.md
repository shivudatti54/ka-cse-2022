# Euler's Theorem and Planar Graphs

## Table of Contents

- [Euler's Theorem and Planar Graphs](#eulers-theorem-and-planar-graphs)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Planar Graphs](#planar-graphs)
  - [Euler's Formula (Euler's Theorem)](#eulers-formula-eulers-theorem)
  - [Proof of Euler's Formula](#proof-of-eulers-formula)
  - [Corollaries of Euler's Theorem](#corollaries-of-eulers-theorem)
  - [Non-Planar Graphs](#non-planar-graphs)
  - [Kuratowski's Theorem (Introduction)](#kuratowskis-theorem-introduction)
- [Examples](#examples)
  - [Example 1: Cube Graph](#example-1-cube-graph)
  - [Example 2: Determining Planarity of a Graph](#example-2-determining-planarity-of-a-graph)
  - [Example 3: Using Euler's Formula to Prove Non-Planarity](#example-3-using-eulers-formula-to-prove-non-planarity)
- [Exam Tips](#exam-tips)

## Introduction

Euler's Theorem is one of the most fundamental results in graph theory, establishing a beautiful relationship between the number of vertices, edges, and faces in a connected planar graph. This theorem, discovered by the Swiss mathematician Leonhard Euler in 1752, provides a crucial invariant that helps distinguish planar graphs from non-planar graphs and serves as the foundation for many advanced concepts in graph theory and topology.

The significance of Euler's Theorem extends beyond pure mathematics into practical applications such as circuit design, road network planning, and geographic information systems. Understanding this theorem is essential for any computer science student, as planar graph concepts are directly applied in algorithm design, particularly in computational geometry and network routing problems. This module explores Euler's formula, its proofs, and its applications in determining whether a given graph is planar.

## Key Concepts

### Planar Graphs

A graph is said to be **planar** if it can be drawn in a plane without any of its edges crossing each other. Such a drawing is called a **plane graph**. The faces (or regions) of a plane graph are the areas bounded by edges, including the unbounded outer region. For any connected planar graph drawn without edge crossings, Euler's formula establishes a relationship between the number of vertices (V), edges (E), and faces (F).

**Important Properties of Planar Graphs:**

- A planar graph with V vertices must have E ≤ 3V - 6 for V ≥ 3
- If the graph is triangle-free (contains no cycles of length 3), then E ≤ 2V - 4
- Every planar graph has a vertex of degree at most 5

### Euler's Formula (Euler's Theorem)

For any connected planar graph:
$$V - E + F = 2$$

Where:

- V = Number of vertices
- E = Number of edges
- F = Number of faces (including the outer face)

This theorem holds true for all connected plane graphs and is independent of how the graph is drawn, as long as no edges cross.

### Proof of Euler's Formula

**Proof by Induction on Edges:**

**Base Case:** For a tree (connected graph with no cycles), E = V - 1 and F = 1 (only the outer face). Therefore:
$$V - E + F = V - (V - 1) + 1 = 2$$

**Inductive Step:** Assume Euler's formula holds for a connected graph with k edges. Add one more edge to form a new graph. This edge must connect two existing vertices and either:

1. Creates a new face (if it connects vertices in the same face), increasing F by 1
2. Does not create a new face (if it connects vertices along the boundary), in which case we remove the edge from a cycle

In both cases, the value V - E + F remains unchanged, proving the formula holds for all connected planar graphs.

### Corollaries of Euler's Theorem

**Corollary 1:** For any planar graph with V ≥ 3:
$$E \leq 3V - 6$$

This follows because each face requires at least 3 edges, and each edge borders exactly 2 faces, giving 3F ≤ 2E. Substituting F = 2 - V + E yields the inequality.

**Corollary 2:** For a triangle-free planar graph:
$$E \leq 2V - 4$$

This stricter bound applies when no face is bounded by fewer than 4 edges.

### Non-Planar Graphs

A graph is **non-planar** if it cannot be drawn without edge crossings. Two fundamental non-planar graphs are:

1. **K5 (Complete Graph on 5 vertices):** A graph where every pair of vertices is connected by an edge. K5 has V = 5, E = 10, and applying Euler's formula would require F = 2 - V + E = 2 - 5 + 10 = 7 faces. However, with 10 edges, the minimum edges required would be 3F/2 = 10.5, which is impossible.

2. **K3,3 (Complete Bipartite Graph):** A bipartite graph with two sets of 3 vertices, where every vertex in one set connects to all vertices in the other set. K3,3 has V = 6, E = 9. If planar, it would require F = 2 - 6 + 9 = 5 faces. However, K3,3 is bipartite, so all cycles have even length (minimum 4), requiring 4F/2 = 2F ≤ E, which gives 2F ≤ 9, meaning F ≤ 4.5, contradicting F = 5.

### Kuratowski's Theorem (Introduction)

A graph is non-planar if and only if it contains a subgraph that is a subdivision of K5 or K3,3. This theorem provides a complete characterization of planar graphs and is essential for determining planarity.

## Examples

### Example 1: Cube Graph

Consider the graph of a cube (3D cube projected as a planar graph):

**Given:** A cube has 8 vertices, 12 edges, and 6 faces (including the outer face in the projection)

**Solution:**

- V = 8
- E = 12
- F = 6

**Verification:**
$$V - E + F = 8 - 12 + 6 = 2$$

Euler's formula is satisfied!

### Example 2: Determining Planarity of a Graph

**Problem:** Show that the complete graph K4 is planar.

**Solution:**

K4 has:

- V = 4 vertices
- E = 6 edges (complete graph: n(n-1)/2 = 4×3/2 = 6)

If K4 were planar, applying Euler's formula:
$$F = 2 - V + E = 2 - 4 + 6 = 4$$

With 4 faces and 6 edges, each face requires at least 3 edges, giving minimum 3F/2 = 6 edges. This is exactly satisfied when each edge borders two faces. K4 can indeed be drawn as a plane graph (a triangle with one vertex inside connected to all three outer vertices), proving it is planar.

### Example 3: Using Euler's Formula to Prove Non-Planarity

**Problem:** Prove that K5 is non-planar using Euler's formula.

**Solution:**

For K5:

- V = 5
- E = 10 (complete graph: 5×4/2 = 10)

If K5 were planar, the number of faces would be:
$$F = 2 - V + E = 2 - 5 + 10 = 7$$

Since each face requires at least 3 edges (graph is simple with no multiple edges):
$$3F \leq 2E$$
$$3(7) \leq 2(10)$$
$$21 \leq 20$$

This is a contradiction! Therefore, K5 cannot be planar.

## Exam Tips

1. **Memorize Euler's Formula:** V - E + F = 2 is the most important formula. Remember it applies only to connected planar graphs.

2. **Include the Outer Face:** Always count the unbounded outer region as a face when applying Euler's formula.

3. **Use Corollaries to Check Planarity:** For V ≥ 3, if E > 3V - 6, the graph is definitely non-planar. This is a quick test.

4. **Know K5 and K3,3:** These are the fundamental non-planar graphs. Be prepared to identify them as subdivisions in larger graphs.

5. **Apply Triangle-Free Condition:** Remember the stricter bound E ≤ 2V - 4 when the graph has no 3-cycles.

6. **Proof by Contradiction:** Many exam questions ask you to prove non-planarity using Euler's formula—follow the contradiction approach demonstrated in Example 3.

7. **Drawing Matters:** When checking planarity, first attempt to draw the graph without crossings. A successful drawing proves planarity; a failed attempt doesn't prove non-planarity.

8. **Connection to Kuratowski's Theorem:** Understand that K5 and K3,3 are the "building blocks" of all non-planar graphs according to Kuratowski's characterization.
