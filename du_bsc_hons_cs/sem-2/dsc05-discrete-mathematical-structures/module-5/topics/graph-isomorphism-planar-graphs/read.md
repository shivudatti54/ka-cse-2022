# Graph Isomorphism and Planar Graphs

## Introduction

Graph theory, a fundamental branch of discrete mathematics, provides powerful tools for modeling relationships and structures in computer science, chemistry, social networks, and transportation systems. Two critical concepts in advanced graph theory are **graph isomorphism** and **planar graphs** — topics that form an essential part of the University of Delhi's DSC05 curriculum under Module 5.

**Graph isomorphism** addresses a fundamental question: When can we consider two graphs to be "the same" despite different visual representations? Two graphs are isomorphic if one can be transformed into the other by renaming vertices while preserving adjacency relationships. This concept is crucial in chemical compound analysis (determining if molecules are identical), database schema matching, and pattern recognition.

**Planar graphs** deal with a fascinating geometric constraint: Can a graph be drawn on a plane without any edges crossing? This property has profound implications in circuit design (printed circuit boards), road network planning, and algorithmic efficiency. Determining whether a graph is planar and understanding the characteristics of planar graphs has significant practical applications in VLSI design and geographic information systems.

These concepts together represent sophisticated tools in the graph theorist's arsenal, with direct applications in network design, algorithm optimization, and structural analysis.

## Key Concepts

### Graph Isomorphism

**Definition:** Two graphs G₁ = (V₁, E₁) and G₂ = (V₂, E₂) are said to be **isomorphic** if there exists a bijection f: V₁ → V₂ such that {u, v} ∈ E₁ if and only if {f(u), f(v)} ∈ E₂. The function f is called an **isomorphism**.

**Properties of Isomorphic Graphs:**
- They have the same number of vertices
- They have the same number of edges
- They have the same degree sequence (degrees of vertices when sorted)
- The number of vertices of each degree must match
- They must have the same number of connected components
- They must have the same number of cycles of each length

**Key Invariants (Properties preserved under isomorphism):**
1. Number of vertices |V|
2. Number of edges |E|
3. Degree sequence (multiset of vertex degrees)
4. Number of connected components
5. Number of cycles of various lengths
6. Graph being complete, bipartite, regular, or Eulerian
7. Chromatic number and clique number

**How to Determine Isomorphism:**
1. Compare basic invariants (vertices, edges, degree sequence)
2. Check degree sequences match
3. Look for subgraph structures
4. Try to construct an explicit bijection
5. Use computational algorithms for larger graphs

### Planar Graphs

**Definition:** A graph is called **planar** if it can be drawn in a plane without any edges crossing. Such a drawing is called a **plane embedding** of the graph.

**Important Planar Graph Properties:**

1. **Euler's Formula:** For any connected planar graph with n vertices, m edges, and f faces (including the unbounded outer face):
   **n - m + f = 2**

2. **Corollaries of Euler's Formula:**
   - For simple planar graphs (no loops or multiple edges): m ≤ 3n - 6 (for n ≥ 3)
   - If the graph is also triangle-free: m ≤ 2n - 4
   - Every planar graph has a vertex of degree at most 5

3. **Kuratowski's Theorem:** A graph is planar if and only if it contains no subgraph that is a subdivision of K₅ (complete graph on 5 vertices) or K₃,₃ (complete bipartite graph with 3 vertices on each side).

4. **Homeomorphic Graphs:** Two graphs are homeomorphic if each can be obtained from the other by inserting or removing vertices of degree 2 along edges.

5. **Dual Graphs:** Every plane graph has a **dual graph** where each face becomes a vertex, and edges between faces become edges in the dual.

**Non-Planar Graphs:**
- K₅ (complete graph on 5 vertices) - requires minimum 6 crossings
- K₃,₃ (complete bipartite graph) - requires minimum 6 crossings
- Any graph containing K₅ or K₃,₃ as a minor is non-planar

## Examples

