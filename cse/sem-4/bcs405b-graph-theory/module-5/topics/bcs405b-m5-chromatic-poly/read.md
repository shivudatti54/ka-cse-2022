# Chromatic Polynomial

## Table of Contents

- [Chromatic Polynomial](#chromatic-polynomial)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Graph Coloring Fundamentals](#graph-coloring-fundamentals)
  - [Definition of Chromatic Polynomial](#definition-of-chromatic-polynomial)
  - [Properties of Chromatic Polynomials](#properties-of-chromatic-polynomials)
  - [Chromatic Polynomials of Special Graphs](#chromatic-polynomials-of-special-graphs)
  - [Whitney's Theorem and Further Properties](#whitneys-theorem-and-further-properties)
- [Examples](#examples)
  - [Example 1: Computing Chromatic Polynomial of a Triangle (K_3)](#example-1-computing-chromatic-polynomial-of-a-triangle-k3)
  - [Example 2: Chromatic Polynomial of a Cycle with 4 Vertices (C_4)](#example-2-chromatic-polynomial-of-a-cycle-with-4-vertices-c4)
  - [Example 3: Using Deletion-Contraction for a Simple Graph](#example-3-using-deletion-contraction-for-a-simple-graph)
- [Exam Tips](#exam-tips)

## Introduction

The chromatic polynomial is a fundamental concept in graph theory that provides a powerful way to study graph colorings. Introduced by George Birkhoff in 1912 as part of his work on the four-color problem, the chromatic polynomial encodes the number of proper vertex colorings of a graph as a function of the number of available colors. This polynomial serves as a bridge between combinatorics and algebra, offering deep insights into the structural properties of graphs.

In the context of graph coloring, we are concerned with assigning colors to vertices such that no two adjacent vertices share the same color. The chromatic polynomial P(G, k) counts exactly how many different proper colorings are possible using k distinct colors. ThisCounting approach transforms a combinatorial problem into an algebraic one, making it amenable to various analytical techniques. The study of chromatic polynomials has applications in scheduling problems, register allocation in compilers, map coloring, and frequency assignment in wireless communications.

The chromatic polynomial represents one of the most elegant connections in mathematics where a discrete combinatorial object (a graph) gives rise to a polynomial with significant algebraic properties. Understanding chromatic polynomials is essential for any computer science student, as it forms the foundation for many algorithms related to graph coloring and has direct applications in optimization problems.

## Key Concepts

### Graph Coloring Fundamentals

A proper coloring of a graph G = (V, E) is an assignment of colors to vertices such that no edge has both endpoints colored with the same color. The minimum number of colors required to properly color a graph is called the chromatic number, denoted χ(G). A graph is k-colorable if it can be properly colored using k colors.

The relationship between proper colorings and the chromatic polynomial is fundamental: if P(G, k) > 0, then G is k-colorable. Conversely, if P(G, k) = 0, then G cannot be colored with k colors. This makes the chromatic polynomial a complete characterization of the coloring possibilities of a graph.

### Definition of Chromatic Polynomial

For a graph G with n vertices, the chromatic polynomial P(G, k) is defined as the function that gives the number of proper k-colorings of G. Formally:

P(G, k) = number of functions f: V(G) → {1, 2, ..., k} such that f(u) ≠ f(v) for every edge uv ∈ E(G)

The chromatic polynomial is a polynomial in k of degree n (the number of vertices) with integer coefficients. This polynomial is one of the most important graph invariants in algebraic graph theory.

### Properties of Chromatic Polynomials

Several fundamental properties distinguish chromatic polynomials from arbitrary polynomials:

**1. Evaluation at k = 0, 1, 2:** P(G, 0) = 0 for any graph with at least one edge (no coloring possible with 0 colors). P(G, 1) = 0 for any graph with at least one edge (adjacent vertices cannot share the same color). P(G, 2) equals the number of ways to 2-color a graph, which is zero if and only if the graph contains an odd cycle.

**2. Sign Alternation:** For a connected graph with n vertices, the coefficients of the chromatic polynomial alternate in sign. The leading coefficient is always 1, and the constant term is 0.

**3. Deletion-Contraction Recurrence:** This is the most fundamental method for computing chromatic polynomials. For any edge e in G:
P(G, k) = P(G - e, k) - P(G/e, k)
where G - e is the graph obtained by deleting edge e, and G/e is the graph obtained by contracting edge e (merging its endpoints).

### Chromatic Polynomials of Special Graphs

Understanding chromatic polynomials for basic graph families provides a foundation for more complex analyses:

**Complete Graph K_n:**
The chromatic polynomial is P(K_n, k) = k(k-1)(k-2)...(k-n+1) = k!/(k-n)!
This follows directly since each vertex must have a different color in a proper coloring of a complete graph.

**Path Graph P_n:**
P(P_n, k) = k(k-1)^(n-1)
The first vertex can be colored in k ways, and each subsequent vertex has k-1 choices (any color except its predecessor).

**Cycle Graph C_n:**
P(C_n, k) = (k-1)^n + (-1)^n(k-1)
This formula demonstrates the interesting behavior of cycles: for odd cycles (n odd), the polynomial is divisible by k, while for even cycles, it is not.

**Complete Bipartite Graph K_m,n:**
P(K_m,n, k) = k^m + k^n - k (for small cases) and more generally involves Stirling numbers. For K_m,n, we color the m vertices in one part with colors from a set of k, and similarly for the n vertices, ensuring no color appears in both parts simultaneously.

**Tree with n vertices:**
P(T_n, k) = k(k-1)^(n-1)
All trees with n vertices share the same chromatic polynomial, reflecting that trees are essentially path-like in their coloring properties.

### Whitney's Theorem and Further Properties

Whitney's theorem states that for a connected graph, the absolute values of the coefficients of the chromatic polynomial equal the number of certain edge subsets. Specifically, the coefficient of k^(n-1) equals -(n-1), and more generally, the coefficients count connected subgraphs with specific properties.

The chromatic polynomial is known to satisfy the deletion-contraction property, making it computable for any finite graph. However, computing chromatic polynomials is generally #P-hard, meaning there is likely no efficient algorithm for arbitrary graphs. This complexity explains why special cases and approximation methods remain important areas of research.

## Examples

### Example 1: Computing Chromatic Polynomial of a Triangle (K_3)

**Problem:** Find the chromatic polynomial of the complete graph K_3 (a triangle) and evaluate it for k = 2 and k = 3.

**Solution:**

Using the formula for complete graphs: P(K_3, k) = k(k-1)(k-2)

For k = 2: P(K_3, 2) = 2 × 1 × 0 = 0
This makes sense - a triangle requires 3 different colors, so 2 colors are insufficient.

For k = 3: P(K_3, 3) = 3 × 2 × 1 = 6
There are exactly 6 proper 3-colorings of a triangle. These correspond to all permutations of the 3 colors assigned to the 3 vertices.

**Verification using deletion-contraction:**
Let G = K_3 with edges e1, e2, e3. Starting with one edge:
P(K_3, k) = P(K_3 - e1, k) - P(K_3/e1, k)
= P(P_3, k) - P(K_2, k)
= k(k-1)^2 - k(k-1)
= k[(k-1)^2 - (k-1)]
= k(k-1)(k-2) ✓

### Example 2: Chromatic Polynomial of a Cycle with 4 Vertices (C_4)

**Problem:** Compute the chromatic polynomial of the cycle graph C_4.

**Solution:**

Using the cycle formula: P(C_4, k) = (k-1)^4 + (-1)^4(k-1) = (k-1)^4 + (k-1)

Expanding: (k-1)^4 + (k-1) = (k^4 - 4k^3 + 6k^2 - 4k + 1) + k - 1 = k^4 - 4k^3 + 6k^2 - 3k

Let's verify for specific values:

- For k = 2: P(C_4, 2) = 2^4 - 4(8) + 6(4) - 3(2) = 16 - 32 + 24 - 6 = 2
  Indeed, a 4-cycle can be 2-colored in exactly 2 ways (alternating colors).

- For k = 3: P(C_4, 3) = 81 - 108 + 54 - 6 = 21
  There are 21 proper 3-colorings of C_4.

### Example 3: Using Deletion-Contraction for a Simple Graph

**Problem:** Find the chromatic polynomial of the graph G shown below (a path of 2 edges with a middle edge, essentially P_3):

Vertices: v1 - v2 - v3 (a path with 3 vertices)

**Solution:**

Method 1 (Direct formula for paths):
P(P_3, k) = k(k-1)^2 = k(k^2 - 2k + 1) = k^3 - 2k^2 + k

Method 2 (Deletion-contraction):
Let G be P_3 with edge e connecting v2-v3:
P(G, k) = P(G - e, k) - P(G/e, k)

- G - e = Two disconnected vertices = P_2 ∪ K_1
  P(G - e, k) = k × k(k-1) = k^2(k-1)
- G/e = After contracting v2-v3, we get two vertices with an edge
  P(G/e, k) = k(k-1)

Therefore: P(G, k) = k^2(k-1) - k(k-1) = k(k-1)(k-1) = k(k-1)^2 ✓

## Exam Tips

1. **Remember the fundamental deletion-contraction recurrence:** P(G, k) = P(G-e, k) - P(G/e, k). This is the key to computing chromatic polynomials for any graph and is frequently tested in university exams.

2. **Know the chromatic polynomials for special graphs:** K_n: k(k-1)...(k-n+1), P_n: k(k-1)^(n-1), C_n: (k-1)^n + (-1)^n(k-1), Trees: k(k-1)^(n-1). These frequently appear in exam problems.

3. **Understand the relationship between chromatic number and polynomial:** If χ(G) > k, then P(G, k) = 0. The smallest positive integer root of the chromatic polynomial equals the chromatic number.

4. **Key property: Coefficient of k^n is 1:** The leading coefficient of any chromatic polynomial is always 1, regardless of the graph structure.

5. **Application of 2-coloring:** A graph is bipartite (2-colorable) if and only if P(G, 2) > 0. For odd cycles, P(C_n, 2) = 0. This is a common exam concept.

6. **Whitney's theorem for connected graphs:** The coefficient of k^(n-1) is -(n-1) for any connected graph with n vertices. This provides a quick check on your computed polynomial.

7. **Practice evaluation problems:** Problems asking you to evaluate P(G, k) for specific k values are common. Remember that P(G, 0) = 0 for any graph with edges, and P(G, 1) = 0 for any graph with at least one edge.

8. **Deletion-contraction strategy:** When computing chromatic polynomials for complex graphs, systematically apply deletion-contraction to reduce to known special cases. Start with edges whose removal simplifies the graph most.

9. **Connection to graph connectivity:** The number of terms in the chromatic polynomial relates to the structure of the graph. More connected subgraphs generally mean more terms.

10. **Time management in exams:** For complex graphs, decide whether to use deletion-contract repeatedly or find an alternative approach. Sometimes recognizing a graph as a modification of a known case saves time.
