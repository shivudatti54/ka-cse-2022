# Four Colour Problem and Five Colour Problem

## Table of Contents

- [Four Colour Problem and Five Colour Problem](#four-colour-problem-and-five-colour-problem)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Planar Graphs](#planar-graphs)
  - [Graph Colouring](#graph-colouring)
  - [Dual Graphs](#dual-graphs)
  - [The Five Colour Theorem (1890)](#the-five-colour-theorem-1890)
  - [The Four Colour Theorem (1976)](#the-four-colour-theorem-1976)
  - [Kempe Chains and Heawood's Argument](#kempe-chains-and-heawoods-argument)
- [Examples](#examples)
  - [Example 1: Five Colour Theorem Proof Application](#example-1-five-colour-theorem-proof-application)
  - [Example 2: Colouring a Simple Planar Map](#example-2-colouring-a-simple-planar-map)
  - [Example 3: Using Euler's Formula](#example-3-using-eulers-formula)
- [Exam Tips](#exam-tips)

## Introduction

The Four Colour Problem is one of the most famous and historically significant problems in graph theory and mathematics overall. It posed the question: can every map on a plane or sphere be coloured using at most four colours such that no two adjacent regions (countries, states, or territories) share the same colour? This seemingly simple question took over a century to solve and led to significant advances in graph theory, topology, and computational mathematics.

The problem was first posed in 1852 by Francis Guthrie, a young mathematics student at University College London, who noticed that four colours seemed sufficient to colour the counties of England. The problem remained unsolved for over 120 years until Appel and Haken provided a proof in 1976, marking the first major mathematical theorem to be proven with substantial computer assistance. The Five Colour Problem, which asks whether five colours are always sufficient for planar maps, was solved earlier in 1890 by Percy Heawood and serves as an important intermediate result that helped mathematicians understand the structure of planar graphs.

## Key Concepts

### Planar Graphs

A planar graph is a graph that can be drawn on a plane without any edges crossing each other. The regions bounded by the edges of a planar graph are called faces. The Four Colour Problem applies specifically to planar graphs, where vertices represent regions and edges connect vertices whose regions share a common boundary. A fundamental theorem states that for any connected planar graph, the relationship V - E + F = 2 holds, where V is the number of vertices, E is the number of edges, and F is the number of faces. This is known as Euler's formula for planar graphs.

### Graph Colouring

Graph colouring involves assigning colours to vertices of a graph such that no two adjacent vertices share the same colour. The minimum number of colours required to colour a graph is called its chromatic number. For planar graphs, the Four Colour Theorem states that the chromatic number is at most 4, while the Five Colour Theorem guarantees a chromatic number of at most 5.

### Dual Graphs

The relationship between map colouring and graph colouring is established through dual graphs. In a map, regions become vertices, and two vertices are connected by an edge if their corresponding regions share a border. This dual graph is always planar, and colouring the regions of the original map is equivalent to colouring the vertices of its dual graph.

### The Five Colour Theorem (1890)

Percy Heawood proved that any planar graph can be coloured with five or fewer colours. His proof used a reduction argument based on the fact that every planar graph contains a vertex of degree 5 or less. The proof technique involves assuming a minimal counterexample exists and then showing that such a graph must contain a vertex of degree at most 5, which leads to a contradiction. This proof is constructive and can be implemented as a colouring algorithm.

### The Four Colour Theorem (1976)

Kenneth Appel and Wolfgang Haken proved that four colours are sufficient for any planar graph. Their proof was revolutionary because it was the first major mathematical proof to rely heavily on computer computation. They identified 1,936 reducible configurations and showed that any minimal counterexample to the four-colour conjecture must contain one of these configurations. By exhaustive computer checking, they proved all these configurations were reducible, thereby establishing the theorem. The proof was later simplified but still requires computer verification.

### Kempe Chains and Heawood's Argument

A key technique in colouring proofs is the use of Kempe chains. Given a vertex v coloured with colour A, a Kempe chain is a maximal connected subgraph containing vertices coloured only with colours A and B. Heawood's five-colour proof uses these chains to show that if a planar graph has a vertex of degree 5, we can reduce the colouring problem to a smaller graph, eventually reaching a contradiction unless five colours are available.

## Examples

### Example 1: Five Colour Theorem Proof Application

**Problem**: Show that the graph with vertices {A, B, C, D, E} and edges AB, AC, AD, AE, BC, BD, BE, CD, CE, DE (a complete graph K₅) can be coloured with 5 colours.

**Solution**: K₅ has 5 vertices and each vertex is adjacent to all other 4 vertices. According to the definition of graph colouring, adjacent vertices must have different colours. Therefore, we need 5 different colours, one for each vertex. This demonstrates that K₅ is not planar (it requires 5 colours, which is more than what planar graphs need), and in fact, K₅ cannot be embedded in the plane without edge crossings.

### Example 2: Colouring a Simple Planar Map

**Problem**: A map consists of four regions where each region touches at least one other region. Prove that four colours are sufficient.

**Solution**: Consider the planar graph representation where each region is a vertex and edges connect adjacent regions. In the worst case, this forms a complete graph K₄ where each region touches all other three. K₄ is planar and requires exactly 4 colours (each vertex needs a different colour from all others it touches). Since no region touches all other three in most practical maps, we can often colour with fewer colours. The Four Colour Theorem guarantees that four colours will always be sufficient regardless of the specific arrangement.

### Example 3: Using Euler's Formula

**Problem**: Prove that every planar graph contains a vertex of degree at most 5.

**Solution**: Using Euler's formula V - E + F = 2 for connected planar graphs, and noting that each face has at least 3 edges and each edge is incident to 2 faces, we have 2E ≥ 3F. Substituting F = 2 - V + E into this inequality gives 2E ≥ 3(2 - V + E), which simplifies to E ≤ 3V - 6. If every vertex had degree at least 6, then the sum of degrees would be at least 6V, which equals 2E. Therefore, 2E ≥ 6V, giving E ≥ 3V, which contradicts E ≤ 3V - 6 for V ≥ 3. Hence, at least one vertex must have degree at most 5.

## Exam Tips

1. **Remember the key difference**: The Five Colour Theorem was proven analytically in 1890 by Heawood, while the Four Colour Theorem required computer assistance in 1976 by Appel and Haken.

2. **Euler's formula application**: For university exams, frequently remember that V - E + F = 2 for connected planar graphs, and use this to derive bounds on edges (E ≤ 3V - 6 for simple planar graphs).

3. **Vertex degree proof**: The proof that every planar graph has a vertex of degree at most 5 is crucial and frequently tested. Know the contradiction approach using edge counting.

4. **Dual graph concept**: Understand that map colouring problems transform into vertex colouring problems in dual graphs, and the dual of a planar graph is always planar.

5. **Historical context**: Remember Francis Guthrie (1852), Percy Heawood (1890), and Appel-Haken (1976) as key figures in this problem's history.

6. **Kuratowski's Theorem connection**: Remember that K₅ and K₃,₃ are non-planar, and a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃.

7. **Four vs Five colours**: The Five Colour Theorem provides an upper bound of 5, while the Four Colour Theorem improves this to 4. Know that K₄ requires exactly 4 colours, proving that 4 is the tight bound.