### Example 1: Verifying Graph Isomorphism

**Problem:** Determine whether the following two graphs G₁ and G₂ are isomorphic.

**Graph G₁:** Vertices {a, b, c, d, e}, edges: {ab, bc, cd, de, ea, ac}

**Graph G₂:** Vertices {w, x, y, z, u}, edges: {wx, xy, yz, zu, uw, wy}

**Solution:**

**Step 1: Check basic invariants**
- Both graphs have n = 5 vertices
- Both graphs have m = 6 edges

**Step 2: Check degree sequence**
- In G₁: deg(a)=3, deg(b)=2, deg(c)=3, deg(d)=2, deg(e)=2 → Degree sequence: {3, 3, 2, 2, 2}
- In G₂: deg(w)=3, deg(x)=3, deg(y)=3, deg(z)=2, deg(u)=2 → Degree sequence: {3, 3, 3, 2, 2}

**Step 3: Compare degree sequences**
The degree sequences don't match (G₁ has two vertices of degree 3, G₂ has three vertices of degree 3).

**Step 4: Conclusion**
Since the degree sequences differ, G₁ and G₂ are **NOT isomorphic**.

### Example 2: Applying Euler's Formula

**Problem:** A connected planar graph has 8 vertices and 12 edges. Find the number of faces in a plane embedding.

**Solution:**

**Step 1: Identify known values**
- n = 8 (number of vertices)
- m = 12 (number of edges)
- f = ? (number of faces)

**Step 2: Apply Euler's formula**
For connected planar graphs:
n - m + f = 2

**Step 3: Substitute and solve**
8 - 12 + f = 2
-4 + f = 2
f = 6

**Answer:** The graph has **6 faces** in its plane embedding.

### Example 3: Proving Non-Planarity Using Kuratowski's Theorem

**Problem:** Show that the complete graph K₅ is non-planar.

**Solution:**

**Step 1: Recall Kuratowski's Theorem**
A graph is non-planar if it contains a subgraph that is a subdivision of K₅ or K₃,₃.

**Step 2: Examine K₅**
K₅ is the complete graph with 5 vertices, where every pair of vertices is connected by an edge. It has:
- n = 5 vertices
- m = 10 edges

**Step 3: Apply Euler's formula constraint**
For a simple planar graph with n = 5:
m ≤ 3n - 6 = 3(5) - 6 = 15 - 6 = 9

But K₅ has m = 10 edges, which violates m ≤ 3n - 6.

**Step 4: Alternative proof using Kuratowski**
K₅ itself is a subdivision of K₅ (trivially, since no subdivisions are needed). Since K₅ contains a subgraph isomorphic to K₅, by Kuratowski's Theorem, K₅ is non-planar.

**Conclusion:** K₅ is non-planar.

## Exam Tips

1. **Memorize Euler's formula thoroughly:** n - m + f = 2 is fundamental. Remember it applies only to connected planar graphs; for disconnected graphs, apply it to each component.

2. **Know the non-planar culprits:** K₅ and K₃,₃ are the fundamental non-planar graphs. Any graph containing them as a minor is non-planar.

3. **Check invariants first when solving isomorphism problems:** Before attempting complex bijection construction, verify that vertex count, edge count, and degree sequences match.

4. **Remember the 3n - 6 bound:** For simple planar graphs with n ≥ 3, m ≤ 3n - 6. This provides a quick test for non-planarity.

5. **Practice identifying subdivisions:** When applying Kuratowski's theorem, learn to recognize when a graph contains a subdivision (not just a subgraph) of K₅ or K₃,₃.

6. **Dual graphs are important:** Understand how to construct the dual of a plane graph — faces become vertices, adjacency becomes edges.

7. **State assumptions clearly:** When answering exam questions, explicitly mention whether graphs are simple, connected, or contain multiple edges, as these affect which formulas apply.

8. **Know the handshake lemma connection:** The sum of all vertex degrees equals 2m. This helps in degree sequence calculations for isomorphism problems.