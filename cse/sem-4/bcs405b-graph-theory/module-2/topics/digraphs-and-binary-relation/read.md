# Digraphs and Binary Relations

## Table of Contents

- [Digraphs and Binary Relations](#digraphs-and-binary-relations)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Directed Graphs (Digraphs)](#directed-graphs-digraphs)
  - [Binary Relations on Sets](#binary-relations-on-sets)
  - [Properties of Binary Relations](#properties-of-binary-relations)
  - [Operations on Digraphs](#operations-on-digraphs)
  - [Paths and Connectivity in Digraphs](#paths-and-connectivity-in-digraphs)
  - [Special Relations](#special-relations)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

A directed graph, commonly referred to as a digraph, is a fundamental structure in graph theory where edges have a specific direction. Unlike undirected graphs where edges connect vertices bidirectionally, digraphs assign a unique orientation to each edge, making them essential for modeling asymmetric relationships in various real-world applications. In computer science, digraphs are extensively used to represent dependencies in project scheduling, traffic flow analysis, web page linking structures, and data flow in computer programs.

Binary relations form the mathematical foundation for understanding connections between pairs of elements in a set. When combined with digraphs, binary relations provide a powerful framework for representing and analyzing directed connections. This topic explores the intricate relationship between digraphs and binary relations, examining how mathematical relations can be visualized and manipulated using directed graphs. Understanding these concepts is crucial for CSE students as they form the basis for database theory, algorithm design, and discrete mathematics applications.

## Key Concepts

### Directed Graphs (Digraphs)

A digraph G consists of a finite set V of vertices (or nodes) and a finite set A of arcs (or directed edges). Each arc is an ordered pair (u, v) where u is the initial vertex and v is the terminal vertex. We denote this as G = (V, A) where A ⊆ V × V. The arc (u, v) can be visualized as an arrow pointing from u to v.

**Types of Digraphs:**

- **Simple Digraph**: No loops and no multiple arcs in the same direction
- **Multi-digraph**: May contain multiple arcs between the same pair of vertices
- **Complete Digraph**: Every pair of distinct vertices has arcs in both directions

**In-degree and Out-degree**: For a vertex v in a digraph, the out-degree d⁺(v) is the number of arcs leaving v, while the in-degree d⁻(v) is the number of arcs entering v.

### Binary Relations on Sets

A binary relation R from set A to set B is a subset of the Cartesian product A × B. When A = B, we say R is a binary relation on A. For elements a ∈ A and b ∈ B, we write aRb to indicate that (a, b) ∈ R.

**Representation as Digraph**: Any binary relation R on a finite set A can be represented as a digraph G = (V, A) where V = A and there is an arc from a to b if and only if aRb holds.

### Properties of Binary Relations

For a relation R on a set A:

1. **Reflexive**: ∀a ∈ A, (a, a) ∈ R
2. **Irreflexive**: ∀a ∈ A, (a, a) ∉ R
3. **Symmetric**: ∀a, b ∈ A, if (a, b) ∈ R then (b, a) ∈ R
4. **Asymmetric**: ∀a, b ∈ A, if (a, b) ∈ R then (b, a) ∉ R
5. **Antisymmetric**: ∀a, b ∈ A, if (a, b) ∈ R and (b, a) ∈ R then a = b
6. **Transitive**: ∀a, b, c ∈ A, if (a, b) ∈ R and (b, c) ∈ R then (a, c) ∈ R

### Operations on Digraphs

**Union**: G₁ ∪ G₂ = (V₁ ∪ V₂, A₁ ∪ A₂)
**Intersection**: G₁ ∩ G₂ = (V₁ ∩ V₂, A₁ ∩ A₂)
**Complement**: The complement of G, denoted G̅, has arcs where G has none (excluding loops)

**Matrix Representation**: A digraph with n vertices can be represented by an n × n adjacency matrix M where M[i][j] = 1 if there is an arc from vertex i to vertex j, and 0 otherwise.

### Paths and Connectivity in Digraphs

A path in a digraph is a sequence of vertices where each consecutive pair is connected by an arc. A path is simple if no vertex is repeated. A cycle is a path that starts and ends at the same vertex. A digraph is weakly connected if its underlying undirected graph is connected, and strongly connected if there is a path from every vertex to every other vertex.

### Special Relations

- **Equivalence Relation**: Reflexive, symmetric, and transitive
- **Partial Order**: Reflexive, antisymmetric, and transitive
- **Total Order**: A partial order where every pair of elements is comparable

## Examples

**Example 1: Converting a Relation to Digraph**

Let A = {1, 2, 3} and R = {(1,1), (1,2), (2,3), (3,2)} be a relation on A. Represent R as a digraph and identify its properties.

**Solution:**

- Vertices: V = {1, 2, 3}
- Arcs: A = {(1,1), (1,2), (2,3), (3,2)}

**Property Analysis:**

- Not reflexive: Missing (2,2) and (3,3)
- Not symmetric: (2,3) ∈ R but (3,2) ∈ R (actually symmetric in this case), but check (1,2) ∈ R and (2,1) ∉ R - not symmetric
- Not transitive: (1,2) ∈ R and (2,3) ∈ R, but (1,3) ∉ R

The digraph has a loop at vertex 1, an arc from 1 to 2, from 2 to 3, and from 3 to 2 (forming a cycle between 2 and 3).

**Example 2: Finding Connectivity**

Given the digraph with vertices {a, b, c, d} and arcs {(a,b), (b,c), (c,d), (d,a)}, determine if it is strongly connected.

**Solution:**

- From a: a → b → c → d → a
- From b: b → c → d → a → b
- From c: c → d → a → b → c
- From d: d → a → b → c → d

Since there is a path from every vertex to every other vertex, the digraph is strongly connected. This is actually a directed cycle of length 4.

**Example 3: Matrix Representation and Path Finding**

For the digraph with adjacency matrix:

```
 a b c
a [ 0 1 1 ]
b [ 0 0 1 ]
c [ 1 0 0 ]
```

Find M² and interpret the result.

**Solution:**
M² = M × M:

- Row a: (0×0 + 1×0 + 1×1, 0×1 + 1×0 + 1×0, 0×1 + 1×1 + 1×0) = (1, 0, 1)
- Row b: (0×0 + 0×0 + 1×1, 0×1 + 0×0 + 1×0, 0×1 + 0×1 + 1×0) = (1, 0, 0)
- Row c: (1×0 + 0×0 + 0×1, 1×1 + 0×0 + 0×0, 1×1 + 0×1 + 0×0) = (0, 1, 1)

M² =

```
a [ 1 0 1 ]
b [ 1 0 0 ]
c [ 0 1 1 ]
```

M²[i][j] = number of paths of length 2 from vertex i to vertex j. For example, there is 1 path of length 2 from a to a (a→b→c→a would require b→c and c→a, but c→a exists, so a→c→a).

## Exam Tips

1. **Remember the key difference**: Symmetric relations correspond to undirected graphs, while asymmetric relations correspond to digraphs where (u,v) implies (v,u) does not exist.

2. **Transitive closure**: For exam problems, remember that the transitive closure R\* can be found by computing R, R², R³, ... until no new pairs are added.

3. **Matrix multiplication for paths**: The (i,j) entry of M^k (where M is the adjacency matrix) gives the number of distinct paths of length k from vertex i to vertex j.

4. **Partial orders and Hasse diagrams**: Be able to draw Hasse diagrams for partial orders and identify maximal, minimal, greatest, and least elements.

5. **Connectivity terminology**: Strongly connected requires paths in both directions; weakly connected only requires the underlying undirected graph to be connected.

6. **Relation properties checklist**: When analyzing a relation, check in order: reflexive → symmetric → transitive. Each property has specific conditions to verify.

7. **Composition of relations**: R₁ ∘ R₂ = {(a,c) | ∃b such that (a,b) ∈ R₁ and (b,c) ∈ R₂}. This corresponds to path finding in digraphs.

8. **Matrix representation**: Practice converting between relation notation, digraphs, and adjacency matrices as all three forms commonly appear in university exams.
