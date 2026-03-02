# Graph Colouring and Chromatic Number - Summary

## Key Definitions and Concepts

- **Proper Graph Colouring**: Assignment of colours to vertices such that no adjacent vertices share the same colour
- **Chromatic Number χ(G)**: Minimum number of colours required for a proper colouring of graph G
- **Chromatic Polynomial P(G, k)**: Number of ways to colour graph G using exactly k colours
- **k-Colourable**: A graph that can be properly coloured with k colours

## Important Formulas and Theorems

| Theorem/Formula        | Statement                                              |
| ---------------------- | ------------------------------------------------------ |
| Trivial Bound          | χ(G) ≤ Δ(G) + 1                                        |
| Brooks' Theorem        | χ(G) ≤ Δ(G) for connected G (except Kₙ and odd cycles) |
| Four Colour Theorem    | Every planar graph is 4-colourable                     |
| Five Colour Theorem    | Every planar graph is 5-colourable                     |
| Chromatic Polynomial   | P(G, k) = P(G-e, k) - P(G/e, k)                        |
| Clique-Chromatic Bound | χ(G) ≥ ω(G)                                            |

## Key Points

- Complete graph Kₙ requires exactly n colours (χ(Kₙ) = n)
- Even cycles are 2-colourable; odd cycles require 3 colours
- All bipartite graphs have chromatic number 2
- K₅ and K₃,₃ are non-planar and cannot be coloured with 4 colours
- Greedy colouring uses at most Δ(G) + 1 colours; ordering matters significantly
- Chromatic polynomial is always a polynomial in k with integer coefficients
- Every k-chromatic graph has a k-critical subgraph

## Common Mistakes to Avoid

1. **Applying Four Colour Theorem to non-planar graphs**: The theorem only applies to planar graphs; non-planar graphs like K₅ require 5 colours
2. **Confusing chromatic number with degree**: χ(G) ≤ Δ(G) + 1, but equality holds only for complete graphs and odd cycles
3. **Forgetting edge cases**: An empty graph has chromatic number 1, while a single vertex graph also has χ(G) = 1
4. **Incorrect vertex ordering in greedy colouring**: Random ordering can lead to worst-case performance; degree-based ordering is better

## Revision Tips

1. **Practice with small graphs**: Draw cycles, complete graphs, and bipartite graphs and try colouring them manually
2. **Memorize key results**: Know which graph families have chromatic numbers 1, 2, or require more colours
3. **Understand the proofs**: The Five Colour Theorem proof is constructive and often appears in exams
4. **Work through chromatic polynomials**: Use the deletion-contraction recurrence on small graphs to build intuition
5. **Solve application problems**: Recognise scheduling and allocation problems as graph colouring disguised as real-world scenarios
