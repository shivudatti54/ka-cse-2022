# Graph Colouring and Chromatic Number

## Table of Contents

- [Graph Colouring and Chromatic Number](#graph-colouring-and-chromatic-number)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Proper Graph Colouring](#proper-graph-colouring)
  - [Chromatic Number](#chromatic-number)
  - [Chromatic Polynomial](#chromatic-polynomial)
  - [Four Colour Theorem](#four-colour-theorem)
  - [Five Colour Theorem](#five-colour-theorem)
  - [Greedy Colouring Algorithm](#greedy-colouring-algorithm)
  - [Brooks' Theorem](#brooks-theorem)
  - [Critical Graphs](#critical-graphs)
- [Examples](#examples)
  - [Example 1: Determining Chromatic Number of C₅ (Cycle with 5 vertices)](#example-1-determining-chromatic-number-of-c-cycle-with-5-vertices)
  - [Example 2: Chromatic Polynomial of a Path Graph](#example-2-chromatic-polynomial-of-a-path-graph)
  - [Example 3: Register Allocation Problem](#example-3-register-allocation-problem)
- [Exam Tips](#exam-tips)

## Introduction

Graph colouring is one of the most fundamental and visually intuitive concepts in graph theory, with widespread applications in computer science, scheduling, register allocation, and map colouring. The fundamental question underlying graph colouring is: "How can we assign colours to the vertices of a graph such that no two adjacent vertices share the same colour?" This simple question leads to deep mathematical results and practical algorithms that form the backbone of many real-world solutions.

The chromatic number of a graph, denoted as χ(G), represents the minimum number of colours required to achieve a proper colouring of the graph. Determining the exact chromatic number for an arbitrary graph is an NP-hard problem, making it computationally challenging. However, various theoretical bounds, algorithms, and special cases provide valuable tools for both theoretical analysis and practical applications. This topic connects pure mathematics with applied computer science, making it essential for any computer science engineer studying at university.

## Key Concepts

### Proper Graph Colouring

A proper colouring of a graph G = (V, E) is an assignment of colours to each vertex in V such that no two adjacent vertices receive the same colour. If a graph can be coloured with k colours, it is said to be k-colourable. The smallest k for which G is k-colourable is the chromatic number χ(G).

For a graph to have a proper colouring:

- Each vertex gets exactly one colour
- If (u, v) is an edge in G, then colour(u) ≠ colour(v)
- The colour set need not be consecutive integers; any k distinct labels work

### Chromatic Number

The chromatic number χ(G) is defined as the minimum number of colours needed to colour the vertices of G properly. Several important properties characterize this fundamental parameter:

- For any graph G, χ(G) ≤ Δ(G) + 1, where Δ(G) is the maximum degree of the graph
- Complete graphs require n colours for Kₙ, so χ(Kₙ) = n
- Bipartite graphs are 2-colourable, so χ(G) = 2 for any non-trivial bipartite graph
- A cycle of even length is 2-colourable, while a cycle of odd length requires 3 colours

### Chromatic Polynomial

The chromatic polynomial P(G, k) counts the number of ways to colour a graph G using exactly k colours. This polynomial provides deep insights into the colouring properties of graphs:

- For a graph with n vertices, P(G, k) is a polynomial of degree n
- P(G, k) = k(k-1)(k-2)...(k-n+1) for an empty graph with n vertices
- P(Kₙ, k) = k(k-1)(k-2)...(k-n+1), the falling factorial

The chromatic polynomial satisfies the deletion-contraction recurrence: P(G, k) = P(G-e, k) - P(G/e, k), where e is any edge, G-e is the graph with e deleted, and G/e is the graph with e contracted.

### Four Colour Theorem

The Four Colour Theorem, proven by Appel and Haken in 1976, states that any planar graph can be coloured with at most four colours such that no two adjacent regions share the same colour. This theorem, originally posed as a conjecture in 1852, was the first major theorem proved using computer assistance.

Key implications:

- Every planar graph is 4-colourable
- Every planar graph is 5-colourable (proved earlier by Kempe)
- The bound of 4 is tight (consider K₄, which is planar and requires 4 colours)

### Five Colour Theorem

The Five Colour Theorem provides a simpler proof that every planar graph can be coloured with at most five colours. This constructive proof uses induction and the fact that every planar graph has a vertex of degree at most 5.

The algorithm proceeds by:

1. Finding a vertex v with degree ≤ 5
2. Removing v, colour the remaining graph recursively
3. Reinsert v and colour it with a colour not used by its neighbours (available since at most 5 neighbours exist)

### Greedy Colouring Algorithm

The greedy colouring algorithm processes vertices sequentially, assigning each vertex the smallest available colour not used by its already-coloured neighbours. The performance depends heavily on the vertex ordering:

```
GREEDY-COLOURING(G):
 for each vertex v in order:
 C = set of colours used by neighbours of v
 assign v the smallest colour not in C
```

The number of colours used by greedy colouring equals Δ(G) + 1 in worst case, but often performs much better for specific orderings (like smallest-degree-first).

### Brooks' Theorem

Brooks' Theorem provides a tight bound on the chromatic number: For any connected graph G that is neither a complete graph nor an odd cycle, χ(G) ≤ Δ(G). This theorem refines the trivial bound χ(G) ≤ Δ(G) + 1 for most graphs.

### Critical Graphs

A graph G is k-chromatic if χ(G) = k. A k-chromatic graph is critically k-chromatic (or k-critical) if every proper subgraph has chromatic number less than k. These graphs are minimal in the sense that removing any vertex reduces the chromatic number.

## Examples

### Example 1: Determining Chromatic Number of C₅ (Cycle with 5 vertices)

**Problem:** Find the chromatic number of a cycle graph with 5 vertices.

**Solution:**

Step 1: Understand the structure

- C₅ is a cycle with 5 vertices and 5 edges
- Each vertex has degree 2

Step 2: Check if 2 colours suffice

- Try alternating colours: assign colour A to vertex 1, colour B to vertex 2
- Continue around the cycle
- After assigning colours to vertices 1, 2, 3, 4, we reach vertex 5
- Vertex 5 is adjacent to vertex 1 (colour A) and vertex 4 (colour B)
- Both colours A and B are used by neighbours, so vertex 5 cannot use either

Step 3: Conclusion

- 2 colours are insufficient
- 3 colours work: use colours A, B, A for the first three vertices, then B, C for vertices 4 and 5
- Therefore, χ(C₅) = 3

### Example 2: Chromatic Polynomial of a Path Graph

**Problem:** Find the chromatic polynomial P(P₃, k) for a path graph with 3 vertices.

**Solution:**

Method 1: Direct counting

- Vertex 1: k choices
- Vertex 2: cannot equal vertex 1, so (k-1) choices
- Vertex 3: cannot equal vertex 2, so (k-1) choices
- Total: k(k-1)²

Method 2: Using the deletion-contraction recurrence

- Let edge e be between vertices 1 and 2
- P(P₃-e, k): This is a graph with two disconnected edges, each edge independent
- Each edge can be coloured in k(k-1) ways, so k(k-1)²
- P(P₃/e, k): Contract edge (1,2), getting a path P₂ with 2 vertices
- P(P₂, k) = k(k-1)
- P(P₃, k) = P(P₃-e, k) - P(P₃/e, k) = k(k-1)² - k(k-1) = k(k-1)[(k-1) - 1] = k(k-1)(k-2)

Wait, let's recalculate:

- P₃-e gives two components: a single edge (vertices 1-2) and a single vertex (vertex 3)
- The edge: k(k-1) ways, the isolated vertex: k ways
- Total: k²(k-1)
- P₃/e gives P₂: k(k-1)
- So P(P₃, k) = k²(k-1) - k(k-1) = k(k-1)(k-1) = k(k-1)² ✓

### Example 3: Register Allocation Problem

**Problem:** A compiler needs to allocate registers for variables in a program. Two variables can share a register if they are not live simultaneously. Given the interference graph where vertices represent variables and edges connect variables that cannot share a register, determine the minimum number of registers needed if the graph is a cycle C₆.

**Solution:**

Step 1: Model the problem

- This is exactly the graph colouring problem
- Each vertex is a variable
- Each edge indicates interference (cannot share register)
- Minimum registers = chromatic number

Step 2: Analyse C₆

- C₆ is an even cycle (6 vertices)
- Even cycles are bipartite
- Therefore, 2-colourable

Step 3: Verify

- Alternate colours around the cycle
- All adjacent vertices have different colours
- No two adjacent vertices share a colour

Step 4: Conclusion

- χ(C₆) = 2
- Minimum 2 registers are sufficient

## Exam Tips

1. **Know the definitions thoroughly**: Remember that χ(G) is the minimum colours needed, while Δ(G) + 1 is an upper bound (trivial bound).

2. **Four Colour Theorem is for planar graphs only**: Don't apply it to non-planar graphs. Remember K₅ and K₃,₃ are non-planar and require 5 and 4 colours respectively.

3. **Odd cycles require 3 colours**: All odd cycles (C₃, C₅, C₇, ...) have chromatic number 3, while even cycles (C₄, C₆, C₈, ...) have chromatic number 2.

4. **Complete bipartite graphs**: Kₘ,ₙ has chromatic number 2 (for m, n ≥ 1), regardless of size.

5. **Brooks' Theorem exceptions**: Remember that Kₙ requires n colours and odd cycles require 3 colours—these are the exceptions to χ(G) ≤ Δ(G).

6. **Chromatic polynomial properties**: The coefficient of kⁿ is always 1, the coefficient of kⁿ⁻¹ is -|E|, and P(G, 0) = 0 for any graph with at least one edge.

7. **Greedy colouring performance**: The worst-case uses Δ(G) + 1 colours, but ordering vertices by decreasing degree often yields better results.

8. **Application problems**: Many exam questions frame colouring problems as scheduling or allocation problems—recognize these as graph colouring in disguise.

9. **Know the relationship**: χ(G) ≥ ω(G), where ω(G) is the clique number (size of largest complete subgraph). This provides a lower bound.

10. **Verify your colouring**: Always check that adjacent vertices have different colours when solving problems.
