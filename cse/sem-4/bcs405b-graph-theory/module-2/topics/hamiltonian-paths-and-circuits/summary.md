# Hamiltonian Paths and Circuits - Summary

## Key Definitions and Concepts

- **Hamiltonian Path**: A path that visits each vertex exactly once in a graph
- **Hamiltonian Circuit**: A cycle that visits each vertex exactly once and returns to the starting vertex
- **Hamiltonian Graph**: A graph containing at least one Hamiltonian circuit

## Important Formulas and Theorems

- **Dirac's Theorem**: If δ(G) ≥ n/2 for n ≥ 3, then G is Hamiltonian (sufficient condition)
- **Ore's Theorem**: If deg(u) + deg(v) ≥ n for every pair of non-adjacent vertices u, v, then G is Hamiltonian (sufficient condition)
- **Number of Hamiltonian circuits in Kₙ**: (n-1)!/2 (accounting for rotation and reflection equivalence)

## Key Points

- Hamiltonian problems visit each vertex exactly once; Eulerian problems traverse each edge exactly once
- Complete graphs Kₙ are always Hamiltonian with (n-1)!/2 distinct circuits
- Dirac's theorem is a special case of Ore's theorem
- Minimum degree ≥ n/2 guarantees Hamiltonicity but is not necessary
- A Hamiltonian graph with n vertices must have at least n edges
- Graphs with vertices of degree 1 cannot have Hamiltonian paths (except as endpoints)

## Common Mistakes to Avoid

- Confusing Eulerian and Hamiltonian concepts (edges vs vertices)
- Forgetting that Dirac's and Ore's theorems provide sufficient, not necessary conditions
- Not accounting for rotation equivalence when counting Hamiltonian circuits
- Assuming a graph without the degree conditions cannot be Hamiltonian (counterexamples exist)

## Revision Tips

1. Practice identifying Hamiltonian paths by inspection in small graphs
2. Memorize both Dirac's and Ore's theorems with their precise conditions
3. Remember the NP-complete nature distinguishes Hamiltonian from Eulerian problems
4. Focus on the practical link to the Traveling Salesman Problem for application context
