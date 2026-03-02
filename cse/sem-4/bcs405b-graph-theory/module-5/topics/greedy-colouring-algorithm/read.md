# Greedy Colouring Algorithm

## Table of Contents

- [Greedy Colouring Algorithm](#greedy-colouring-algorithm)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Greedy Colouring Algorithm](#basic-greedy-colouring-algorithm)
  - [Vertex Ordering Strategies](#vertex-ordering-strategies)
  - [Welsh-Powell Algorithm](#welsh-powell-algorithm)
  - [Upper Bounds for Chromatic Number](#upper-bounds-for-chromatic-number)
  - [Perfect Graphs and Optimal Colouring](#perfect-graphs-and-optimal-colouring)
- [Examples](#examples)
  - [Example 1: Simple Graph Greedy Colouring](#example-1-simple-graph-greedy-colouring)
  - [Example 2: Welsh-Powell Algorithm on Cycle Graph](#example-2-welsh-powell-algorithm-on-cycle-graph)
  - [Example 3: DSATUR Algorithm](#example-3-dsatur-algorithm)
- [Exam Tips](#exam-tips)

## Introduction

Graph colouring is one of the most fundamental problems in graph theory with numerous practical applications in scheduling, register allocation in compilers, frequency assignment in mobile communications, and map colouring. The greedy colouring algorithm provides a practical approach to colour vertices of a graph using the minimum number of colours possible under certain ordering constraints. Unlike finding the optimal chromatic number (which is NP-hard), the greedy algorithm runs in polynomial time and provides a reasonable colouring solution.

The greedy colouring approach works by processing vertices in a specific order and assigning the smallest available colour that is not used by any adjacent vertex already coloured. The quality of the colouring produced depends heavily on the order in which vertices are processed. This module explores the greedy colouring algorithm, various vertex ordering strategies, and the theoretical bounds on the number of colours required.

## Key Concepts

### Basic Greedy Colouring Algorithm

The greedy colouring algorithm follows a simple principle: process each vertex in a predetermined order and assign the smallest indexed colour that doesn't conflict with previously coloured neighbours.

**Algorithm Steps:**

1. Sort all vertices according to a chosen ordering
2. For each vertex v in order:

- Examine all neighbours already coloured
- Assign the smallest colour index (starting from 1) that is not used by any neighbour
- If all colours 1 to k are used, create a new colour (k+1)

The algorithm uses at most Δ(G) + 1 colours, where Δ(G) is the maximum degree of the graph.

### Vertex Ordering Strategies

The effectiveness of greedy colouring depends significantly on how vertices are ordered. Different ordering strategies produce different colourings:

**1. Natural Ordering:** Process vertices in the order they appear in the adjacency list or input. This is simple but often produces suboptimal colourings.

**2. Descending Degree Ordering (Welsh-Powell):** Sort vertices in non-increasing order of their degrees. Vertices with higher degrees are coloured first, reducing conflicts later.

**3. Smallest Degree Ordering:** Process vertices in non-decreasing order of degrees. This is a greedy approach that sometimes works better in practice.

**4. DSATUR (Degree of Saturation):** At each step, choose the vertex with the highest saturation degree - the number of different colours used on its neighbours. This is a more sophisticated heuristic.

### Welsh-Powell Algorithm

The Welsh-Powell algorithm is a popular greedy colouring method:

1. Sort vertices by degree in descending order
2. Assign colour 1 to the first uncoloured vertex
3. Scan through the remaining vertices, assigning colour 1 to any vertex not adjacent to previously coloured vertices
4. Move to colour 2 and repeat the process
5. Continue until all vertices are coloured

### Upper Bounds for Chromatic Number

The greedy algorithm provides several theoretical bounds:

- **Trivial Bound:** χ(G) ≤ Δ(G) + 1, where χ(G) is the chromatic number and Δ(G) is the maximum degree
- **Greedy Bound:** For any ordering, greedy colouring uses at most 1 + max_i deg_i vertices, where deg_i is the degree in the subgraph induced by vertices from position i onwards
- **Brook's Theorem:** If G is connected, not a complete graph or odd cycle, then χ(G) ≤ Δ(G)

### Perfect Graphs and Optimal Colouring

A graph is **perfect** if for every subgraph, the chromatic number equals the clique number. For perfect graphs, the greedy algorithm with any ordering produces an optimal colouring. Examples include interval graphs, chordal graphs, and bipartite graphs.

## Examples

### Example 1: Simple Graph Greedy Colouring

Consider the following graph:

```
 A
 /|\
 B | C
 |/ \
 D----E
```

**Adjacency List:**

- A: B, C, D
- B: A, D
- C: A, E
- D: A, B, E
- E: C, D

**Solution using Descending Degree Ordering:**

Degrees: A(3), D(3), E(2), C(2), B(2)
Ordering: A, D, E, C, B

1. Colour vertex A with colour 1
2. Vertex D: neighbours (A) uses colour 1 → assign colour 2
3. Vertex E: neighbours (D) uses colour 2 → assign colour 1
4. Vertex C: neighbours (A, E) → A uses 1, E uses 1 → both use colour 1 → assign colour 2
5. Vertex B: neighbours (A, D) → A uses 1, D uses 2 → assign colour 3

**Result:** 3 colours used (A:1, D:2, E:1, C:2, B:3)

### Example 2: Welsh-Powell Algorithm on Cycle Graph

Consider a cycle graph C₅ with 5 vertices labeled 1, 2, 3, 4, 5 in order (1-2-3-4-5-1).

All vertices have degree 2, so any ordering works. Let's apply Welsh-Powell:

1. Start with colour 1: Assign to vertex 1, skip vertex 2 (adjacent to 1), skip vertex 3, skip vertex 4, skip vertex 5 → colour 1 assigned to vertex 1
2. Move to colour 2: Assign to vertex 2 (not adjacent to vertex 1 with colour 1), skip vertex 3 (adjacent to 2), skip vertex 4, skip vertex 5
3. Move to colour 3: Assign to vertex 3 (not adjacent to coloured vertices 1 and 2), skip vertex 4 (adjacent to 3), skip vertex 5
4. Move to colour 4: Assign to vertex 4, skip vertex 5
5. Move to colour 5: Assign to vertex 5

**Result:** 5 colours used! This is because C₅ (odd cycle) requires 3 colours, but this particular ordering was poor. With better ordering (any vertex first, then every other vertex), we get 3 colours.

### Example 3: DSATUR Algorithm

Consider a graph with vertices: W, X, Y, Z where edges are W-X, W-Y, X-Y, X-Z, Y-Z

```
 W
 /|\
 X---Y
 | |
 Z---+
```

**Adjacency:** W(2), X(3), Y(3), Z(2)

**DSATUR Execution:**

1. Initial: All vertices have saturation 0. Choose any vertex with max degree: X (degree 3)

- Colour X with colour 1
- Update: W(sat=1), Y(sat=1), Z(sat=1)

2. All have sat=1, choose any with max degree: W (deg 2)

- W not adjacent to X → colour 1
- Update: Y(sat=1), Z(sat=1)

3. All have sat=1, choose with max degree: Y (deg 3)

- Y adjacent to X(1), W(1) → both use colour 1 → use colour 2
- Update: Z(sat=2)

4. Z has sat=2, colour Z

- Z adjacent to X(1), Y(2) → both colours 1,2 used → use colour 3

**Result:** 3 colours used (X:1, W:1, Y:2, Z:3)

## Exam Tips

1. **Remember the greedy algorithm complexity:** O(V + E) when vertices are processed in a fixed order, making it efficient for large graphs.

2. **Know the theoretical bounds:** χ(G) ≤ Δ(G) + 1 is the fundamental upper bound; Brook's Theorem improves this for most connected graphs.

3. **Vertex ordering matters:** The same graph can require vastly different numbers of colours based on ordering - this is crucial for exam problems.

4. **Perfect graphs guarantee optimality:** For chordal graphs, interval graphs, and bipartite graphs, greedy colouring always produces optimal results.

5. **Welsh-Powell is exam-friendly:** This is the most commonly tested greedy colouring method - know its steps: sort by degree descending, then scan for each colour.

6. **DSATUR uses saturation degree:** The saturation degree is the number of different colours used on adjacent vertices - higher saturation often means more constrained vertices.

7. **Odd cycles and complete graphs are exceptions:** Brook's Theorem states that for complete graphs Kₙ and odd cycles C₂ₙ₊₁, χ(G) = Δ(G) + 1; for other connected graphs, χ(G) ≤ Δ(G).

8. **Understand when greedy fails:** The worst-case for greedy colouring can be as bad as χ(G) = n for a complete graph, but this is rare in practice.

9. **Applications matter:** Be prepared to explain practical applications like register allocation, scheduling, and frequency assignment.

10. **Draw examples carefully:** When solving exam problems, always list vertex degrees first to determine ordering, then systematically apply the colouring rules.
