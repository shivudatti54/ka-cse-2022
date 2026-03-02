Of course. Here is a comprehensive educational module on the different representations of planar graphs, tailored for  engineering students.

# Module 4: Representations of Planar Graphs

**Subject:** Graph Theory & Combinatorics (as per  syllabus)
**Semester:** IV

## Introduction

A graph is called **planar** if it can be drawn on a plane without any of its edges crossing. This property is fundamental in applications like circuit board design, network routing, and geographic information systems (GIS). Once we have established that a graph is planar, we can represent it in more structured and useful ways than a simple drawing. This module explores two powerful representations: **planar embeddings** and the **dual graph**.

## Core Concepts and Representations

### 1. Planar Embedding (or Planar Representation)

A planar embedding is a drawing of a planar graph in the plane such that no edges intersect, except at their common endpoints. However, it's more than just a drawing; it's a concrete realization that defines the **cyclic order** of edges around each vertex.

- **Key Idea:** For a given planar graph, there can be multiple, different planar embeddings. Each embedding divides the plane into connected regions called **faces**.
- **The Role of Faces:** A face is a maximal region of the plane surrounded by edges. One of these faces is always the unbounded, infinite outer face.
- **Euler's Formula:** For any connected planar graph with `n` vertices, `e` edges, and `f` faces, the formula `n - e + f = 2` always holds. This is a crucial tool for verifying planarity and analyzing planar graphs.

**Example:**
Consider the simple planar graph `K₄` (the complete graph on 4 vertices). The two images below show two different planar embeddings of the same graph. While they are isomorphic, the cyclic order of edges around the vertices and the _size_ (number of edges bounding) of the faces are different. In one embedding, the outer face is a triangle, and in the other, it is a quadrilateral.

_(Imagine two different drawings of K₄ here: one as a triangle with a central vertex, and another as a square with both diagonals drawn.)_

### 2. The Dual Graph

For any planar embedding, we can define a new graph called its **dual graph**, denoted as `G*`. The dual graph provides a powerful tool for analyzing the original graph's properties, especially its faces.

**Construction of a Dual Graph (`G*`):**

1.  **Place Vertices:** For each face `F` in the original graph `G`, place a vertex `f*` in `G*`.
2.  **Draw Edges:** For each edge `e` in `G`, draw an edge `e*` in `G*` that crosses the edge `e` and connects the vertices `f*` corresponding to the faces on either side of `e`.
    - If an edge `e` lies on the boundary of a single face (e.g., a bridge), the corresponding edge `e*` in the dual will be a self-loop.

**Properties of the Dual Graph:**

- The dual graph `G*` is always planar.
- The number of vertices in `G*` equals the number of faces in `G` (`|V*| = f`).
- The number of edges in `G*` equals the number of edges in `G` (`|E*| = e`).
- The number of faces in `G*` equals the number of vertices in `G` (`|F*| = n`).
- The dual of the dual graph is isomorphic to the original graph (`(G*)* ≅ G`), provided `G` is connected.

**Example:**
Let's construct the dual for a simple graph `G` shaped like a square with one diagonal.

1.  **Original Graph (`G`):** It has 4 vertices, 5 edges, and 3 faces (2 triangular faces, F1 and F2, and 1 unbounded quadrilateral face, F3).
2.  **Dual Graph (`G*`):**
    - Place a vertex inside each of the three faces: `v1*` in F1, `v2*` in F2, and `v3*` in F3.
    - For each edge in `G`:
      - The diagonal edge separates F1 and F2. Draw an edge connecting `v1*` and `v2*`.
      - The top edge of the square separates F1 and F3. Draw an edge connecting `v1*` and `v3*`.
      - The left edge separates F1 and F3. Draw an edge connecting `v1*` and `v3*`.
      - The right edge separates F2 and F3. Draw an edge connecting `v2*` and `v3*`.
      - The bottom edge separates F2 and F3. Draw an edge connecting `v2*` and `v3*`.

The resulting dual graph `G*` is a graph with 3 vertices (`v1*, v2*, v3*`) and 5 edges. Notice that `v1*` and `v3*` are connected by two edges (a multi-edge), and `v2*` and `v3*` are also connected by two edges. This matches the properties: `|V*| = f = 3`, `|E*| = e = 5`.

## Key Points & Summary

| Concept               | Description                                                                                                 | Key Takeaway                                                                                |
| :-------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **Planar Graph**      | A graph that can be drawn on a plane without edge crossings.                                                | The foundation for all representations discussed.                                           |
| **Planar Embedding**  | A specific drawing of a planar graph defining the cyclic order of edges around vertices and creating faces. | A graph can have multiple embeddings. Euler's formula (`n - e + f = 2`) always holds.       |
| **Face**              | A region of the plane bounded by edges.                                                                     | One face is always unbounded (the outer face).                                              |
| **Dual Graph (`G*`)** | A graph constructed from a planar embedding where faces become vertices and edges become connecting edges.  | `\|V*\| = f`, `\|E*\| = e`, `\|F*\| = n`. It is a powerful abstraction for problem-solving. |

Understanding these representations is crucial for advanced topics like graph coloring (the Four Color Theorem is stated in terms of faces/dual graphs) and for practical applications in VLSI design and algorithm development.
