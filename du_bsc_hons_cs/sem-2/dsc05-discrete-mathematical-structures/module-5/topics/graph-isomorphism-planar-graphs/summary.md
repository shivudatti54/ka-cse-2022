# Graph Isomorphism and Planar Graphs - Summary

## Key Definitions and Concepts

- **Graph Isomorphism:** Two graphs G₁ = (V₁, E₁) and G₂ = (V₂, E₂) are isomorphic if there exists a bijection f: V₁ → V₂ such that {u, v} ∈ E₁ iff {f(u), f(v)} ∈ E₂.

- **Planar Graph:** A graph that can be drawn on a plane without any edges crossing.

- **Plane Embedding:** A specific drawing of a planar graph with no edge crossings.

- **Homeomorphic Graphs:** Graphs that can be obtained from each other by inserting/removing vertices of degree 2.

- **Graph Minor:** A graph obtained by contracting edges of the original graph.

## Important Formulas and Theorems

- **Euler's Formula:** For connected planar graphs: n - m + f = 2

- **Edge Bound for Planar Graphs:** For simple planar graphs with n ≥ 3: m ≤ 3n - 6

- **Triangle-free Bound:** For planar graphs without triangles: m ≤ 2n - 4

- **Kuratowski's Theorem:** A graph is planar iff it contains no subdivision of K₅ or K₃,₃

## Key Points

1. Isomorphic graphs must have identical vertex count, edge count, and degree sequence
2. Graph isomorphism is an equivalence relation (reflexive, symmetric, transitive)
3. Planar graphs always have a vertex of degree at most 5
4. K₅ and K₃,₃ are the fundamental non-planar graphs
5. Adding edges to a non-planar graph cannot make it planar
6. Every planar graph can be colored with at most 4 colors (Four Color Theorem)
7. The dual of a plane graph relates faces to vertices
8. Subdivisions of non-planar graphs are also non-planar

## Common Mistakes to Avoid

1. Assuming graphs with the same degree sequence are always isomorphic (they may not be)
2. Applying Euler's formula to disconnected planar graphs without considering each component separately
3. Forgetting to check the "if and only if" direction when verifying isomorphism conditions
4. Confusing graph subdivisions with subgraphs — Kuratowski's theorem uses subdivisions
5. Using m ≤ 3n - 6 for graphs with loops or multiple edges (formula only applies to simple graphs)

## Revision Tips

1. Practice determining isomorphism by comparing degree sequences of various graph pairs
2. Memorize the exact statement of Euler's formula and its standard proofs
3. Draw K₅ and K₃,₃ repeatedly until you can recognize their subdivisions instantly
4. Solve at least 5-10 problems involving Euler's formula to become comfortable with its applications
5. Create a checklist for isomorphism testing: vertex count → edge count → degree sequence → structural properties