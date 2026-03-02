# Operations on Graphs

## Table of Contents

- [Operations on Graphs](#operations-on-graphs)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Union of Two Graphs](#1-union-of-two-graphs)
  - [2. Intersection of Two Graphs](#2-intersection-of-two-graphs)
  - [3. Join of Two Graphs](#3-join-of-two-graphs)
  - [4. Complement of a Graph](#4-complement-of-a-graph)
  - [5. Cartesian Product of Graphs](#5-cartesian-product-of-graphs)
  - [6. Strong Product of Graphs](#6-strong-product-of-graphs)
  - [7. Composition of Graphs](#7-composition-of-graphs)
  - [8. Graph Subtractions](#8-graph-subtractions)
  - [9. Subgraph Concepts](#9-subgraph-concepts)
- [Examples](#examples)
  - [Example 1: Union and Intersection](#example-1-union-and-intersection)
  - [Example 2: Cartesian Product](#example-2-cartesian-product)
  - [Example 3: Complement of a Path](#example-3-complement-of-a-path)
- [Exam Tips](#exam-tips)

## Introduction

Graph operations are fundamental techniques in graph theory that allow us to construct new graphs from existing ones. These operations play a crucial role in solving complex problems in computer science, network design, and discrete mathematics. Understanding graph operations is essential for CSE students as these concepts form the backbone of algorithmic graph theory and have practical applications in social networks, transportation systems, and data structures.

In this module, we will explore various binary and unary operations on graphs, including union, intersection, join, complement, and different products of graphs. These operations enable us to analyze complex graph structures by breaking them down into simpler components or combining simpler graphs to create more complex structures. Mastery of these operations is crucial for problem-solving in graph theory and for understanding advanced topics like graph isomorphism, planarity, and graph algorithms.

## Key Concepts

### 1. Union of Two Graphs

The union of two graphs G₁ = (V₁, E₁) and G₂ = (V₂, E₂), denoted by G₁ ∪ G₂, creates a new graph where:

- The vertex set is V₁ ∪ V₂ (union of vertex sets)
- The edge set is E₁ ∪ E₂ (union of edge sets)

**Important Property**: If G₁ and G₂ are disjoint (have no common vertices), this operation is called the **disjoint union** or **sum** of graphs, denoted by G₁ + G₂.

Example: If G₁ is a triangle (3 vertices, 3 edges) and G₂ is an isolated edge (2 vertices, 1 edge) with no common vertices, their union produces a graph with 5 vertices and 4 edges.

### 2. Intersection of Two Graphs

The intersection of two graphs G₁ = (V₁, E₁) and G₂ = (V₂, E₂), denoted by G₁ ∩ G₂, creates a new graph where:

- The vertex set is V₁ ∩ V₂ (intersection of vertex sets)
- The edge set contains edges that are in both E₁ and E₂

**Condition**: For intersection to be defined, the graphs must share common vertices. If V₁ ∩ V₂ = ∅, the intersection is not defined.

### 3. Join of Two Graphs

The join of two graphs G₁ and G₂, denoted by G₁ + G₂ (different from disjoint union), combines the graphs by connecting every vertex of G₁ to every vertex of G₂.

For G₁ with n₁ vertices and G₂ with n₂ vertices:

- The resulting graph has n₁ + n₂ vertices
- All edges from G₁ and G₂ are preserved
- Additional edges connect every vertex in G₁ to every vertex in G₂

The join operation increases connectivity significantly and is used to construct many important graph classes.

### 4. Complement of a Graph

The complement of a simple graph G, denoted by G̅, is defined such that:

- Two vertices are adjacent in G̅ if and only if they are NOT adjacent in G
- G and G̅ together contain all possible edges among n vertices

**Properties**:

- (G̅)̅ = G (Complement of complement returns the original graph)
- A graph is self-complementary if G ≅ G̅
- The complement of a complete graph Kₙ is an empty graph (n isolated vertices)
- The complement of a cycle Cₙ is a specific graph structure

### 5. Cartesian Product of Graphs

The Cartesian product of two graphs G₁ and G₂, denoted by G₁ × G₂, creates a graph where:

- Vertex set: V(G₁) × V(G₂) (Cartesian product of vertex sets)
- Two vertices (u₁, v₁) and (u₂, v₂) are adjacent if:
- u₁ = u₂ and v₁v₂ ∈ E(G₂), OR
- v₁ = v₂ and u₁u₂ ∈ E(G₁)

**Examples**:

- K₂ × K₂ = C₄ (a cycle of 4 vertices)
- Pₘ × Pₙ creates an m × n grid graph
- The Cartesian product is commutative: G₁ × G₂ ≅ G₂ × G₁

### 6. Strong Product of Graphs

The strong product of graphs G₁ and G₂, denoted by G₁ ⊠ G₂, combines properties of both Cartesian product and join:

- Vertices (u₁, v₁) and (u₂, v₂) are adjacent if:
- They are adjacent in Cartesian product, OR
- Both coordinates are adjacent in respective graphs

This product is more connected than the Cartesian product.

### 7. Composition of Graphs

The composition (or lexicographic product) of G₁ and G₂, denoted by G₁[G₂], creates:

- Vertices: All ordered pairs (u, v) where u ∈ V(G₁) and v ∈ V(G₂)
- Adjacency: (u₁, v₁) is adjacent to (u₂, v₂) if:
- u₁u₂ ∈ E(G₁), OR
- u₁ = u₂ and v₁v₂ ∈ E(G₂)

### 8. Graph Subtractions

**Removing an Edge**: G - e removes edge e while keeping all vertices.

**Removing a Vertex**: G - v removes vertex v and all edges incident to it.

**Edge Addition**: G + e adds a new edge e between non-adjacent vertices.

### 9. Subgraph Concepts

**Subgraph**: A graph H is a subgraph of G if V(H) ⊆ V(G) and E(H) ⊆ E(G).

**Spanning Subgraph**: A subgraph that contains all vertices of the original graph.

**Induced Subgraph**: Created by selecting a subset of vertices and including ALL edges between them that exist in the original graph.

## Examples

### Example 1: Union and Intersection

Given G₁ = (V₁, E₁) where V₁ = {a, b, c, d} and E₁ = {ab, bc, cd, da}
Given G₂ = (V₂, E₂) where V₂ = {c, d, e, f} and E₂ = {cd, de, ef, fc}

**Solution**:

- Union G₁ ∪ G₂: V = {a, b, c, d, e, f}, E = {ab, bc, cd, da, de, ef, fc}
- Intersection G₁ ∩ G₂: V = {c, d}, E = {cd}

### Example 2: Cartesian Product

Find K₂ × K₃.

**Solution**:

- K₂ has vertices {0, 1}, K₃ has vertices {a, b, c}
- Vertices of product: {(0,a), (0,b), (0,c), (1,a), (1,b), (1,c)} — total 6 vertices
- Adjacency rules:
- (0,a) adjacent to (0,b), (0,c) [same first coordinate, adjacent in K₃]
- (0,a) adjacent to (1,a) [same second coordinate, adjacent in K₂]
- Result: This is isomorphic to K₃, K₂ (bipartite structure) — specifically the graph K₃, K₂

### Example 3: Complement of a Path

Find the complement of P₄ (path with 4 vertices).

**Solution**:

- P₄ vertices: v₁, v₂, v₃, v₄ with edges: v₁v₂, v₂v₃, v₃v₄
- In P₄: v₁ is adjacent to v₂ only; v₄ is adjacent to v₃ only; v₂ adjacent to v₁, v₃; v₃ adjacent to v₂, v₄
- In complement, add all missing edges:
- v₁v₃, v₁v₄ (v₁ not adjacent to these in P₄)
- v₂v₄ (v₂ not adjacent to v₄ in P₄)
- Result: The complement of P₄ is P₄ + edge v₂v₄ (adding one diagonal to make it more connected)

## Exam Tips

1. **Understand the difference** between various graph products (Cartesian, strong, composition) — this is a frequent exam question.

2. **Remember properties**: Union is always defined; Intersection requires common vertices; Complement always exists for simple graphs.

3. **For Cartesian product**: Vertices connect horizontally OR vertically, not diagonally — visualize as a grid.

4. **Self-complementary graphs**: Only specific graphs like P₄ and C₅ are self-complementary — remember these examples.

5. **Join operation**: Creates highly connected graphs; the join of two disconnected graphs becomes connected.

6. **Induced vs Spanning Subgraph**: Induced subgraph may have fewer edges; spanning subgraph must use all original vertices.

7. **Notation clarity**: G₁ + G₂ can mean either disjoint union or join depending on context — check the textbook definition.

8. **Vertex removal**: Always removes all incident edges; edge removal preserves vertices.

9. **Cartesian product properties**: The product of two bipartite graphs is always bipartite.

10. **Complement relationship**: For any graph G with n vertices, G and G̅ together contain C(n,2) total edges.
