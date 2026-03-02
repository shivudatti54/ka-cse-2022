# **Geometric Dual of a Planar Graph**

### Introduction

In graph theory, a planar graph is a graph that can be drawn in a plane without any edge crossings. The geometric dual of a planar graph is a planar graph that is constructed from the original graph by replacing each face of the original graph with a vertex, and each edge with an edge between the corresponding vertices of the dual graph.

### Definition

A planar graph `G` has a geometric dual `G^*`, whose vertices are the faces of `G`, and whose edges are the edges of `G`. More formally, for each face `f` of `G`, there is a vertex `v_f` in `G^*`, and for each edge `e` of `G`, there is an edge `e^*` in `G^*` between the vertices `v_f` and `v_g` corresponding to the edges `e` and `f` that `e` bounds.

### Properties of the Geometric Dual

- The dual graph has the same number of vertices as the original graph.
- The dual graph has the same number of edges as the original graph.
- The dual graph is also planar.
- The dual graph is a bijection of the vertices and edges of the original graph.

### Examples

- Consider a cube graph, which has 8 vertices and 12 edges. The dual graph of the cube is a tetrahedral graph, which has 8 vertices and 12 edges.
- Consider a grid graph, which has 16 vertices and 8 edges. The dual graph of the grid is also a grid graph, which has 16 vertices and 8 edges.

### Key Concepts

- **Euler formula**: The Euler formula states that for a planar graph, the number of vertices (V), edges (E), and faces (F) satisfy the equation: V - E + F = 2.
- **Face bounding**: Each edge of the original graph bounds two faces of the original graph.
- **Dual face**: Each face of the original graph corresponds to a vertex of the dual graph.

### Applications

- The geometric dual of a planar graph can be used to solve problems related to planar graph theory, such as finding the maximum area of a planar graph.
- The geometric dual can be used to construct a planar embedding of a non-planar graph.

### Summary

The geometric dual of a planar graph is a planar graph that is constructed from the original graph by replacing each face of the original graph with a vertex, and each edge with an edge between the corresponding vertices of the dual graph. The dual graph has the same number of vertices and edges as the original graph, and it is also planar. The geometric dual can be used to solve problems related to planar graph theory and to construct a planar embedding of a non-planar graph.
