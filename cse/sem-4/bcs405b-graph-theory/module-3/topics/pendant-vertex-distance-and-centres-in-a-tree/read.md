# Pendant Vertex, Distance and Centres in a Tree

## Table of Contents

- [Pendant Vertex, Distance and Centres in a Tree](#pendant-vertex-distance-and-centres-in-a-tree)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Pendant Vertex (Leaf Vertex)](#pendant-vertex-leaf-vertex)
  - [Distance in a Tree](#distance-in-a-tree)
  - [Eccentricity of a Vertex](#eccentricity-of-a-vertex)
  - [Radius and Diameter](#radius-and-diameter)
  - [Centre of a Tree](#centre-of-a-tree)
- [Examples](#examples)
  - [Example 1: Identifying Pendant Vertices and Computing Distances](#example-1-identifying-pendant-vertices-and-computing-distances)
  - [Example 2: Finding the Center of a Tree](#example-2-finding-the-center-of-a-tree)
  - [Example 3: Verifying Radius-Diameter Relationship](#example-3-verifying-radius-diameter-relationship)
- [Exam Tips](#exam-tips)

## Introduction

Trees are fundamental structures in graph theory, representing connected acyclic graphs that form the backbone of many algorithmic applications in computer science. A tree with n vertices contains exactly n-1 edges, and between any two vertices, there exists a unique path. This unique path property makes trees particularly important for understanding distance metrics in graphs.

In this module, we explore three interconnected concepts: pendant vertices (leaf nodes), distance measurement between vertices, and the concept of centers in a tree. These concepts are crucial for various applications including network design, hierarchical data structures, and algorithm optimization. Understanding how to identify pendant vertices, compute distances, and determine the center of a tree provides the foundation for solving complex problems in data communications, organizational structures, and computational biology.

The study of tree centers has practical significance in facility location problems, such as determining optimal placements for warehouses or emergency services to minimize maximum distance to all service points. In computer science, tree centers help in designing efficient data structures and load balancing algorithms.

## Key Concepts

### Pendant Vertex (Leaf Vertex)

A **pendant vertex** (also called a leaf vertex or simply a leaf) is a vertex in a tree that has degree 1. In other words, it is connected to exactly one other vertex in the tree. The significance of pendant vertices lies in their role as endpoints or terminals in tree structures.

**Properties of Pendant Vertices:**

- Every tree with at least two vertices has at least two pendant vertices
- Removing a pendant vertex (and its incident edge) from a tree results in a smaller tree
- In a tree with n vertices, if there are p pendant vertices, then the sum of degrees equals 2(n-1)

**Example:** In a simple path graph Pₙ with n vertices, vertices 1 and n are pendant vertices. In a star graph K₁,ₙ₋₁, all vertices except the center are pendant vertices.

### Distance in a Tree

The **distance** between two vertices in a tree is defined as the number of edges in the unique path connecting them. Since trees are acyclic and connected, there is exactly one path between any pair of vertices, making distance computation straightforward.

**Key Definitions:**

- **d(u,v)**: The distance between vertices u and v, equal to the length (number of edges) of the unique path from u to v
- **Distance from a vertex**: The set of distances from a given vertex to all other vertices in the tree

**Properties of Distance:**

- Distance is always a non-negative integer
- d(u,v) = 0 if and only if u = v
- d(u,v) = d(v,u) (symmetric property)
- d(u,v) + d(v,w) ≥ d(u,w) (triangle inequality)

### Eccentricity of a Vertex

The **eccentricity** of a vertex v, denoted by ecc(v), is the maximum distance from v to any other vertex in the tree. It represents the "farness" of a vertex—how far it must travel to reach the farthest vertex in the tree.

**Formal Definition:**
ecc(v) = max{d(v, u) : u ∈ V(T)}

**Example:** In a path graph with 5 vertices (1-2-3-4-5), the eccentricities are:

- ecc(1) = 4 (distance to vertex 5)
- ecc(2) = 3 (distance to vertex 5)
- ecc(3) = 2 (distance to vertices 1 or 5)
- ecc(4) = 3 (distance to vertex 1)
- ecc(5) = 4 (distance to vertex 1)

### Radius and Diameter

**Radius of a Tree:** The radius of a tree T, denoted by rad(T), is the minimum eccentricity among all vertices. It represents the "best" center vertex's distance to the farthest vertex.

rad(T) = min{ecc(v) : v ∈ V(T)}

**Diameter of a Tree:** The diameter of a tree T, denoted by diam(T), is the maximum eccentricity. It represents the longest shortest path between any two vertices in the tree.

diam(T) = max{ecc(v) : v ∈ V(T)} = max{d(u, v) : u, v ∈ V(T)}

**Important Relationship:**
For any tree T: rad(T) ≤ diam(T) ≤ 2 × rad(T)

### Centre of a Tree

The **center** of a tree consists of one or two vertices that have minimum eccentricity. These are the "best" vertices in terms of being centrally located. A vertex v is in the center if ecc(v) = rad(T).

**Key Theorems:**

1. **Theorem 1:** A tree has either one center or two adjacent centers.

2. **Theorem 2:** If a tree has diameter d, then the center(s) can be found by removing pendant vertices from the tree floor-by-floor. After removing floor(d/2) layers of pendant vertices, the remaining vertices form the center.

**Finding the Center Algorithm:**

1. Start with the tree T
2. Find all pendant vertices
3. Remove all pendant vertices simultaneously (this forms one "layer")
4. Repeat with the resulting tree until 1 or 2 vertices remain
5. These remaining vertices are the center(s)

## Examples

### Example 1: Identifying Pendant Vertices and Computing Distances

Consider the tree with vertices {1,2,3,4,5,6} and edges: {(1,2), (2,3), (3,4), (2,5), (5,6)}

**Solution:**

Step 1: Determine degrees of all vertices:

- deg(1) = 1 → Pendant vertex
- deg(2) = 3
- deg(3) = 2
- deg(4) = 1 → Pendant vertex
- deg(5) = 2
- deg(6) = 1 → Pendant vertex

Pendant vertices: 1, 4, 6

Step 2: Compute distances from vertex 2 to all other vertices:

- d(2,1) = 1
- d(2,3) = 1
- d(2,4) = d(2,3) + d(3,4) = 1 + 1 = 2
- d(2,5) = 1
- d(2,6) = d(2,5) + d(5,6) = 1 + 1 = 2

### Example 2: Finding the Center of a Tree

Find the center of the tree with vertices {1,2,3,4,5,6,7} and edges: {(1,2), (2,3), (3,4), (4,5), (3,6), (6,7)}

**Solution:**

The tree structure: 1-2-3-4-5 (a path) and 3-6-7 (a branch)

**Method 1: Using Eccentricity**

Compute distances from each vertex:

From vertex 1: distances to {2,3,4,5,6,7} = {1,2,3,4,3,4} → ecc(1) = 4
From vertex 2: distances to {1,3,4,5,6,7} = {1,1,2,3,2,3} → ecc(2) = 3
From vertex 3: distances to {1,2,4,5,6,7} = {2,1,1,2,1,2} → ecc(3) = 2
From vertex 4: distances to {1,2,3,5,6,7} = {3,2,1,1,2,3} → ecc(4) = 3
From vertex 5: distances to {1,2,3,4,6,7} = {4,3,2,1,3,4} → ecc(5) = 4
From vertex 6: distances to {1,2,3,4,5,7} = {3,2,1,2,2,1} → ecc(6) = 3
From vertex 7: distances to {1,2,3,4,5,6} = {4,3,2,3,3,2} → ecc(7) = 4

Minimum eccentricity = 2 (at vertex 3)
Therefore, center = {3}

rad(T) = 2, diam(T) = 4

**Method 2: Using Pruning Algorithm**

Step 1: Identify pendant vertices: 1, 5, 7
Step 2: Remove them → Remaining vertices: {2,3,4,6}
Step 3: Identify new pendant vertices: 2, 4, 6
Step 4: Remove them → Remaining vertex: {3}
Step 5: Only 1 vertex remains → Center = {3}

### Example 3: Verifying Radius-Diameter Relationship

For a star graph K₁,₆ (1 center vertex connected to 6 leaves):

- The center has eccentricity 1 (to any leaf)
- Each leaf has eccentricity 1 (to the center)
- rad(T) = 1, diam(T) = 1

Relationship: rad(T) = diam(T) = 1 (equality case for star graphs)

For a path graph P₅:

- rad(P₅) = 2, diam(P₅) = 4
- diam = 2 × rad (maximum possible difference)

This verifies: rad(T) ≤ diam(T) ≤ 2 × rad(T)

## Exam Tips

1. **Remember the definition**: A pendant vertex has degree 1. This is frequently tested in university exams.

2. **Minimum pendant vertices**: Every tree with n ≥ 2 has at least 2 pendant vertices. This is a theorem worth memorizing.

3. **Center theorem**: A tree has either 1 center or 2 adjacent centers. If asked to find the center, use the pruning algorithm (removing layers of pendant vertices).

4. **Radius-Diameter inequality**: Always remember rad(T) ≤ diam(T) ≤ 2 × rad(T). This relationship is commonly tested.

5. **Distance computation**: In a tree, always find the unique path between vertices. Count edges, not vertices.

6. **Eccentricity definition**: Remember eccentricity is the maximum distance from a vertex to any other vertex, not the sum or average.

7. **Center location**: The center(s) lie on the middle of the longest path(s) in the tree. For diameter d, the center is at distance floor(d/2) from any endpoint.

8. **Star graph special case**: In a star graph, the center is the single central vertex, and radius equals diameter equals 1.
