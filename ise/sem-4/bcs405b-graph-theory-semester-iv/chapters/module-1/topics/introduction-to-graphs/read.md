# Planar Graphs

## Introduction to Planarity

A **planar graph** is a graph that can be drawn on a plane without any edges crossing. This property is fundamental in graph theory and has significant applications in circuit board design, geographic information systems, and operations research. The study of planar graphs helps us understand the limitations and possibilities of representing complex networks in two dimensions.

Formally, a graph G is planar if there exists a drawing of G in the plane such that no two edges intersect except at their endpoints. Such a drawing is called a **planar embedding** or **plane graph**.

## Key Concepts and Definitions

### Planar Embedding

A planar embedding is a specific drawing of a graph in the plane with no edge crossings. It's important to note that while a graph may be planar, not all drawings of it will be planar embeddings.

### Regions (Faces)

When a planar graph is drawn without crossings, it divides the plane into connected areas called **regions** or **faces**. One of these regions is unbounded and is called the **outer face** or **infinite face**.

```
Example of a planar graph with faces:

    A---B
    |   |
    C---D

Faces:
1. Bounded face: ABCD (internal)
2. Outer face: the area outside the rectangle
```

### Euler's Formula for Planar Graphs

For any connected planar graph with:

- V vertices
- E edges
- F faces

Euler's formula states: **V - E + F = 2**

This formula is fundamental to planar graph theory and has important consequences.

**Example**:
Consider a simple triangle (3 vertices, 3 edges)
V = 3, E = 3, F = 2 (internal face + outer face)
3 - 3 + 2 = 2 ✓

## Necessary Conditions for Planarity

### Edge-Vertex Inequality

For any connected planar graph with V ≥ 3 vertices and E edges:
**E ≤ 3V - 6**

This provides a quick test for non-planarity: if E > 3V - 6, the graph cannot be planar.

### Face-Edge Relationship

Since each face is bounded by at least 3 edges and each edge borders 2 faces:
**2E ≥ 3F**

This inequality, combined with Euler's formula, leads to the edge-vertex inequality above.

## Complete Graphs and Planarity

### K₅ (Complete Graph on 5 Vertices)

K₅ has 5 vertices and 10 edges. Using the edge-vertex inequality:
3V - 6 = 3×5 - 6 = 9
Since 10 > 9, K₅ is non-planar.

### K₃,₃ (Complete Bipartite Graph)

K₃,₃ has 6 vertices and 9 edges. While 9 ≤ 3×6 - 6 = 12, K₃,₃ is still non-planar, showing that the edge-vertex inequality is necessary but not sufficient for planarity.

## Kuratowski's Theorem

**Kuratowski's Theorem**: A graph is planar if and only if it does not contain a subdivision of K₅ or K₃,₃.

This means that any non-planar graph must contain either K₅ or K₃,₃ hidden within its structure, possibly with additional vertices along the edges (subdivisions).

## Wagner's Theorem

**Wagner's Theorem**: A graph is planar if and only if it does not contain K₅ or K₃,₃ as a minor.

A minor of a graph is obtained by contracting edges, deleting edges, or deleting vertices.

## Planarity Testing Algorithms

### Demoucron, Malgrange, and Pertuiset Algorithm

This algorithm provides a systematic way to test planarity by attempting to build a planar embedding face by face.

### Linear Time Algorithms

More efficient algorithms exist that can test planarity in O(V) time, such as:

- Hopcroft-Tarjan algorithm
- Boyer-Myrvold algorithm

## Dual Graphs

For any planar graph G, we can construct its **dual graph** G\* by:

1. Placing a vertex in each face of G
2. Connecting vertices of G\* if their corresponding faces in G share an edge

Properties:

- The dual of the dual is the original graph (for connected planar graphs)
- The number of edges remains the same
- Bridges in G become loops in G\*, and vice versa

## Applications of Planar Graphs

### Circuit Board Design

Planar graphs are essential in printed circuit board (PCB) design, where conductors must not cross without proper insulation layers.

### Geographic Information Systems

Road networks, political boundaries, and other geographic features often form planar graphs when represented on maps.

### Operations Research

Transportation networks and facility location problems frequently use planar graph concepts.

## Special Classes of Planar Graphs

### Outerplanar Graphs

Graphs that can be drawn with all vertices on the outer face and no edge crossings. These are a subset of planar graphs with additional restrictions.

### Maximal Planar Graphs

Planar graphs where no additional edge can be added without violating planarity. In a maximal planar graph, all faces are triangles (including the outer face).

## Table: Comparison of Graph Planarity Properties

| Graph Type | Vertices | Edges | Planar? | Reason                         |
| ---------- | -------- | ----- | ------- | ------------------------------ |
| K₄         | 4        | 6     | Yes     | E = 6 ≤ 3×4 - 6 = 6            |
| K₅         | 5        | 10    | No      | E = 10 > 3×5 - 6 = 9           |
| K₃,₃       | 6        | 9     | No      | Contains K₃,₃ subdivision      |
| Cube Graph | 8        | 12    | Yes     | Can be drawn without crossings |
| K₂,₃       | 5        | 6     | Yes     | E = 6 ≤ 3×5 - 6 = 9            |

## Exam Tips

1. **Remember Euler's Formula**: V - E + F = 2 for connected planar graphs
2. **Use the edge test**: If E > 3V - 6, the graph is definitely non-planar
3. **Look for K₅ and K₃,₃**: These are the fundamental non-planar structures
4. **Practice drawing**: Try to find planar embeddings for various graphs
5. **Understand the limitations**: The edge test is necessary but not sufficient - K₃,₃ has E ≤ 3V - 6 but is non-planar
6. **Consider special cases**: Trees are planar (E = V - 1, which is always ≤ 3V - 6 for V ≥ 1)
